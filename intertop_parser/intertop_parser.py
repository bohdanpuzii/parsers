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

raw_reviews_html = '<div class="new-prod-comments-name"> Отзывы </div> <div class="new-prod-comments-top"> <div class="new-comments-score"> <div class="bl-sc"> <span> 5.0 </span> </div> <div class="new-comments-score-in">' \
                   ' <i> <img src="/local/templates/intertop/images/comm-big-star.svg" alt=""> </i> <span> 8 оценок </span> </div> </div> <div class="leave-comm"> <a onclick="App.Auth.clickAuth(); return false;"> Оставить' \
                   ' отзыв </a> </div> </div> <div class="wrap-new-comm"> <div class="all-new-comm"> <div class="one-new-comm" data-comment_id="5148353"> <div class="one-new-comm-name"> <span class="one-review-author"> Г' \
                   'ригорій </span> </div> <div class="one-new-comm-info"> <div class="one-new-comm-star"> <span></span><span></span><span></span><span></span><span></span> </div> <div class="one-new-comm-date "> 26.04.2' \
                   '021 </div> </div> <div class="one-new-comm-wrap"> Замовив ще вчора, досі не відравили. </div> <div class="one-new-comm-size"> <div class="one-new-comm-size-top"> </div> <div class="one-new-comm-size-t' \
                   'humb"> </div> </div> <div class="answer-admin one-new-comm-wrap"> <span class="one-review-children-author admin"> Администратор </span> <span class="one-new-comm-date "> 27.04.2021 </span> <div class="' \
                   'one-new-comm-wrap"> Доброго дня! Повідомте, будь ласка, номер Вашого замовлення нам за номером телефону 0 800 30 99 19 та ми зможемо перевірити стан замовлення. </div> </div> <div class="one-comm-bot"> ' \
                   '<div class="one-new-comm-feed"> <a onclick="App.Auth.clickAuth(); return false;"> Ответить </a> </div> <div class="comm-like"> <a class="new-like" href="javascript:;"> <i> <svg width="16" height="14" v' \
                   'iewBox="0 0 16 14" fill="none" xmlns="http://www.w3.org/2000/svg"> <path d="M1.66666 6.10583C0.748 6.10583 0 6.77485 0 7.59651V12.3667C0 13.1884 0.748 13.8574 1.66666 13.8574H3.66666C4.042 13.8574 4.38' \
                   '731 13.7441 4.66666 13.5556V6.10583H1.66666Z" fill="#C2C2C2"></path> <path d="M15.9987 8.34144C15.9987 7.98309 15.84 7.64917 15.5647 7.4029C15.876 7.09821 16.0347 6.68975 15.9913 6.26462C15.9133 5.' \
                   ' 15.15 4.91286 14.2527 4.91286H10.1347C10.3387 4.35892 10.6653 3.34348 10.6653 2.52778C10.6653 1.23447 9.43669 0.1427 8.66534 0.1427C7.97269 0.1427 7.478 0.49152 7.45669 0.50583C7.37803 0.562486 7.3320' \
                   '3 0.648349 7.33203 0.738964V2.76092L5.41203 6.48107L5.33203 6.51744V12.9083C5.87469 13.1373 6.56134 13.2607 6.99869 13.2607H13.118C13.844 13.2607 14.4794 12.823 14.6287 12.219C14.7053 11.9083 14.6607 11' \
                   '.5953 14.508 11.3234C15.0007 11.1016 15.332 10.6478 15.332 10.1303C15.332 9.91918 15.278 9.71704 15.1754 9.534C15.668 9.31219 15.9987 8.85841 15.9987 8.34144Z" fill="#C2C2C2"></path> </svg> </i> <span c' \
                   'lass="likes-count">0</span> </a> <a class="new-dislike" href="javascript:;"> <i> <svg width="16" height="14" viewBox="0 0 16 14" fill="none" xmlns="http://www.w3.org/2000/svg"> <path d="M14.3333 7.89417' \
                   'C15.252 7.89417 16 7.22515 16 6.40349V1.6333C16 0.811645 15.252 0.142626 14.3333 0.142626H12.3333C11.958 0.142626 11.6127 0.255909 11.3333 0.44435V7.89417H14.3333Z" fill="#C2C2C2"></path> <path d="M0.00' \
                   '131226 5.65856C0.00131226 6.01691 0.159968 6.35083 0.435312 6.5971C0.123968 6.90179 -0.034688 7.31025 0.00865555 7.73538C0.0866556 8.49325 0.85 9.08714 1.74731 9.08714H5.86531C5.66131 9.64108 5.33466 1' \
                   '0.6565 5.33466 11.4722C5.33466 12.7655 6.56331 13.8573 7.33466 13.8573C8.02731 13.8573 8.522 13.5085 8.54331 13.4942C8.62197 13.4375 8.66797 13.3517 8.66797 13.261V11.2391L10.588 7.51893L10.668 7..091' \
                   '7C10.1253 0.862734 9.43866 0.739305 9.00131 0.739305H2.88197C2.15597 0.739305 1.52063 1.17698 1.37131 1.78098C1.29466 2.09165 1.33931 2.4047 1.49197 2.6766C0.999311 2.89841 0.667969 3.35218 0.667969 3.' \
                   '86974C0.667969 4.08082 0.721969 4.28296 0.824625 4.466C0.331968 4.68781 0.00131226 5.14159 0.00131226 5.65856Z" fill="#C2C2C2"></path> </svg> </i> <span class="dislike-count">0</span> </a> </div> </div' \
                   '> <div class="comm-inside" id="answers_group_id_5148353"> </div> </div> <div class="one-new-comm" data-comment_id="5293407"> <div class="one-new-comm-name"> <span class="one-review-author"> Наташа </sp' \
                   'an> </div> <div class="one-new-comm-info"> <div class="one-new-comm-star"> <span class="active"></span><span class="active"></span><span class="active"></span><span class="active"></span><span class="' \
                   'active"></span> </div> <div class="one-new-comm-date "> 06.07.2021 </div> </div> <div class="one-new-comm-wrap"> Неймовірно зручні. Підходять для усіх типів ноги. Біг у цих кросівках перетворюється на ' \
                   'заняття, яким хочеться займатися весь час. </div> <div class="one-new-comm-size"> <div class="one-new-comm-size-top"> </div> <div class="one-new-comm-size-thumb"> </div> </div> <div class="one-comm-bot' \
                   '"> <div class="one-new-comm-feed"> <a onclick="App.Auth.clickAuth(); return false;"> Ответить </a> </div> <div class="comm-like"> <a class="new-like" href="javascript:;"> <i> <svg width="16" height="14' \
                   '" viewBox="0 0 16 14" fill="none" xmlns="http://www.w3.org/2000/svg"> <path d="M1.66666 6.10583C0.748 6.10583 0 6.77485 0 7.59651V12.3667C0 13.1884 0.748 13.8574 1.66666 13.8574H3.66666C4.042 13.8574 ' \
                   '4.38731 13.7441 4.66666 13.5556V6.10583H1.66666Z" fill="#C2C2C2"></path> <path d="M15.9987 8.34144C15.9987 7.98309 15.84 7.64917 15.5647 7.4029C15.876 7.09821 16.0347 6.68975 15.9913 6.26462C15.9133 5' \
                   '.50675 15.15 4.91286 14.2527 4.91286H10.1347C10.3387 4.35892 10.6653 3.34348 10.6653 2.52778C10.6653 1.23447 9.43669 0.1427 8.66534 0.1427C7.97269 0.1427 7.478 0.49152 7.45669 0.50583C7.37803 0.562486' \
                   ' 7.33203 0.648349 7.33203 0.738964V2.76092L5.41203 6.48107L5.33203 6.51744V12.9083C5.87469 13.1373 6.56134 13.2607 6.99869 13.2607H13.118C13.844 13.2607 14.4794 12.823 14.6287 12.219C14.7053 11.9083 1' \
                   '4.6607 11.5953 14.508 11.3234C15.0007 11.1016 15.332 10.6478 15.332 10.1303C15.332 9.91918 15.278 9.71704 15.1754 9.534C15.668 9.31219 15.9987 8.85841 15.9987 8.34144Z" fill="#C2C2C2"></path> </svg> <' \
                   '/i> <span class="likes-count">0</span> </a> <a class="new-dislike" href="javascript:;"> <i> <svg width="16" height="14" viewBox="0 0 16 14" fill="none" xmlns="http://www.w3.org/2000/svg"> <path d="M14' \
                   '.3333 7.89417C15.252 7.89417 16 7.22515 16 6.40349V1.6333C16 0.811645 15.252 0.142626 14.3333 0.142626H12.3333C11.958 0.142626 11.6127 0.255909 11.3333 0.44435V7.89417H14.3333Z" fill="#C2C2C2"></path>' \
                   ' <path d="M0.00131226 5.65856C0.00131226 6.01691 0.159968 6.35083 0.435312 6.5971C0.123968 6.90179 -0.034688 7.31025 0.00865555 7.73538C0.0866556 8.49325 0.85 9.08714 1.74731 9.08714H5.86531C5.66131 9' \
                   '.64108 5.33466 10.6565 5.33466 11.4722C5.33466 12.7655 6.56331 13.8573 7.33466 13.8573C8.02731 13.8573 8.522 13.5085 8.54331 13.4942C8.62197 13.4375 8.66797 13.3517 8.66797 13.261V11.2391L10.588 7.518' \
                   '93L10.668 7.48256V1.0917C10.1253 0.862734 9.43866 0.739305 9.00131 0.739305H2.88197C2.15597 0.739305 1.52063 1.17698 1.37131 1.78098C1.29466 2.09165 1.33931 2.4047 1.49197 2.6766C0.999311 2.89841 0.6' \
                   '67969 3.35218 0.667969 3.86974C0.667969 4.08082 0.721969 4.28296 0.824625 4.466C0.331968 4.68781 0.00131226 5.14159 0.00131226 5.65856Z" fill="#C2C2C2"></path> </svg> </i> <span class="dislike-count' \
                   '">0</span> </a> </div> </div> <div class="comm-inside" id="answers_group_id_5293407"> </div> </div> <div class="one-new-comm" data-comment_id="5316972"> <div class="one-new-comm-name"> <span class' \
                   '="one-review-author"> Наталія </span> </div> <div class="one-new-comm-info"> <div class="one-new-comm-star"> <span></span><span></span><span></span><span></span><span></span> </div> <div class="' \
                   'one-new-comm-date "> 12.07.2021 </div> </div> <div class="one-new-comm-wrap"> Ношу в спортзал. Качеством довольна. Стильные. </div> <div class="one-new-comm-size"> <div class="one-new-comm-size-top' \
                   '"> </div> <div class="one-new-comm-size-thumb"> </div> </div> <div class="one-comm-bot"> <div class="one-new-comm-feed"> <a onclick="App.Auth.clickAuth(); return false;"> Ответить </a> </div> <div cl' \
                   'ass="comm-like"> <a class="new-like" href="javascript:;"> <i> <svg width="16" height="14" viewBox="0 0 16 14" fill="none" xmlns="http://www.w3.org/2000/svg"> <path d="M1.66666 6.10583C0.748 6.10583 0' \
                   ' 6.77485 0 7.59651V12.3667C0 13.1884 0.748 13.8574 1.66666 13.8574H3.66666C4.042 13.8574 4.38731 13.7441 4.66666 13.5556V6.10583H1.66666Z" fill="#C2C2C2"></path> <path d="M15.9987 8.34144C15.9987 7.' \
                   '98309 15.84 7.64917 15.5647 7.4029C15.876 7.09821 16.0347 6.68975 15.9913 6.26462C15.9133 5.50675 15.15 4.91286 14.2527 4.91286H10.1347C10.3387 4.35892 10.6653 3.34348 10.6653 2.52778C10.6653 1.23447' \
                   ' 9.43669 0.1427 8.66534 0.1427C7.97269 0.1427 7.478 0.49152 7.45669 0.50583C7.37803 0.562486 7.33203 0.648349 7.33203 0.738964V2.76092L5.41203 6.48107L5.33203 6.51744V12.9083C5.87469 13.1373 6.56134' \
                   ' 13.2607 6.99869 13.2607H13.118C13.844 13.2607 14.4794 12.823 14.6287 12.219C14.7053 11.9083 14.6607 11.5953 14.508 11.3234C15.0007 11.1016 15.332 10.6478 15.332 10.1303C15.332 9.91918 15.278 9.717' \
                   '04 15.1754 9.534C15.668 9.31219 15.9987 8.85841 15.9987 8.34144Z" fill="#C2C2C2"></path> </svg> </i> <span class="likes-count">0</span> </a> <a class="new-dislike" href="javascript:;"> <i> <svg wid' \
                   'th="16" height="14" viewBox="0 0 16 14" fill="none" xmlns="http://www.w3.org/2000/svg"> <path d="M14.3333 7.89417C15.252 7.89417 16 7.22515 16 6.40349V1.6333C16 0.811645 15.252 0.142626 14.3333 0.1' \
                   '42626H12.3333C11.958 0.142626 11.6127 0.255909 11.3333 0.44435V7.89417H14.3333Z" fill="#C2C2C2"></path> <path d="M0.00131226 5.65856C0.00131226 6.01691 0.159968 6.35083 0.435312 6.5971C0.123968 6.9' \
                   '0179 -0.034688 7.31025 0.00865555 7.73538C0.0866556 8.49325 0.85 9.08714 1.74731 9.08714H5.86531C5.66131 9.64108 5.33466 10.6565 5.33466 11.4722C5.33466 12.7655 6.56331 13.8573 7.33466 13.8573C8.02' \
                   '731 13.8573 8.522 13.5085 8.54331 13.4942C8.62197 13.4375 8.66797 13.3517 8.66797 13.261V11.2391L10.588 7.51893L10.668 7.48256V1.0917C10.1253 0.862734 9.43866 0.739305 9.00131 0.739305H2.88197C2.15' \
                   '597 0.739305 1.52063 1.17698 1.37131 1.78098C1.29466 2.09165 1.33931 2.4047 1.49197 2.6766C0.999311 2.89841 0.667969 3.35218 0.667969 3.86974C0.667969 4.08082 0.721969 4.28296 0.824625 4.466C0.3319' \
                   '68 4.68781 0.00131226 5.14159 0.00131226 5.65856Z" fill="#C2C2C2"></path> </svg> </i> <span class="dislike-count">0</span> </a> </div> </div> <div class="comm-inside" id="answers_group_id_5316972">' \
                   ' </div> </div> </div> <div class="more-comm load-next-page"> <a>Больше отзывов</a> </div> </div>'


def clear_intertop_characteristics_html(raw_characteristics):
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    chars_text = [string for string in soup.strings]
    cleared_text = list(filter(lambda string: string != ' ' and string != ', ' and string != '\n', chars_text))
    text_without_extra_spaces = list(map(lambda string: string.strip(' ').replace('\n',''), cleared_text))
    return text_without_extra_spaces


def intertop_characteristics_pretty_view(description_list):
    grouped_by_2 = [description_list[n:n + 2] for n in range(0, len(description_list), 2)]
    return '\n'.join(list(map(' '.join, grouped_by_2)))


def clear_intertop_reviews_html(raw_reviews):
    comments_list = []
    comment = {}
    soup = BeautifulSoup(raw_reviews, 'html.parser')
    for item in soup.find_all('div', {'class': 'one-new-comm'}):
        comment['author'] = item.find('div', {'class': 'one-new-comm-name'}).text
        comment['date'] = item.find('div', {'class': 'one-new-comm-date'}).text
        comment['body'] = item.find('div', {'class': 'one-new-comm-wrap'}).text
        comment_copy = comment.copy()
        comments_list.append(comment_copy)
    return comments_list

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
    #print(intertop_characteristics_pretty_view(clear_intertop_characteristics_html(raw_chars)))
    print(clear_intertop_reviews_html(raw_reviews_html))

