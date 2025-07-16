# Unique_Search

A program that takes in a set of google searches and processes the text to find the most unique search made.

Creating this repository to keep track of my work on this project and using this README as a statement of intent I suppose?

Step 1:
The goal is going to be to take in a csv of searches and output the most unique one from the set (possibly the top 5 or so searches. Will make choosing that a stretch goal as it were.)

Step 2:
After that, next goal should be setting up something that allows the user to download and parse their search history for their searches. Then format the results to be used in the unique search program.

Planning:

I need to decide what constitutes uniqueness for the classification of the searches. I'm leaning towards the average of the rarity of the words as determined by a word frequency dataset like the one here: [https://www.wordfrequency.info/]. (Probably one that's more free due to this being a personal project)

An additional stretch goal for this project will be other definitions of unique since I'm seeing edge cases in my go to definition. (What if someone uses archaic vernacular or some such. Basing uniqueness on just the user's searches could work (like having the most unique search be the one with the words that the user uses the least.). )
