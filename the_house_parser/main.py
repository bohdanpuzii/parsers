from bs4 import BeautifulSoup


def clear_the_house_characteristics_ua(raw_characteristics):
    soup = BeautifulSoup(raw_characteristics, 'html.parser')
    text = [string for string in soup.strings]
    text = list(filter(lambda string: string != '\n' and string != '\xa0', text))
    text = list(map(lambda string: string.replace('\n', ''), text))
    text = list(map(lambda string: string.replace('\xa0', ''), text))
    text = list(map(lambda string: string.strip(' '), text))
    return '\n'.join(text) if len(text) > 1 else None