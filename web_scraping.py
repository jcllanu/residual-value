# -*- coding: utf-8 -*-
# !pip install beautifulsoup4
# !pip install lxml
# !pip install requests
# !pip install selenium
# !pip install playwright

from selenium import webdriver
from bs4 import BeautifulSoup
import json


def parse(url):
    driver = webdriver.Chrome()
    driver.get(url)
    soup=BeautifulSoup(driver.page_source,'lxml')
    cars = soup.find_all('div',{'class':'vehicle-details'})
    data = []
    for car in cars:
         rawHref = car.find('a')['href']
         href = rawHref if 'https' in rawHref else 'https://cars.com'+rawHref
         name = car.find('h2',{'class':'title'}).text
         price = car.find('span',{'class':'primary-price'}).text
         mileage = car.find(attrs={'class':'mileage'}).text if car.find(attrs={'class':'mileage'}) else None
         dealer = car.find(attrs={'class':'dealer-name'}).text.replace('\n','') if car.find(attrs={'class':'dealer-name'}) else None
         reviews = car.find('span',{'class':'test1 sds-rating__link sds-button-link'}).text.replace('(','').replace(')','') if car.find('span',{'class':'test1 sds-rating__link sds-button-link'}) else None
         location = car.find(attrs={'class':'miles-from'}).text.replace('\n','')
         rating = car.find('span',{'class':'sds-rating__count'}).text if car.find('span',{'class':'sds-rating__count'}) else None
         stock_type = car.find('p',{'class':'stock-type'}).text
         
         
         driver.get(href)
         newSoup=BeautifulSoup(driver.page_source,'lxml')
         
         print('getting details of'+name)
         description = newSoup.find('dl',{'class':'fancy-description-list'})
         rawBasicKeys = description.find_all('dt')
         basicKeys = [key.text.replace('\n',' ') for key in rawBasicKeys]
         rawBasicValues = description.find_all('dd')
         basicValues = [value.text.replace('\n',' ') for value in rawBasicValues]
         basics = dict(zip(basicKeys,basicValues))


         data.append({
              "Name":name,
              "Price":price,
              "URL":href,
              "Mileage":mileage,
              "Stock-Type":stock_type,
              "Dealer Details":{"Name":dealer,
                                "Rating":rating,
                                "Review Count":reviews,
                                "Location":location
                                },
                   
              "Specifications":basics
         }
         )
    driver.quit()
    return data



def paginate(max_pages):
    carData = []
    for i in range(int(max_pages)):
        url = "https://www.cars.com/shopping/results/?_unused_include_shippable=&_unused_keyword=&_unused_list_price_max=&_unused_list_price_min=&_unused_makes[]=&_unused_mileage_max=&_unused_monthly_payment=&_unused_stock_type=&_unused_year_max=&_unused_year_min=&_unused_zip=&dealer_id=&include_shippable=true&keyword=&list_price_max=&list_price_min=&makes[]=&maximum_distance=all&mileage_max=&monthly_payment=&page="+str(i)+"&page_size=20&sort=best_match_desc&stock_type=all&year_max=&year_min=&zip=60606"  
        scraped_data =  parse(url)
        print(url)
        for data in scraped_data:
            carData.append(data)
    return carData


def writeData(carData):
    if carData:
        print(len(carData))
        with open('cars.json','w',encoding='utf-8') as jsonfile:
            json.dump(carData,jsonfile,indent=4,ensure_ascii=False)
    else:
        print("No data scraped")



if __name__=="__main__":
    # extract data
    max_pages=4
    carData=paginate(max_pages)
    # write data
    writeData(carData)

