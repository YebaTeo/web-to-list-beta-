import requests
from bs4 import BeautifulSoup

# URLs of the pages containing product information
urls = [
    'https://www.longchamp.com/gb/en/sale/sales-uk/women/sale_002-uk/?cgid=Sale_002-UK&page=8',
    'https://www.longchamp.com/gb/en/sale/sales-uk/women/sale_002-uk/?cgid=Sale_002-UK&page=9',
    'https://www.longchamp.com/gb/en/sale/sales-uk/women/sale_002-uk/?cgid=Sale_002-UK&page=10',
    'https://www.longchamp.com/gb/en/sale/sales-uk/women/sale_002-uk/?cgid=Sale_002-UK&page=11',
    'https://www.longchamp.com/gb/en/sale/sales-uk/women/sale_002-uk/?cgid=Sale_002-UK&page=12',
    'https://www.longchamp.com/gb/en/sale/sales-uk/women/sale_002-uk/?cgid=Sale_002-UK&page=13',
    # Add more URLs for other pages
]

product_data = []

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        product_tiles = soup.find_all('a', class_='product-item__link')
        for product_tile in product_tiles:
            product_name = product_tile.select_one('span.product-item__line.upper.fs-l')
            product_style = product_tile.select_one('span.product-item__style.upper')
            price = product_tile.select_one('span.product-item__price.price.flex .price-formatted')

            if product_name and product_style and price:
                product_data.append({
                    'name': product_name.text.strip(),
                    'style': product_style.text.strip(),
                    'price': price.text.strip()
                })

# Print the extracted product information
for product in product_data:
    print("Product Name:", product['name'])
    print("Product Style:", product['style'])
    print("Price:", product['price'])
    print()



