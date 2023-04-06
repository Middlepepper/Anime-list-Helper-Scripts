# Anime-list-Helper-Scripts
Repository I have for Script I made to help with formating or filling in https://github.com/Anime-Lists/anime-lists


# Validate_anime-list-unknown.xml
A script to check for any errors in the .anime-list-unknown.xml

Currently there are 4 checks

- Check 1 - Checks the 'tvdbid' is valid per the readme (One of the Anidb Type, Unknown or is number)
- Check 2 - Checks the 'defaulttvdbseason' value in the XML valid ('defaulttvdbseason' is not empty, is number or "a")
- Check 3 - Checks there are no values in 'tmdbid' and 'imdbid' if TVDB is unknown. as they should only be used for OVA, ONA, Movies and TV Specials
- Check 4 - Checks the 'episodeoffset' is set when TVDB is linked to specials (Season 0 only)

# XMLtoMarkdown.py
A script to convert the .xml to .md to help with submitting pull request.

This can be used on filed like https://github.com/Anime-Lists/anime-lists/blob/master/anime-list-unknown.xml

You will fill in the missing detailed feed in the .xml you have updated to the script to generate the description for Pull Requests.

# getunknownshownamefromgithub.py

A script to check the last copy of anime-list-unknown.xml and output the list of missing anime names.

# copychangestoanimelistmaster.py
A script to allow for any changed done in the working .xml file to be copied over to a fresh copy to prep for a pull request.
