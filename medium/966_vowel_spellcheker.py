from typing import List


class Solution:
    vowels = ["a", "e", "i", "o", "u"]

    def make_key(self, word):
        key = ""
        for index in range(len(word)):
            if word[index].lower() not in self.vowels:
                key += str(index) + word[index].lower()
        return key

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        words_data = {}
        words = {}
        result = []

        for word in wordlist:
            key = self.make_key(word)
            if key not in words_data:
                words_data[key] = [word]
            else:
                words_data[key].append(word)

            words[word] = 1

        for query in queries:
            if words.get(query):
                result.append(query)
                continue

            key = self.make_key(query)

            if not words_data.get(key):
                result.append("")
            else:
                for word in words_data[key]:
                    if query.lower() == word.lower():
                        result.append(word)
                        break
                else:
                    result.append(words_data[key][0])

        return result
