from bs4 import BeautifulSoup

raw_characteristics_html = '<tr class="col-6 col-md-4" style="float: left;"><td class="heading">Метал</td> <td>\n Срібло' \
                           ' 925\n </td></tr><tr class="col-6 col-md-4" style="float: left;"><td class="heading">Матеріал' \
                           '</td> <td>\n Кубічний оксид цирконію\n </td><td>\n Срібло 925\n </td></tr><tr class="col-6 col-md-4"' \
                           ' style="float: left;"><td class="heading">Колір</td> <td>\n Срібний\n </td></tr><!----><tr class="col-6 ' \
                           'col-md-4" style="float: left;"><td class="heading">Тема</td> <td>\n Родина та друзі\n </td></tr><tr ' \
                           'class="col-6 col-md-4" style="float: left;"><td class="heading">Країна виробництва</td> <td>\n Таїланд\n ' \
                           '</td></tr><tr class="col-6 col-md-4" style="float: left;"><td class="heading">Колекція</td> ' \
                           '<td>\n Pandora Moments\n </td></tr><tr class="col-6 col-md-4" style="float: left;">' \
                           '<td class="heading">Концепція</td> <td>\n Pandora Moments\n </td></tr><!----><!---->' \
                           '<tr class="col-6 col-md-4" style="float: left;"><td class="heading">Тип сережок</td> <td>\n Пусети\n </td>' \
                           '</tr><!----><!----><!---->'


def clear_pandora_characteristics_html(raw_characteristics):
    characteristics_list = []
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    for tr in soup.select('tr'):
        characteristics_list.append(
            tr.select('td')[0].text.replace('\n', '') + ':' + tr.select('td')[1].text.replace('\n', ''))
    return '\n'.join(characteristics_list)


if __name__ == '__main__':
    print(clear_pandora_characteristics_html(raw_characteristics_html))
