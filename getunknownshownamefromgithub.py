import xml.etree.ElementTree as ET
import requests

# URL for the XML file
url = "https://raw.githubusercontent.com/Anime-Lists/anime-lists/master/anime-list-unknown.xml"

# Download the XML file
response = requests.get(url)
xml_text = response.text

# Parse the XML file
root = ET.fromstring(xml_text)

# Extract the name field for each anime
for anime in root.findall("./anime"):
    name = anime.find("name").text
    print(name)
