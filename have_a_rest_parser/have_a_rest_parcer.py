from bs4 import BeautifulSoup

raw_characteristics = '<ul class="features"> <li class="feature_list_style"> <span class="features_name_new">Вага: </span> <span cla' \
      'ss="features_value_new">0,1 кг</span> </li> <li class="feature_list_style"> <span class="features_name_new">Р' \
      'озмір: </span> <span class="features_value_new">23*18,5*10,5 см</span> </li> </ul><ul class="features"> <li cl' \
      'ass="feature_list_style"> <span class="features_name_new">Матеріал: </span> <span class="features_value_new">в' \
      'одовідштовхувальний поліестер з PVC покриттям</span> </li> <li class="feature_list_style"> <span class="featur' \
      'es_name_new">Внутрішній простір: </span> <span class="features_value_new">2 великі кишені-сітки, двосторонній з' \
      'німний пенал з прозорою кишенею на блискавці і двома кишенями на резинці на зворотному боці</span> </li> </ul> <' \
      'div class="clear"></div> <div class="dopotstnewnew"> </div>'


def clear_have_a_rest_characteristics_html(raw_characteristics):
    characteristics_list = []
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    for td in soup.select('li'):
        characteristics_list.append(td.text)
    return "\n".join(list(map(lambda string: string.strip(' '), characteristics_list)))


if __name__ == '__main__':
    print(clear_have_a_rest_characteristics_html(raw_characteristics))