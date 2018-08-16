from requests_html import HTMLSession


def get_ulr_links(url):
    session = HTMLSession()
    r = session.get(url)
    return r
