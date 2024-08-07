class WordsFinder:
    file_names = []
    def __init__(self, *args):
        for i in args:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        punctuations = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                words_in_file = []
                for line in file:
                    str_ = line.lower()
                    for j in str_:
                        if j in punctuations:
                            str_ = str_.replace(j, '')
                        list_of_words = str_.split()
                    for k in list_of_words:
                        words_in_file.append(k)
                all_words[i] = words_in_file
        return all_words

    def find(self, word):
        find_word_first_position = {}
        dict_1 = self.get_all_words()
        low_word = word.lower()
        for name, words in dict_1.items():
            if low_word in dict_1[name]:
                find_word_first_position[name] = dict_1[name].index(low_word) + 1
        return find_word_first_position


    def count(self, word):
        count_word = {}
        dict_1 = self.get_all_words()
        low_word = word.lower()
        for name, words in dict_1.items():
            if word.lower() in dict_1[name]:
                count_word[name] = dict_1[name].count(low_word)
        return count_word



finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))