from pydantic import BaseModel, model_serializer, ConfigDict
import json

from db.core import NotFoundError, save_db, get_db


class Product(BaseModel):
    name: str
    description: str|dict
    calories: float|str
    fats: float|str
    carbs: float|str
    proteins: float|str
    unsaturated_fats: float|str
    sugar: float|str
    salt: float|str
    portion: float
    
    model_config = ConfigDict(extra="ignore")


    @model_serializer(mode="wrap", when_used="json")
    def serialize_product(self, serializer, info) -> dict[str, str]:
        return {
            "name": f"{self.name}",
            "description": f"{self.description}",
            "calories": f"{self.calories} ккал/kcal",
            "fats": f"{self.fats} г/g",
            "carbs": f"{self.carbs} г/g",
            "proteins": f"{self.proteins} г/g",
            "unsaturated_fats": f"{self.unsaturated_fats} г/g",
            "sugar": f"{self.sugar} г/g",
            "salt": f"{self.salt} г/g",
            "portion": f"{self.portion} г/g"
        }


class ProductSerialize(BaseModel):
    name: str
    description: str
    calories: str
    fats: str
    carbs: str
    proteins: str
    unsaturated_fats: str
    sugar: str
    salt: str
    portion: str


def create_product(product: Product) -> None:
    product_key = product.name
    product_data = product.model_dump()
    
    db = get_db()
    db.update({f"{product_key}": product_data})
    save_db(db)
    

def read_product(product_key: str, db: dict) -> dict:
    product = db.get(product_key)
    
    if product is None:
        raise NotFoundError(f"Product '{product_key}' not found")
    
    return json.loads(Product(**product).model_dump_json())


def read_products(db: dict) -> list[ProductSerialize]:
    db_values = db.values()
    
    return [json.loads(Product(**value).model_dump_json()) for value in db_values]
    
    
def read_product_field(product_key: str, product_field: str, db: dict) -> str:
    product = read_product(product_key=product_key, db=db)
    field_value = product.get(product_field)
    
    if field_value is None:
        raise NotFoundError(f"Field '{product_field}' not found in '{product_key}' product")
    
    return field_value