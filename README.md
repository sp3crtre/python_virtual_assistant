#Virtual-Assistant
<p>  Scarlet is a custom-built, open-source virtual assistant that was developed using the programming language Python. I created this software as part of a human-computer interaction (HCI) research project at our school. HCI is a field that studies how people interact with computers and how to design technologies that are easy and effective for people to use. By creating Scarlet, I was able to explore and research different ways in which virtual assistants can be used to improve the user experience. However, this project is still under development and is not yet fully functional. I am working to incorporate machine learning and other features to make it more useful for users. This code appears to be a Python script that uses a variety of libraries and APIs to implement a virtual assistant. The script initializes a text-to-speech engine using the pyttsx3 library and sets various properties such as the voice and speaking rate. It then uses the speech_recognition library to listen for audio input from the user, and uses the recognize_google function to convert the audio to text.

The script then reads in data from a JSON file called 'scarlet_brain.json' and uses this data to define a number of commands and corresponding responses for the virtual assistant. The script also uses the wikipedia library to provide summaries of Wikipedia articles based on user input, and the spotipy library to search for and play songs on Spotify.

The script also uses the openai library to generate responses using the OpenAI GPT-3 language model, and the requests library to make HTTP requests to external APIs. The script also uses the webbrowser library to open a song in the user's web browser when the user asks the virtual assistant to play a song.

Finally, the script enters a loop that listens for and processes user input indefinitely, unless the user asks the virtual assistant to exit or the script encounters an error. I hope this helps clarify the purpose and functionality of the code. Let me know if you have any other questions! </p>
 
<h1>Feature</h1>
<ul>
  <li> Natural language processing: the ability to understand and respond to user input in a human-like way, using natural language rather than specific commands.</li>
  <li>Text-to-speech and speech-to-text: the ability to convert text to spoken words and vice versa, allowing users to communicate with the assistant using their voice.</li>
  <li> Information retrieval: the ability to search for and provide information on a wide range of topics, such as news, weather, and general knowledge.
</li>
  <li>Task completion: the ability to perform various tasks and activities on behalf of the user, such as setting reminders, making reservations, and sending emails.</li>
  <li> Personalization: the ability to learn and adapt to the user's preferences, habits, and interests, in order to provide a more personalized experience.
</li>
  <li> Integration with other devices and services: the ability to connect with and control other devices and services, such as smart home systems and messaging apps.</li>
</ul>


<h1>Requirements:</h1>
<p>The first step is to install some Python dependencies using pip install</p>

```
pip install -r requirements.txt
```

<h1>Usage:</h1>

#LINUX
```python
python3 main_scarlet.py 
```

#WINDOW
```python
py main_scarlet.py
```


