# Missing-Music 
A small set of python scripts to find new music from the artists in your playlist. 
## arguments
```
--artist Specifies the artist you are searching for
--album  List album names from artist and saves IDs to a JSON file
--song   List song names from album and saves titles to a JSON file
--feed   Feed album ids from a JSON file into song function to return all song names for all albums
```
## Meaningful user agent 
The scripts in this repository use the MusicBrainz API. The MusicBrainz API requires a meaningful user agent string when making requests so if there is a problem they can contact you. The user agent can be configured from your .env file. To see what a meaningful user agent looks like or to learn more please see: [MusicBrainz](https://musicbrainz.org/doc/MusicBrainz_API/Rate_Limiting#Provide_meaningful_User-Agent_strings)
## License 
[MIT](https://choosealicense.com/licenses/mit/)
