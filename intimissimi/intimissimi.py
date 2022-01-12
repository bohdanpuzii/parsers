from bs4 import BeautifulSoup

raw_description_html = 'Код товару: RBD2442<br> Бюстгальтер каріока з круглими та боковими вертикальними кісточками. ' \
                       'Основна тканина – мереживо, яке доповнює елегантна атласна обробка та оригінальне переплетення ' \
                       'резинок регульовної довжини вздовж декольте, оздоблене стразами. Бретельки обшиті атласом й регулюються ззаду.' \
                       ' Ідеальний вибір для звабливих й жіночних образів.<br><br>Мереживо, з якого виготовлено модель, містить перероблений поліамід.'


def clear_intimissimi_description_html(raw_description):
    return raw_description.replace('<br>', '\n')


if __name__ == '__main__':
    print(clear_intimissimi_description_html(raw_description_html))
