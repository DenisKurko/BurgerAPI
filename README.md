# BurgerAPI 🍔
Python based web scraping project. Project scrape, organise and store data from https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html.

## 🛠 Tech Stack

- **API:** FastAPI  
- **Data Validation:** Pydantic  
- **Scraping/Parsing:** Requests, BeautifulSoup4  
- **Deployment:** Docker

## 🚀 Deployment

To deploy this project in a Docker container, run:

```bash
docker-compose up
```

Or run it locally with Poetry (preferred over building the environment from scratch):

```bash
poetry lock
poetry run python app/main.py
```

The service will be accessible at: [http://localhost:8000](http://localhost:8000)

---

## 📚 API Reference

### ⚠️ Attention
Data must be passed in the URL using **percent-encoding**.

It is preferred to use the [docs](http://localhost:8000/docs) instead of just visiting [localhost:8000](http://localhost:8000) for a better experience.

---

###  Test Status  
```http
GET /
```
Returns: `"I AM OK"`

---

###  Get All Products  
```http
GET /products
```
Returns JSON with information about all products.

---

###  Get Product  
```http
GET /products/{product_key}
```

| Parameter     | Type     | Description                                   |
|---------------|----------|-----------------------------------------------|
| `product_key` | `string` | **Required.** Product name as in the database |

---

###  Get Product Field  
```http
GET /products/{product_key}/{product_field}
```

| Parameter        | Type     | Description                                   |
|------------------|----------|-----------------------------------------------|
| `product_key`    | `string` | **Required.** Product name as in the database |
| `product_field`  | `string` | **Required.** Product field to return         |

---

## 👤 Author

- [@DenisKurko](https://github.com/DenisKurko)
