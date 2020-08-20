import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from multiprocessing import Process

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BROWSER = os.environ.get('BROWSER', 'ChromeHeadless')


class QuietHTTPRequestHandler(SimpleHTTPRequestHandler):
    def log_request(*args):
        pass


@pytest.fixture(scope="module")
def browser(request):
    if BROWSER == 'ChromeHeadless':
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        browser = webdriver.Chrome(options=options)
    else:
        browser = getattr(webdriver, BROWSER)()
    browser.implicitly_wait(3)
    request.addfinalizer(lambda: browser.quit())
    return browser


@pytest.fixture(scope="module")
def server(request):
    if 'CUSTOM_SERVER_URL' in os.environ:
        return os.environ['CUSTOM_SERVER_URL']

    host = 'localhost'
    port_number = 8331

    def run():
        os.chdir('build')
        server_address = (host, port_number)
        httpd = HTTPServer(server_address, QuietHTTPRequestHandler)
        httpd.serve_forever()

    p = Process(target=run)
    p.start()

    def fin():
        p.terminate()
    request.addfinalizer(fin)

    return 'http://{}:{}/'.format(host, port_number)
