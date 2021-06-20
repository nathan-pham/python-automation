from bs4 import BeautifulSoup
import requests

shop = "https://www.spaceposters.co/"

def get_space_product(product_number=1):
    response = requests.get(shop)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # retrieve paths with element -> left click -> copy -> selector
        title_element = soup.select(f"#posters > div > div > div > div:nth-child({product_number}) > div.prodcut-list-content-wrapper > h2")[0]
        price_element = soup.select(f"#posters > div > div > div > div:nth-child({product_number}) > div.prodcut-list-content-wrapper > div.product-list-price")[0]

        return title_element.text.strip(), float("".join([char for char in price_element.text.strip() if char.isdigit() or char == "."]))

    return "unknown product", 0.0

print(get_space_product(1))    
print(get_space_product(2))    