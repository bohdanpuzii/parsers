from bs4 import BeautifulSoup

raw_char = '<strong>Прем’єра аромату:</strong> 2000<br><strong>Країна ТМ:</strong> Франція<br><strong>Зроблено в:</strong>' \
           ' Франція<br><strong>Стать:</strong> для жінок<br><strong>Тип аромату:</strong> альдегідні, квіткові<br><strong>К' \
           'ласифікація:</strong> елітна<br><strong>Початкова нота:</strong> Альдегіди, Апельсиновий цвіт, Бергамот, Лимон<b' \
           'r><strong>Нота серця:</strong> Ірис, Жасмин, Конвалія, Троянда<br><strong>Кінцева нота:</strong> Бурштин, Ваніль,' \
           ' Ветівер, Сандал<br>'

raw_desc = '<div itemprop="description"><p><strong>Склад набору:</strong> Парфумована вода (міні) Charrier Parfums Ambre' \
           ', 5,2 мл + Парфумована вода (міні) Charrier Parfums Mon Otage, 5,2 мл + Парфумована вода (міні) Charrier Parf' \
           'ums Reine de Mai, 5,2 мл + Парфумована вода (міні) Charrier Parfums Air de France, 8 мл + Парфумована вода ' \
           '(міні) Charrier Parfums Gerine, 4,9 мл.<br><br>Набір Parfums De France французького бренда Charrier Parfum' \
           's стане чудовим подарунком подрузі, мамі або собі. Комплект із пяти неперевершених ароматів у мініатюрних ф' \
           'лаконах зачарує вимогливу та вишукану леді. Тravel-версії займуть зовсім небагато місця в косметичці або до' \
           'рожній сумці.<br><br><strong>Парфумована вода Charrier Parfums Mon Otage<br><br></strong>Фруктова свіжість ' \
           'зеленого яблука та цитрусові ноти мандарина стануть чудовим вступом до витонченої композиції. У «серці» си' \
           'мфонії букет із троянд, жасмину, бузку й листя чорної смородини вражає уяву красою та багатством переливів' \
           '. Деревні акорди, чуттєвість амбри й насичені барви мускусу залишаться на шкірі довготривалим шлейфом.<br>' \
           '<br><strong>Парфумована вода Charrier Parfums Reine de Mai<br><br></strong>Неймовірний коктейль із гранат' \
           'а, джекфрута, папайї й пітахайї вирізняється тонізувальним впливом. Яскрава увертюра переходить у квітков' \
           'о-фруктове «серце» з гібіскусу, фрезії, білого персика та гуави. Завершує піраміду дует білого мускусу й ' \
           'амбрети.<br><br><strong>Парфумована вода Charrier Parfums Air de France<br><br></strong>Танжерин, лимон і ' \
           'бергамот – натхненна увертюра, з якої починається звучання Air de France. «Серце» з букета жасмину, троян' \
           'ди, ірису та конвалії дасть змогу подумки перенестися в квітучий сад і відволіктися від повсякденної мету' \
           'шні. Димні ноти ветиверу, деревне тепло сандала, солодкість ванілі й смолисті вкраплення бурштину залишать' \
           'ся на шкірі привабливим посмаком.&nbsp;<br><br><strong>Парфумована вода Charrier Parfums Ambre<br><br></st' \
           'rong>На початку зустрічає свіжість зелених нот, тонізувальна гра цитрусових акордів і квіткова мелодія гер' \
           'ані та фрезії. Вступ зливається з жасмином, трояндою й магнолією в «серці». Чуттєвий мускус, насичені барв' \
           'и амбри, солодкість ванілі та деревний спокій кедра завершують піраміду.<br><br><strong>Парфумована вода C' \
           'harrier Parfums Gerine<br><br></strong>Ягідна партія чорної смородини й ніжність троянди – натхненна увер' \
           'тюра неперевершеної композиції. «Серце» з магнолії, жасмину та ірису наповнить життєвою енергією та весня' \
           'ною свіжістю. Бурштин і мускус завершують симфонію насиченими барвами, які залишаться на шкірі таємничим ' \
           'шлейфом.</p></div>'


def clear_makeup_html(raw_characteristics):
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    text = [string for string in soup.strings]
    return text


def makeup_characteristics_pretty_view(description_list):
    grouped_by_2 = [description_list[n:n + 2] for n in range(0, len(description_list), 2)]
    return '\n'.join(list(map(''.join, grouped_by_2)))


def makeup_description_pretty_view(description_list):
    description_list = list(map(lambda string: ('  ' + string), description_list))
    return '\n'.join(description_list)


if __name__ == '__main__':
    print(makeup_characteristics_pretty_view(clear_makeup_html(raw_char)))
    print(makeup_description_pretty_view(clear_makeup_html(raw_desc)))
