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

raw_reviews_html = '<div><div class="rating__comment"><div class="review-avatar"><img src="/imgw/loc/64x64/io/user-photos/avatars/default_uni.png' \
                   '"></div><div class="review-content"><div class="review-head-row"><div class="rating__comment-user">Наталія Р.</div><div clas' \
                   's="rating__created-at">11.04.2021</div></div><div class="review-head-row"><div class="starbox"><div class="starbox__containe' \
                   'r"><div class="starbox__stars"><div style="width:100%" class="starbox__colorbar"></div><div class="starbox__holder"><div clas' \
                   's="starbox__item"></div><div class="starbox__item"></div><div class="starbox__item"></div><div class="starbox__item"></div><di' \
                   'v class="starbox__item"></div></div></div></div></div><div class="verified-buy">Товар куплений</div></div><div class="rating__' \
                   'comment-body"></div></div><div class="rating__comment-footer"><a href="#" class="comment-link">Коментувати</a><div class="wrapp' \
                   'er-rating-comments"><div class="flex voting-disabled-unauthorized"><div class="rating__comment-vote vote"><div class="vote_' \
                   '_icon "></div><span class="vote__count t-bold">1</span></div><div class="rating__comment-vote vote ml-3"><div class="vote__i' \
                   'con --down "></div><span class="vote__count t-bold">1</span></div></div><div class="wrapper-comment-complain"><div class="com' \
                   'ment-complain ban-complain"></div></div></div></div></div><div></div></div><div><div class="rating__comment"><div class="revi' \
                   'ew-avatar"><img src="/imgw/loc/64x64/io/user-photos/avatars/default_uni.png"></div><div class="review-content"><div class="rev' \
                   'iew-head-row"><div class="rating__comment-user">Леся К.</div><div class="rating__created-at">06.04.2021</div></div><div class="re' \
                   'view-head-row"><div class="starbox"><div class="starbox__container"><div class="starbox__stars"><div style="width:60%" class="star' \
                   'box__colorbar"></div><div class="starbox__holder"><div class="starbox__item"></div><div class="starbox__item"></div><div class="sta' \
                   'rbox__item"></div><div class="starbox__item"></div><div class="starbox__item"></div></div></div></div></div></div><div class="rati' \
                   'ng__comment-body">На 50 р. заміри плаття в проймі ПОГ- 50 см,в грудях не ввійшла.</div></div><div class="rating__comment-footer"><a' \
                   ' href="#" class="comment-link">Коментувати</a><div class="wrapper-rating-comments"><div class="flex voting-disabled-unauthorized">' \
                   '<div class="rating__comment-vote vote"><div class="vote__icon "></div><span class="vote__count t-bold">3</span></div><div class="ra' \
                   'ting__comment-vote vote ml-3"><div class="vote__icon --down "></div></div></div><div class="wrapper-comment-complain"><div class="co' \
                   'mment-complain ban-complain"></div></div></div></div></div><div></div></div><div><div class="rating__comment"><div class="review-ava' \
                   'tar"><img src="/imgw/loc/64x64/io/user-photos/avatars/default_uni.png"></div><div class="review-content"><div class="review-head-row' \
                   '"><div class="rating__comment-user">vika123</div><div class="rating__created-at">01.04.2021</div></div><div class="review-head-row">' \
                   '<div class="starbox"><div class="starbox__container"><div class="starbox__stars"><div style="width:40%" class="starbox__colorbar"></' \
                   'div><div class="starbox__holder"><div class="starbox__item"></div><div class="starbox__item"></div><div class="starbox__item"></div>' \
                   '<div class="starbox__item"></div><div class="starbox__item"></div></div></div></div></div><div class="verified-buy">Товар куплений</di' \
                   'v></div><div class="rating__comment-body">Мені не сподобалось ,і не мій зріст ,на 174 талія не там ,а за повернення прийшлось платити ' \
                   'так, як Каста неповідомивши змінила умови повернення ,що дуже неприємно!!!</div></div><div class="rating__comment-footer"><a href="#" ' \
                   'class="comment-link">Коментувати</a><div class="wrapper-rating-comments"><div class="flex voting-disabled-unauthorized"><div class="ra' \
                   'ting__comment-vote vote"><div class="vote__icon "></div><span class="vote__count t-bold">2</span></div><div class="rating__comment-vot' \
                   'e vote ml-3"><div class="vote__icon --down "></div></div></div><div class="wrapper-comment-complain"><div class="comment-complain ban-' \
                   'complain"></div></div></div></div></div><div></div></div><div><div class="rating__comment"><div class="review-avatar"><img src="/imgw/' \
                   'loc/64x64/io/user-photos/avatars/default_uni.png"></div><div class="review-content"><div class="review-head-row"><div class="rating__c' \
                   'omment-user">Наталія Р.</div><div class="rating__created-at">01.04.2021</div></div><div class="review-head-row"><div class="starbox"><' \
                   'div class="starbox__container"><div class="starbox__stars"><div style="width:100%" class="starbox__colorbar"></div><div class="starbox' \
                   '__holder"><div class="starbox__item"></div><div class="starbox__item"></div><div class="starbox__item"></div><div class="starbox__item' \
                   '"></div><div class="starbox__item"></div></div></div></div></div><div class="verified-buy">Товар куплений</div></div><div class="ratin' \
                   'g__comment-body">Плаття хороше. Тканина приємна. Шкода, що замалий розмір замовила.</div></div><div class="rating__comment-footer"><a ' \
                   'href="#" class="comment-link">Коментувати</a><div class="wrapper-rating-comments"><div class="flex voting-disabled-unauthorized"><div ' \
                   'class="rating__comment-vote vote"><div class="vote__icon "></div><span class="vote__count t-bold">1</span></div><div class="rating__co' \
                   'mment-vote vote ml-3"><div class="vote__icon --down "></div></div></div><div class="wrapper-comment-complain"><div class="comment-comp' \
                   'lain ban-complain"></div></div></div></div></div><div></div></div><div><div class="rating__comment"><div class="review-avatar"><img sr' \
                   'c="/imgw/loc/64x64/io/user-photos/avatars/default_uni.png"></div><div class="review-content"><div class="review-head-row"><div class="' \
                   'rating__comment-user">vika123</div><div class="rating__created-at">25.03.2021</div></div><div class="review-head-row"><div class="star' \
                   'box"><div class="starbox__container"><div class="starbox__stars"><div style="width:60%" class="starbox__colorbar"></div><div class="st' \
                   'arbox__holder"><div class="starbox__item"></div><div class="starbox__item"></div><div class="starbox__item"></div><div class="starbox_' \
                   '_item"></div><div class="starbox__item"></div></div></div></div></div></div><div class="rating__comment-body">Якість непогана ,але не ' \
                   'мій фасон,і колір.</div></div><div class="rating__comment-footer"><a href="#" class="comment-link">Коментувати</a><div class="wrapper-' \
                   'rating-comments"><div class="flex voting-disabled-unauthorized"><div class="rating__comment-vote vote"><div class="vote__icon "></div><' \
                   'span class="vote__count t-bold">1</span></div><div class="rating__comment-vote vote ml-3"><div class="vote__icon --down "></div></div>' \
                   '</div><div class="wrapper-comment-complain"><div class="comment-complain ban-complain"></div></div></div></div></div><div></div></div><' \
                   'div><div class="rating__comment"><div class="review-avatar"><img src="/imgw/loc/64x64/io/user-photos/avatars/default_uni.png"></div><di' \
                   'v class="review-content"><div class="review-head-row"><div class="rating__comment-user">Елена К.</div><div class="rating__created-at">1' \
                   '7.03.2021</div></div><div class="review-head-row"><div class="starbox"><div class="starbox__container"><div class="starbox__stars"><div' \
                   ' style="width:100%" class="starbox__colorbar"></div><div class="starbox__holder"><div class="starbox__item"></div><div class="starbox__' \
                   'item"></div><div class="starbox__item"></div><div class="starbox__item"></div><div class="starbox__item"></div></div></div></div></div>' \
                   '<div class="verified-buy">Товар куплений</div></div><div class="rating__comment-body">За такі кошти - навіть не очікувала таку якість ,' \
                   ' але якщо великі бедра, низ спідниці візуально буде збільшувати ! </div></div><div class="rating__comment-footer"><a href="#" class="co' \
                   'mment-link">Коментувати</a><div class="wrapper-rating-comments"><div class="flex voting-disabled-unauthorized"><div class="rating__comm' \
                   'ent-vote vote"><div class="vote__icon "></div><span class="vote__count t-bold">1</span></div><div class="rating__comment-vote vote ml-3' \
                   '"><div class="vote__icon --down "></div><span class="vote__count t-bold">1</span></div></div><div class="wrapper-comment-complain"><div' \
                   ' class="comment-complain ban-complain"></div></div></div></div></div><div></div></div><div><div class="rating__comment"><div class="rev' \
                   'iew-avatar"><img src="/imgw/loc/64x64/io/user-photos/avatars/default_uni.png"></div><div class="review-content"><div class="review-head' \
                   '-row"><div class="rating__comment-user">Светлана С.</div><div class="rating__created-at">16.02.2021</div></div><div class="review-head-' \
                   'row"><div class="starbox"><div class="starbox__container"><div class="starbox__stars"><div style="width:100%" class="starbox__colorbar"' \
                   '></div><div class="starbox__holder"><div class="starbox__item"></div><div class="starbox__item"></div><div class="starbox__item"></div>' \
                   '<div class="starbox__item"></div><div class="starbox__item"></div></div></div></div></div><div class="verified-buy">Товар куплений</div' \
                   '></div><div class="rating__comment-body">Гарне, тканина приємна, колір- сірий, а не чорний. Високим леді буде пасувати краще.На мій зріст' \
                   ' 160 теж з каблуками буде класно.</div></div><div class="rating__comment-footer"><a href="#" class="comment-link">Коментувати</a><div class="wrapper-rating-comments"><div class="flex voting-d' \
                   'isabled-unauthorized"><div class="rating__comment-vote vote"><div class="vote__icon "></div><span class="vote__count t-bold">2</span></div><div class="rating__comment-vote vote ml-3"><div clas' \
                   's="vote__icon --down "></div></div></div><div class="wrapper-comment-complain"><div class="comment-complain ban-complain"></div></div></div></div></div><div></div></div><div><div class="rating' \
                   '__comment"><div class="review-avatar"><img src="/imgw/loc/64x64/io/user-photos/avatars/2021/02/11/4b318d9d-b11a-481d-872a-d145fa83e251.jpg"></div><div class="review-content"><div class="revie' \
                   'w-head-row"><div class="rating__comment-user">Nano</div><div class="rating__created-at">06.02.2021</div></div><div class="review-head-row"><div class="starbox"><div class="starbox__container"' \
                   '><div class="starbox__stars"><div style="width:100%" class="starbox__colorbar"></div><div class="starbox__holder"><div class="starbox__item"></div><div class="starbox__item"></div><div class=' \
                   '"starbox__item"></div><div class="starbox__item"></div><div class="starbox__item"></div></div></div></div></div><div class="verified-buy">Товар куплений</div></div><div class="rating__comment' \
                   '-body">Спасибо за платье, очень красивое и ткань очень приятная мне повезло взяла за 282 грн</div></div><div class="rating__comment-footer"><a href="#" class="comment-link">Коментувати</a><di' \
                   'v class="wrapper-rating-comments"><div class="flex voting-disabled-unauthorized"><div class="rating__comment-vote vote"><div class="vote__icon "></div><span class="vote__count t-bold">3</span' \
                   '></div><div class="rating__comment-vote vote ml-3"><div class="vote__icon --down "></div></div></div><div class="wrapper-comment-complain"><div class="comment-complain ban-complain"></div></d' \
                   'iv></div></div></div><div></div></div><div><div class="rating__comment"><div class="review-avatar"><img src="/imgw/loc/64x64/io/user-photos/avatars/default_uni.png"></div><div class="review-c' \
                   'ontent"><div class="review-head-row"><div class="rating__comment-user">марина д.</div><div class="rating__created-at">29.12.2020</div></div><div class="review-head-row"><div class="starbox"><' \
                   'div class="starbox__container"><div class="starbox__stars"><div style="width:100%" class="starbox__colorbar"></div><div class="starbox__holder"><div class="starbox__item"></div><div class="st' \
                   'arbox__item"></div><div class="starbox__item"></div><div class="starbox__item"></div><div class="starbox__item"></div></div></div></div></div><div class="verified-buy">Товар куплений</div></' \
                   'div><div class="rating__comment-body"></div></div><div class="rating__comment-footer"><a href="#" class="comment-link">Коментувати</a><div class="wrapper-rating-comments"><div class="flex vo' \
                   'ting-disabled-unauthorized"><div class="rating__comment-vote vote"><div class="vote__icon "></div><span class="vote__count t-bold">1</span></div><div class="rating__comment-vote vote ml-3"><' \
                   'div class="vote__icon --down "></div><span class="vote__count t-bold">1</span></div></div><div class="wrapper-comment-complain"><div class="comment-complain ban-complain"></div></div></div><' \
                   '/div></div><div></div></div><div><div class="rating__comment"><div class="review-avatar"><img src="/imgw/loc/64x64/io/user-photos/avatars/default_uni.png"></div><div class="review-content"><' \
                   'div class="review-head-row"><div class="rating__comment-user">Валерия С.</div><div class="rating__created-at">23.12.2020</div></div><div class="review-head-row"><div class="starbox"><div clas' \
                   's="starbox__container"><div class="starbox__stars"><div style="width:100%" class="starbox__colorbar"></div><div class="starbox__holder"><div class="starbox__item"></div><div class="starbox__' \
                   'item"></div><div class="starbox__item"></div><div class="starbox__item"></div><div class="starbox__item"></div></div></div></div></div><div class="verified-buy">Товар куплений</div></div><d' \
                   'iv class="rating__comment-body">Всё супер!!! Полномерки. Рукава тянутся, не давит. Всё как на фото!</div></div><div class="rating__comment-footer"><a href="#" class="comment-link">Коментува' \
                   'ти</a><div class="wrapper-rating-comments"><div class="flex voting-disabled-unauthorized"><div class="rating__comment-vote vote"><div class="vote__icon "></div><span class="vote__count t-bo' \
                   'ld">1</span></div><div class="rating__comment-vote vote ml-3"><div class="vote__icon --down "></div></div></div><div class="wrapper-comment-complain"><div class="comment-complain ban-compl' \
                   'ain"></div></div></div></div></div><div></div></div><div><div class="rating__comment"><div class="review-avatar"><img src="/imgw/loc/64x64/io/user-photos/avatars/default_uni.png"></div><div' \
                   ' class="review-content"><div class="review-head-row"><div class="rating__comment-user">Інна Ч.</div><div class="rating__created-at">25.11.2020</div></div><div class="review-head-row"><div c' \
                   'lass="starbox"><div class="starbox__container"><div class="starbox__stars"><div style="width:100%" class="starbox__colorbar"></div><div class="starbox__holder"><div class="starbox__item"></' \
                   'div><div class="starbox__item"></div><div class="starbox__item"></div><div class="starbox__item"></div><div class="starbox__item"></div></div></div></div></div></div><div class="rating__comme' \
                   'nt-body">Плаття сподобалось, тканина легка, тянеться, приємна, гарно виглдає. Хороша ціна.З доставкою- 410грн.</div></div><div class="rating__comment-footer"><a href="#" class="comment-link' \
                   '">Коментувати</a><div class="wrapper-rating-comments"><div class="flex voting-disabled-unauthorized"><div class="rating__comment-vote vote"><div class="vote__icon "></div><span class="vote_' \
                   '_count t-bold">1</span></div><div class="rating__comment-vote vote ml-3"><div class="vote__icon --down "></div></div></div><div class="wrapper-comment-complain"><div class="comment-complain ' \
                   'ban-complain"></div></div></div></div></div><div></div></div><div><div class="rating__comment"><div class="review-avatar"><img src="/imgw/loc/64x64/io/user-photos/avatars/default_uni.png"></' \
                   'div><div class="review-content"><div class="review-head-row"><div class="rating__comment-user">Елена К.</div><div class="rating__created-at">04.08.2020</div></div><div class="review-head-row' \
                   '"><div class="starbox"><div class="starbox__container"><div class="starbox__stars"><div style="width:80%" class="starbox__colorbar"></div><div class="starbox__holder"><div class="starbox__it' \
                   'em"></div><div class="starbox__item"></div><div class="starbox__item"></div><div class="starbox__item"></div><div class="starbox__item"></div></div></div></div></div></div><div class="rating__comm' \
                   'ent-body"></div></div><div class="rating__comment-footer"><a href="#" class="comment-link">Коментувати</a><div class="wrapper-rating-comments"><div class="flex voting-disabled-unauthorized"><div' \
                   ' class="rating__comment-vote vote"><div class="vote__icon "></div><span class="vote__count t-bold">1</span></div><div class="rating__comment-vote vote ml-3"><div class="vote__icon --down "></div' \
                   '><span class="vote__count t-bold">3</span></div></div><div class="wrapper-comment-complain"><div class="comment-complain ban-complain"></div></div></div></div></div><div></div></div>'


def clear_kasta_characteristics(raw_characteristics):
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    text = [string for string in soup.strings]
    return text


def kasta_characteristics_pretty_view(description_list):
    grouped_by_2 = [description_list[n:n + 2] for n in range(0, len(description_list), 2)]
    return '\n'.join(list(map(' : '.join, grouped_by_2)))


def clear_moyo_reviews_html(raw_reviews):
    comments_list = []
    comment = {}
    soup = BeautifulSoup(raw_reviews, 'html.parser')
    for item in soup.find_all('div', {'class': 'rating__comment'}):
        comment['author'] = item.find('div', {'class': 'rating__comment-user'}).text
        comment['date'] = item.find('div', {'class': 'rating__created-at'}).text
        comment['body'] = item.find('div', {'class': 'rating__comment-body'}).text
        comment_copy = comment.copy()
        comments_list.append(comment_copy)
    return comments_list


if __name__ == '__main__':
    # print(kasta_characteristics_pretty_view(clear_kasta_characteristics(raw_html_chars)))
    print(clear_moyo_reviews_html(raw_reviews_html))
