# Missing-Music 
A small set of python scripts to find new music from the artists in your playlist. 
## arguments
### query.py 
```
--artist Specifies the artist you are searching for
--album  List album names from artist and saves IDs to a JSON file
--song   List song names from album and saves titles to a JSON file
--feed   Feed album ids from a JSON file into song function to return all song names for all albums
```
### music_sort.py
```
--spattern if the default regex search pattern for songs does not work for you specify your own here. Escape your regex pattern with single quotes
--apattern if the default regex search pattern for artist does not work for you specify your own here. Escape your regex pattern with single quotes
--outfile  Specifies the name of the output file. If not specified the file defaults to Artists.json
--artist   Use this option to filter out songs by a particular artist
```
## Meaningful user agent 
The scripts in this repository use the MusicBrainz API. The MusicBrainz API requires a meaningful user agent string when making requests so if there is a problem they can contact you. The user agent can be configured from your .env file. To see what a meaningful user agent looks like or to learn more please see: [MusicBrainz](https://musicbrainz.org/doc/MusicBrainz_API/Rate_Limiting#Provide_meaningful_User-Agent_strings)
## License 
[MIT](https://choosealicense.com/licenses/mit/)
