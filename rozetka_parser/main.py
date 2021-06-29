from bs4 import BeautifulSoup

raw_char = '<!----><!----><div class="characteristics-full__item ng-star-inserted"><dt class="characteristics-fu' \
           'll__label">' \
           '<span>Стандарт связи</span></dt><dd class="characteristics-full__value"><ul class="characteristics-full__sub-' \
           'list"><!----><!----><li class="ng-star-inserted"><!----><a href="/mobile-phones/c80003/standart-svyazi-83148=' \
           '406363/" class="ng-star-inserted">4G (LTE)</a><!----><!----></li></ul></dd></div><!----><div class="characte' \
           'ristics-full__item ng-star-inserted"><dt class="characteristics-full__label"><span>Диагональ экрана</span><' \
           '/dt><dd class="characteristics-full__value"><ul class="characteristics-full__sub-list"><!----><!----><li cl' \
           'ass="ng-star-inserted"><!----><a href="/mobile-phones/c80003/23777=50074/" class="ng-star-inserted">4.7</a>' \
           '<!----><!----></li></ul></dd></div><!----><div class="characteristics-full__item ng-star-inserted"><dt class' \
           '="characteristics-full__label"><span>Разрешение дисплея</span></dt><dd class="characteristics-full__value"><ul' \
           ' class="characteristics-full__sub-list"><!----><!----><li class="ng-star-inserted"><!----><a href="/mobile-pho' \
           'nes/c80003/23778=25481/" class="ng-star-inserted">HD (1280x720)</a><!----><!----></li></ul></dd></div><!----' \
           '><div class="characteristics-full__item ng-star-inserted"><dt class="characteristics-full__label"><span>Тип' \
           ' матрицы</span></dt><dd class="characteristics-full__value"><ul class="characteristics-full__sub-list"><!-' \
           '---><!----><li class="ng-star-inserted"><!----><a href="/mobile-phones/c80003/31565=292039/" class="ng-st' \
           'ar-inserted">IGZO</a><!----><!----></li></ul></dd></div><!----><div class="characteristics-full__item ng-' \
           'star-inserted"><dt class="characteristics-full__label"><span>Количество СИМ-карт</span></dt><dd class="ch' \
           'aracteristics-full__value"><ul class="characteristics-full__sub-list"><!----><!----><li class="ng-star-in' \
           'serted"><!----><a href="/mobile-phones/c80003/23017=15760/" class="ng-star-inserted">2</a><!----><!----><' \
           '/li></ul></dd></div><!----><div class="characteristics-full__item ng-star-inserted"><dt class="characteri' \
           'stics-full__label"><span>Размеры СИМ-карты</span></dt><dd class="characteristics-full__value"><ul class="' \
           'characteristics-full__sub-list"><!----><!----><li class="ng-star-inserted"><!----><a href="/mobile-phones/' \
           'c80003/26360=23237/" class="ng-star-inserted">Micro-SIM</a><!----><!----></li></ul></dd></div><!----><div cl' \
           'ass="characteristics-full__item ng-star-inserted"><dt class="characteristics-full__label"><span>Оперативная' \
           ' память</span></dt><dd class="characteristics-full__value"><ul class="characteristics-full__sub-list"><!-' \
           '---><!----><li class="ng-star-inserted"><!----><a href="/mobile-phones/c80003/38435=103765/" class="ng-star' \
           '-inserted">3 ГБ</a><!----><!----></li></ul></dd></div><!----><div class="characteristics-full__item ng-st' \
           'ar-inserted"><dt class="characteristics-full__label"><span>Встроенная память</span></dt><dd class="charact' \
           'eristics-full__value"><ul class="characteristics-full__sub-list"><!----><!----><li class="ng-star-inserte' \
           'd"><!----><a href="/mobile-phones/c80003/41404=32-gb/" class="ng-star-inserted">32 ГБ</a><!----><!----></' \
           'li></ul></dd></div><!----><div class="characteristics-full__item ng-star-inserted"><dt class="characteris' \
           'tics-full__label"><span>Формат поддерживаемых карт памяти</span></dt><dd class="characteristics-full__valu' \
           'e"><ul class="characteristics-full__sub-list"><!----><!----><li class="ng-star-inserted"><!----><span cla' \
           'ss="ng-star-inserted">microSD</span><!----><!----></li></ul></dd></div><!----><div class="characteristi' \
           'cs-full__item ng-star-inserted"><dt class="characteristics-full__label"><span>Максимальный объем поддерж' \
           'иваемой карты памяти</span></dt><dd class="characteristics-full__value"><ul class="characteristics-fu' \
           'll__sub-list"><!----><!----><li class="ng-star-inserted"><!----><span class="ng-star-inserted">32 ГБ</s' \
           'pan><!----><!----></li></ul></dd></div>'

raw_desc = '<p><b>Четкие и резкие снимки при низком уровне освещения</b> <br>Двойная камера 13 Мп + 2 Мп имеет ' \
           'высокое разрешение и апертуру, что позволяет передать неподражаемый эффект глубины — даже на улице ' \
           'и при низком уровне освещения. Фронтальная камера 5 Мп дает возможность делать более качественные сел' \
           'фи. </p><p><b>Большой экран с улучшенным обзором</b><br>Смартфон E6s с дисплеем 6.1" создает эффект при' \
           'сутствия благодаря широкому экрану большого размера. Комфортный угол обзора превращает просмотр вашего ко' \
           'нтента в настоящее удовольствие.</p><p><b>Корпус в который поместилось еще больше</b><br>Внутри тонкого ' \
           '(всего 8.5 мм) корпуса E6s незаметно размещается емкая батарея на 3000 мА*ч.</p>'


def clean_rozetka_characteristics(raw_html_characteristics):
    characteristic_value = []
    characteristics_list = []
    soup = BeautifulSoup(raw_html_characteristics, 'html.parser')
    for div in soup.select('div'):
        for dt in div.select('dt'):
            characteristic_name = dt.text
            characteristics_list.append(characteristic_name)
        for li in div.select('li'):
            characteristic_value.append(li.text)
        characteristics_list.append(' '.join(characteristic_value))
        characteristic_value.clear()
    return characteristics_list


def clean_rozetka_description(raw_html_description):
    description_list = []
    soup = BeautifulSoup(raw_html_description, 'html.parser')
    for p in soup.select('p'):
        for b in p.select('b'):
            header = b.text
        body = p.text.replace(header, '')
        description_list.append(header)
        description_list.append(body)
    description_list = [x.strip(' ') for x in description_list]
    return '\n'.join(description_list)


def rozetka_characteristics_pretty_view(characteristics_list):
    characteristics_list = [x.strip(' ') for x in characteristics_list]
    grouped_by_2 = [characteristics_list[n:n + 2] for n in range(0, len(characteristics_list), 2)]
    return '\n'.join(list(map(' : '.join, grouped_by_2)))


if __name__ == '__main__':
    print(rozetka_characteristics_pretty_view(clean_rozetka_characteristics(raw_char)))
    print(clean_rozetka_description(raw_desc))
