from flask import Flask, render_template, redirect, request
import json
from artist import Artist, artist_ids
import random
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    try:
        if request.method == 'POST' and "refresh" in request.form:
            i = random.randint(0, len(artist_ids)-1)
            artist = Artist(i)
            a = artist.random_track()
            print(a)
        elif request.method == 'POST' and "search_lyrics" in request.form: #redirects to genius url
            try:
                name = request.form['artist']
                song = request.form['track']
                artist = Artist(None, song, name)
                url = artist.lyrics()
                if url == None:
                    i = random.randint(0, len(artist_ids)-1) #CHANGE THIS SO RANDOM METHOD TAKES PARAMETER INSTEAD OF CREATING NEW ARTIST
                    artist = Artist(i)
                    a = artist.random_track()
                    return render_template('index.html', artist=a, lyric_error=True)
                else:
                    return redirect(url)
            except:
                print("Baby Shark working")
                return redirect("https://genius.com/Pinkfong-baby-shark-lyrics")
        else:
            i = random.randint(0, len(artist_ids)-1)
            artist = Artist(i)
            a = artist.random_track()
            print(a)
        return render_template('index.html', artist=a)
    except:
        print("Baby Shark")
        track_info = {"artist": "Pink Fong", "album": "Baby Shark", "track": "Baby Shark", "image": "https://cdns-images.dzcdn.net/images/cover/9d42e4daa95703c8665b72208d7b11fe/264x264.jpg", "preview": "/static/baby_shark.mp3"}
        return render_template('index.html', artist=track_info)
    

if __name__ == "__main__":
    app.run(port = int(os.getenv('PORT', 5000)),
            host = os.getenv('IP', '0.0.0.0'),
            debug = True
            )
