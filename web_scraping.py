# -*- coding: utf-8 -*-
# !pip install beautifulsoup4
# !pip install lxml
# !pip install requests
# !pip install selenium
# !pip install playwright

from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time

driver = webdriver.Chrome()
driver.minimize_window()

def parse(url, make):
    try:
        driver.get(url)
    except:
        time.sleep(1)
        driver.get(url)
    
    soup=BeautifulSoup(driver.page_source,'lxml')
    cars = soup.find_all('div',class_='vehicle-details')
    data = []
    for car in cars:
        try:
             rawHref = car.find('a')['href']
             href = rawHref if 'https' in rawHref else 'https://cars.com'+rawHref
             name = car.find('h2',class_='title').text.replace('\n','').strip()
             
             year=name.split()[0]
             model=' '.join(name.split()[1:])
             price_USD = float(car.find('span',class_='primary-price').text.replace('\n','').replace('$','').replace(',','').replace(' ',''))
             # mileage = car.find(attrs={'class':'mileage'}).text.split()[0] if car.find(attrs={'class':'mileage'}) else None
             stock_type = car.find('p',class_='stock-type').text
             
             
             driver.get(href)
             newSoup=BeautifulSoup(driver.page_source,'lxml')
             
             print('getting details of '+name)
             description = newSoup.find('dl',class_ = 'fancy-description-list')
             rawBasicKeys = description.find_all('dt')
             basicKeys = [key.text.replace('\n',' ') for key in rawBasicKeys]
             rawBasicValues = description.find_all('dd')
             basicValues = [value.text.replace('\n',' ') for value in rawBasicValues]
             basics = dict(zip(basicKeys,basicValues))
    
             exterior_color = basics["Exterior color"].strip()
             interior_color = basics["Interior color"].strip()
             drive_train = basics["Drivetrain"].strip()
             mpg= basics["MPG"].strip() if "MPG" in basicKeys else None
             fuel_type = basics["Fuel type"].strip() if "Fuel type" in basicKeys else None
             transmission = basics["Transmission"].strip()
             engine = basics["Engine"].strip()
             mileage = basics["Mileage"].split()[0].replace(',','')
    
            
    
             data.append({
                  "year_manufacture":int(year),
                  "years": 2025-int(year),
                  "make": make,
                  "model": model,              
                  "mileage": float(mileage),
                  "stock_type": stock_type,
                  "interior_color": interior_color,
                  "exterior_color": exterior_color,
                  "drive_train": drive_train,
                  "mpg": mpg,
                  "fuel_type": fuel_type,
                  "transmission": transmission,
                  "engine": engine,
                  "price_USD": price_USD,
                  'url': href
             }
             )
        except:
            continue
    return data



def paginate(initial_page, final_page, make):
    batch_size=10
    num_cars=0
    carData = []
    for i in range(initial_page, final_page+1):
        url="https://www.cars.com/shopping/results/?makes[]="+make+"&maximum_distance=all&page="+str(i)+"&stock_type=used&zip=60606"
        scraped_data = parse(url, make)
        for data in scraped_data:
            carData.append(data)
        num_cars=len(carData)
        print(f"Make {make},  Page {i}, {num_cars} cars")
        if i%batch_size==0:
            writeData(carData, i//batch_size, make)
            num_cars=0
            carData = []
    writeData(carData, final_page//batch_size + 1, make)


def writeData(carData, batch, make):
    if carData:
        print(len(carData))
        with open('cars\\'+make+'\\cars_'+make+'_'+str(batch)+'.json','w',encoding='utf-8') as jsonfile:
            json.dump(carData,jsonfile,indent=4,ensure_ascii=False)
    else:
        print("No data scraped")



if __name__=="__main__":
    # extract data
    # makes=["acura","audi","bmw","buick","cadillac","chevrolet","chrysler","dodge","ford","gmc","honda","hyundai","infiniti","jeep","kia","land_rover","lexus",
    #        "lincoln","mazda","mercedes_benz","mini","mitsubishi","nissan","porsche","ram","subaru","tesla","toyota","volkswagen","volvo"]
    
    # Lucía: "chrysler","dodge","ford","gmc","honda"
    # Ana: "jeep","kia","land_rover","lexus", "lincoln"
    makes=["infiniti","mazda","lincoln"]
    # makes=makes[::-1]
    initial_page=141
    final_page=250
    for make in makes:
        paginate(initial_page, final_page, make)
        initial_page=1


