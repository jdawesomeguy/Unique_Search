# This file will hold the code for inputing the google activity data from their Google Takeout service.
# It'll then parse the activity data for the search activity specifically to grab the search terms.

import json
import unittest


def read_json(file_path):
    try:
        with open(file_path, 'r', encoding="utf8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise ValueError(f"Error: The file {file_path} does not exist.")
    except json.JSONDecodeError:
        raise ValueError(f"Error: The file {file_path} is not a valid JSON file.")
    
def parse_data(file_path):
    data = read_json(file_path)
    if data is None:
        return
    
    searches = set()
    # JSON structure is a list of dictionaries
    for activity in data:
        # For all dictionaries, check if 'header' is 'Search'
        if activity.get('header') == 'Search':
            #if header is search, check that title matches a pattern of "Searched for <search term(s)>"
            title = activity.get('title', '')
            if title.startswith("Searched for "):
                search_term = title[len("Searched for "):]
                searches.add(search_term)
    
    #return the unique searches
    return searches

class testParseData(unittest.TestCase):
    def test_read_json(self):
        # Test reading a valid JSON file
        data = read_json("test.json")
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)

    def test_parse_data(self):
        # Test parsing the search terms from the JSON data
        searches = parse_data("test.json")
        self.assertIsNotNone(searches)
        self.assertGreater(len(searches), 0)
        self.assertIn("Google Search", searches)
        self.assertIn("Another Search Query", searches)
        self.assertIn("My Third Search", searches)

if __name__ == "__main__":
    # Run the tests
    unittest.main()