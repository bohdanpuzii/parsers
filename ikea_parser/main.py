from bs4 import BeautifulSoup

raw_html_size = '<h2 class="range-revamp-product-dimensions__title">Розмір товару</h2><dl class="range-revamp-product' \
                '-dimensions__list"><div class="range-revamp-product-dimensions__list-container"><dt class="range-reva' \
                'mp-product-dimensions__list-item-name">Довжина:&nbsp;</dt><dd class="range-revamp-product-dimensions_' \
                '_list-item-measure">200 см</dd></div><div class="range-revamp-product-dimensions__list-container"><dt' \
                ' class="range-revamp-product-dimensions__list-item-name">Ширина:&nbsp;</dt><dd class="range-revamp-pro' \
                'duct-dimensions__list-item-measure">150 см</dd></div><div class="range-revamp-product-dimensions__list' \
                '-container"><dt class="range-revamp-product-dimensions__list-item-name">Вага наповнювача:&nbsp;</dt><' \
                'dd class="range-revamp-product-dimensions__list-item-measure">450 г</dd></div><div class="range-revam' \
                'p-product-dimensions__list-container"><dt class="range-revamp-product-dimensions__list-item-name">Заг' \
                'альна вага:&nbsp;</dt><dd class="range-revamp-product-dimensions__list-item-measure">1080 г</dd></div>' \
                '</dl><div class="range-revamp-product-dimensions-content__images"><div class="range-revamp-product-dim' \
                'ensions__image-container" data-ga-action="measurement_image_modal" data-ga-label="0776666_PE758188"><s' \
                'pan class="range-revamp-aspect-ratio-image range-revamp-aspect-ratio-image--square"><img loading="lazy' \
                '" class="range-revamp-aspect-ratio-image__image" alt="SMÅSPORRE СМОСПОРРЕ Ковдра, тепла, 150x200 см" ' \
                'srcset=" https://www.ikea.com/ua/uk/images/products/smasporre-smosporre-kovdra-tepla__0776666_pe758188' \
                '_s5.jpg?f=g 1600w, https://www.ikea.com/ua/uk/images/products/smasporre-smosporre-kovdra-tepla__077666' \
                '6_pe758188_s5.jpg?f=sg 1400w, https://www.ikea.com/ua/uk/images/products/smasporre-smosporre-kovdra-te' \
                'pla__0776666_pe758188_s5.jpg?f=xxxl 1100w, https://www.ikea.com/ua/uk/images/products/smasporre-smospo' \
                'rre-kovdra-tepla__0776666_pe758188_s5.jpg?f=xxl 900w, https://www.ikea.com/ua/uk/images/products/smas' \
                'porre-smosporre-kovdra-tepla__0776666_pe758188_s5.jpg?f=xl 750w, https://www.ikea.com/ua/uk/images/pr' \
                'oducts/smasporre-smosporre-kovdra-tepla__0776666_pe758188_s5.jpg?f=l 700w, https://www.ikea.com/ua/uk/i' \
                'mages/products/smasporre-smosporre-kovdra-tepla__0776666_pe758188_s5.jpg?f=m 600w, https://www.ikea.com' \
                '/ua/uk/images/products/smasporre-smosporre-kovdra-tepla__0776666_pe758188_s5.jpg?f=s 500w, https://www' \
                '.ikea.com/ua/uk/images/products/smasporre-smosporre-kovdra-tepla__0776666_pe758188_s5.jpg?f=xs 400w, ' \
                'https://www.ikea.com/ua/uk/images/products/smasporre-smosporre-kovdra-tepla__0776666_pe758188_s5.jpg?f' \
                '=xxs 300w, https://www.ikea.com/ua/uk/images/products/smasporre-smosporre-kovdra-tepla__0776666_pe758' \
                '188_s5.jpg?f=xxxs 160w, https://www.ikea.com/ua/uk/images/products/smasporre-smosporre-kovdra-tepla__' \
                '0776666_pe758188_s5.jpg?f=u 80w, https://www.ikea.com/ua/uk/images/products/smasporre-smosporre-kovdra' \
                '-tepla__0776666_pe758188_s5.jpg?f=xu 40w, https://www.ikea.com/ua/uk/images/products/smasporre-smosp' \
                'orre-kovdra-tepla__0776666_pe758188_s5.jpg?f=xxu 39w " sizes="(max-width: 400px) 300px, (max-width: 60' \
                '0px) 500px, 400px" src="https://www.ikea.com/ua/uk/images/products/smasporre-smosporre-kovdra-tepla_' \
                '_0776666_pe758188_s5.jpg?f=xs"></span></div></div>'

raw_html_info = '<span class="range-revamp-product-details__paragraph">Легка, тепла та проста в догляді ковдра, вигото' \
                'влена із суміші бавовни та поліестера з наповнювачем із м’якого холлофайбера з перероблених матеріалів.' \
                '</span><span class="range-revamp-product-details__paragraph">М’які, легкі волокна зберігають обєм та і' \
                'золяційну здатність, що дозволяє вашому тілу «дихати» і підтримувати рівну температуру протягом ночі.<' \
                '/span><div class="range-revamp-expander"><div class="range-revamp-expander__content" aria-hidden="true' \
                '" role="region" tabindex="-1" style="margin-bottom: 0px; height: 0px;"><div style="display: none;"><sp' \
                'an class="range-revamp-product-details__paragraph">Хороший вибір, якщо вам часто спекотно під час сну.<' \
                '/span><span class="range-revamp-product-details__paragraph">Чохол можна прати у пральній машині за 60°С' \
                ' — температури, що знищує пилових кліщів.</span><span class="range-revamp-product-details__paragraph">К' \
                'ількість ниток на кв. дюйм: 186.</span><span class="range-revamp-product-details__paragraph">Цей показни' \
                'к вказує кількість ниток на квадратний дюйм тканини. Чим більший цей показник, тим щільніше сплетена тк' \
                'анина.</span><span class="range-revamp-product-details__paragraph">Цей товар можна використовувати в гр' \
                'омадських місцях, оскільки його конструкція та матеріал призначені для частого використання.</span><spa' \
                'n class="range-revamp-product-details__header">Дизайнер</span><p>Maja Ganszyniec</p></div></div><button' \
                ' class="range-revamp-expander__btn" aria-expanded="false" visibleitems="2">Читати далі</button></div>'


def clear_ikea_size_characteristics(raw_chars):
    soup = BeautifulSoup(raw_chars, 'html.parser')
    text = [string.replace('\xa0', '') for string in soup.strings]
    return text


def ikea_size_characteristics_pretty_view(description_list):
    extra_text = 'Розмір товару'
    try:
        description_list.remove(extra_text)
    except:
        pass
    grouped_by_2 = [description_list[n:n + 2] for n in range(0, len(description_list), 2)]
    return '\n'.join(list(map(' '.join, grouped_by_2)))


def clear_ikea_info(raw_info):
    soup = BeautifulSoup(raw_info, 'html.parser')
    text = [string for string in soup.strings]
    return text


def ikea_info_pretty_view(description_list):
    extra_text = 'Читати далі'
    try:
        description_list.remove(extra_text)
    except:
        pass
    description_list = list(map(lambda string: '   ' + string, description_list))
    return '\n'.join(description_list)


if __name__ == '__main__':
    print(ikea_size_characteristics_pretty_view(clear_ikea_size_characteristics(raw_html_size)))
    print(ikea_info_pretty_view(clear_ikea_info(raw_html_info)))
