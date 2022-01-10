from bs4 import BeautifulSoup

raw_description_html = '<h2>Опис</h2> <div class="model-wrapper"></div> <p class="description">Колір: ЧОРНИЙ</p> <p ' \
                  'class="description">Висота підборів: 8,5&nbsp;см.</p> <p class="description">Black high-heel ankle' \
                  ' boots. Stretch material. Pointed toe. Sporty sole.</p>'

raw_characteristics_html = '<h2>Склад</h2><article class="composition"><h3>Верх</h3><p>100% поліестер</p></article><article class="co' \
            'mposition"><h3>Підкладка</h3><p>80% поліуретан</p><p>20% поліестер</p></article><article class="compositio' \
            'n"><h3>Підошва</h3><p>90% поліуретановий термопластик</p><p>10% поліуретан</p></article>'


def clear_bershka_description_html(raw_description):
    characteristics_list = []
    soup = BeautifulSoup(raw_description, 'html.parser')
    for p in soup.select('p'):
        characteristics_list.append(p.text)
    return '\n'.join(list(map(lambda string: string.strip(' '), characteristics_list)))


def clear_bershka_characteristics_html(raw_characteristics):
    characteristics_list = []
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    for div in soup.select('article'):
        for h3 in div.select('h3'):
            characteristics_list.append(h3.text + ': ' + div.select('p')[0].text)
    return '\n'.join(characteristics_list)


if __name__ == '__main__':
    print(clear_bershka_description_html(raw_description_html))
    print(clear_bershka_characteristics_html(raw_characteristics_html))
