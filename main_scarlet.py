import speech_recognition as sr
import pyttsx3, os, requests, json, random
import openai, wikipedia, time, os
import json, spotipy, webbrowser

#pyttsx3 api
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 140)
engine.setProperty('volume', 1.0)


r = sr.Recognizer()

t = time.strftime("%I:%M %p")

while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 0.2)
        print("listening....................")
        print("Talking....................")
        audio_text = r.listen(source)
        print("\n")

    with open('scarlet_brain.json', 'r') as f:
        data = json.load(f)

    try:
        def speak(command):
            engine = pyttsx3.init()
            engine.say(command)
            engine.runAndWait()

        words = r.recognize_google(audio_text)

        if words == data['cmd1']:
            speak(random.choice(data['query1']))

        elif words == data['cmd2']:
            speak(data['query2'])

        elif words == data['cmd3'] or words == data['cmd3.1']:
            speak(data['query3'])   

        elif words == data['cmd4']: 
            speak(data['query4'])

        elif words == data['cmd5']:
            continue

        elif words == data['cmd6']:
            _time_check = f"{data['query10']} {t}"
            speak(_time_check)
        
        elif words == data['cmd7']:
            speak(data['query8'])

        elif words == data['cmd8']:
            speak(data['query9'])
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration = 0.2)
                print("listening....................")
                print("Talking....................")
                audio_text = r.listen(source)
                print("\n")
                print(audio_text)
                _wiki = wikipedia.summary(audio_text)
                speak(_wiki)

        elif words == data['cmd9']:
            #spotify api
            username = '31o4qxbgg2n55ol4qrq3wesor7hu'
            clientID = 'c59a699f709442c1a679dc08e739713c'
            clientSecret = 'b4b4bbffe63f466eb1e6fbd12ad415bb'
            redirect_uri = 'http://google.com/callback/'

            oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
            token_dict = oauth_object.get_access_token()
            token = token_dict['access_token']
            spotifyObject = spotipy.Spotify(auth=token)
            user_name = spotifyObject.current_user()
            
            search_song = words[17:]
            results = spotifyObject.search(search_song, 1, 0, "track")
            songs_dict = results['tracks']
            song_items = songs_dict['items']
            song = song_items[0]['external_urls']['spotify']
            webbrowser.open(song)
            speak('Song has opened in your browser.')
                      
        elif words == data['cmd10']:
            speak()

        elif words == data['cmd11']:
            speak(data['query7'])

        elif words == data['cmd0']:
            speak(data['query0'])
            speak('in three')
            speak('two')
            speak('one')
            break

        elif words not in data:
            ask = f"{words[7:]}."
            Api_Key = openai.api_key_path = "apikey.txt"
            openai.api_key = os.getenv(Api_Key)
            response = openai.Completion.create(
                engine = "text-davinci-003",
                prompt = ask,
                temperature = 0.7,
                max_tokens = 203,
                top_p = 1,
                frequency_penalty = 0,
                presence_penalty = 0

            )
            
            print(response.choices[0].text)
            speak(response.choices[0].text)

        else:
            speak(data['query5'])

    except sr.UnknownValueError:
        speak("Sorry, I did not get that")

    except sr.RequestError:
        speak("No internet connection")
        speak("Try Checking the network cables, modem, and router")
        