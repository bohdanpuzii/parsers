from bs4 import BeautifulSoup

raw_characteristics_html = '<dl><dt id="product_attribute_label_54420"><label class="text-prompt"> Сканкод: </label></dt>' \
                           '<dd id="product_attribute_input_54420"><ul class="option-list"><li><label for="product_attribute_54420_55404">' \
                           '4035644004493</label></li></ul></dd><dt id="product_attribute_label_67156"><label class="text-prompt">' \
                           ' Колір: </label></dt><dd id="product_attribute_input_67156"><ul class="option-list"><li>' \
                           '<label for="product_attribute_67156_68150">Зелений</label></li></ul></dd><dt id="product_attribute_label_54421">' \
                           '<label class="text-prompt"> Висота: </label></dt><dd id="product_attribute_input_54421"><ul class="option-list">' \
                           '<li><label for="product_attribute_54421_55405">7 см.</label></li></ul></dd><dt id="product_attribute_label_54422">' \
                           '<label class="text-prompt"> Склад: </label></dt><dd id="product_attribute_input_54422"><ul class="option-list"><li>' \
                           '<label for="product_attribute_54422_55406">Скло</label></li></ul></dd></dl>'


def clear_pandora_characteristics_html(raw_characteristics):
    characteristics_list = []
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    name = soup.select('dt')
    value = soup.select('dd')
    for i in range(len(name)):
        characteristics_list.append(name[i].text+value[i].text)
    return '\n'.join(characteristics_list)


if __name__ == '__main__':
    print(clear_pandora_characteristics_html(raw_characteristics_html))