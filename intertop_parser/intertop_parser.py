from bs4 import BeautifulSoup

raw_desc = 'Текстильні сліпони Skechers Seager - Stat (49481 NVY) з акуратним мінімалістичним верхом, фірмовою устілко' \
           'ю і пружною підошвою.<br> Особливості:<br> • Безшовний сітчастий верх з оригінальним кантом<br> • Спеціальн' \
           'а підкладка Bio-Dri ™ підтримує відмінну циркуляцію повітря всередині взуття і швидко сохне<br> • Мяка устілка' \
           ' з охолодженням і ефектом памяті стопи Air Cooled Memory Foam ™<br> • Пружна підошва поглинає удари<br> • Можна' \
           ' прати в пральній машині'

raw_chars = '<li>\n<span class="prop-name"> Артикул: </span>\n<span class="prop-value">\nKW6150 </span>\n</li>\n<li>\n' \
            '<span class="prop-name"> Бренд: </span>\n<span class="prop-value">\n<a href="/ua/catalog/zhenskaya_obuv/brand' \
            '-skechers-good_type-clipony/">Skechers</a>\n</span>\n</li>\n<li>\nВерх:\n<span class="prop-value">\nтекстиль ' \
            '</span>\n</li>\n<li>\nМатеріал підкладки:\n<span class="prop-value">\n<a href="/ua/catalog/zhenskaya_obuv/good' \
            '_type-clipony-lining_material-tekstil/">текстиль</a>\n</span>\n</li>\n<li>\nМатеріал підошви:\n<span class=' \
            '"prop-value">етиленвінілацетат (ЕВА)</span>\n</li>\n<li>\nКолір:\n<span class="prop-value">\n<a href="/ua/' \
            'catalog/zhenskaya_obuv/color-siniy-good_type-clipony/"> Синій </a> </span>\n</li>\n<li>\nВид товару:\n<span' \
            ' class="prop-value">\n<a href="/ua/catalog/zhenskaya_obuv/good_type-clipony/"> Сліпони та еспадрильї </a> ' \
            '</span>\n</li>\n<li>\nСезон:\n<a href="/ua/catalog/zhenskaya_obuv/good_type-clipony-season-vesna-leto/"> ' \
            '<span class="prop-value">Весна-Літо 2021</span>\n</a> </li>\n<li>\nСтиль:\n<span class="prop-value">Casual' \
            '</span>\n</li>\n<li>\nКраїна:\n<span class="prop-value">Китай</span>\n</li>\n<li>\nСтать:\n<span class="prop-' \
            'value">Жіноче</span>\n</li>\n<li>\nВид носку взуття:\n<span>Круглий</span>\n</li>'


def clear_intertop_characteristics_html(raw_characteristics):
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    chars_text = [string for string in soup.strings]
    cleared_text = list(filter(lambda string: string != ' ' and string != ', ' and string != '\n', chars_text))
    text_without_extra_spaces = list(map(lambda string: string.strip(' ').replace('\n',''), cleared_text))
    return text_without_extra_spaces


def intertop_characteristics_pretty_view(description_list):
    grouped_by_2 = [description_list[n:n + 2] for n in range(0, len(description_list), 2)]
    return '\n'.join(list(map(' '.join, grouped_by_2)))


# def clear_intertop_characteristics_html(raw_characteristics):
#     characteristics_list = []
#     soup = BeautifulSoup(raw_characteristics, 'html.parser')
#     for li in soup.select('li'):
#         characteristics_list.append(li.text.replace('\n', '').strip(' '))
#     return characteristics_list
#
#
# def intertop_characteristics_pretty_view(characteristics_list):
#     return '\n'.join(characteristics_list)


def clear_intertop_description_html(raw_characteristics):
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    text = [string.replace('\n', '') for string in soup.strings]
    return text


def intertop_description_pretty_view(description_list):
    description_list = list(map(lambda string: ('  ' + string), description_list))
    print(description_list)
    return '\n'.join(description_list)


if __name__ == '__main__':
    print(intertop_characteristics_pretty_view(clear_intertop_characteristics_html(raw_chars)))
    (intertop_description_pretty_view(clear_intertop_description_html(raw_desc)))
