import json

from db.models.products import Product


def parse_product(product_json: str) -> Product:
    product_data: dict = json.loads(product_json)
    
    scraped_data = {
        "name": product_data["item"]["item_name"],
        "description": product_data["item"]["description"],
        "calories": product_data["item"]["nutrient_facts"]["nutrient"][2]["value"],
        "fats": product_data["item"]["nutrient_facts"]["nutrient"][3]["value"],
        "carbs": product_data["item"]["nutrient_facts"]["nutrient"][5]["value"],
        "proteins": product_data["item"]["nutrient_facts"]["nutrient"][7]["value"],
        "unsaturated_fats": product_data["item"]["nutrient_facts"]["nutrient"][4]["value"],
        "sugar": product_data["item"]["nutrient_facts"]["nutrient"][6]["value"],
        "salt": product_data["item"]["nutrient_facts"]["nutrient"][8]["value"],
        "portion": product_data["item"]["nutrient_facts"]["nutrient"][0]["value"]
    }
    
    return Product(**scraped_data)