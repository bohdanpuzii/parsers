from bs4 import BeautifulSoup

raw_characteristics_html = '<tr class="col-6 col-md-4" style="float: left;"><td class="heading">Метал</td> <td> Срібло 925 ' \
                      '</td></tr><tr class="col-6 col-md-4" style="float: left;"><td class="heading">Матеріал</td> <td> ' \
                      'Срібло 925 </td></tr><!----><!----><!----><tr class="col-6 col-md-4" style="float: left;"><td ' \
                      'class="heading">Країна виробництва</td> <td> Таїланд </td></tr><tr class="col-6 col-md-4" style=' \
                      '"float: left;"><td class="heading">Колекція</td> <td> Pandora Moments </td></tr><tr class="col-6 ' \
                      'col-md-4" style="float: left;"><td class="heading">Концепція</td> <td> Pandora Moments </td></tr>' \
                      '<tr class="col-6 col-md-4" style="float: left;"><td class="heading">Тип браслета</td> <td> ' \
                      'Браслет-бангл Pandora Moments </td></tr><!----><!----><!----><!----><tr class="col-6 col-md-4" ' \
                      'style="float: left;"><td class="heading">Сумісний з намистинами</td> <td> Для намистин Pandora Moments </td></tr>'


def clear_pandora_characteristics_html(raw_characteristics):
    characteristics_list = []
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    for tr in soup.select('tr'):
        characteristics_list.append(tr.select('td')[0].text+':'+tr.select('td')[1].text)
    return '\n'.join(characteristics_list)

if __name__ == '__main__':
    print(clear_pandora_characteristics_html(raw_characteristics_html))