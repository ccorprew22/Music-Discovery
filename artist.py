import requests
import json
import urllib.request as urllib2
import random
import os
from dotenv import load_dotenv, find_dotenv

artist_ids = [["The Weeknd", "1Xyo4u8uXC1ZmMpatF05PJ"], ["ASAP Rocky", "13ubrt8QOOCPljQ2FL1Kca"], ["Drake", "3TVXtAsR1Inumwj472S9r4"], ["Post Malone", "246dkjvS1zLTtiykXe5h60"], ["Lil Baby","5f7VJjfbwm532GiveGC0ZK"], ["DaBaby", "4r63FhuTkUYltbVAg5TQnk"], ["Roddy Ricch", "757aE44tKEUQEqRuT6GnEB"],["Wiz Khalifa", "137W8MRPWKqSmrBGDBFSop"]]

load_dotenv(find_dotenv())

def refresh():
    query = "https://accounts.spotify.com/api/token"
    response = requests.post(query, data={"grant_type": "client_credentials"},
                headers= {"Authorization"
                 : "Basic " + os.getenv('base64')})
    token = response.json()['access_token']
    return token

def song_preview(_id_, tok):
    query = "https://api.spotify.com/v1/tracks/{}?market=US".format(_id_)
    response = requests.get(query, headers={"Content-Type": "application/json",
                                            "Authorization": "Bearer {}".format(tok)})
    response_json = response.json()
    #print(response_json)
    prev = response_json['preview_url']
    #print(prev)
    return prev

class Artist:
    def __init__(self, num=None, song=None, artist=None):
        self.num = num if num is not None else None
        self.song = song if song is not None else None
        self.artist = artist if artist is not None else None

    def top_track(self, response_json, token):
        tracks_lst = response_json["tracks"] #Big list of tracks
        num = random.randint(0, len(tracks_lst)-1) #Picks track in json file
        song = tracks_lst[num]
        artist = song["album"]["artists"][0]["name"]
        album = song["album"]["name"]
        track = song["name"]
        type = song["type"]
        image = song["album"]["images"][0]["url"]
        preview = song_preview(song["id"], token)
        #song name, song artist, song-related image, song preview URL
        track_info = {"artist": artist, "album": album, "track": track, "image": image, "preview": preview}
        return track_info

    def random_track(self):
        artist_id = artist_ids[self.num][1]
        query = "https://api.spotify.com/v1/artists/{}/top-tracks?market=US".format(artist_id)
        token = refresh()
        response = requests.get(query, headers={"Content-Type": "application/json",
                                                "Authorization": "Bearer {}".format(token)})
        response_json = response.json()
        track_info = self.top_track(response_json, token)
        return track_info
        
    def lyrics(self):
        print(self.song)
        query = "https://api.genius.com/search?q=" + urllib2.quote(self.song) #puts %20 between words

        response = requests.get(query, headers={"Content-Type": "application/json",
                                                "Authorization": "Bearer {}".format(os.getenv('genius_access_token')),
                                                "User-Agent":""})
        print(response)
        response_json = response.json()
        hits_lst = response_json['response']['hits']
        #print(hits_lst)
        url = None
        for hit in hits_lst:
            result = hit['result']
            primary_artist = result['primary_artist']
            if self.artist in primary_artist['name']:
                url = result['url']
                break
        print(url)
        return url
        
    def search(self):
        search = "https://api.spotify.com/v1/search?q=" + urllib2.quote(self.artist) + "&type=artist"
        token = refresh()
        response = requests.get(search, headers={"Content-Type": "application/json",
                                                "Authorization": "Bearer {}".format(token)})
        search_json = response.json()
        artist_id = search_json["artists"]["items"][0]["id"]
        query = "https://api.spotify.com/v1/artists/{}/top-tracks?market=US".format(artist_id)
        response = requests.get(query, headers={"Content-Type": "application/json",
                                                "Authorization": "Bearer {}".format(token)})
        response_json = response.json()
        track_info = self.top_track(response_json, token)
        #print(track_info)
        return track_info
#artist = Artist(3)
#print(artist.random_track())
