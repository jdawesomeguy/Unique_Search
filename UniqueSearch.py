# This file will hold the code for taking the parsed searches and scoring them based on their uniqueness.
# It will then output the top 3 unique searches.

import input

def score_searches():
    # Read and parse the search data
    searches = input.parse_data("MyActivity.json")
    if searches is None:
        raise ValueError("No searches found or data could not be parsed.")
    
    # Score the searches based on their frequency in the word corpus