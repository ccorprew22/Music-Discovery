# Technologies, Frameworks, Libraries, and APIs
+ Flask, Requests, json, python-dotenv, and urllib.request
+ Spotify API and Genius API
+ Use pip install "PYTHON_MODULE"

# Setup
+ Create .env file in your project directory
+ Create a Spotify developer account to obtain a client_id and secret key
+ Base 64 encode your client id and secret key in this format: client_id:client_secret.
+ Add your base64 encoded string to your .env file and write export base64='YOUR_KEY_HERE'

# How to Run Application
+ Run python app.py 
+ Enter "/" or "localhost:8080"

# How to deploy

# Technical Issues
1. Not every song had a song preview, which would break the app. So I wrote the function to either return None or a string with the preview url. If it was None, it would display an error message to the user.
2. On mobile devices the page would look very out of proportion, to fix this I included a meta tag link that scales the app to device screen sizes. Reference https://stackoverflow.com/questions/32782454/how-can-i-make-an-html-page-automatically-fit-mobile-device-screens

# Known Problems/Acknowledgements
1. When parsing the JSON file sent through the Genius API, there are times when no url is found or it is provided with a url that redirects the user to a non-English speaking version of genius.com.
2. As of right now, the artist history is saved across all users. In the future I would try to make it so that each user gets their own history list.
3. On mobile devices, the displays are responsive but are not centered correctly for each device size.
4. The parsing method that I used to find the song lyrics works most of the time, but occasionally returns no url or the wrong song url.
5. If the page is taking too long to load and if you press a button without waiting, sometimes the default error song page is displayed because not all the background information is ready.

# How would I improve my project
+ I would like to make it responsive amongst all devices, and I would like to connect it to user's spotify accounts so that they can add the song to their playlist.
+ To fix the issue of the recent played songs being shared with all users, I would use some kind of module that handles session variables.
