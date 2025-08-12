import uvicorn
import os

from scrape.scrapers.mcdonalds import scrape_mcdonalds

from config import HOST


if __name__ == "__main__":
    
    
    scrape_mcdonalds()
    uvicorn.run(app="api.main:app", host=HOST, port=8000, reload=False)