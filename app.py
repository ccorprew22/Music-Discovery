from flask import Flask, render_template, redirect, request
import json
from artist import Artist, artist_ids
import random
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

global artist_hist
artist_hist = []
@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    global artist_hist
    a = None
    try:
        if request.method == 'POST' and "refresh" in request.form: #refresh
            i = random.randint(0, len(artist_ids)-1)
            artist = Artist(i)
            a = artist.random_track()
            print(a)
        elif request.method == 'POST' and "search_lyrics" in request.form: #redirects to genius url
            name = request.form['artist']
            song = request.form['track']
            artist = Artist(None, song, name)
            url = artist.lyrics()
            if url != None:
                return redirect(url)
            else:
                print("Lyrics not found")
                i = random.randint(0, len(artist_ids)-1) #CHANGE THIS SO RANDOM METHOD TAKES PARAMETER INSTEAD OF CREATING NEW ARTIST
                artist = Artist(i)
                a = artist.random_track()
                return render_template('index.html', artist=a,history=artist_hist, length=len(artist_hist), lyric_error=True)
        elif request.method == 'POST' and "search-btn" in request.form: #searches for input artist
            try:
                name = request.form['artist_input']
                artist = Artist(None, None, name)
                a = artist.search()
                #return render_template('index.html', artist=a, history=artist_hist, length=len(artist_hist))
            except:#This except function has an error message with the redirect
                track_info = {"artist": "Pinkfong", "album": "Baby Shark Special", "track": "Baby Shark", "image": "/static/baby_shark.jpg", "preview": "/static/baby_shark.mp3"}
                return render_template('index.html', artist=track_info, error=True, history=artist_hist, length=len(artist_hist))
        elif request.method == 'POST' and "recent" in request.form: #replays song from history
            index = int(request.form['index'])
            a = artist_hist[index]
            print(a)
            #return render_template('index.html', artist=a, history=artist_hist, length=len(artist_hist))
        else: #Random song 
            i = random.randint(0, len(artist_ids)-1)
            artist = Artist(i)
            a = artist.random_track()
            print(a)
        #Adds to artist history list
        if a not in artist_hist:
            if len(artist_hist) == 5:
                artist_hist.pop(0)
                artist_hist.append(a)
            else:
                artist_hist.append(a)
        print(artist_hist)
        print(len(artist_hist))
        return render_template('index.html', artist=a, history=artist_hist, length=len(artist_hist))
    except: #if something doesn't work
        print("Baby Shark")
        track_info = {"artist": "Pink Fong", "album": "Baby Shark", "track": "Baby Shark", "image": "https://cdns-images.dzcdn.net/images/cover/9d42e4daa95703c8665b72208d7b11fe/264x264.jpg", "preview": "/static/baby_shark.mp3"}
        return render_template('index.html', artist=track_info)
    

if __name__ == "__main__":
    app.run(port = int(os.getenv('PORT', 5000)),
            host = os.getenv('IP', '0.0.0.0'),
            debug = True
            )
