from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
print ("Lets scrape some websites")

my_url = 'https://www.newegg.com/p/pl?d=rtx+3080'
 #opening up connection, grabbing the page
uClient=uReq(my_url)
page_html= uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})

for container in containers:
#brand name
 brand = container.div.div.img["title"]
#product name
 title_container = container.findAll("a", {"class":"item-title"})
 product_name = title_container[0].text
#current price
 price_container = container.findAll("li",{"class":"price-current"})
 item_price = price_container[0].strong

 print(brand)
 print(product_name)
 print(item_price)


