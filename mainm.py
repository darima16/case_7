# Получение звеньев и связей
def made_dict(text):
    relations_word = defaultdict(list)
    more_word = []
    for k in text:
        if k not in more_word:
            more_word.append(k)
    for k in more_word:
        for i in range(len(text) -1):
            if text[i] == k:
                word = text[i + 1]
                if word in relations_word:
                    break
                elif word not in relations_word:
                    relations_word.append(word)
                    return relation_word

#Список стартовых слов
text_list = list(text)
start = []
for t in text_list:
    if t == t.capitalize():
        if not t in start:
            start.append(t)

