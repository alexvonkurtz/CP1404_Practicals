
text = input("Text: ")
words_in_text = text.strip().split()
words = {}

for word in words_in_text:
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1
sorted_words = sorted(words.keys())

#list comprehension can be used for below covered in week 6 "classes"
max_word_length = 0
for word in sorted_words:
    if len(word) > max_word_length:
        max_word_length = len(word)
for word in sorted_words:
    print("{:{}} : {}".format(word, max_word_length, words[word])) #prints word, uses max_word_length as width, uses word count in words dict for output