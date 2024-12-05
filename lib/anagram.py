class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words_list):
        result = []
        for word in words_list:
            if sorted(self.word) == sorted(word):
                result.append(word)
        return result
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))
