from bs4 import BeautifulSoup

raw_description_html = '<h2>Опис</h2> <div class="model-wrapper"><p class="model"> Розмір моделі: S </p><p class="model"> ' \
                       'Висота моделі: 177 cm </p></div> <p class="description"> Колір: Зелений </p> <!----> <!---->'

raw_characteristics_html = '<h2>Склад</h2> <article class="composition"><h3>Зовнішня сторона</h3> <p>\n 100% поліестер\n ' \
                           '</p></article><article class="composition"><h3>Підкладка</h3> <p>\n 100% поліестер\n </p>' \
                           '</article><article class="composition"><h3>Внутрішня сторона</h3> <p>\n 100% поліестер\n </p></article>'


def clear_bershka_description_html(raw_description):
    characteristics_list = []
    soup = BeautifulSoup(raw_description, 'html.parser')
    for p in soup.select('p'):
        characteristics_list.append(p.text.replace('\n', ''))
    return '\n'.join(list(map(lambda string: string.strip(' ').replace(' ', ''), characteristics_list)))


def clear_bershka_characteristics_html(raw_characteristics):
    characteristics_list = []
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    for div in soup.select('article'):
        for h3 in div.select('h3'):
            characteristics_list.append(h3.text + ':' + div.select('p')[0].text.replace('\n', ''))
    return '\n'.join(characteristics_list)


if __name__ == '__main__':
    print(clear_bershka_description_html(raw_description_html))
    print(clear_bershka_characteristics_html(raw_characteristics_html))
