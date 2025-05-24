import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import json
import re

def read_excel(file):
    df = pd.read_excel(file)
    df['Original Value'] = None
    return df

# Count number of appearences of keywords in text
def count_matches(text, keywords):
    if isinstance(text, list):
        text = ' '.join(text)
    return sum(1 for keyword in keywords if keyword.lower() in text.lower())

# Extract table and prices from KBB website
def get_car_data(make, model, year, keywords):
    url = f'https://www.kbb.com/{make}/{model}/{year}/'
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        page = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find('table', class_="css-lb65co ee33uo30")

        if not table:
            print(f"[!] Tabla no encontrada en: {url}")
            return None

        rows = table.find_all('tr')
        car_data = []

        for row in rows:
            th = row.find('th')
            td = row.find_all('td')
            if th and len(td) > 1:
                model_name = th.text.strip()
                price = td[1].text.strip()
                coincidences = count_matches(model_name, keywords)
                car_data.append({"model": model_name, "price": price, "coincidence": coincidences})

        return pd.DataFrame(car_data)

    except Exception as e:
        print(f"[ERROR] Fallo al obtener datos de {url}: {e}")
        return None


if __name__ == "__main__":
    pd.set_option('future.no_silent_downcasting', True)
    df_full = read_excel('raw_data.xlsx')
    df_chunks = np.array_split(df_full, 30)

    for k, chunk in enumerate(df_chunks):
        df = chunk.reset_index(drop=True)

        for j in range(len(df)):
            model_str = df.loc[j, "model"]
            make = df.loc[j, "make"]
            year = df.loc[j, "year_manufacture"]

            words = model_str.split()
            if len(words) < 2:
                print(f"[{k}-{j}] Modelo con formato invalido: '{model_str}'")
                continue

            second_word = words[1]
            car_df = get_car_data(make, second_word, year, words)

            if car_df is None or car_df.empty:
                df.loc[j, 'Original Value'] = None
                continue

            # Get the most probable price
            if car_df['coincidence'].max() == 0:
                df.loc[j, 'Original Value'] = car_df.iloc[1]['price'] if len(car_df) > 1 else car_df.iloc[0]['price']
            else:
                best_match = car_df.loc[car_df['coincidence'].idxmax()]
                df.loc[j, 'Original Value'] = best_match['price']

        df.to_csv(f'raw_data_{k}_OV.csv', index=False)
        print(f"Chunk {k} procesado y guardado.")
