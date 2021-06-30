from bs4 import BeautifulSoup


def remove_extra_elements(characteristics_list):
    pos = None
    searched_element = 'Додатково'
    try:
        pos = characteristics_list.index(searched_element)
    except Exception:
        pass
    if pos is not None:
        characteristics_list.pop(pos)
        characteristics_list.pop(pos)
    return characteristics_list


def clean_description_html(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    result = []
    for p in soup.select('p'):
        result.append(p.text)
    empty_element_count = result.count('')
    for i in range(0, empty_element_count):
        result.remove('')
    result = list(map(lambda string: ('  ' + string), result))
    return '\n'.join(result)


def clean_characteristics_html(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    try:
        soup.h2.decompose()
        soup.div.decompose()
    except Exception:
        pass
    characteristics = []
    for li in soup.select('li'):
        for span in li.select('span'):
            characteristics.append(span.text)
    return characteristics


def pretty_view(characteristics_list):
    characteristics_list = [x.strip(' ') for x in characteristics_list]
    grouped_by_2 = [characteristics_list[n:n + 2] for n in range(0, len(characteristics_list), 2)]
    return '\n'.join(list(map(' : '.join, grouped_by_2)))


def is_html(cell_value):
    html = False
    try:
        html = bool(BeautifulSoup(cell_value, "html.parser").find())
    except Exception:
        pass
    return html


if __name__ == '__main__':
    raw_html_characteristics = '<h2 class="h2 f-icon-before f-icon-107"> Характеристики <span> Смартфон Samsung Galaxy A' \
                               '51 (A515F) 6/128GB DS Black</span></h2><div class="articul-inline">Артикул: <span class=' \
                               '"bold">SM-A515FZKWSEK</span></div><div class="characteristics withHidden addCopyright op' \
                               'ened"><div class="text"><div class="full_content"><ul><li class=""><div><span>Модель</sp' \
                               'an><span class="bold">Galaxy A51</span></div><div class="dashed-delimiter"></div></li><l' \
                               'i class=""><div><span> Дисплей (діагональ) </span><span class="bold">6.5</span></div><di' \
                               'v class="dashed-delimiter"></div></li><li class=""><div><span>Дисплей (макс.роздільна зд' \
                               'атність) </span><span class="bold">2400x1080</span></div><div class="dashed-delimiter"><' \
                               '/div></li><li class=""><div><span>Дисплей (тип матриці)</span><span class="bold"><a href=' \
                               '"/ua/telecommunication/smart/super-amoled/">Super AMOLED</a></span></div><div class="dash' \
                               'ed-delimiter"></div></li><li class=""><div><span>Вбудована память</span><span class="bold' \
                               '"><a href="/ua/telecommunication/smart/vstroennaya_pamyat_gb_128/">128 ГБ</a></span></div' \
                               '><div class="dashed-delimiter"></div></li><li class=""><div><span> Оперативна память (обєм' \
                               ') </span><span class="bold"><a href="/ua/telecommunication/smart/6gb-ram/">6 Гб</a></span>' \
                               '</div><div class="dashed-delimiter"></div></li><li class=""><div><span>Підтримка карт памя' \
                               'ті</span><span class="bold">Так</span></div><div class="dashed-delimiter"></div></li><li c' \
                               'lass=""><div><span> Обєм карт памяті, до </span><span class="bold">microSD до 512 Гб</span' \
                               '></div><div class="dashed-delimiter"></div></li><li class=""><div><span>Кількість SIM-карт<' \
                               '/span><span class="bold"><a href="/ua/telecommunication/smart/dve-sim-karty/">2</a></span>' \
                               '</div><div class="dashed-delimiter"></div></li><li class=""><div><span>Формат SIM-карти</s' \
                               'pan><span class="bold"><a href="/ua/telecommunication/smart/format_sim-karty_nano-sim/">Nano' \
                               '-SIM</a></span></div><div class="dashed-delimiter"></div></li><li class=""><div><span>Режим' \
                               ' роботи SIM-карт</span><span class="bold">Одночасно</span></div><div class="dashed-delimiter"' \
                               '></div></li><li class=""><div><span>Стандарти передачі даних</span><span class="bold">2G, 3G,' \
                               ' <a href="/ua/telecommunication/smart/4g_lte/">4G (LTE)</a></span></div><div class="dashed' \
                               '-delimiter"></div></li><li class=""><div><span>LTE</span><span class="bold">Так</span></d' \
                               'iv><div class="dashed-delimiter"></div></li><li class=""><div><span> Процесор (к-сть ядер)' \
                               ' </span><span class="bold"><a href="/ua/telecommunication/smart/processor_k-vo_yader_sht_8' \
                               '/">8 ядер</a></span></div><div class="dashed-delimiter"></div></li><li class="hidden-chara' \
                               'cteristics "><div><span>Процесор (тактова частота - turbo), ГГц</span><span class="bold">1' \
                               ',7, 2,3</span></div><div class="dashed-delimiter"></div></li><li class="hidden-characteris' \
                               'tics "><div><span>Основна камера, Мпікс</span><span class="bold">48+12+5+5</span></div><div ' \
                               'class="dashed-delimiter"></div></li><li class="hidden-characteristics "><div><span>Запис ві' \
                               'део</span><span class="bold">UHD (3840x2160)</span></div><div class="dashed-delimiter"></d' \
                               'iv></li><li class="hidden-characteristics "><div><span>Фронтальна (селфі) камера, Мпікс</s' \
                               'pan><span class="bold">32</span></div><div class="dashed-delimiter"></div></li><li class="' \
                               'hidden-characteristics "><div><span>Безпека</span><span class="bold"><a href="/ua/telecommu' \
                               'nication/smart/skaner_otpechatka_palca/">Сканер відбитка пальця</a></span></div><div class' \
                               '="dashed-delimiter"></div></li><li class="hidden-characteristics "><div><span>Операційна си' \
                               'стема</span><span class="bold"><a href="/ua/telecommunication/smart/android/">Android</a></' \
                               'span></div><div class="dashed-delimiter"></div></li><li class="hidden-characteristics "><di' \
                               'v><span>Ємність акумулятора, мАг</span><span class="bold">4000</span></div><div class="dashe' \
                               'd-delimiter"></div></li><li class="hidden-characteristics "><div><span> Бездротові технолог' \
                               'ії </span><span class="bold">Bluetooth, <a href="/ua/telecommunication/smart/gps/">GPS</a>,' \
                               ' <a href="/ua/telecommunication/smart/nfc/">NFC</a>, Wi-Fi</span></div><div class="dashed-d' \
                               'elimiter"></div></li><li class="hidden-characteristics "><div><span>Bluetooth</span><span cl' \
                               'ass="bold">v5.0</span></div><div class="dashed-delimiter"></div></li><li class="hidden-chara' \
                               'cteristics "><div><span><p>NFC-чіп (комунікація ближнього поля)</p></span><span class="bold">' \
                               'Так</span></div><div class="dashed-delimiter"></div></li><li class="hidden-characteristics ">' \
                               '<div><span> Супутникова система </span><span class="bold">Beidou (BDS), Galileo, Glonass</spa' \
                               'n></div><div class="dashed-delimiter"></div></li><li class="hidden-characteristics "><div><sp' \
                               'an>Колір (основний) </span><span class="bold"><a href="/ua/telecommunication/smart/chernyyi/"' \
                               '>Чорний</a></span></div><div class="dashed-delimiter"></div></li><li class="hidden-characteri' \
                               'stics "><div><span>Товщина, мм</span><span class="bold">7,9</span></div><div class="dashed-de' \
                               'limiter"></div></li><li class="hidden-characteristics "><div><span>Загальна ширина виробу (W),' \
                               ' мм</span><span class="bold">73,6</span></div><div class="dashed-delimiter"></div></li><li cla' \
                               'ss="hidden-characteristics "><div><span>Загальна висота виробу (H), мм</span><span class="bold' \
                               '">158,5</span></div><div class="dashed-delimiter"></div></li><li class="hidden-characteristics' \
                               ' "><div><span>Вага, грам</span><span class="bold">172</span></div><div class="dashed-delimiter' \
                               '"></div></li><li class="hidden-characteristics "><div><span>Інтерфейси</span><span class="bol' \
                               'd">3,5 mm, USB 2.0, USB Type-C</span></div><div class="dashed-delimiter"></div></li><li class="' \
                               'hidden-characteristics "><div><span>Клас</span><span class="bold"><a href="/ua/telecommunication' \
                               '/smart/bezramochnye/"> безрамковий </a>, <a href="/ua/telecommunication/smart/dlya_devushek/">дл' \
                               'я дівчат</a>, для роботи, <a href="/ua/telecommunication/smart/dlya_selfi/">Для селфі</a>, <a hr' \
                               'ef="/ua/telecommunication/smart/imidzhevye/">Іміджевий</a>, <a href="/ua/telecommunication/smart/' \
                               's_bolshim_ekranom/">З великим екраном</a></span></div><div class="dashed-delimiter"></div></li><l' \
                               'i class="hidden-characteristics "><div><span>Гарантія, міс.</span><span class="bold">12</span></d' \
                               'iv><div class="dashed-delimiter"></div></li><li><div><span>Штрихкод</span><span class="bold barc' \
                               'ode">8806090213748</span></div><div class="dashed-delimiter"></div></li><li><div><span>Додатково</' \
                               'span><span class="bold"><a href="/ua/telecommunication/smart/samsung_dual_sim/">Смартфон Самсунг ' \
                               'на 2 сім карти</a>, <a href="/ua/telecommunication/smart/android_dual_sim/">Андроїд на 2 сім карт' \
                               'и</a>, <a href="/ua/telecommunication/smart/telefon-s-bolshoj-batareej/">телефон з великою батареє' \
                               'ю</a>, <a href="/ua/telecommunication/smart/byudzhetnye-smartfony/">Бюджетні смартфони</a>, <a hre' \
                               'f="/ua/telecommunication/smart/for-men/">Телефони для чоловіків</a>, <a href="/ua/telecommunicatio' \
                               'n/smart/nedorogie-bezramochnie/">Недорогі безрамкові смартфони</a>, <a href="/ua/telecommunication' \
                               '/smart/nedorogoy-s-bolshim-ekranom/">Недорогі смартфони з великим екраном</a>, <a href="/ua/teleco' \
                               'mmunication/smart/s-horoshey-selfi-kameroy/">Телефони із хорошою передньою камерою</a>, <a href="/' \
                               'ua/telecommunication/smart/nedorogie-igrovie/">Бюджетні ігрові смартфони</a>, <a href="/ua/telecom' \
                               'munication/smart/samsung-nfc/">Samsung з NFC</a>, <a href="/ua/telecommunication/smart/ot-4000-grn' \
                               '/">Телефони до 20к грн</a>, <a href="/ua/telecommunication/smart/do-8000-grn/"> Смартфони до 8000 ' \
                               'грн </a>, <a href="/ua/telecommunication/smart/do-12000-grn/"> Смартфони до 12000 грн </a>, <a hre' \
                               'f="/ua/telecommunication/smart/video-4k/"> Смартфони із записом відео 4К </a></span></div><div cla' \
                               'ss="dashed-delimiter"></div></li></ul></div><div id="018572e6-986b-4c6e-9d0b-55cdd5213d49" class="m' \
                               'ore-characteristics gtm-more-characteristics hash_links" data-gtm-track="moreCharacteristics" data-h' \
                               'ash="L3VhL3NtYXJ0Zm9uLXNhbXN1bmctZ2FsYXh5LWE1MS1hNTE1Zi0xMjhnYi1ibGFjay9jaGFyYWN0ZXJpc3RpY3MvNDU5MjY' \
                               'zLmh0bWw="> Показати всі характеристики </div></div></div>'
    if raw_html_characteristics is not None and is_html(raw_html_characteristics):
        cleaned_text = clean_characteristics_html(raw_html_characteristics)
        characteristics = pretty_view(remove_extra_elements(cleaned_text))
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
    if raw_html_description is not None and is_html(raw_html_description):
        description = clean_description_html(raw_html_description)
        print(description)
        # write description to db
