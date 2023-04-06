import xml.etree.ElementTree as ET

# Step 1: Open the XML file
tree = ET.parse('anime-list-masterxml')
root = tree.getroot()

# Step 2: Define functions to check the file based on rules
def check_rule_1(xml_tree):
    # Function to check if the 'tvdbid' value in the XML follows rules
    changes = []
    for elem in xml_tree.iter():
        if elem.tag == 'anime':
            tvdbid = elem.get('tvdbid')
            defaulttvdbseason = elem.get('defaulttvdbseason')
            if tvdbid:
                try:
                    if tvdbid.isdigit() or tvdbid in ["MOVIE", "OVA", "ONA", "SPECIAL","TV Special", "Music Video", "HENTAI", "movie", "ova", "ona", "tv special", "music video", "hentai", "unknown", "web"]:
                        pass  # valid 'tvdbid' value
                    else:
                        changes.append(f'Error: Invalid "tvdbid" value"')
                except ValueError:
                    changes.append(f'Error: Invalid "tvdbid" value')
    return changes

def check_rule_2(xml_tree):
    # Function to check if the 'tvdbid' value in the XML is a number and if 'defaulttvdbseason' is not empty or "a"
    changes = []
    for elem in xml_tree.iter():
        if elem.tag == 'anime':
            tvdbid = elem.get('tvdbid')
            defaulttvdbseason = elem.get('defaulttvdbseason')
            if tvdbid:
                try:
                    if not defaulttvdbseason:
                        raise ValueError("Error: The 'defaulttvdbseason' value is empty")
                    elif not defaulttvdbseason.isdigit() and defaulttvdbseason != "a":
                        raise ValueError("Error: The 'defaulttvdbseason' value must be a number or the letter 'a'")
                    elif not tvdbid.isdigit():
                        raise ValueError("Error: Invalid 'tvdbid' value")
                except ValueError as e:
                    changes.append(f'Error: {e}')
    return changes

def check_rule_3(xml_tree):
    # Function to check if the 'tvdbid' value in the XML is unknown (i.e TV Show) and no values in tmdbid and imdbid
    changes = []
    for elem in xml_tree.iter():
        if elem.tag == 'anime':
            tvdbid = elem.get('tvdbid')
            if tvdbid == 'unknown':
                episodeoffset = elem.get('episodeoffset')
                tmdbid = elem.get('tmdbid')
                imdbid = elem.get('imdbid')
                if episodeoffset != '' or tmdbid != '' or imdbid != '':
                    changes.append(f'Error: "episodeoffset", "tmdbid", and/or "imdbid" should be blank')
    return changes


def check_rule_4(xml_tree):
    # Function to check if the 'tvdbid' value in the XML is unknown and follows rules, including checking if 'episodeoffset' is provided when 'defaulttvdbseason' is 0
    changes = []
    for elem in xml_tree.iter():
        if elem.tag == 'anime':
            tvdbid = elem.get('tvdbid')
            if tvdbid.isdigit():
                episodeoffset = elem.get('episodeoffset')
                defaulttvdbseason = elem.get('defaulttvdbseason')
                if defaulttvdbseason == '0' and not episodeoffset:
                    changes.append('Error: An "episodeoffset" value must be provided when the "defaulttvdbseason" value is 0')
                elif episodeoffset != '':
                    changes.append('Error: "episodeoffset" should be blank')
    return changes


# Add more functions to check other rules as needed

# Step 3 (continued): Run the functions to check the file for errors
rule_1_changes = check_rule_1(root)
rule_2_changes = check_rule_2(root)
rule_3_changes = check_rule_3(root)
rule_4_changes = check_rule_4(root)

# Step 4: Output the results in markdfown format
changes = rule_1_changes + rule_2_changes + rule_3_changes + rule_4_changes
if changes:
    print('|Name|Check 1 - TVDB is Valid |Check 2 - Season is valid |Check 3 - Movie is valid|Check 4 - Episodeoffset for Show (Season 0 only) |')
    print('|---|---|---|---|')
    for anime_elem in root.iter('anime'):
        anidbid = anime_elem.get('anidbid')
        name = anime_elem.find('name').text + f' (AniDB:{anidbid})'
        rule_1 = 'Passed' if check_rule_1(anime_elem) == [] else 'Error'
        rule_2 = 'Passed' if check_rule_2(anime_elem) == [] else 'Error'
        rule_3 = 'Passed' if check_rule_3(anime_elem) == [] else 'Error'
        rule_4 = 'Passed' if check_rule_4(anime_elem) == [] else 'Error'
        if 'Error' in [rule_1, rule_2, rule_3, rule_4]:
            print(f'|{name}|{rule_1}|{rule_2}|{rule_3}|{rule_4}|')
