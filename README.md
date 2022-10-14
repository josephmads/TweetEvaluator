# TweetEvaluator

## Introduction

TweetEvaluator is an application that allows the user to count the frequency their own, or any other Twitter user's, most tweeted words.

![screenshot1 of TweetEval](https://i.imgur.com/aYYjpd5.png)

![screenshopt2 of TweetEval](https://i.imgur.com/vMrBxGO.png)

## Getting Started

1. To use TweetEvaluator you will need: 
- A [Twitter Dev](https://developer.twitter.com/en) account. 
- Create an app and generate an API Key and Secret.
- In `functions.py`, replace the variable values in lines 7 and 8 with your API Key and Secret.

2. Run `gui.py` for graphical interface.

3. Run `cli.py` for command-line interface.

*Note: Twitter's API only allows non-academic dev accounts to pull the 3200 most recent tweets.*

### Credit:

The `word_counter()` function was adapted from Abder-Rahman Ali's tutorial at [code.tutsplus.com](https://code.tutsplus.com/tutorials/counting-word-frequency-in-a-file-using-python--cms-25965)