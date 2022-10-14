from os import environ as env
import tweepy
import re

# Twitter Tokens

api_key = env["API_KEY"]
api_secret = env["API_KEY_SECRET"]

# Get Twitter content from user

def get_tweets(username, max_results):
    """Function gets tweets from specified user's timeline.

    Args:
        username (str): The Twitter user whose tweets will be analyzed

        max_results (int): The maximum number of tweets to get. (max: 3200)

    Returns:
        list: text of up to 3200 tweets in a list of strings.
    """

    auth = tweepy.AppAuthHandler(api_key, api_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True) 
    tweets = tweepy.Cursor(api.user_timeline, screen_name=username, 
                           count=200).items(max_results)

    all_tweets = []

    for tweet in tweets:
        tweet = tweet.text.lower()
        all_tweets.append(tweet)

    return all_tweets


def word_counter(text_str):
    """Function that counts word frequency in a text string.

    Args:
        text_str (str): Any text, group of strings, etc.

    Returns:
        list: list of tuples that contain the word and the number of uses.
    """

    text_str = str(text_str)
    results_list = []
    frequency = {}

    regex = r"[@#]*[a-z]*[']*[a-z]\b[^\"';:.,?! ]*"

    matches = re.findall(regex, text_str, re.MULTILINE | re.IGNORECASE)
    
    # match_pattern = re.findall(r"[#@]*[a-z]{3,20}[']*[a-z]*", text_str) 

    blacklisted = [
        "a", "to", "is", "if", "of", "an", "as", "or", "in", "on", "be", "and", 
        "rt", "t", "the", "that", "this", "for", "it", "so", "http", "https",
        "n\\nhttps", "are", "was", "m", "have", "has", "had", "re", "at", "by", 
        "c"
        ]

    for word in matches:
        if word not in blacklisted:
            count = frequency.get(word, 0)
            frequency[word] = count + 1

    most_frequent = dict(sorted(frequency.items(), 
                         key=lambda elem: elem[1], reverse=True))

    frequency_list = most_frequent.keys()

    for words in frequency_list:
        final_count = (words, frequency[words])
        results_list.append(final_count)

    return results_list

def evaluator(user, max_tweets, max_display):
    """Function combines get_tweets() and word_counter() to display 
       evaulated reuslts.

    Args:
        user (str): Twitter user's handle
        max_tweets (int): Maximum number of tweets to be evaluated (max: 3200)
        max_display (int): Maximum number of words to be displayed

    Returns:
        str: Displays results
    """
    tweets = get_tweets(user, max_tweets)
    results = word_counter(tweets)
    
    title = (f"Unique Words In Tweets: {len(results)}\n"
              "Top Words In Tweets:\n")
    words = ""

    for item in results[0:max_display]:
        word = f"\n{item[0]} - {item[1]}"
        words += word
    # breakpoint()
    return title + words    

if __name__ == "__main__":
    print(evaluator("MalleyNathan", 3200, 50))
    
