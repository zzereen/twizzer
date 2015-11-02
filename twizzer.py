from TwitterAPI import TwitterAPI
import tweepy, json, os, sys, time

#set directory to application folder and database folder
MY_DIR  = os.path.realpath(os.path.dirname(__file__))
DATA_DIR = os.path.join(MY_DIR, 'db')

#load consumer data from database folder
if not os.path.exists(os.path.join(DATA_DIR, 'consumerdb.txt')):
    print("PLEASE PUT IN CONSUMER KEY AND DATA IN consumerdb.txt")
    sys.exit()
#assign consumer key and secret
else:
    load_file = open(os.path.join(DATA_DIR, 'consumerdb.txt'),"r")
    loaddata = json.load(load_file)
    load_file.close()
    consumer_key = loaddata['consumer_key']
    consumer_secret = loaddata['consumer_secret']

#load access token and secret
if not os.path.exists(os.path.join(DATA_DIR, 'accessdb.txt')):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    print('authorize app: \n' + auth.get_authorization_url())
    verifier = input('\ncode:')
    auth.get_access_token(verifier)
    access_token = auth.access_token
    access_token_secret = auth.access_token_secret
    save_file = open(os.path.join(DATA_DIR, 'accessdb.txt'),"w")
    savedata = {'access_token':access_token,'access_token_secret':access_token_secret}
    json.dump(savedata,save_file)
    save_file.close()
#assign access token and secret
else:
    load_file = open(os.path.join(DATA_DIR, 'accessdb.txt'),"r")
    loaddata = json.load(load_file)
    load_file.close()
    access_token = loaddata['access_token']
    access_token_secret = loaddata['access_token_secret']


#create instance to access api
api = TwitterAPI(consumer_key,consumer_secret,access_token,access_token_secret)

#class to get user input
class Listener:
    def numberInput():
        result = input("input >>> ")
        try :
            result = int(result)
        except ValueError :
            print("Invalid Input")
        return result
    def textInput():
        result = input("input >>> set status: ")
        return(result)

#class containing all timeline functions
class Twizzer:

    #retrieve home timeline and display
    def home_timeline(self):
        tweet_strings = []
        try:
            timeline = api.request('statuses/home_timeline',{'count':20})
            for item in timeline:
                tweet_strings.append(item['user']['name'] + ": \n" + item['text'] + "\n")
            print("\n                            ***************************************************TIMELINE****************************************************")
            if len(retweet_tweet_strings) == 0 :
                print("                                                                                 EMPTY")
            else :
                for tweet in tweet_strings:
                    try:
                        print(tweet)
                        time.sleep(1)
                    except:
                        print("********** Tweet not supported ********* \n")
            print("""                            ***************************************************************************************************************
                                                                              1) Refresh
                                                                              2) Go Back
    """)
            while True:
                option = Listener.numberInput()
                if option == 1 :
                    Twizzer().home_timeline()
                elif option == 2 :
                    WelcomeScreen()
                else :
                    print("Invalid Selection")
        except:
            print("\n ERROR CONNECTING TO TWITTER!")

    #retrieve retweet timeline and display
    def retweet_timeline(self):
        retweet_tweet_strings = []
        try :
            timeline = api.request('statuses/retweets_of_me',{'count':20})
            for item in timeline:
                retweet_tweet_strings.append(item['user']['name'] + ": \n" + item['text'] + "\n")
                print("\n                            ***************************************************RETWEETS****************************************************")
                if len(retweet_tweet_strings) == 0 :
                    print("                                                                                 EMPTY")
                else :
                    for tweet in retweet_tweet_strings:
                        try:
                            print(tweet)
                            time.sleep(1)
                        except:
                            print("********** Tweet not supported ********* \n")
                            print("""                            ***************************************************************************************************************
                                                                            1) Refresh
                                                                            2) Go Back
""")
            while True:
                option = Listener.numberInput()
                if option == 1 :
                    Twizzer().retweet_timeline()
                elif option == 2 :
                    WelcomeScreen()
                else :
                    print("Invalid Selection")

        except:
            print("\n ERROR CONNECTING TO TWITTER!")


    #retrieve mention timeline and display
    def mention_timeline(self):
        mention_tweet_strings = []
        timeline = api.request('statuses/mentions_timeline',{'count':20})
        try :
            for item in timeline:
                mention_tweet_strings.append(item['user']['name'] + ": \n" + item['text'] + "\n")
                print("\n                            ***************************************************MENTIONS****************************************************")
                if len(retweet_tweet_strings) == 0 :
                    print("                                                                                 EMPTY")
                else :
                    for tweet in mention_tweet_strings:
                        try:
                            print(tweet)
                            time.sleep(1)
                        except:
                            print("********** Tweet not supported ********* \n")
                            print("""                            ***************************************************************************************************************
                                                                            1) Refresh
                                                                            2) Go Back
""")
            while True:
                option = Listener.numberInput()
                if option == 1 :
                    Twizzer().mention_timeline()
                elif option == 2 :
                    WelcomeScreen()
                else :
                    print("Invalid Selection")
        except :
            print("\n ERROR CONNECTING TO TWITTER!")

    #retrieve user timeline and display
    def profile_timeline(self):
        profile_tweet_strings = []
        timeline = api.request('statuses/user_timeline',{'count':20})
        try :
            for item in timeline:
                profile_tweet_strings.append(item['user']['name'] + ": \n" + item['text'] + "\n")
                print("\n                            ****************************************************PROFILE****************************************************")
                if len(retweet_tweet_strings) == 0 :
                    print("                                                                                 EMPTY")
                else :
                    for tweet in profile_tweet_strings:
                        try:
                            print(tweet)
                            time.sleep(1)
                        except:
                            print("********** Tweet not supported ********* \n")
                            print("""                            ***************************************************************************************************************
                                                                          1) Refresh
                                                                          2) Go Back
""")
            while True:
                option = Listener.numberInput()
                if option == 1 :
                    Twizzer().profile_timeline()
                elif option == 2 :
                    WelcomeScreen()
                else :
                    print("Invalid Selection")
        except :
            print("\n ERROR CONNECTING TO TWITTER!")


    #post status
    def post_status(self):
        status = Listener.textInput()
        api.request('statuses/update',{'status': status})
        print("\n                            ****************************************************SUCCESS****************************************************")
        print("""
                                                                          1) Go Back
""")
        option = Listener.numberInput()
        if option == 1 :
            WelcomeScreen()


#class containing all homescreen fuctions
class WelcomeScreen:
    def __init__(self):
        print("""

                            ***************************************************************************************************************


                                                        ████████╗██╗    ██╗██╗███████╗███████╗███████╗██████╗
                                                        ╚══██╔══╝██║    ██║██║╚══███╔╝╚══███╔╝██╔════╝██╔══██╗
                                                           ██║   ██║ █╗ ██║██║  ███╔╝   ███╔╝ █████╗  ██████╔╝
                                                           ██║   ██║███╗██║██║ ███╔╝   ███╔╝  ██╔══╝  ██╔══██╗
                                                           ██║   ╚███╔███╔╝██║███████╗███████╗███████╗██║  ██║
                                                           ╚═╝    ╚══╝╚══╝ ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝


                                                                                   ████████
                                                                                   ███▄███████
                                                                                   ███████████
                                                                                   ███████████
                                                                                   ██████
                                                                                   █████████
                                                                         █       ███████
                                                                         ██    ████████████
                                                                         ███  ██████████  █
                                                                         ███████████████
                                                                         ███████████████
                                                                          █████████████
                                                                           ███████████
                                                                             ████████
                                                                              ███  ██
                                                                              ██    █
                                                                              █     █
                                                                              ██    ██

                                                                          created by shazrin

                                                                             version 2.1


                            ***************************************************************************************************************
                                                                          1) Home timeline
                                                                          2) Retweet timeline
                                                                          3) Mentions timeline
                                                                          4) Profile timeline
                                                                          5) Post status
                                                                          6) Quit :(

""")
        while True:
            option = Listener.numberInput()
            if option == 1 :
                Twizzer().home_timeline()
            elif option == 2 :
                Twizzer().retweet_timeline()
            elif option == 3 :
                Twizzer().mention_timeline()
            elif option == 4 :
                Twizzer().profile_timeline()
            elif option == 5 :
               Twizzer().post_status()
            elif option == 6 :
                quit()
            else :
                print("Invalid Selection")

#so called main thread
if __name__ == "__main__":
   WelcomeScreen()
