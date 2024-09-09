from bs4 import BeautifulSoup
import requests

def check_link_status(url, ):
    results = {}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.google.com/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive'
    }

    site_indicators = {
        'etsy.com': {'selector': 'button.wt-btn.wt-btn--filled.wt-width-full[type="submit"]', 'text': 'Add to basket'}
    }

    for url in urls:
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')

                for domain, config in site_indicators.items():
                    if domain in url:
                        indicator = soup.select_one(config['selector'])
                        if indicator:
                            if 'text' in config and config['text'] in indicator.text:
                                results[url] = 'Up'
                                break
                        results[url] = 'Down'
            else:
                results[url] = f'Down (status code: {response.status_code})'
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
