import sys
import xml.etree.ElementTree as ET

# Check if file argument was provided
if len(sys.argv) < 2:
    print("Usage: python xml_to_markdown.py [file.xml]")
    exit(1)

# Parse XML file
tree = ET.parse(sys.argv[1])
root = tree.getroot()

# Initialize Markdown table header
table_header = "| AniDB | TVDB/TMDB/IMDB | Notes |\n|-------|----------------|-------|\n"

# Initialize Markdown table rows
table_rows = ""

# Process each 'anime' element recursively
def process_anime_element(element):
    # Extract values from XML
    anidbid = element.get("anidbid")
    tvdbid = element.get("tvdbid")
    name_element = element.find("name")
    if name_element is not None:
        name = name_element.text
    else:
        name = ""

    # Check if tvdbid is not unknown
    if tvdbid != "unknown":
        # Format values into Markdown table row
        row = f"| https://anidb.net/anime/{anidbid} | https://thetvdb.com/index.php?tab=series&id={tvdbid}| {name} |\n"

        # Add row to table_rows
        global table_rows
        table_rows += row

    # Recursively process child elements
    for child in element:
        if child.tag == "anime":
            process_anime_element(child)

# Start recursive processing with root element
for child in root:
    if child.tag == "anime":
        process_anime_element(child)

# Combine header and rows into Markdown table
table = table_header + table_rows

# Print Markdown table
print(table)
