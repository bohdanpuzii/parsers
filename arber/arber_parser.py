from bs4 import BeautifulSoup

raw_chars = '<div class="ty-product-feature"><span class="ty-product-feature__label" itemprop="brand">Артикул:</span>' \
            '<div class="ty-product-feature__value"><span>AR 06.02.02</span></div></div><div class="ty-product-feature">' \
            '<span class="ty-product-feature__label" itemprop="brand">Бренд:</span><div class="ty-product-feature__value">' \
            '<span>Arber</span></div></div><div class="ty-product-feature"><span class="ty-product-feature__label" itemprop="brand">' \
            'Країна виробника:</span><div class="ty-product-feature__value"><span>Україна</span></div></div><div class="ty-product-feature">' \
            '<span class="ty-product-feature__label" itemprop="brand">Склад тканини:</span><div class="ty-product-feature__value"><span>100% Шкіра</span>' \
            '</div></div><div class="ty-product-feature"><span class="ty-product-feature__label" itemprop="brand">Стать:</span>' \
            '<div class="ty-product-feature__value"><span>Мужской</span></div></div><div class="ty-product-feature">' \
            '<span class="ty-product-feature__label" itemprop="brand">Стиль:</span><div class="ty-product-feature__value">' \
            '<span>Повсякденний</span></div></div><div class="ty-product-feature"><span class="ty-product-feature__label" itemprop="brand">Тип продукта:</span>' \
            '<div class="ty-product-feature__value"><span>Ремені</span></div></div><div class="ty-product-feature">' \
            '<span class="ty-product-feature__label" itemprop="brand">Цвет:</span><div class="ty-product-feature__value"><span>чорний</span></div></div>'


def clear_arber_characteristics_html(raw_characteristics):
    characteristics_list = []
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    for div in soup.select('div', {"class": "ty-product-feature__value"}):
        characteristics_list.append(div.select('span')[0].text)
    characteristics_list = [characteristics_list[n:n + 2] for n in range(0, len(characteristics_list), 2)]
    characteristics_list = list(map(' '.join, characteristics_list))
    return "\n".join(characteristics_list)


if __name__ == '__main__':
    print(clear_arber_characteristics_html(raw_chars))
