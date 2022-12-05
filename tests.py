from unittest import TestCase
from functions import get_tweets, word_counter, regex, blacklisted
import re


class TestTweetEvaluatorFunctions(TestCase):

    def test_get_tweets_max_results(self):
        """Verifies max_result equals arguements entered."""
        result = get_tweets("josephmads", 100)
        self.assertEqual(len(result), 100)

    def test_word_counter_returns_good_count(self):
        """Verifies words are counted correctly."""
        string = "hello hello hello world world world"
        result = word_counter(string)
        self.assertListEqual(result, [("hello", 3), ("world", 3)])

    def test_word_counter_regex_matches_correct_patterns(self):
        """Verifies regex pattern finds matches correctly."""
        REGEX = re.compile(regex, re.MULTILINE | re.IGNORECASE)
        text = "@josephmads #regex HELLO world! 'don't' try this?"
        self.assertTrue(REGEX.match(text))
        
