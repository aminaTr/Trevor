import speech_recognition as sr
import os
import webbrowser
import subprocess
import sys
import datetime
import openai
from config import apikey, weatherApikey, newsApikey
import random
import subprocess
import requests
import random
import pyttsx3
import redis
from sharedObject import message

r = redis.StrictRedis(host='localhost', port=6379, db=0)

chatStr = " "

folder_path = "Trevor's History"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print("Directory is created Successfully")

def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"User: {query}\n Trevor: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
     
    response_text = f"Trevor: {response['choices'][0]['text']}"
    print(response_text)
    say(response_text)
    chatStr += f"{response['choices'][0]['text']}\n"
    interaction_text = f"User: {query}\nTrevor: {response_text}"
    save_interaction(interaction_text, query)
    return response["choices"][0]["text"]

def save_interaction(text, question):
    sanitized_question = "".join(e for e in question if e.isalnum() or e == " ")
    sanitized_question = sanitized_question.replace(" ", "_")[:50]
    
    # Use the first query to create a new file for each session
    if not hasattr(save_interaction, 'file_name'):
        save_interaction.file_name = f"{sanitized_question}.txt"
    
    file_path = os.path.join(folder_path, save_interaction.file_name)
    
    try:
        with open(file_path, "a") as f:  # Use 'a' mode for appending
            f.write(text + "\n")
        print(f"Appended interaction in: {file_path}") 
    except Exception as e:
        print(f"Error saving interaction: {e}")

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for prompt: {prompt} \n************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    try:
        response_text = response["choices"][0]["text"]
        interaction_text = f"User: {prompt}\nTrevor: {response_text}" 
        print("Trying to save the interaction...")
        save_interaction(interaction_text, prompt)  
        return response_text

    except Exception as e:
        error_message = "Some Error Occurred, Sorry from TREVOR"
        interaction_text = f"User: {prompt}\nTrevor: {error_message}"
        save_interaction(interaction_text, prompt)  
        return error_message


def save_ai_response(text):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"{timestamp}_ai_response.txt"
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "w") as f:
        f.write(text)


def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    say("Choose rock, paper, or scissors.")
    user_choice = takeCommand().lower()

    if user_choice not in choices:
        say("Invalid choice. Please choose rock, paper, or scissors.")
        return

    computer_choice = random.choice(choices)
    say(f"I choose {computer_choice}.")

    if user_choice == computer_choice:
        say("It's a draw!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        say("You win!")
    else:
        say("I win!")


def guess_the_number():
    number = random.randint(1, 100)
    say("I've chosen a number between 1 and 100. Try guessing it!")
    
    attempts = 0
    while True:
        say("Please guess a number.")
        guess = int(takeCommand())
        attempts += 1

        if guess < number:
            say("Guess higher!")
        elif guess > number:
            say("Guess lower!")
        else:
            say(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

        
    
#Live weather api for latest weather news
def get_weather(city, api_key): 
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        description = weather["description"]
        return f"The current temperature in {city} is {temperature}°C with {description}."
    else:
        return data.get("message", "Error fetching weather data.")
   


#Live news api for latest news
def get_news(api_key, country="us", keyword=None):
    base_url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": country,
        "apiKey": api_key,
        "pageSize": 5 
    }
    if keyword:
        params["q"] = keyword

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["status"] == "ok":
        articles = data["articles"]
        news = [f"Headline: {article['title']}. {article['description']}" for article in articles]
        return news
    else:
        return [data.get("message", "Error fetching news data.")]


def say(text, voice="Daniel"):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()



def say_and_print(text):
    print(text)
    say(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-US")
            print(f"Speaker said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured, Sorry from TREVOR"


def calculate(expression):
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}."
    except Exception as e:
        return f"Error: {e}"


def update_message(new_message):
    global message
    message = new_message

def start():
    say_and_print("Hello I am Trevor A.I, How can I assist you?")
    while True:
        print("Listening...", end='', flush=True)
        update_message('listening')
        query = takeCommand()
        chat(query)
        sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"], ["google",
                                                                                              "https://google.com"], ["instagram", "https://instagram.com"], ["facebook", "https://facebook.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}...")
                webbrowser.open(site[1])
        if "play music" in query:
            #Add MusicPath of your computer of a song you want to play
            musicPath = "/Users/macbookair/Downloads/OTILIA - Bilionera (radio edit)-1.mp3"
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, musicPath])
            
        elif "time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strfTime}")
            # say(query)

        elif "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")

    
        elif "Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = " "

        elif "calculate" in query.lower():
            expression = query.split("calculate")[-1].strip()
            response = calculate(expression)
            say(response)
            
        elif "weather in" in query.lower():
            city = query.split("weather in")[-1].strip() # Ask Trevor "weather in......any city i.e. Islamabad"
            api_key = weatherApikey  # Replace with your own actual weather API key
            weather_report = get_weather(city, api_key)
            say(weather_report)
            
        elif "get news" in query.lower():
            keyword = None
        if "about" in query.lower():
            keyword = query.split("about")[-1].strip()  # Extract the keyword after 'about'
            api_key = newsApikey  # Replace with your own actual News API key
            news_reports = get_news(api_key, keyword=keyword)
            for report in news_reports:
                say(report)
                
        elif "play guess the number" in query.lower():
            guess_the_number()
        elif "play rock paper scissors" in query.lower():
            rock_paper_scissors()

       # else:
            # print("Chatting...")
            # chat(query)
