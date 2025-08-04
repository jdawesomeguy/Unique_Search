# Unique_Search

A program that takes in a set of google searches and processes the text to find the most unique search made.

Creating this repository to keep track of my work on this project and using this README as a statement of intent I suppose?

So far I have the project working in its most basic form. It can take in the data from the json file from google takeout,
then it can process that data and return the top 3 unique searches based on the product of the zipf scores of each word in the search.

Obviously this favors shorter searches because there are less numbers you are multiplying by there.

Next Steps:

- Use Tkinter to make the program GUI for people to interact with.

- Create other scoring algorithms for determining how unique a search is

- Make running the tool easier/more asthetically pleasing.
