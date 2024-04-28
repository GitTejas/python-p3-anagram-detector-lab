# your code goes here!
import ipdb


#Initialization: The __init__ method initializes the class with a word, storing it in self.word. 

#Matching: The match method takes a list of words as input. For each word in the input list, it splits it into a list of characters. Then, it checks if the sorted list of characters of the input word matches the sorted list of characters of the initialized word. If there is a match, it joins the characters back into a string and adds it to the matches list.

class Anagram:
    def __init__(self, word):
        # Initialize the class with a word
        self.word = word

    def match(self, input_list):
        # Splitting self.word into a lsit of letters
        init_word = [char for char in self.word]

        # Splitting every element in the input_list
        split_strings = [[char for char in word] for word in input_list]

        # Iterate through split_strings and if there is a match, turn into string and save in a list
        matches = ["".join(word) for word in split_strings if sorted(word) == sorted(init_word)]

        return matches
    

#================================================================================================#
# class Anagram:
#    def __init__(self, word):
  #      self.word = word.lower()

 #   def match(self, word_list):
        # Convert the initialized word to lowercase for case-insensitive comparison
   #     init_sorted = sorted(self.word)

        # Initialize an empty list to store matches
    #    matches = []

        # Iterate through each word in the input list
     #   for candidate in word_list:
            # Convert the candidate word to lowercase and sort its characters
 #           candidate_sorted = sorted(candidate.lower())

            # Check if the sorted candidate word matches the sorted initialized word
#            if candidate_sorted == init_sorted:
                # If it's an anagram, add it to the list of matches
 #               matches.append(candidate)

  #      return matches


  #In this version: Case Insensitivity: The initialization ensures that the initialized word is converted to lowercase. This eliminates the need to convert each candidate word to lowercase within the loop for case-insensitive comparison. Efficient Sorting: Instead of sorting the characters of the initialized word repeatedly within the loop, it's sorted only once outside the loop. This reduces unnecessary sorting operations, especially if the match method is called multiple times with different word lists. Simplified List Comprehension: The list comprehension for initializing init_word and split_strings has been replaced with a simpler approach that directly sorts the characters within the loop. This version maintains the core logic of checking for anagrams but simplifies the implementation and potentially improves performance by reducing redundant operations.