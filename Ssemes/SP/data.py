import requests
import xml.etree.ElementTree as ET

# Obtener el XML desde la URL
url = "https://www.ncbi.nlm.nih.gov/pmc/oai/oai.cgi?verb=GetRecord&identifier=oai:pubmedcentral.nih.gov:6148705&metadataPrefix=pmc"
response = requests.get(url)
xml_data = response.content

# Parsear el XML
root = ET.fromstring(xml_data)

# Suponiendo una estructura XML específica, extrae los datos
identifier = root.find('.//{http://www.openarchives.org/OAI/2.0/}identifier').text
title = root.find('.//{http://dtd.nlm.nih.gov/publishing/2.3}article-title').text
journal = root.find('.//{http://dtd.nlm.nih.gov/publishing/2.3}journal-title').text

# Para los autores, podrías tener que recorrer un conjunto de nodos
authors = []
for contrib in root.findall('.//{http://dtd.nlm.nih.gov/publishing/2.3}contrib'):
    author_name = contrib.find('.//{http://dtd.nlm.nih.gov/publishing/2.3}name').text
    authors.append(author_name)

authors_str = ', '.join(authors)

pub_date = root.find('.//{http://dtd.nlm.nih.gov/publishing/2.3}pub-date').text
