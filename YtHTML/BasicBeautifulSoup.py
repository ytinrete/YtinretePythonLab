from YtHttp import BasicHttp
from bs4 import BeautifulSoup


def test(html_str):
    try:
        html_tree = BeautifulSoup(html_str, 'lxml')

        divs = html_tree.body.select('div')

        for div in divs:
            print(div.prettify())

        button = html_tree.body.find('a', class_='button')
        print(button.get('target'))

        buttons = html_tree.body.findAll('a', class_='button')
        for btn in buttons:
            print(btn.get('href'))

    except BaseException as e:
        print(e)

    pass


if __name__ == '__main__':
    test(BasicHttp.get(BasicHttp.common_request_maker('http://www.ytinrete.com')))
    pass
