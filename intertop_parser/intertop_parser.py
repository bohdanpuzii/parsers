from bs4 import BeautifulSoup

raw_desc = 'Жіночі черевики ECCO SOLICE (42010301291) - ідеально ' \
           'повторюють вигини стопи та захищають від вологи.<br> ' \
           'Особливості:<br> • Верх виконаний з промасленого нубук' \
           'у та текстилю<br> • Застібка-блискавка і шнурки<br> • ' \
           'Мембрана GoreTex® захищає від води<br> • Лита підошва ' \
           'FLUIDFORM ™ повторює вигини стопи, забезпечує легкість ' \
           'ходи<br> • Гумовий протектор для кращого зчеплення з поверхнею'

raw_chars = '<li> <span class="prop-name"> Артикул: </span> <span class="prop-value"> PW188 </span> </li> <li> <span clas' \
            's="prop-name"> Бренд: </span> <span class="prop-value"> <a href="/ua/catalog/zhenskaya_obuv/brand-panama-jack' \
            '-good_type-sapogi/">Panama Jack</a> </span> </li> <li> Верх: <span class="prop-value"> шкіра </span> </li> <li' \
            '> Матеріал підкладки: <span class="prop-value"> <a href="/ua/catalog/zhenskaya_obuv/good_type-sapogi-lining_m' \
            'aterial-sherst/">вовна</a> </span> </li> <li> Матеріал підошви: <span class="prop-value">поліуретан</span> </l' \
            'i> <li> Колір: <span class="prop-value"> <a href="/ua/catalog/zhenskaya_obuv/color-korichnevyy-good_type-sapog' \
            'i/"> Коричневий </a> </span> </li> <li> Вид товару: <span class="prop-value"> <a href="/ua/catalog/zhenskaya_obu' \
            'v/good_type-sapogi/"> Чоботи та ботфорти </a> </span> </li> <li> Сезон: <a href="/ua/catalog/zhenskaya_obuv/goo' \
            'd_type-sapogi-season-osen-zima/"> <span class="prop-value">Осінь-Зима 2019</span> </a> </li> <li> Стиль: <span c' \
            'lass="prop-value">Casual</span> </li> <li> Країна: <span class="prop-value">Іспанія</span> </li> <li> Стать: <spa' \
            'n class="prop-value">Жіноче</span> </li> <li> Вид носку взуття: <span>Круглий</span> </li> <li> Вид підошви: <spa' \
            'n>Каблук-цеглинка</span> </li> '


# def clear_intertop_characteristics_html(raw_characteristics):
#     soup = BeautifulSoup(raw_characteristics, 'html.parser')
#     chars_text = [string for string in soup.strings]
#     cleared_text = list(filter(lambda string: string != ' ' and string != ', ', chars_text))
#     text_without_extra_spaces = list(map(lambda string: string.strip(' '), cleared_text))
#     return text_without_extra_spaces
#
#
# def intertop_characteristics_pretty_view(description_list):
#     grouped_by_2 = [description_list[n:n + 2] for n in range(0, len(description_list), 2)]
#     return '\n'.join(list(map(' '.join, grouped_by_2)))


def clear_intertop_characteristics_html(raw_characteristics):
    characteristics_list = []
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    for li in soup.select('li'):
        characteristics_list.append(li.text.strip(' '))
    return characteristics_list


def intertop_characteristics_pretty_view(characteristics_list):
    return '\n'.join(characteristics_list)


def clear_intertop_description_html(raw_characteristics):
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    text = [string for string in soup.strings]
    return text


def intertop_description_pretty_view(description_list):
    description_list = list(map(lambda string: ('  ' + string), description_list))
    return '\n'.join(description_list)


if __name__ == '__main__':
    print(((intertop_characteristics_pretty_view(clear_intertop_characteristics_html(raw_chars)))))
    #print(intertop_description_pretty_view(clear_intertop_description_html(raw_desc)))
