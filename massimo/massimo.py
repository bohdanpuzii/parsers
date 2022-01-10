from bs4 import BeautifulSoup

raw_description = '<li _ngcontent-vmp-c150="" class="description"><div _ngcontent-vmp-c150="" class="descriptionDot">' \
                  '</div><p _ngcontent-vmp-c150="" class="p1">Виготовлено зі 100%-ї бавовни</p></li><li _ngcontent-vmp-c' \
                  '150="" class="description"><div _ngcontent-vmp-c150="" class="descriptionDot"></div><p _ngcontent-vmp' \
                  '-c150="" class="p1">Вузький крій</p></li><li _ngcontent-vmp-c150="" class="description"><div _ngconte' \
                  'nt-vmp-c150="" class="descriptionDot"></div><p _ngcontent-vmp-c150="" class="p1">Застібка ґудзиками.' \
                  '</p></li><li _ngcontent-vmp-c150="" class="description"><div _ngcontent-vmp-c150="" class="descriptio' \
                  'nDot"></div><p _ngcontent-vmp-c150="" class="p1">Заокруглені манжети з ґудзиками</p></li><!---->'


def clear_massimo_description_html(raw_description):
    characteristics_list = []
    soup = BeautifulSoup(raw_description, 'html.parser')
    for div in soup.select('li'):
        characteristics_list.append(div.text)
    return '\n'.join(list(map(lambda string: string.strip(' '), characteristics_list)))


if __name__ == '__main__':
    print(clear_massimo_description_html(raw_description))