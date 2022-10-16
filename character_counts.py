# This file contains code that will count characters in
# a list of words. It was written to prove a hypothesis
# that "e" is the most frequently used character in the 
# English language. We use the list of crossword answers
# as a representation of English, and count the occurrences
# of each character in the file.

# Open words.txt for reading
infile = open("words.txt")

# Create an empty dictionary to store counts.
# The dictionary will contain the following mapping:
#
# {
#   "a": <number of times "a" occurs in words.txt>,
#   "b": <number of times "b" occurs in words.txt>,
#   "c": <number of times "c" occurs in words.txt>,
#   ...
# }
char_counts = {}

# Iterate through every line in words.txt
for line in infile:
    # Get rid of the trailing newline character
    line = line.strip()

    # Now iterate through each character in every word
    for c in line:
        if c not in char_counts:
            # If the character is not in the dictionary,
            # add it with an initial count of 1
            char_counts[c] = 1
        else:
            # If the character is already in the dictionary,
            # increment its count
            char_counts[c] = char_counts[c] + 1

# Iterate through the dictionary and print all key/value pairs.
# If we're right, "e" should have the largest count.
for k in char_counts:
    print(k + ": " + str(char_counts[k]))