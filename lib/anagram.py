class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, test_words):
        anagrams = []
        for test_word in test_words:
            lower_test_word = test_word.lower()
            if sorted(lower_test_word) == self.sorted_word:
                anagrams.append(test_word)
        return anagrams
    


#! Unnecessary to pass -- Version below tests whether the submitted word matches word in submitted potential anagram list

    # def match(self, test_words):
    #     anagrams = []
    #     for test_word in test_words:
    #         lower_test_word = test_word.lower()
    #         if lower_test_word != self.word and sorted(lower_test_word) == self.sorted_word:
    #             anagrams.append(test_word)
    #     return anagrams