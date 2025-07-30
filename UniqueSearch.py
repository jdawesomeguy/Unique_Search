# This file will hold the code for taking the parsed searches and scoring them based on their uniqueness.
# It will then output the top 3 unique searches.

import input
from wordfreq import zipf_frequency

def unique_mult(searches):
    """
    Calculate the uniqueness score for each search term by multiplying the frequency of each word in the search term.

    For frequency, we are using the Zipf frequency from the wordfreq library
    "The Zipf scale was proposed by Marc Brysbaert, who created the SUBTLEX lists. 
    The Zipf frequency of a word is the base-10 logarithm of the number of times it appears per billion words. 
    A word with Zipf value 6 appears once per thousand words, for example, and a word with Zipf value 3 appears once per million words."
    -- rspeer

    We will also divide the score by the number of words in the search term to normalize it.

    searches: set, A set of searches with a minimum of 1 word.
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

        scores[search] = (score / len(words))  # Normalize by number of words
    
    return scores


def score_searches():
    """
    This function will score the searches based on their uniqueness using one of the scoring functions.
    """
    # Read and parse the search data
    searches = input.parse_data("MyActivity.json")
    if searches is None:
        raise ValueError("No searches found or data could not be parsed.")
    
    # Score the searches based on their frequency in the word corpus
    # for now, we only have the one scoring function, so we will use unique_mult
    scores = unique_mult(searches)

    # Sort the searches by their uniqueness score in ascending order
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=False)

    # Get the 3 lowest scoring searches (least frequent words)
    top_unique_searches = sorted_scores[:3]

    return top_unique_searches

if __name__ == "__main__":
    # Run the scoring function and print the top 3 unique searches
    top_searches = score_searches()
    for search, score in top_searches:
        print(f"Search: {search}, Uniqueness Score: {score:.4f}")