# Music Discovery Application

## Heroku Link
https://powerful-atoll-61635.herokuapp.com/

## Technologies, Frameworks, Libraries, and APIs
+ Modules: Flask, Requests, json, python-dotenv, and urllib.request
+ Spotify API and Genius API
+ Use `pip install "PYTHON_MODULE"`

## Setup
1. Create `.env` file in your project directory
2. Create a Spotify developer account and follow the instructions to obtain a client id
3. Base 64 encode your client id and secret key in this format: client_id:client_secret.
4. Add your base64 encoded string to your .env file and write `export base64='YOUR_KEY_HERE'`

## How to Run Application
+ Run `python app.py`
+ Enter "/" or "localhost:8080"

## How to deploy
1. Create Heroku account at https://signup.heroku.com/login
2. In your terminal, enter `npm install -g heroku` to install Heroku CLI.
3. Create a `requirements.txt` file and `pip freeze > requirements.txt` to put all your installed python dependencies into the file.
4. Create a `Procfile` and write `python app.py`, which is the command needed to run the program.
5. Commit all of your changes with git
6. Log into Heroku in your terminal with `heroku login -i`
7. Create a Heroku app with `heroku create`
8. Push your code to Heroku with `git push heroku main`
9. Go to https://dashboard.heroku.com/apps and click your App, then go to Settings, and click "Reveal Config Vars"
10. Enter in your variables that are in your `.env` file
11. Go to Resources and make sure that the switch is turned on next to `web python app.py`.
12. Your app is deployed to the internet

## Technical Issues
1. Not every song had a song preview, which would break the app. So I wrote the function to either return None or a string with the preview url. If it was None, it would display an error message to the user.
2. On mobile devices the page would look very out of proportion, to fix this I included a meta tag link that scales the app to device screen sizes. Reference https://stackoverflow.com/questions/32782454/how-can-i-make-an-html-page-automatically-fit-mobile-device-screens
3. The application would not update when changes were made to the css file. To fix this, I added `app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0` after `app = Flask(__name__)` to essentially disable caching in Flask. Reference https://stackoverflow.com/questions/34066804/disabling-caching-in-flask
4. To address the issue of the application not fitting if the browser window size changed, I used a the `@media only screen and (max-width: 800px)` to change the css for the html if the window size is less than 800px. Reference https://www.w3schools.com/cssref/css3_pr_mediaquery.asp

## Known Problems/Acknowledgements
1. When parsing the JSON file sent through the Genius API, there are times when no url is found or it is provided with a url that redirects the user to a non-English speaking version of genius.com.
2. As of right now, the artist history is saved across all users. In the future I would try to make it so that each user gets their own history list.
3. On mobile devices, the displays are responsive but are not centered correctly for each device size.
4. The parsing method that I used to find the song lyrics works most of the time, but occasionally returns no url or the wrong song url.
5. If the page is taking too long to load and if you press a button without waiting, sometimes the default error song page is displayed because not all the background information is ready.
6. If a song name is too long, the song name may start to extend off the history display.

## How would I improve my project
+ I would like to make it responsive amongst all devices, and I would like to connect it to user's spotify accounts so that they can add the song to their playlist.
+ To fix the issue of the recent played songs being shared with all users, I would use some kind of module that handles session variables.
