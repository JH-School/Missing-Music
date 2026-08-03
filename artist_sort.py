from collections import defaultdict
from dotenv import load_dotenv
import argparse
import json 
import os 
import re 

parser = argparse.ArgumentParser(description="Use this script to find artists from your playlist")

def regCheck(argument):
    return re.compile(argument)

parser.add_argument("--spattern", type=regCheck, help="if the default regex search pattern for songs does not work for you specify your own here. Escape your regex pattern with single quotes")
parser.add_argument("--apattern", type=regCheck, help="if the default regex search pattern for artist does not work for you specify your own here. Esacape your regex pattern with single quotes")
parser.add_argument("--outfile", type=str, help="Specifies the name of the outfile. If not specified the file defaults to Artists.json")
parser.add_argument("--artist", type=str, help="Use this option to filter out songs by a particular artist")

args = parser.parse_args()

load_dotenv()

m_path = os.getenv("musicPath")
p_path = os.getenv("playlistPath")

#regex search patterns 
artist_search = r"^([^-]*)\s"
song_search = r"\s([^-]*)$"

#Gets all of the files in the music playlist directory and puts them in a list
def getFiles() -> list[str]:
    all_files = []
    music_files = os.listdir(f"{p_path}")
    for file in music_files:
        file = file.casefold().strip()
        all_files.append(file)
    return all_files

#Gets all of the artists from a list using regex should pass the all_files return value to this 
def getArtist(files: list[str]) -> list[str]:
    artist_results = []
    for file in files:
        if not args.apattern:
            artists = re.search(artist_search,file)
            if artists:
                artist_results.append(artists.group())
        elif args.apattern:
            artists = re.search(args.apattern,file)
            if artists:
                artist_results.append(artists.group())
    artist_results = list(set(artist_results))
    artist_results.sort()
    return artist_results

#Gets all of the songs from a list using regex should pass all_files return value or findSongByArtist() return value to this  
def getSongs(files: list[str]) -> list[str]:
    song_results = []
    if files:
        for file in files:
            file = file.casefold().strip()
            if not args.spattern:
                songs = re.search(song_search,file)
                if songs:
                    song_results.append(songs.group().strip())
            elif args.spattern:
                songs = re.search(args.spattern,file)
                if songs:
                    song_results.append(songs.group().strip())
        song_results = list(set(song_results))
        song_results.sort()
        return song_results

#Finds a particular artist and their songs by using regex, returning the whole string should pass all_files return value to this 
def findSongByArtist(files: list[str], artist: str) -> list[str]:
    title_results = []
    if files:
        for file in files:
            artist_search = re.compile(artist,re.IGNORECASE)
            if artist_search.search(file):
                cleaned = artist_search.sub("",file)
                title_results.append(cleaned)
        title_results.sort()
        return title_results

#Creates the JSON output file with the artist name and song titles
def createSongs(output: dict, outputFile: str) -> None:
    with open(f"{m_path}/{outputFile}.json", "a") as textDoc:
        json.dump(output, textDoc, ensure_ascii=False, sort_keys=True, indent=4)

#The main function. Compares the arguments from argparse, sets output file name if specified, and creates song files. 
def main() -> None:
    allFiles = getFiles()
    if args.artist:
        grouped = defaultdict(list)
        songMatches = findSongByArtist(allFiles, args.artist)
        songTitles = getSongs(songMatches)
        grouped[args.artist].append({"Titles":songTitles})
        if not args.outfile:
            createSongs(grouped,"Artists")
        elif args.outfile:
            createSongs(grouped,args.outfile)
    if not args.artist:
        artists = getArtist(allFiles)
        grouped = defaultdict(list)
        for artist in artists:
            songMatches = findSongByArtist(allFiles, artist)
            songTitles = getSongs(songMatches)
            grouped[artist].append({"Titles":songTitles})

        if not args.outfile:
            createSongs(grouped,outputFile="Artists")
        elif args.outfile:
            createSongs(args.artist,args.outfile)
        
main()
