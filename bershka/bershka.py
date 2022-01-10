from bs4 import BeautifulSoup

raw_description = '<h2>Опис</h2> <div class="model-wrapper"><p class="model">Розмір моделі: 36</p><p class="model">Висота моделі: ' \
      '175 cm</p></div> <p class="description">Колір: Світло-синій</p> <!----> <!---->'

raw_chars = '<h2>Склад</h2> <article class="composition"><h3>MAIN FABRIC</h3> <p>86% cotton</p></article><article cla' \
            'ss="composition"><h3>MAIN FABRIC</h3> <p>14% polyester</p></article><article class="composition"><h3>DET' \
            'AILS</h3> <p>97% cotton</p></article><article class="composition"><h3>DETAILS</h3> <p>3% elastane</p></article>'


def clear_bershka_description_html(raw_characteristics):
    characteristics_list = []
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    for div in soup.select('div'):
        for p in div.select('p'):
            characteristics_list.append(p.text)
    return '\n'.join(list(map(lambda string: string.strip(' '), characteristics_list)))


def clear_bershka_characteristics_html(raw_characteristics):
    characteristics_list = []
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    for div in soup.select('article'):
        for h3 in div.select('h3'):
            characteristics_list.append(h3.text)
            characteristics_list.append(div.select('p')[0].text)
    return list(map(lambda string: string.strip(' '), characteristics_list))


def pretty_bershka_characteristics(chars_list):
    grouped_by_2 = [chars_list[i:i+2] for i in range(0, len(chars_list), 2)]
    return '\n'.join(list(map(' : '.join, grouped_by_2)))


if __name__ == '__main__':
    print((clear_bershka_description_html(raw_description)))
    print((pretty_bershka_characteristics(clear_bershka_characteristics_html(raw_chars))))