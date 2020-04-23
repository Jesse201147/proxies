import requests_html as req


def get_url(url):
    with req.HTMLSession() as sess:
        r = sess.get(url)
        return r
