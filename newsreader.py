
# Article reading
import requests
import json
#speaking function
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today.. Lets begin")
    #url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=d093053d72bc40248998159804e0e67d"
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=4404060df36a4b419e108c42b65eaf1d"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        print(article['title'])
        speak(article['title'])
        speak("Moving on to the next news..Listen Carefully")

    speak("Thanks for listening...")


