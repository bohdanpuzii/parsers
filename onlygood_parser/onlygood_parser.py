from bs4 import BeautifulSoup

raw_characteristics = '<ul><li><span style="font-weight: 400;">Матеріал: Срібло покрите золотом</span></li><li><span st' \
                      'yle="font-weight: 400;">Каміння: Перлини</span></li><li><span style="font-weight: 400;">Застібка:' \
                      ' Пусет</span></li><li><span style="font-weight: 400;">Країна походження: Канада</span></li></ul>'


def clear_onlygood_characteristics_html(raw_characteristics):
    characteristics_list = []
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    for td in soup.select('li'):
        characteristics_list.append(td.text)
    return "\n".join(list(map(lambda string: string.strip(' '), characteristics_list)))


if __name__ == '__main__':
    print(clear_onlygood_characteristics_html(raw_characteristics))