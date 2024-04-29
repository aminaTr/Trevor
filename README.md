TREVOR_OpenAI_VoiceAssistant

Introduction:

Trevor A.I is a voice-activated personal assistant developed to assist users in various tasks, ranging from answering questions and playing music to fetching the latest weather and news updates.

Installation:

Before running Trevor, make sure you have the following dependencies installed:

1. Python: [Download Python](https://www.python.org/downloads/)

2. Required Python Libraries:

   - speech_recognition:  
     
     pip install SpeechRecognition
     

   - openai:  
     
     pip install openai

 
   - OpenWeatherMap & NewsAPI Accounts: 
   
     To fetch weather details and news respectively.
     
Required Python libraries: speech_recognition, os, webbrowser, subprocess, datetime, openai, requests, random.

3. Config File: Create a file named `config.py` with your OpenAI API key. The content should be:
   ```python
   apikey = "YOUR_API_KEY"


TREVOR is a voice assistant powered by OpenAI. It can perform a range of tasks, including:

    Chat with Users
        Engage in conversations with users based on prompts.
        Utilizes OpenAI's GPT-3 model for natural language processing.

    Voice Responses
        Responds to user queries or prompts with speech output.
        Uses the macOS say command to generate voice responses.

    Web Browsing
        Opens websites based on user requests.
        Supports popular websites like YouTube, Wikipedia, Google, Instagram, and Facebook.

    Music Playback
        Plays music from a specified local file path.
        Supports macOS and Linux systems.
        (Note: Add your own musicPath of the song you want to play)


    Time Information
        Provides the current time.

    Launch FaceTime (For mac users only)
        Opens the FaceTime application on macOS.

    Artificial Intelligence Queries
        Utilizes OpenAI's GPT-3 to respond to prompts related to artificial intelligence. Engage in meaningful conversation using the power of GPT-3.

    Simple Calculations
        Performs basic arithmetic calculations.

    Games: 
        Play games like "Guess the Number" and "Rock Paper Scissors".

    Conversational Chat: 
        Engage in a dynamic conversation with Trevor, backed by OpenAI's powerful GPT-4 model.

    Web Services:
        Open popular websites like YouTube, Google, Instagram, etc., on voice command.
        Fetch live weather updates for any city.
        Retrieve the latest news headlines.

    Utilities:
        Ask the current time.
        Launch FaceTime.
        Engage in small text-based games like "Rock, Paper, Scissors" and "Guess the Number".
        Perform simple arithmetic calculations.

    Interaction History: 
        All interactions with Trevor are saved in a dedicated folder for later reference. History folder contains all the Trevor's history to access those content later on.

How to Use:

    Dependencies:
        openai: For accessing the OpenAI GPT-3 API.
        requests: For making HTTP requests.
        speech_recognition: To recognize voice commands.
        Python 3: The assistant is written in Python.
        OpenAI Account: Required for GPT-3 based chat.
        OpenWeatherMap & NewsAPI Accounts: To fetch weather details and news respectively.

    Installation
        Install the required Python packages.

    Configuration
        Set up the API keys by creating a config.py file with your API keys.

    Running the Assistant
        Execute python main.py to start the voice assistant.

    Voice Commands
        Interact with TREVOR by speaking commands or prompts.

    OPEN AI API Key:
        Use your own OPEN AI API Key in config.py because Our project, Trevor, relies on the OpenAI API to enable advanced natural language processing capabilities. The API serves as the backbone of Trevor's conversational abilities, allowing it to generate responses based on user queries. To use the OpenAI API, you'll need to obtain an API key from OpenAI. This key serves as a secure way to authenticate requests made from our application to the OpenAI servers. It ensures that Trevor can access the full range of language processing features provided by OpenAI. To obtain your own API key, visit the OpenAI Developer platform and follow the steps outlined in their documentation. Once you have your API key, you can integrate it with our project to start using Trevor's advanced language processing capabilities. It's crucial to treat your API key with care. Avoid sharing it publicly or storing it in easily accessible locations. Consider using environment variables or a secure configuration management system to keep your API key safe. 

    For more detailed information on using the OpenAI API, refer to the [OpenAI Developer Documentation](https://platform.openai.com/docs).

    OpenWeatherMap API Key: 
        This key provides access to the weather data for various cities. It is used for getting live weather data of any city.
        Usage: Inside the get_weather function as api_key.

    News API Key: 
        This key provides access to the news data. It is used for getting live news data for any field like Technology.
        Usage: Inside the get_news function as api_key. It is used to fetch the latest news.
        Usage: Inside a function like get_news.

Note: Use your own API Keys for OpenAI, Weather and news.
      You can add your own API Keys in the file named config.py.


Usage Examples:

    "Open YouTube" - Opens the YouTube website.
    "Play music" - Plays a specified music file.
    "What's the time?" - Provides the current time.
    "Tell me about artificial intelligence" - Provides information about AI.

Important Notes:

    Be cautious with voice commands, especially when performing tasks like calculations or opening websites.

Acknowledgements:

    This project utilizes OpenAI's GPT-3 for natural language processing.
    Voice responses are generated using the macOS say command.


Tasks that TREVOR can perform:
You can ask Trevor a wide range of questions and give it various prompts. Here are some examples of questions and prompts you can try:

Change Gender of Trevor:
    You can also change the gender of voice assistant to male or female
    Select "Daniel" for male 
    Select "Samantha" for female 
    in the "say" function.

1. General Questions:
   - "What's the weather like today?"
   - "Who is the president of France?"
   - "How far is the moon from Earth?"

2. Conversational Prompts:
   - "Tell me a joke."
   - "What's your favorite movie?"
   - "How are you feeling today?"

3. Informational Requests:
   - "Define the word 'supercalifragilisticexpialidocious'."
   - "Give me a brief overview of the French Revolution."
   - "What is the capital of Japan?"

4. Mathematical Queries:
   - "What is the square root of 144?"
   - "Calculate 25 times 4."

5. Technology and AI:
   - "Explain artificial intelligence in simple terms."
   - "What are the applications of machine learning?"

6. Entertainment:
   - "Recommend a good book to read."
   - "What are some popular movies released this year?"

7. Open Websites:
   - "Open YouTube."
   - "Take me to Wikipedia."
   - "Open Google"
   - "Open Instagram"
   - "Open Facebook"

8. Time and Date:
   - "What time is it?"
   - "What's the date today?"

9. Voice Commands:
   - "Open FaceTime."
   - "Play some music."

10. Creative Writing Prompts:
    - "Write a short story about a mysterious island."
    - "Compose a poem about the beauty of nature."

11. Chat:
    - Any other general question or statement will trigger a chat response from Trevor using the OpenAI GPT-3 API.

12. Reset Chat with Trevor:
    - "Reset chat"

13. Exit the Program:
    - "Quit"

Remember, Trevor's responses will be generated based on the capabilities of the underlying OpenAI model. Feel free to experiment with different prompts and questions to explore its capabilities further. If you extend the code with more functionalities, Trevor's capabilities will also expand.

    Security:
        Do not expose your API keys. Store them securely, avoid hard-coding them directly, and do not commit them to version control.

    Caution:
        Trevor may produce inaccurate information about people, places, or facts.


Note for windows users:

Certainly! Here are some notes and considerations specifically for Windows users who might want to use the provided code:

1. Playing Music: 
    - The code uses `open` for MacOS and `xdg-open` for Linux to play music. For Windows, you might want to use `start` to open a file with its default application. Modify the `play_music` function accordingly.

2. Voice Synthesis (`say` function): 
    - The code uses MacOS's `say` command to convert text to speech. Windows users can use the `pyttsx3` library as an alternative. You'll need to install it (`pip install pyttsx3`) and modify the `say` function.

3. Microphone Access:
    - Ensure that you have given the necessary permissions for Python to access the microphone. Also, ensure that the microphone is working and set as the default recording device.

4. Path Notation:
    - Windows uses a different path notation (`\` instead of `/`). Make sure to use raw string notation for paths, like `r"C:\Users\yourname\path\to\file.mp3"`.

5. API Keys:
    - Store API keys securely. The `config.py` file contains your OpenAI API key. Ensure it's kept safe and not shared. Avoid publishing your code with this file.

6. Dependencies:
    - Ensure you've installed all necessary libraries using pip. For speech recognition, you might need `pyaudio`. Sometimes, installing `pyaudio` can be problematic on Windows. Consider using a precompiled binary (`pip install pipwin`, followed by `pipwin install pyaudio`).

7. Running as Admin:
    - Some operations, like modifying system settings or accessing certain files, might require you to run the script as an administrator.

8. FaceTime:
    - The code has a command to open FaceTime, which is exclusive to Apple devices. Windows users can replace this with a command to open Skype, Zoom, or another preferred video-calling application.

9. Error Handling:
    - Be sure to have proper error handling in place, especially when working with file paths, internet connections, and third-party APIs.

10. Testing:
    - Before fully relying on the application, do a thorough test of all functions to ensure they operate as expected on a Windows machine.

By considering these notes, Windows users can adapt and get the most out of the provided code.
Thankyou.