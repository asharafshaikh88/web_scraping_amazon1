from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('a', class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")

with open('Result.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['productlink','productname','productprice','rating','reviews']
    thewriter.writerow(header)

    for list in lists:
        productlink = list.find('a', class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal").text.replace('\n', '')
        productname = list.find('span', class_="a-size-medium a-color-base a-text-normal").text.replace('\n', '')
        productprice = list.find('span', class_="a-price-whole").text.replace('\n', '')
        rating = list.find('i', class_="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom").text.replace('\n', '')
        reviews = list.find('span', class_="a-size-base s-underline-text").text.replace('\n', '')

        info = [productlink,productname,productprice,rating,reviews]
        thewriter.writerow(info)