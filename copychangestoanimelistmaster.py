import sys
import xml.etree.ElementTree as ET

# check if both input and output file are provided
if len(sys.argv) < 3:
    print("Usage: python copychangestoanimelistmaster.py input_file output_file")
    sys.exit(1)

# parse the input file
tree = ET.parse(sys.argv[1])
root = tree.getroot()

# iterate over all anime elements and fill in any empty fields
for anime in root.findall('anime'):
    if anime.get('tvdbid') == "":
        anime.set('tvdbid', "")

    if anime.get('tmdbid') == "":
        anime.set('tmdbid', "")

    if anime.get('defaulttvdbseason') == "":
        anime.set('defaulttvdbseason', "")

# write the result to the output file
tree.write(sys.argv[2], encoding="utf-8")
