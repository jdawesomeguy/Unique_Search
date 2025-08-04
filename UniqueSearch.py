# This file will hold the code for taking the parsed searches and scoring them based on their uniqueness.
# It will then output the top 3 unique searches.

import unittest
import input
from wordfreq import zipf_frequency

def zipf_norm(searches, min_words=0):
    """
    Calculate the uniqueness score for each search term by multiplying the frequency of each word in the search term.

    For frequency, we are using the Zipf frequency from the wordfreq library
    "The Zipf scale was proposed by Marc Brysbaert, who created the SUBTLEX lists. 
    The Zipf frequency of a word is the base-10 logarithm of the number of times it appears per billion words. 
    A word with Zipf value 6 appears once per thousand words, for example, and a word with Zipf value 3 appears once per million words."
    -- rspeer

    We will also divide the score by the number of words in the search term to normalize it.

    Input:
    -----------
    searches: set, A set of searches with a minimum of 1 word.
    min_words: int, Minimum number of words in a search term to be considered for scoring.
    -----------
    returns: dict, A dictionary with search terms as keys and their uniqueness scores as values.
    """

    scores = {}
    for search in searches:
        words = search.split()
        score = 1
        for word in words:
            # Get the Zipf frequency of the word
            freq = zipf_frequency(word, 'en')
            #if the word is not found, it will return 0, which we will treat as 1 to avoid multiplying by 0
            if freq == 0:
                freq = 1
            score *= freq

        # Only consider searches with at least min_words words
        if len(words) < min_words:
            continue
        scores[search] = (score / len(words))  # Normalize by number of words
    
    return scores


def score_searches(filepath, min_words=0):
    """
    This function will score the searches based on their uniqueness using one of the scoring functions.

    returns: list, A list of the top 3 unique searches sorted by their uniqueness score in ascending order.
    """
    # Read and parse the search data
    searches = input.parse_data(filepath)
    if searches is None:
        raise ValueError("No searches found or the data could not be parsed.")
    
    # Score the searches based on their frequency in the word corpus
    # for now, we only have the one scoring function, so we will use zipf_norm
    scores = zipf_norm(searches, min_words)

    # Sort the searches by their uniqueness score in ascending order
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=False)

    # Get the 3 lowest scoring searches (least frequent words)
    top_unique_searches = sorted_scores[:3]

    return top_unique_searches

class TestScoreSearches(unittest.TestCase):
    def test_zipf_norm(self):
        # Test scoring a set of searches
        searches = {"Google Search", "Another Search Query", "My Third Search"}
        scores = zipf_norm(searches, min_words=2)
        self.assertIsInstance(scores, dict)
        self.assertGreater(len(scores), 0)
        for search in searches:
            self.assertIn(search, scores)

    def test_score_searches(self):
        # Test scoring the searches from a file
        top_searches = score_searches("./Input_Files/test.json")
        self.assertIsInstance(top_searches, list)
        self.assertEqual(len(top_searches), 3)

if __name__ == "__main__":
    # Run the tests
    unittest.main()

    # top_searches = score_searches("./Input_Files/MyActivity.json")
    # print("Top 3 Unique Searches:")
    # for search, score in top_searches:
    #     print(f"Search: {search}, Score: {score:.2f}")