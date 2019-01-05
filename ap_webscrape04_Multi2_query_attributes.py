from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import urllib, time, datetime

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

#query_item="power bank"
query_item = input("Query Item: ")
query_item = query_item.replace(" ", "+")
pages = input("Pages: ")
#pages = 2

filename = datetime.date.today().strftime('%Y-%m-%d') + "_Multi_" + query_item.replace("+", "_") + "_" + str(pages) + "_Pages.csv"
f = open(filename, "w")
headers= "source,product,price,review\n"
f.write(headers)

for page in range(1, int(pages)):
    query_url = "https://www.amazon.in/s/ref=sr_pg_"+ str(page) + "?fst=as%3Aon&rh=i%3Aaps%2Ck%3"+ query_item +"%2Cp_85%3A10440599031&page="+ str(page) +"&keywords="+ query_item +"&ie=UTF8&qid=1546581629"
    response = opener.open(query_url)
    time.sleep(.300)
    page_html = response.read()
    
    page_soup = soup(page_html, "html.parser")

    containers = page_soup.findAll("div",{"class":"s-item-container"})
    for container in containers:
        try:
            product_container = container.findAll("h2")
            product = product_container[0].text
        except (IndexError, AttributeError, TypeError):
            product = "Not Found"
        product = product.replace("\uff0c", "|")
        try:
            price_container = container.findAll("span", {"class":"a-color-price"})
            price = price_container[0].text
            price = price.strip()
        except (IndexError, AttributeError, TypeError):
            price = "Not Found"

        try:
            review_container = container.findAll("i", {"class":"a-icon-star"})
            review=review_container[0].span.text
        except (IndexError, AttributeError, TypeError):
            review = "Not Found"
        review = review.replace("out of 5 stars", "")
        print("Processing...")
        f.write("Amazon ," + product.replace(",", "|") + "," + price.replace(",", "") + "," + review.replace(",", "|") + "\n")

for page in range(1, int(pages)):
    query_url = "https://www.flipkart.com/search?q="+ query_item +"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(page)
    response = opener.open(query_url)
    time.sleep(.300)
    page_html = response.read()
    
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div",{"class":"_3liAhj _1R0K0g"})

    for container in containers:
        try:
            product_container = container.findAll("a",{"class","_2cLu-l"})
            product = product_container[0].text
        except (IndexError, AttributeError, TypeError):
            product = "Not Found"
        product = product.replace("\uff0c", "|")
        try:
            price_container = container.findAll("div", {"class":"_1vC4OE"})
            price = price_container[0].text
            price = price.strip()
        except (IndexError, AttributeError, TypeError):
            price = "Not Found"
        price = price.replace("\u20b9", "")
        try:
            review_container = container.findAll("div", {"class":"_2beYZw"})
            review=review_container[0].text
        except (IndexError, AttributeError, TypeError):
            review = "Not Found"
        
        
        ##    print ("product: " + product)
        ##    print("price: " + price)
        ##    print("review:" + review)
        print("Processing...")
        f.write("Flipkart ," + product.replace(",", "|") + "," + price.replace(",", "") + "," + review.replace(",", "|") + "\n")
print("Completed!")
f.close()
