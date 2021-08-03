from bs4 import BeautifulSoup


def clear_moyo_html(raw_characteristics):
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    text = [string for string in soup.strings]
    return text


def moyo_characteristics_pretty_view(description_list):
    description_list = remove_extra_elements(description_list)
    grouped_by_2 = [description_list[n:n + 2] for n in range(0, len(description_list), 2)]
    return '\n'.join(list(map(' : '.join, grouped_by_2)))


def remove_extra_elements(characteristics_list):
    pos = None
    searched_element = 'Додатково'
    try:
        pos = characteristics_list.index(searched_element)
    except Exception:
        pass
    return list(map(lambda string: string.strip(' '), characteristics_list[0:pos]))


def moyo_description_pretty_view(description_list):
    description_list = list(map(lambda string: ('  ' + string), description_list))
    return '\n'.join(description_list)


if __name__ == '__main__':
    raw_html_characteristics = '<tbody><tr class="product_characteristics_list_item"><td class="key">Артикул</td><td ' \
                               'class="value">F2J3HS2W</td></tr><tr class="product_characteristics_list_item"><td clas' \
                               's="key">Штрихкод</td><td class="value">8806098648689</td></tr><tr class="product_chara' \
                               'cteristics_list_item"><td class="key">Тип</td><td class="value"><a href="/ua/bt/kbt/st' \
                               'iralnie-mashiny/tip_polnogabaritnye/">Повногабаритні 48-65 см</a></td></tr><tr class="p' \
                               'roduct_characteristics_list_item"><td class="key">Модель</td><td class="value">F2J3HS2W<' \
                               '/td></tr><tr class="product_characteristics_list_item"><td class="key">Вид прання</td><' \
                               'td class="value">Водою</td></tr><tr class="product_characteristics_list_item"><td class' \
                               '="key">Технологія</td><td class="value">6 Motion, Smart Diagnosis, SpaSteam</td></tr><t' \
                               'r class="product_characteristics_list_item"><td class="key">Тип двигуна</td><td class="' \
                               'value"><a href="/ua/bt/kbt/stiralnie-mashiny/invertornyyi/">Інверторний</a></td></tr><t' \
                               'r class="product_characteristics_list_item"><td class="key">Клас прання</td><td class=' \
                               '"value">A</td></tr><tr class="product_characteristics_list_item"><td class="key">Клас в' \
                               'іджимання</td><td class="value">B</td></tr><tr class="product_characteristics_list_item' \
                               '"><td class="key">Клас енергоспоживання</td><td class="value"><a href="/ua/bt/kbt/stira' \
                               'lnie-mashiny/klass_energopotrebleniya_a_1/">A</a></td></tr><tr class="product_character' \
                               'istics_list_item"><td class="key">Споживання води при пранні, л</td><td class="value">' \
                               '56</td></tr><tr class="product_characteristics_list_item" style="display: none;"><td c' \
                               'lass="key">Швидкість віджимання (об/хв)</td><td class="value">1200</td></tr><tr class=' \
                               '"product_characteristics_list_item" style="display: none;"><td class="key">Тип заванта' \
                               'ження</td><td class="value"><a href="/ua/bt/kbt/stiralnie-mashiny/tip_zagruzki_frontal' \
                               'naya/">Фронтальне</a></td></tr><tr class="product_characteristics_list_item" style="d' \
                               'isplay: none;"><td class="key">Завантаження білизни, кг</td><td class="value">7</td></' \
                               'tr><tr class="product_characteristics_list_item" style="display: none;"><td class="ke' \
                               'y">Споживання електроенергії, кВт/рік</td><td class="value">1,06</td></tr><tr class="' \
                               'product_characteristics_list_item" style="display: none;"><td class="key">Рівень шуму ' \
                               'при пранні, дБ</td><td class="value">55</td></tr><tr class="product_characteristics_l' \
                               'ist_item" style="display: none;"><td class="key">Рівень шуму при віджиманні, дБ</td><' \
                               'td class="value">73</td></tr><tr class="product_characteristics_list_item" style="dis' \
                               'play: none;"><td class="key">Матеріал бака</td><td class="value">Нержавіюча сталь</td>' \
                               '</tr><tr class="product_characteristics_list_item" style="display: none;"><td class="k' \
                               'ey">Діапазон температур прання</td><td class="value">до 95</td></tr><tr class="product' \
                               '_characteristics_list_item" style="display: none;"><td class="key">Кількість програм</' \
                               'td><td class="value">10</td></tr><tr class="product_characteristics_list_item" style=' \
                               '"display: none;"><td class="key">Програми</td><td class="value"> швидко 30 , делікатн' \
                               'а , одяг малюка , повсякденна прання, Полоскання+віджим, змішані тканини, Спортивний од' \
                               'яг, Бавовна, Бавовна макс, Вовна</td></tr><tr class="product_characteristics_list_item"' \
                               ' style="display: none;"><td class="key"> Габарити (ВхШхГ), см </td><td class="value">60' \
                               'х44х85</td></tr><tr class="product_characteristics_list_item" style="display: none;"><' \
                               'td class="key">Ширина, см</td><td class="value">60</td></tr><tr class="product_charact' \
                               'eristics_list_item" style="display: none;"><td class="key"> Висота, см </td><td class=' \
                               '"value">85</td></tr><tr class="product_characteristics_list_item" style="display: none' \
                               ';"><td class="key">Глибина, см</td><td class="value">44</td></tr><tr class="product_ch' \
                               'aracteristics_list_item" style="display: none;"><td class="key"> Вага </td><td class="v' \
                               'alue">59</td></tr><tr class="product_characteristics_list_item" style="display: none;">' \
                               '<td class="key"> Колір </td><td class="value"><a href="/ua/bt/kbt/stiralnie-mashiny/bel' \
                               'yyi/">Білий</a></td></tr><tr class="product_characteristics_list_item" style="display:' \
                               ' none;"><td class="key">Колір (основний)</td><td class="value">Білий</td></tr><tr cla' \
                               'ss="product_characteristics_list_item" style="display: none;"><td class="key">Особливо' \
                               'сті</td><td class="value"> LED дисплей , Звуковий сигнал, Сенсорний дисплей, таймер н' \
                               'а прання </td></tr><tr class="product_characteristics_list_item" style="display: non' \
                               'e;"><td class="key"> SMART Функції </td><td class="value">Smart Diagnosis</td></tr><' \
                               'tr class="product_characteristics_list_item" style="display: none;"><td class="key">До' \
                               'даткові опції</td><td class="value">Захист від дітей, очищення барабана , Система пено' \
                               'подавленія </td></tr><tr class="product_characteristics_list_item" style="display: non' \
                               'e;"><td class="key"> Гарантія, міс. </td><td class="value">12</td></tr><tr class="prod' \
                               'uct_characteristics_list_item" style="display: none;"><td class="key"> Країна-виробник' \
                               ' </td><td class="value">Китай</td></tr><tr class="product_characteristics_list_item" st' \
                               'yle="display: none;"><td class="key">Додатково</td><td class="value"><a href="/ua/bt/kbt' \
                               '/stiralnie-mashiny/stiralnye-mashiny-1200-oborotov/"> Пральні машини 1200 оборотів </a>' \
                               ', <a href="/ua/bt/kbt/stiralnie-mashiny/stiralnye-mashiny-s-nerzhaveyushhim-bakom/"> П' \
                               'ральні машини з нержавіючим баком </a>, <a href="/ua/bt/kbt/stiralnie-mashiny/stiraln' \
                               'ye-mashiny-s-nizkim-urovnem-shuma/"> Пральні машини з низьким рівнем шуму </a>, <a h' \
                               'ref="/ua/bt/kbt/stiralnie-mashiny/deshevye-stiralnye-mashiny/"> Дешеві пральні машини ' \
                               '</a>, <a href="/ua/bt/kbt/stiralnie-mashiny/lg-7kg/"> Пральні машини LG 7 кг </a>, <a' \
                               ' href="/ua/bt/kbt/stiralnie-mashiny/lg-frontalnaya-zagruzka/"> Пральні машини LG з ' \
                               'фронтальним завантаженням </a></td></tr></tbody>'
    characteristics = moyo_characteristics_pretty_view(clear_moyo_html(raw_html_characteristics))
    print(characteristics)
    # write characteristics to db
    raw_html_description = '<h2 style="text-align:center"><div class="textimg-wrap" style="text-align: center;"><div cl' \
                           'ass="textimg-block" style="width: 1000px; height: auto;"><img class="lazy-intersection lazy' \
                           '-space intersection-observing" src="https://img.moyo.ua/img/products_desc/4730/473062_15991' \
                           '33741_0.jpg" alt="" data-srcset-hash="aHR0cHM6Ly9pbWcubW95by51YS9pbWcvcHJvZHVjdHNfZGVzYy80N' \
                           'zMwLzQ3MzA2Ml8xNTk5MTMzNzQxXzAuanBn" srcset="/images/bx_loader_grey.gif"><div class="lazy-' \
                           'space-holder" style="padding-top: 40.6%;"></div></div></div></h2><h2 style="text-align:ju' \
                           'stify">СКОРОСТНОЙ ПРОРЫВ</h2><p style="text-align:justify">Новейший процессор 10-го покол' \
                           'ения Intel® Core™ i7 обеспечивает 15% прирост производительности по сравнению со своим пр' \
                           'едшественником. Повышенная частота в однопоточном режиме будет особенно полезной для игр.' \
                           '</p><p style="text-align:center"></p><div class="textimg-wrap" style="text-align: center;"' \
                           '><div class="textimg-block" style="width: 1000px; height: auto;"><img class="lazy-intersec' \
                           'tion lazy-space intersection-observing" src="https://img.moyo.ua/img/products_desc/4730/473' \
                           '062_1599133741_1.jpg" alt="" data-srcset-hash="aHR0cHM6Ly9pbWcubW95by51YS9pbWcvcHJvZHVjdHNfZ' \
                           'GVzYy80NzMwLzQ3MzA2Ml8xNTk5MTMzNzQxXzEuanBn" srcset="/images/bx_loader_grey.gif"><div class' \
                           '="lazy-space-holder" style="padding-top: 63.1%;"></div></div></div><p></p><h2 style="text-al' \
                           'ign:justify">СОВРЕМЕННЫЙ УСКОРИТЕЛЬ</h2><p style="text-align:justify">Графический процессо' \
                           'р GeForce® GTX 1660 Ti: создан на базе высокопроизводительной микроархитектуры NVIDIA Turi' \
                           'ng™ и сравним по скорости с GeForce GTX 1070. Он прекрасно проявляет себя в популярных иг' \
                           'рах, особенно тех, которые используют современные графические технологии.</p><p style="te' \
                           'xt-align:center"></p><div class="textimg-wrap" style="text-align: center;"><div class="tex' \
                           'timg-block" style="width: 1000px; height: auto;"><img class="lazy-intersection lazy-space ' \
                           'intersection-observing" src="https://img.moyo.ua/img/products_desc/4730/473062_1599133742_' \
                           '2.jpg" alt="" data-srcset-hash="aHR0cHM6Ly9pbWcubW95by51YS9pbWcvcHJvZHVjdHNfZGVzYy80NzMwLz' \
                           'Q3MzA2Ml8xNTk5MTMzNzQyXzIuanBn" srcset="/images/bx_loader_grey.gif"><div class="lazy-space-' \
                           'holder" style="padding-top: 71.6%;"></div></div></div><p></p><h2 style="text-align:justify"' \
                           '>ТОНКОРАМОЧНЫЙ ДИСПЛЕЙ</h2><p style="text-align:justify">Дисплей с великолепными скоростны' \
                           'ми характеристиками обеспечит превосходное изображение в динамичных компьютерных играх.</p' \
                           '><p style="text-align:center"></p><div class="textimg-wrap" style="text-align: center;"><di' \
                           'v class="textimg-block" style="width: 1000px; height: auto;"><img class="lazy-intersection' \
                           ' lazy-space intersection-observing" src="https://img.moyo.ua/img/products_desc/4730/473062' \
                           '_1599133742_3.jpg" alt="" data-srcset-hash="aHR0cHM6Ly9pbWcubW95by51YS9pbWcvcHJvZHVjdHNfZG' \
                           'VzYy80NzMwLzQ3MzA2Ml8xNTk5MTMzNzQyXzMuanBn" srcset="/images/bx_loader_grey.gif"><div class' \
                           '="lazy-space-holder" style="padding-top: 62.4%;"></div></div></div><p></p><h2 style="text-' \
                           'align:justify">ТОНКИЙ И ЛЕГКИЙ АЛЮМИНИЕВЫЙ КОРПУС</h2><p style="text-align:justify">Металл' \
                           'ическая поверхность крышки и области вокруг клавиатуры в сочетании с футуристическим дизайн' \
                           'ом.</p><p style="text-align:center"></p><div class="textimg-wrap" style="text-align: center' \
                           ';"><div class="textimg-block" style="width: 1000px; height: auto;"><img class="lazy-interse' \
                           'ction lazy-space intersection-observing" src="https://img.moyo.ua/img/products_desc/4730/4' \
                           '73062_1599133743_4.jpg" alt="" data-srcset-hash="aHR0cHM6Ly9pbWcubW95by51YS9pbWcvcHJvZHVjd' \
                           'HNfZGVzYy80NzMwLzQ3MzA2Ml8xNTk5MTMzNzQzXzQuanBn" srcset="/images/bx_loader_grey.gif"><div c' \
                           'lass="lazy-space-holder" style="padding-top: 56.4%;"></div></div></div><p></p><h2 style="te' \
                           'xt-align:justify">7 ЧАСОВ В АВТОНОМНОМ РЕЖИМЕ</h2><p style="text-align:justify">Для работы' \
                           ' и развлечений – без привязки к розетке.</p><p style="text-align:center"></p><div class="t' \
                           'extimg-wrap" style="text-align: center;"><div class="textimg-block" style="width: 1000px; ' \
                           'height: auto;"><img class="lazy-intersection lazy-space intersection-observing" src="https' \
                           '://img.moyo.ua/img/products_desc/4730/473062_1599133743_5.jpg" alt="" data-srcset-hash="aH' \
                           'R0cHM6Ly9pbWcubW95by51YS9pbWcvcHJvZHVjdHNfZGVzYy80NzMwLzQ3MzA2Ml8xNTk5MTMzNzQzXzUuanBn" sr' \
                           'cset="/images/bx_loader_grey.gif"><div class="lazy-space-holder" style="padding-top: 73%;"' \
                           '></div></div></div><p></p><h2 style="text-align:justify">РЕВОЛЮЦИОННАЯ СИСТЕМА ОХЛАЖДЕНИЯ<' \
                           '/h2><p style="text-align:justify">Использование 6-ти тепловых трубок для раздельного охлаж' \
                           'дения центрального и графического процессоров гарантирует стабильную работу ноутбука под э' \
                           'кстремальными игровыми нагрузками.</p><p style="text-align:center"></p><div class="textimg' \
                           '-wrap" style="text-align: center;"><div class="textimg-block" style="width: 1000px; height' \
                           ': auto;"><img class="lazy-intersection lazy-space intersection-observing" src="https://img' \
                           '.moyo.ua/img/products_desc/4730/473062_1599133743_6.jpg" alt="" data-srcset-hash="aHR0cHM6' \
                           'Ly9pbWcubW95by51YS9pbWcvcHJvZHVjdHNfZGVzYy80NzMwLzQ3MzA2Ml8xNTk5MTMzNzQzXzYuanBn" srcset="' \
                           '/images/bx_loader_grey.gif"><div class="lazy-space-holder" style="padding-top: 48.2%;"></di' \
                           'v></div></div><p></p><h2 style="text-align:justify">ИСТИННОЕ ЗВУЧАНИЕ МУЗЫКИ</h2><p style="' \
                           'text-align:justify">Погрузитесь в мир безупречного звука с помощью аудиосистемы с поддержк' \
                           'ой форматов высокого разрешения Hi-Res Audio. Слушайте музыку в таком виде, в каком ее хот' \
                           'ели представить исполнители!</p><p style="text-align:center"></p><div class="textimg-wrap" ' \
                           'style="text-align: center;"><div class="textimg-block" style="width: 1000px; height: auto;"' \
                           '><img class="lazy-intersection lazy-space intersection-observing" src="https://img.moyo.ua/' \
                           'img/products_desc/4730/473062_1599133743_7.jpg" alt="" data-srcset-hash="aHR0cHM6Ly9pbWcub' \
                           'W95by51YS9pbWcvcHJvZHVjdHNfZGVzYy80NzMwLzQ3MzA2Ml8xNTk5MTMzNzQzXzcuanBn" srcset="/images/bx' \
                           '_loader_grey.gif"><div class="lazy-space-holder" style="padding-top: 41.7%;"></div></div></d' \
                           'iv><p></p><h2 style="text-align:justify">ПРИЛОЖЕНИЕ MSI APP PLAYER</h2><p style="text-align' \
                           ':justify">Разработанное в эксклюзивном партнерстве с компанией BlueStacks приложение MSI Ap' \
                           'p Player наделяет компьютеры и ноутбуки MSI возможностью запускать мобильные игры – с велик' \
                           'олепным качеством изображения и поддержкой дополнительных функций, например, настройкой под' \
                           'светки клавиатуры в соответствии с текущей игрой.</p><p style="text-align:center"></p><div ' \
                           'class="textimg-wrap" style="text-align: center;"><div class="textimg-block" style="width: 1' \
                           '000px; height: auto;"><img class="lazy-intersection lazy-space intersection-observing" src=' \
                           '"https://img.moyo.ua/img/products_desc/4730/473062_1599133744_8.jpg" alt="" data-srcset-has' \
                           'h="aHR0cHM6Ly9pbWcubW95by51YS9pbWcvcHJvZHVjdHNfZGVzYy80NzMwLzQ3MzA2Ml8xNTk5MTMzNzQ0XzguanBn"' \
                           ' srcset="/images/bx_loader_grey.gif"><div class="lazy-space-holder" style="padding-top: 53.' \
                           '4%;"></div></div></div><p></p>'
    description = moyo_description_pretty_view(clear_moyo_html(raw_html_description))
    print(description)
    # write description to db
