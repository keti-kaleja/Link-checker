from bs4 import BeautifulSoup
import requests

def check_link_status(urls):
    results = {}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.google.com/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1'
    }

    up_indicators = {
        'etsy.com': {'selector': 'div.wt-width-full', 'text': 'Add to basket'}
    }

    down_indicators = {
        'etsy.com': [
            {'selector': 'p.wt-text-body-01', 'text': 'Sorry, this item and shop are currently unavailable'},
            {'selector': 'p.wt-text-body-01', 'text': 'Sorry, this item is unavailable.'}
        ]
    }

    for url in urls:
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')

                classified = False

                for domain, config in up_indicators.items():
                    if domain in url:
                        indicator = soup.select_one(config['selector'])
                        if indicator and config['text'] in indicator.text:
                            results[url] = 'Up'
                            classified = True
                            break

                if not classified:
                    for domain, configs in down_indicators.items():
                        if domain in url:
                            for config in configs:
                                indicator = soup.select_one(config['selector'])
                                if indicator and config['text'] in indicator.text:
                                    results[url] = 'Down'
                                    classified = True
                                    break

                if not classified:
                    results[url] = 'Unclassified'

            else:
                results[url] = f'Page does not exist or blocked (status code: {response.status_code})'
        except requests.RequestException as e:
            results[url] = f'Error: {str(e)}'

    return results

urls = [

    'https://www.etsy.com/listing/1672741595/',
    'https://www.etsy.com/listing/1591509098/',
    'https://www.etsy.com/listing/1638376348/',
    'https://www.etsy.com/listing/1478853734/',
    'https://www.etsy.com/listing/1520692960/',
    'https://www.etsy.com/listing/917993781/',
    'https://www.etsy.com/uk/listing/960028827/'
]

all_products = check_link_status(urls)
for url, status in all_products.items():
    print(f'{url} is {status}')
