from bs4 import BeautifulSoup

raw_desc = 'Жіночі черевики ECCO SOLICE (42010301291) - ідеально ' \
           'повторюють вигини стопи та захищають від вологи.<br> ' \
           'Особливості:<br> • Верх виконаний з промасленого нубук' \
           'у та текстилю<br> • Застібка-блискавка і шнурки<br> • ' \
           'Мембрана GoreTex® захищає від води<br> • Лита підошва ' \
           'FLUIDFORM ™ повторює вигини стопи, забезпечує легкість ' \
           'ходи<br> • Гумовий протектор для кращого зчеплення з поверхнею'

raw_chars = '	<li> <span class="prop-name"> Артикул: </span> <span c' \
            'lass="prop-value"> XW4043 </span> </li> <li> <span class="p' \
            'rop-name"> Бренд: </span> <span class="prop-value"> <a href=' \
            '"/ua/catalog/zhenskaya_obuv/brand-geox-good_type-sapogi/">Ge' \
            'ox</a> </span> </li> <li> Верх: <span class="prop-value"> ком' \
            'бинированный верх </span> </li> <li> Матеріал підкладки: <span ' \
            'class="prop-value"> <a href="/ua/catalog/zhenskaya_obuv/good_ty' \
            'pe-sapogi-lining_material-tekstil/">текстиль</a> </span> </li> <' \
            'li> Матеріал підошви: <span class="prop-value">термопластична гу' \
            'ма</span> </li> <li> Колір: <span class="prop-value"> <a href="/' \
            'ua/catalog/zhenskaya_obuv/color-chernyy-good_type-sapogi/"> Чорни' \
            'й </a> </span> </li> <li> Підбори: <span class="prop-value">21-30' \
            ' мм</span> </li> <li> Вид товару: <span class="prop-value"> <a hr' \
            'ef="/ua/catalog/zhenskaya_obuv/good_type-sapogi/"> Чоботи та ботфо' \
            'рти </a> </span> </li> <li> Сезон: <a href="/ua/catalog/zhenskaya_o' \
            'buv/good_type-sapogi-season-osen-zima/"> <span class="prop-value">О' \
            'сінь-Зима 2021</span> </a> </li> <li> Стиль: <span class="prop-val' \
            'ue">Casual</span> </li> <li> Країна: <span class="prop-value">Інді' \
            'я</span> </li> <li> Стать: <span class="prop-value">Жіноче</span> </li>'


def clear_intertop_characteristics_html(raw_characteristics):
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    chars_text = [string for string in soup.strings]
    cleared_text = list(filter(lambda string: string != ' ' and string != ', ', chars_text))
    text_without_extra_spaces = list(map(lambda string: string.strip(' '), cleared_text))
    return text_without_extra_spaces


def intertop_characteristics_pretty_view(description_list):
    grouped_by_2 = [description_list[n:n + 2] for n in range(0, len(description_list), 2)]
    return '\n'.join(list(map(' '.join, grouped_by_2)))


def clear_intertop_description_html(raw_characteristics):
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    text = [string for string in soup.strings]
    return text


def intertop_description_pretty_view(description_list):
    description_list = list(map(lambda string: ('  ' + string), description_list))
    return '\n'.join(description_list)


if __name__ == '__main__':
    # print(intertop_characteristics_pretty_view(clear_intertop_characteristics_html(raw_chars)))
    print(intertop_description_pretty_view(clear_intertop_description_html(raw_desc)))
