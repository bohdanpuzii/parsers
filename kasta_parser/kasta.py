from bs4 import BeautifulSoup

raw_html_chars = '<div class="pd_prop-item"><div class="wrap-content-title"><div class="pd_prop-title">Артикул товару' \
                 '</div><div class="dots"></div></div><div class="pd_prop-val">184517273</div></div><div class="pd_pro' \
                 'p-item"><div class="wrap-content-title"><div class="pd_prop-title">Бренд</div><div class="dots"></di' \
                 'v></div><div class="pd_prop-val"><a href="/uk/brand/Rifellini/" class="pd_prop-link">Rifellini</a></d' \
                 'iv></div><div class="pd_prop-item"><div class="wrap-content-title"><div class="pd_prop-title">Принал' \
                 'ежність</div><div class="dots"></div></div><div class="pd_prop-val">Чоловікам</div></div><div class="' \
                 'pd_prop-item"><div class="wrap-content-title"><div class="pd_prop-title">Сезонність</div><div class="' \
                 'dots"></div></div><div class="pd_prop-val">Демісезон</div></div><div class="pd_prop-item"><div class=' \
                 '"wrap-content-title"><div class="pd_prop-title">Колір</div><div class="dots"></div></div><div class="p' \
                 'd_prop-val">Коричневий</div></div><div class="pd_prop-item"><div class="wrap-content-title"><div class' \
                 '="pd_prop-title">Склад</div><div class="dots"></div></div><div class="pd_prop-val">верх: натуральна шк' \
                 'іра / підкладка: натуральна шкіра / устілка: натуральна шкіра / підошва: поліуретан</div></div><div cla' \
                 'ss="pd_prop-item"><div class="wrap-content-title"><div class="pd_prop-title">Склад верха</div><div clas' \
                 's="dots"></div></div><div class="pd_prop-val">Натуральна шкіра</div></div><div class="pd_prop-item"><di' \
                 'v class="wrap-content-title"><div class="pd_prop-title">Склад підошви</div><div class="dots"></div></di' \
                 'v><div class="pd_prop-val">Поліуретан</div></div><div class="pd_prop-item"><div class="wrap-content-ti' \
                 'tle"><div class="pd_prop-title">Склад устілки</div><div class="dots"></div></div><div class="pd_prop-va' \
                 'l">Натуральна шкіра</div></div><div class="pd_prop-item"><div class="wrap-content-title"><div class="pd_' \
                 'prop-title">Склад підкладки</div><div class="dots"></div></div><div class="pd_prop-val">Натуральна шкіра' \
                 '</div></div><div class="pd_prop-item"><div class="wrap-content-title"><div class="pd_prop-title">Тип каб' \
                 'лука</div><div class="dots"></div></div><div class="pd_prop-val">Без підборів</div></div><div class="pd_' \
                 'prop-item"><div class="wrap-content-title"><div class="pd_prop-title">Висота підбора</div><div class="do' \
                 'ts"></div></div><div class="pd_prop-val">Без підборів</div></div><div class="pd_prop-item"><div class="w' \
                 'rap-content-title"><div class="pd_prop-title">Вид носка</div><div class="dots"></div></div><div class="' \
                 'pd_prop-val">Круглий</div></div><div class="pd_prop-item"><div class="wrap-content-title"><div class="p' \
                 'd_prop-title">Стиль</div><div class="dots"></div></div><div class="pd_prop-val">Кежуал</div></div><div ' \
                 'class="pd_prop-item"><div class="wrap-content-title"><div class="pd_prop-title">Візерунок</div><div clas' \
                 's="dots"></div></div><div class="pd_prop-val">Однотонний</div></div><div class="pd_prop-item"><div class' \
                 '="wrap-content-title"><div class="pd_prop-title">Застібка</div><div class="dots"></div></div><div class' \
                 '="pd_prop-val">Шнуровка</div></div><div class="pd_prop-item"><div class="wrap-content-title"><div class' \
                 '="pd_prop-title">Колекція</div><div class="dots"></div></div><div class="pd_prop-val">Без колекції</div' \
                 '></div><div class="pd_prop-item"><div class="wrap-content-title"><div class="pd_prop-title">Країна виро' \
                 'бництва</div><div class="dots"></div></div><div class="pd_prop-val">Туреччина</div></div><div class="p' \
                 'd_prop-item"><div class="wrap-content-title"><div class="pd_prop-title">Країна бренду</div><div class="' \
                 'dots"></div></div><div class="pd_prop-val">Туреччина</div></div><div class="pd_prop-item"><div class="w' \
                 'rap-content-title"><div class="pd_prop-title">Вага з упаковкою</div><div class="dots"></div></div><div c' \
                 'lass="pd_prop-val">1000</div></div>'


def clear_kasta_characteristics(raw_characteristics):
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    text = [string for string in soup.strings]
    return text


def kasta_characteristics_pretty_view(description_list):
    grouped_by_2 = [description_list[n:n + 2] for n in range(0, len(description_list), 2)]
    return '\n'.join(list(map(' : '.join, grouped_by_2)))


if __name__ == '__main__':
    print(kasta_characteristics_pretty_view(clear_kasta_characteristics(raw_html_chars)))
