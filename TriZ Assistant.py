#! /usr/bin/python3

#Import Statements
import openai
from gpt import GPT
from gpt import Example
import speech_recognition as sr
import ffmpeg
from pydub import AudioSegment
from pydub.playback import play
import json
import time
from datetime import datetime
import os
import twilio
from twilio.rest import Client
import requests
#from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#import bs4
import random
import urllib.request
import urllib
import wolframalpha
import smtplib, ssl
import pyaudio
import re

import email
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from trello import TrelloClient

import os

os.environ['SDL_AUDIODRIVER'] = 'dsp'



#Object Creations
global recognizer
recognizer = sr.Recognizer()

global r
r = sr.Recognizer()
global now
now = datetime.now()
global local_time2
local_time2 = '61'


openai.api_key = "......"

global contacts
contacts = {"myself": "uspraveenraj@gmail.com","Praveen Raj U S": "uspraveenraj@gmail.com", "me":"uspraveenraj@gmail.com", "mom": "dr.umasundar@gmail.com","dad": "umayampublications@gmail.com","sister":"sivaranjanishyamsundar@gmail.com", "arun": "arunachalam.barathidasan@gmail.com", "president":"arunachalam.barathidasan@gmail.com", }

global gpt
gpt = GPT(engine="davinci",temperature=0.8,max_tokens=412)




gpt.add_example(Example('Lets shop','shopping();'))
gpt.add_example(Example('Lets Start shopping','shopping();'))
gpt.add_example(Example('Turn on shopping mode','shopping();'))
gpt.add_example(Example('scroll down','scroll_down();'))
gpt.add_example(Example('down','scroll_down();'))
gpt.add_example(Example('Give me a glance','glance();'))
gpt.add_example(Example('Keep scrolling','glance();'))
gpt.add_example(Example('Keep crawling','glance();'))
gpt.add_example(Example('search for mobile phones under fifteen thousand','search_product("mobile phones under 15000");'))
gpt.add_example(Example('search for blue laptops with eight gb ram','search_product("blue laptops with 8 gb ram");'))
gpt.add_example(Example('open redmi seven i','search_product("redmi 7i");'))
gpt.add_example(Example('open mac book air m one','search_product("mac book air m1");'))
gpt.add_example(Example('what is the customer feedback on this product','speak_out("Based on the reviews. customers feel that the camera quality is good");'))




def get_audio_1():
    #play_sound('startlistening.mp3')
    with sr.Microphone(sample_rate = 48000,chunk_size = 1024) as source:
        print("speak Now..!")
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source)
        said = ""

        try:
            
            said = r.recognize_google(audio,language='en-in')
            print(said)
            said = said.lower()
        except Exception as e:
            print("Exception: " + str(e))
    print(said)

    return said

def get_audio_2():
    #play_sound('startlistening.mp3')
    with sr.Microphone(sample_rate = 48000,chunk_size = 1024) as source:

        print("speak Now..!")
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source)
        said = ""

        try:
            
            said = r.recognize_google(audio, language='en-in')
            print(said)
            said = said.lower()
        except Exception as e:
            print("Exception: " + str(e))
    print(said)

    return said


def get_tamil_audio():
    with sr.Microphone() as source:
        print("speak Now..!")
        tamil_audio = r.listen(source)
        r.adjust_for_ambient_noise(source)
        tamil_said = ""

        try:
            tamil_said = r.recognize_google(tamil_audio, language='ta-in')
            print(tamil_said)

        except Exception as e:
            print("Exception: " + str(e))

    return tamil_said

def speak_out(speak):
    ibm_authenticator = IAMAuthenticator('A-tma_cGNP01D49kK2vU2eRPBksTcd_F4eJqhrPKTb1E')
    text_to_speech = TextToSpeechV1(authenticator=ibm_authenticator)
    text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/59d67130-f447-4280-98c4-a10aa400fda7')
    #path = ""
    #path.parent.mkdir(parents=True, esist_ok=True)
    with open(r"welcome.mp3", "wb") as audiofile:
        audiofile.write(text_to_speech.synthesize(speak,voice='en-US_MichaelV3Voice', accept='audio/mp3').get_result().content)
    play_sound('welcome.mp3')

def play_sound(sound_file):
    sound = AudioSegment.from_mp3(sound_file)
    play(sound)
    time.sleep(4)

def open_gpt_exec_assign(incoming_prompt):
    print("Inside exec assignment")
    my_str01 = incoming_prompt.split(";")
    len1 = len(my_str01);
    for it in range(len1):
        globals()['my_strr%s' % it] = my_str01[it]
    print("Out of the assignment for loop")
    open_gpt_exec(my_str01,len1)
    return my_str01,len1

def open_gpt(promptt):
    global gpt_output
    gpt_output = gpt.submit_request(promptt)
    output = gpt_output.choices[0].text
    print(output)

    if ';' in output:
        print("; was there")
        open_gpt_exec_assign(output)
    else:
        output = output.replace('output: ',' ')
        speak_out(output)


def play_music(song_name):
    #data_to = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=6LWWBLBXW1GSTIHU&field2=" + str(song_name))
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import requests
    import bs4
    import os
    import time
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    global browser
    browser = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_options)
#/home/triz/Downloads
#/usr/bin/chromedriver
    if re.search('tamil',song_name):
        play_sound('whichtamilsong.mp3')
        song_name = get_tamil_audio()
    song_base_url = "https://www.youtube.com/results?search_query="
    #ong_base_url = str(song_base_url + song_name)
    song_url = os.path.join(song_base_url, song_name)
    song_url = song_url.replace("\\","")
    browser.get(song_url)
        
    time.sleep(6)
    browser.find_element_by_id("title-wrapper").click()
    try:
        time.sleep(10)
        browser.find_element_by_class_name('ytp-ad-skip-button-container').click()
    except:
        print("No Ad 1")
    try:
        time.sleep(6)
        browser.find_element_by_class_name('ytp-ad-skip-button-container').click()
    except:
        print("No Ad 2");

    
    #time.sleep(12)
    #browser.close();

    #import ytscrape
    #from ytscrape import play_song
    #play_song(song_name) 

def shopping():
    from shopping import shopping
    shopping()

def scroll_down():
    
    from shopping import shopping,scroll_down
    scroll_down()

def glance():
    
    from shopping import shopping,scroll_down,scroll_down_continuous
    scroll_down_continuous()

def search_product(product):
    from shopping import shopping,scroll_down,scroll_down_continuous,search_product
    search_product(product)
    



def get_news(country,catagory,q):
    try:
        news_base_url = 'http://newsapi.org/v2/top-headlines?'
        news_api = 'apiKey=7980736ed0554413af17317a120b1952'
        news_url = (news_base_url + country + '&' + catagory + '&' + q + '&' + news_api)
        response = requests.get(news_url)
        article = response.json()["articles"]
        global news_results
        news_results = []

        for ar in article:
            news_results.append(ar["title"])
        for i in range(len(news_results)):
            print(i + 1, news_results[i])

        str1 = ''
        for element in news_results:
            str1 += element
            str1 += '.   '
        print(str1)
        print(type(str1))
        speak_out(str1);

    except:
        play_sound('sorrystatement.mp3')

def get_weather():
    weather_API_KEY = "f79376fe7def8edee56ac6ab5321a11d"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "Chennai"
    URL = BASE_URL + "q=" + CITY + "&appid=" + weather_API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        temperature_in_cel = float(temperature) - float(273.15)
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        Temperature_read = 'The Temperature in Chennai is' + ' ' + str(temperature_in_cel) + ' ' + 'degree celsius' + ' and there might be ' + str(report[0]['description'])
        speak_out(Temperature_read)
        time.sleep(6)
        print(f"Weather Report: {report[0]['description']}")
    else:
        # showing the error message
        print("Error in the HTTP request")
        play_sound('sorrystatement.mp3')




def set_reminder(in_time,current_time):
    local_time = current_time
    global local_time2
    local_time2 = (int(in_time) + int(local_time))
    print(local_time2)
    play_sound('addedyourreminder.mp3')

def ping():

    print("Heyy")
    pygame.mixer.music.load('remindermusic2.mp3')
    pygame.mixer.music.play()
    time.sleep(4)
    print("Turning off")
    global local_time2
    local_time2 = int(local_time2) - int(1);
    print(local_time2)

"""if 'tamil' in song_name.split():
            play_sound('whichtamilsong.mp3')
            song_name = get_tamil_audio()"""





    
    

def open_gpt_exec(my_str01,len1):
    print("Inside of open gpt exec")
    for it in range(len1):
        globals()['my_strr%s' % it] = my_str01[it]

    def add_quote(a):
        return '"{0}"'.format(a)

    exec(my_strr0)
    exec(my_strr1)

global WAKE
WAKE = "galileo";
global WAKE_2
WAKE_2 = "leo";
global WAKE_3
WAKE_3 = "gali";
global WAKE_4
WAKE_4 = "lio";
global INTER;
INTER = "pause";
global INTER2;
INTER2 = "pass";
global INTER3
INTER3 = "paas";
global INTER4
INTER4 = "stop";

current_time = now.strftime("%M")
#set_reminder(1,current_time)
#play_music('anirudh songs')
#create_insta_caption('An insta caption for a pic of taking responsibility as a leader')


if __name__ == '__main__':
    while True:

        if re.search(str(local_time2),str(current_time)):
            ping()

        print("Listening")
        text_1 = get_audio_1()
        current_time = now.strftime("%M")
        



#if text.count(WAKE) > 0:
        if re.search(str(WAKE),str(text_1)):
            #play_sound('startlistening.mp3')
            print("I am ready")
            play_sound('hello_name.mp3')
            
            text = get_audio_2()
            play_sound('stoplistening.mp3')
            #play_sound('onnit.mp3')
            open_gpt(str(text))
            print("Done Listening")

        elif re.search(str(WAKE_2),str(text_1)):
            #play_sound('startlistening.mp3')
            print("I am ready")
            play_sound('hello_name.mp3')
            
            text = get_audio_2()
            play_sound('stoplistening.mp3')
            #play_sound('onnit.mp3')
            open_gpt(str(text))
            print("Done Listening")

        elif re.search(str(WAKE_3),str(text_1)):
            #play_sound('startlistening.mp3')
            print("I am ready")
            play_sound('hello_name.mp3')
            
            text = get_audio_2()
            play_sound('stoplistening.mp3')
            #play_sound('onnit.mp3')
            open_gpt(str(text))
            print("Done Listening")
  
        elif re.search(str(WAKE_4),str(text_1)):
            #play_sound('startlistening.mp3')
            print("I am ready")
            play_sound('hello_name.mp3')
            
            text = get_audio_2()
            play_sound('stoplistening.mp3')
            #play_sound('onnit.mp3')
            open_gpt(str(text))
            print("Done Listening")

        elif re.search(str(INTER),str(text_1)):
            play_sound('stoplistening.mp3')
            print("INTERRUPTED")
            browser.close();
            print("Done Listening")

        elif re.search(str(INTER2),str(text_1)):
            play_sound('stoplistening.mp3')
            print("INTERRUPTED")
            browser.close();         
            print("Done Listening")

        elif re.search(str(INTER3),str(text_1)):
            play_sound('stoplistening.mp3')
            print("INTERRUPTED")
            browser.close();         
            print("Done Listening")

        elif re.search(str(INTER4),str(text_1)):
            play_sound('stoplistening.mp3')
            print("INTERRUPTED")
            browser.close();         
            print("Done Listening")

        if str(local_time2) in current_time:
            ping()


