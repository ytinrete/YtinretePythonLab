import urllib.request
import urllib.parse
import urllib.error


def common_request_maker(path):
    if path:
        req = urllib.request.Request(path)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Linux; Android 4.4.4; Samsung Galaxy S4 - 4.4.4 - API 19 - 1080x1920 Build/KTU84P) '
                       + 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36')
        req.add_header('X-Requested-With', 'com.android.browser')
        return req
    else:
        return None


def post(req, data):
    try:
        response = urllib.request.urlopen(req, data, timeout=10)
    except urllib.error.HTTPError as e:
        print(e)
        return
    res_str = str(response.read(), 'utf-8')
    print('-----------')
    print(res_str)
    print('-----------')

    return res_str


def url_encode(content):
    return urllib.parse.quote_plus(content)


def url_decode(content):
    return urllib.parse.unquote(content)


def get(req):
    return post(req, None)


if __name__ == '__main__':
    # get(common_request_maker('http://www.ytinrete.com'))

    print(url_decode('%3D'))
    print(url_encode('='))

    pass
