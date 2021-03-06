# Stemmer class definition.
class Stemmer:
    # Stores the words loaded from the words.txt file.
    words = []
    # Stores the suffixes loaded from the suffix.txt file.
    suffixes = []

    # Constructor of the Stemmer class.
    def __init__(self):
        # Load words from the words.txt file.
        self.load_words()
        # Load suffixes from the suffix.txt file.
        self.load_suffixes()

    # Destructor of the Stemmer class.
    def __del__(self):
        # Clear both lists to free the memory space.
        self.words.clear()
        self.suffixes.clear()

    # Loads the words from the word.txt file into memory.
    def load_words(self):
        # Open words.txt file in read mode with utf-8 encoding.
        with open("words.txt", "r", encoding="utf8") as words_file:
            # Iterate over each line in the words.txt file
            for word in words_file:
                # Trim the spaces and newline characters from the string before adding to the list.
                self.words.append(word.strip())

    # Loads the suffixes from the suffix.txt file into memory.
    def load_suffixes(self):
        # Open suffix.txt file in read mode with utf-8 encoding.
        with open("suffix.txt", "r", encoding="utf8") as suffix_file:
            # Iterate over each line in the suffix.txt file.
            for suffix in suffix_file:
                # Trim the spaces and newline characters from the string before adding to the list.
                self.suffixes.append(suffix.strip())

    # Returns the stemmed version of word.
    def stem_word(self, word):
        # If the word is already in the database, return it.
        if word in self.words:
            return word
        # Iterate over the suffixes.
        for suffix in self.suffixes:
            # If the word ends with the particular suffix, create a new word by removing that suffix.
            if word.endswith(suffix):
                new_word = word[:word.rfind(suffix)]
                # If new word is in the database, return it.
                if new_word in self.words:
                    return new_word
        # If it is not possible to apply stemming to that word, return it.
        return word

    # Returns the stemmed version of each word in the list of words.
    def stem_words(self, list_of_words):
        # Iterate over the range of word indexes.
        for word_index in range(len(list_of_words)):
            # Apply stemming to each word in the list.
            list_of_words[word_index] = self.stem_word(list_of_words[word_index])
        # Return the updated list.
        return list_of_words
