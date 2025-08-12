from scrape.parsers.mcdonalds_fullmenu import parse_fullmenu
from scrape.parsers.mcdonalds_product import parse_product
from scrape.utils.http import get

from db.models.products import Product, create_product

from config import FULLMENU_URL, PRODUCT_URL


def scrape_mcdonalds() -> None:
    fullmenu_html = get(url=FULLMENU_URL)
    products_ids = parse_fullmenu(html=fullmenu_html)
    
    for product_id in products_ids:
        product_url = PRODUCT_URL.format(id = product_id)

        product_json = get(url=product_url)
        product = parse_product(product_json=product_json)
        
        create_product(product=product)