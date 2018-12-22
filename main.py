"""Case-study #7 Генерация предложений
Разработчики:
Жамбаева Д., Зыкова К.

"""


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

def read():
    while True:
        try:
            file = input('Введите имя файла: ')
            with open(file) as f_in:
                text = f_in.read()
                return text
        except FileNotFoundError:
            print('Файл не найден!'.format(file))
def text_editing(text):
    symbols = '@#$"<>{}^%;»«+*/[]^&'
    for char in symbols:
        text = text.replace(char, "")
    for char in text:
        text = text.replace(' .', ".")
        text = text.replace(' !', "!")
        text = text.replace(' ?', "?")
        text = text.replace(' ,', ",")
    return text


text_list = list(text)
start = []
for t in text_list:
    if t == t.capitalize():
        if not t in start:
            start.append(t)






