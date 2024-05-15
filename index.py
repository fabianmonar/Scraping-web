import requests
from bs4 import BeautifulSoup
import re

# obtener en HTML de la pagina

url = "https://es.wikipedia.org/wiki/The_Doors"
response = requests.get(url)
html = response._content

# Analizar el html utilizando BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

#obtener el titulo de la pagina 
title = soup.title.string

print(f"el titulo es: {title}")
print("*" * 100)

#obtener todos los enlaces de la pagina
links = []
for link in soup.find_all("a", href=True):
    if "http" in link["href"]:
        links.append(link["href"])

print(links)
print("*" *10)

# obtener todos los encabezados de la pagina

encabezados = []

for encabezado in soup.find_all(re.compile("^h[1-6]$")):
    encabezados.append(encabezado.text.strip())

    print(encabezados)
    print("*" *10)
