"""Case-study #7 Генерация предложений
Разработчики:
Жамбаева Д., Зыкова К.

"""

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







