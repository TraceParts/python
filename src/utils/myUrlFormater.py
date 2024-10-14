import urllib.parse


def my_url_formater(raw_string):
    # This is to avoid forbidden characters in URLs
    return urllib.parse.quote_plus(raw_string)
