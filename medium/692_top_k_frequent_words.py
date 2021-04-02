from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        data_words = {}
        for word in words:
            if word in data_words:
                data_words[word] += 1
            else:
                data_words[word] = 1

        count_words = {}
        for word in data_words:
            if data_words[word] in count_words:
                count_words[data_words[word]].append(word)
                count_words[data_words[word]].sort()
            else:
                count_words[data_words[word]] = [word]
        result = []

        for key, value in sorted(count_words.items(), reverse=True):
            for val in value:
                result.append(val)

        return result[:k]
