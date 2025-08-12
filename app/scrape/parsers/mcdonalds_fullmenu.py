from bs4 import BeautifulSoup, Tag


def parse_fullmenu(html: str) -> list[str]:    
    html_soup = BeautifulSoup(html, features="lxml")
    
    items_lies = html_soup.find_all(name="li", attrs={"class": "cmp-category__item"})
    items_ids = [str(item_li.get("data-product-id")) for item_li in items_lies if isinstance(item_li, Tag)]
    
    return items_ids