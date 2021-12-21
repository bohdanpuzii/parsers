from bs4 import BeautifulSoup

raw_characteristics = '<div class="product-fields-title"><span>Колір</span></div><div class="product-field-display">' \
                      '<span>чорний</span></div><div class="clr"></div><div class="product-fields-title"><span>Матеріа' \
                      'л верху</span></div><div class="product-field-display"><span>шкіра</span></div><div class="clr">' \
                      '</div><div class="product-fields-title"><span>Матеріал в середині</span></div><div class="produc' \
                      't-field-display"><span>шкіра</span></div><div class="clr"></div><div class="product-fields-title' \
                      '"><span>Матеріал низу</span></div><div class="product-field-display"><span>шкірволон</span></div' \
                      '><div class="clr"></div><div class="product-fields-title"><span>Висота підборів</span></div><div' \
                      ' class="product-field-display"><span>9 см</span></div><div class="clr"></div><div class="clr"></div>'

def clear_kocharovska_characteristics_html(raw_characteristics):
    characteristics_list = []
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    for td in soup.select('div'):
        characteristics_list.append(td.text)
    return list(map(lambda string: string.strip(' '), characteristics_list))

def pretty_kocharovska_characteristics(chars_list):
    clear_chars_list = list(filter(None, chars_list))
    grouped_by_2 = [clear_chars_list[n:n + 2] for n in range(0, len(clear_chars_list), 2)]
    return '\n'.join(list(map(' : '.join, grouped_by_2)))


if __name__ == '__main__':
    print(pretty_kocharovska_characteristics(clear_kocharovska_characteristics_html(raw_characteristics)))