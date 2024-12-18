from selenium import webdriver
from bs4 import BeautifulSoup
import time

def get_metal_price(url, metal_name):
    """Extrait le prix Ask d'un métal spécifique à partir de la page rendue dynamiquement."""
    # Configurer Selenium (vous devez avoir un WebDriver, ex: ChromeDriver)
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)  # Attendre que la page et le JavaScript se chargent

    # Récupérer le contenu rendu dynamiquement
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # Localiser les informations spécifiques au métal
    rows = soup.find_all('tr', class_='prField')
    for row in rows:
        data_attribute = row.get('data', '')
        if metal_name in data_attribute:
            ask_cell = row.find('td', class_='a')  # Trouve la colonne avec la classe 'a' pour Ask
            if ask_cell:
                driver.quit()
                return ask_cell.text.strip()  # Retourne la valeur 'Ask'

    driver.quit()
    return None

# URL des pages de prix
urls = {
    "Gold USD": "https://www.metalsdaily.com/live-prices/gold/",
    "Silver USD": "https://www.metalsdaily.com/live-prices/silver/",
    "Platinum USD": "https://www.metalsdaily.com/live-prices/pgms/",
    "Palladium USD": "https://www.metalsdaily.com/live-prices/pgms/",
}

# Métaux à extraire
metals = {
    "XAUUSD": "Gold USD",
    "XAGUSD": "Silver USD",
    "XPTUSD": "Platinum USD",
    "XPDUSD": "Palladium USD",
}

# Stocker les résultats
prices = {}

for metal, url_key in metals.items():
    url = urls.get(url_key)
    if url:
        price = get_metal_price(url, metal)
        prices[metal] = price

# Afficher les résultats
for metal, price in prices.items():
    print(f"{metal} (Ask): {price}")
