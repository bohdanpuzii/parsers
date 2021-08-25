from bs4 import BeautifulSoup


def clear_moyo_characteristics_html(raw_characteristics):
    characteristics_list = []
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    for td in soup.select('td'):
        characteristics_list.append(td.text)
    return list(map(lambda string: string.strip(' '), characteristics_list))


def clear_moyo_description_html(raw_characteristics):
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    text = [string for string in soup.strings]
    return text


def moyo_characteristics_pretty_view(characteristics_list):
    pos = None
    searched_element = 'Додатково'
    try:
        pos = characteristics_list.index(searched_element)
    except Exception:
        pass
    cleared_characteristics = list(map(lambda string: string.strip(' '), characteristics_list[0:pos]))
    grouped_by_2 = [cleared_characteristics[n:n + 2] for n in range(0, len(cleared_characteristics), 2)]
    return '\n'.join(list(map(' : '.join, grouped_by_2)))


def moyo_description_pretty_view(description_list):
    description_list = list(map(lambda string: ('  ' + string), description_list))
    return '\n'.join(description_list)


def clear_moyo_reviews_html(raw_reviews):
    comments_list = []
    comment = {}
    soup = BeautifulSoup(raw_reviews, 'html.parser')
    for item in soup.find_all('div', {'class': 'product_review-item_block js-review-item-block'}):
        comment['author'] = item.find('div', {'class': 'product_review-item_username'}).text
        comment['date'] = item.find('div', {'class': 'product_review-item_date'}).text
        comment['body'] = item.find('div', {'class': 'product_review-item_text'}).text
        comment['advantages'] = item.find('div', {'class': 'product_review-item_advantages_text'}).text
        comment['disadvantages'] = item.find('div', {'class': 'product_review-item_advantages negative'}).find('div',
                                                                                                               'product_review-item_advantages_text').text
        comment_copy = comment.copy()
        comments_list.append(comment_copy)
    return comments_list


if __name__ == '__main__':
    raw_html_characteristics = '<tbody><tr class="product_characteristics_list_item"><td class="key">Артикул</td><td clas' \
                               's="value">EW6S326SUI</td></tr><tr class="product_characteristics_list_item"><td class="key"' \
                               '>Штрихкод</td><td class="value">7332543747757</td></tr><tr class="product_characteristics_l' \
                               'ist_item"><td class="key">Тип</td><td class="value"><a href="/ua/bt/kbt/stiralnie-mashiny/t' \
                               'ip_uzkie/">Вузькі 32-47 см</a></td></tr><tr class="product_characteristics_list_item"><td c' \
                               'lass="key">Модель</td><td class="value">EW6S326SUI</td></tr><tr class="product_characteristi' \
                               'cs_list_item"><td class="key">Вид прання</td><td class="value"><a href="/ua/bt/kbt/stiralnie' \
                               '-mashiny/vid_stirki_parom_i_vodoyi/">Парою і водою</a></td></tr><tr class="product_characteri' \
                               'stics_list_item"><td class="key">Технологія</td><td class="value">Fuzzy Logic</td></tr><tr clas' \
                               's="product_characteristics_list_item"><td class="key">Тип двигуна</td><td class="value"><a hre' \
                               'f="/ua/bt/kbt/stiralnie-mashiny/invertornyyi/">Інверторний</a></td></tr><tr class="product_cha' \
                               'racteristics_list_item"><td class="key">Клас прання</td><td class="value">A</td></tr><tr class' \
                               '="product_characteristics_list_item"><td class="key">Клас віджимання</td><td class="value">B</' \
                               'td></tr><tr class="product_characteristics_list_item"><td class="key">Клас енергоспоживання</' \
                               'td><td class="value"><a href="/ua/bt/kbt/stiralnie-mashiny/klass_energopotrebleniya_a_3/">A++' \
                               '+</a></td></tr><tr class="product_characteristics_list_item"><td class="key">Споживання води п' \
                               'ри пранні, л</td><td class="value">9400</td></tr><tr class="product_characteristics_list_item" ' \
                               'style="display: none;"><td class="key">Швидкість віджимання (об/хв)</td><td class="value">1200</' \
                               'td></tr><tr class="product_characteristics_list_item" style="display: none;"><td class="key">Тип' \
                               ' завантаження</td><td class="value"><a href="/ua/bt/kbt/stiralnie-mashiny/tip_zagruzki_frontalna' \
                               'ya/">Фронтальне</a></td></tr><tr class="product_characteristics_list_item" style="display: none;' \
                               '"><td class="key">Завантаження білизни, кг</td><td class="value">6</td></tr><tr class="product_c' \
                               'haracteristics_list_item" style="display: none;"><td class="key">Споживання електроенергії, кВт/' \
                               'рік</td><td class="value">Немає даних</td></tr><tr class="product_characteristics_list_item" sty' \
                               'le="display: none;"><td class="key">Рівень шуму при пранні, дБ</td><td class="value">54</td></t' \
                               'r><tr class="product_characteristics_list_item" style="display: none;"><td class="key">Рівень шу' \
                               'му при віджиманні, дБ</td><td class="value">77</td></tr><tr class="product_characteristics_list_i' \
                               'tem" style="display: none;"><td class="key">Матеріал бака</td><td class="value">Полімер</td></tr>' \
                               '<tr class="product_charac' \
                               'teristics_list_item" style="display: none;"><td class="key">Діапазон температур прання</td><td' \
                               ' class="value">Немає даних</td></tr><tr class="product_characteristics_list_item" style="displa' \
                               'y: none;"><td class="key">Кількість програм</td><td class="value">14</td></tr><tr class="produ' \
                               'ct_characteristics_list_item" style="display: none;"><td class="key">Програми</td><td class="v' \
                               'alue">антиаллергенная з парою, швидке прання , Верхній одяг, увімк/вимк, делікатна , дитячу бі' \
                               'лизну , Джинсова тканина , Віджимання + слив , полоскання, синтетика, Спорт , Бавовна, Бавовна' \
                               ' Еко , шовк , шерсть плюс</td></tr><tr class="product_characteristics_list_item" style="displ' \
                               'ay: none;"><td class="key"> Габарити (ВхШхГ), см </td><td class="value">84,3х59,5х41,1</td></' \
                               'tr><tr class="product_characteristics_list_item" style="display: none;"><td class="key">Шири' \
                               'на, см</td><td class="value">59,5</td></tr><tr class="product_characteristics_list_item" st' \
                               'yle="display: none;"><td class="key"> Висота, см </td><td class="value">84,3</td></tr><tr c' \
                               'lass="product_characteristics_list_item" style="display: none;"><td class="key">Глибина, см<' \
                               '/td><td class="value">41,1</td></tr><tr class="product_characteristics_list_item" style="dis' \
                               'play: none;"><td class="key"> Вага </td><td class="value">58,5</td></tr><tr class="product_ch' \
                               'aracteristics_list_item" style="display: none;"><td class="key"> Колір </td><td class="value' \
                               '"><a href="/ua/bt/kbt/stiralnie-mashiny/belyyi/">Білий</a></td></tr><tr class="product_charac' \
                               'teristics_list_item" style="display: none;"><td class="key">Колір (основний)</td><td class="' \
                               'value">Білий</td></tr><tr class="product_characteristics_list_item" style="display: none;"><' \
                               'td class="key">Особливості</td><td class="value"> LED дисплей , <a href="/ua/bt/kbt/stiralnie' \
                               '-mashiny/zashchita_ot_deteyi/">Захист від дітей</a>, <a href="/ua/bt/kbt/stiralnie-mashiny/sti' \
                               'ralnye-mashiny-s-polnoj-zashhitoj-ot-protechek/">Захист від протікання</a>, Контроль дисбаланс' \
                               'у , контроль піноутворення, Таймер відстрочки початку прання</td></tr><tr class="product_chara' \
                               'cteristics_list_item" style="display: none;"><td class="key">Додаткові опції</td><td class="va' \
                               'lue">регуліромие ніжки</td></tr><tr class="product_characteristics_list_item" style="display:' \
                               ' none;"><td class="key"> Гарантія, міс. </td><td class="value">12</td></tr><tr class="product' \
                               '_characteristics_list_item" style="display: none;"><td class="key"> Країна-виробник </td><td c' \
                               'lass="value">Україна</td></tr><tr class="product_characteristics_list_item" style="display: n' \
                               'one;"><td class="key">Додатково</td><td class="value"><a href="/ua/bt/kbt/stiralnie-mashiny/s' \
                               'tiralnye-mashiny-1200-oborotov/"> Пральні машини 1200 оборотів </a>, <a href="/ua/bt/kbt/stir' \
                               'alnie-mashiny/deshevye-stiralnye-mashiny/"> Дешеві пральні машини </a>, <a href="/ua/bt/kbt/s' \
                               'tiralnie-mashiny/electrolux-6-kg/"> Пральні машини ELECTROLUX 6 кг </a>, <a href="/ua/bt/kbt/st' \
                               'iralnie-mashiny/uzkie-6kg/"> Вузькі пральні машини 6 кг </a>, <a href="/ua/bt/kbt/stiralnie-ma' \
                               'shiny/electrolux-frontalnaya-zagruzka/"> Пральні машини ELECTROLUX з фронтальним завантаженням' \
                               ' </a>, <a href="/ua/bt/kbt/stiralnie-mashiny/electrolux-uzkiye/"> Вузькі пральні машини ELECTR' \
                               'OLUX </a></td></tr></tbody>'
    characteristics = moyo_characteristics_pretty_view(clear_moyo_characteristics_html(raw_html_characteristics))
    # print(characteristics)
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
    description = moyo_description_pretty_view(clear_moyo_description_html(raw_html_description))
    # print(description)
    # write description to db
    raw_html_reviews = '<div class="product_review-item js-comment-item"><div class="product_review-item_img empty"><span>І</span></div><div class="product_review-item_content" ' \
                       'id="comment_770040"><div class="product_review-item_block js-review-item-block" itemprop="review" itemscope="" itemtype="http://schema.org/Review" id="comment_770040">' \
                       '<meta itemprop="name" content=" Смартфон Samsung Galaxy A12 4/64GB Red "><div class="product_review-item_head"><div class="product_review-item_username" itemprop="author">' \
                       'Інна</div><div class="product_review-item_rate"><div class="rate-star_container"><div class="rate-star active-start"></div><div class="rate-star active-start"></div><di' \
                       'v class="rate-star active-start"></div><div class="rate-star active-start"></div><div class="rate-star active-start"></div></div></div><div class="product_review-item_' \
                       'usercheck"></div><div class="hidden_comment" itemprop="reviewRating" itemscope="" itemtype="http://schema.org/Rating"><meta itemprop="worstRating" content="0"><meta it' \
                       'emprop="bestRating" content="5"><meta itemprop="ratingValue" content="5"></div><div class="product_review-item_date">20 квітня 2021, 11:02</div></div><div class="prod' \
                       'uct_review-item_body"><div class="product_review-item_text" itemprop="reviewBody"><p>Телефон сподобався. В порівнянні з моїм попереднім самсунгом J3- ракета)))) Стил' \
                       'ьний і батареї вистачає майже на 2 дні.</p></div><div class="product_review-item_advantages"><div class="product_review-item_advantages_title">Переваги:</div><div cla' \
                       'ss="product_review-item_advantages_text"> Батарея,камера </div></div><div class="product_review-item_advantages negative"><div class="product_review-item_advantages_' \
                       'title">Недоліки:</div><div class="product_review-item_advantages_text"> Не знайшла </div></div></div><div class="product_review-item_footer"><div class="product_revi' \
                       'ew-item_footer_section"><div class="product_review-item_to-answer js-answer-form-btn-action">Відповісти</div></div><div class="product_review-item_likes positive">' \
                       '<div class="product_review-item_likes_text"> Відгук був корисний? </div><button id="like-comment-1" data-product_id="480668" data-id="770040" data-gtm-track="like' \
                       'Comment" class="product_review-item_likes_btn js-positive-like"></button><div class="product_review-item_likes_count js-count-like">1</div></div></div></div><div ' \
                       'class="product_answer-form-holder js-answer-form-holder"></div></div></div><div class="product_review-item js-comment-item"><div class="product_review-item_img emp' \
                       'ty"><span>Е</span></div><div class="product_review-item_content" id="comment_767793"><div class="product_review-item_block js-review-item-block" itemprop="review" ' \
                       'itemscope="" itemtype="http://schema.org/Review" id="comment_767793"><meta itemprop="name" content=" Смартфон Samsung Galaxy A12 4/64GB Red "><div class="product_r' \
                       'eview-item_head"><div class="product_review-item_username" itemprop="author">Евгения</div><div class="product_review-item_rate"><div class="rate-star_container"><d' \
                       'iv class="rate-star active-start"></div><div class="rate-star active-start"></div><div class="rate-star active-start"></div><div class="rate-star active-start"></d' \
                       'iv><div class="rate-star active-start"></div></div></div><div class="hidden_comment" itemprop="reviewRating" itemscope="" itemtype="http://schema.org/Rating"><meta' \
                       ' itemprop="worstRating" content="0"><meta itemprop="bestRating" content="5"><meta itemprop="ratingValue" content="5"></div><div class="product_review-item_date">24' \
                       ' березня 2021, 04:23</div></div><div class="product_review-item_body"><div class="product_review-item_text" itemprop="reviewBody"><p>Брали на подарок ребенку. Телеф' \
                       'он за свою цену хороший, быстрый, приятный большой экран. Внешне симпатичный дизайн. Подарком остались довольны.</p></div><div class="product_review-item_advantages' \
                       '"><div class="product_review-item_advantages_title">Переваги:</div><div class="product_review-item_advantages_text"></div></div><div class="product_review-item_adva' \
                       'ntages negative"><div class="product_review-item_advantages_title">Недоліки:</div><div class="product_review-item_advantages_text"></div></div></div><div class="pro' \
                       'duct_review-item_footer"><div class="product_review-item_footer_section"><div class="product_review-item_to-answer js-answer-form-btn-action">Відповісти</div></div>' \
                       '<div class="product_review-item_likes positive"><div class="product_review-item_likes_text"> Відгук був корисний? </div><button id="like-comment-2" data-product_id' \
                       '="480668" data-id="767793" data-gtm-track="likeComment" class="product_review-item_likes_btn js-positive-like"></button><div class="product_review-item_likes_count' \
                       ' js-count-like"></div></div></div></div><div class="product_answer-form-holder js-answer-form-holder"></div></div></div>'
    #print(clear_moyo_reviews_html(raw_html_reviews))
