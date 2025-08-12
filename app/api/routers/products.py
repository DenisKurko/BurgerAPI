from fastapi import APIRouter, Request, Depends

from db.core import get_db
from db.models.products import (
    ProductSerialize,
    create_product,
    read_product,
    read_products,
    read_product_field
)


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("")
async def get_products(request: Request, db: dict = Depends(get_db)) -> list[ProductSerialize]:
    products = read_products(db=db)
    products = [product for product in products]
    
    return products


@router.get("/{product_key}")
async def get_product(requset: Request, product_key: str, db: dict = Depends(get_db)) -> ProductSerialize:
    product = read_product(product_key=product_key, db=db)
    
    return ProductSerialize(**product)


@router.get("/{product_key}/{product_field}")
async def get_product_field(request: Request, product_key: str, product_field: str, db: dict = Depends(get_db)) -> str | float:
    field_value = read_product_field(product_key=product_key, product_field=product_field, db=db)
    
    return field_value