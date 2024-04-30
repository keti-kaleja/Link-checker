from bs4 import BeautifulSoup
import requests

def check_link_status(urls):
    results = {}

    site_indicators = {
        'rapidgator.net': {'selector': 'div.text-block.file-descr', 'text': 'Downloading:'},
        'katfile.com': {'selector': 'h2', 'text': '.rar'},
        'turbobit.net': {'selector': 'div.file-header', 'text': 'Download file:'}
    }

    for url in urls:
        try:
            response = requests.get(url)
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
    'https://rapidgator.net/file/f7868d946fc34257b8cef78426bc2f19',
    'https://rapidgator.net/file/b2a2da47136afb64127030d747dfdb3b',
    'https://rapidgator.net/file/d91f6be71516f79207103072d3aa4708',
    'https://katfile.com/8md4j7yvel62',
    'https://katfile.com/zbux6b0mta3s',
    'https://katfile.com/ybafbqs6ob3h',
    'https://turbobit.net/b2v6lmha8pid.html',
    'https://turbobit.net/19mb6ptq15jt.html',
    'https://turbobit.net/818c9qqoesxp.html',
    'https://rapidgator.net/file/341915b8acf25368fcef54e5ed03c072',
    'https://rapidgator.net/file/383c1000f897a4b11d44aa52b3a64bf0/Sanet.st.StardewValleyv1.6.3DINOByTES.rar.html',
    'https://rapidgator.net/file/78399f029680e279c2829cb36fef8b31/7823_StHaHD.part1.rar.html',
    'https://katfile.com/7vkysaonxahe/Shonen_Jump_2024-01.rar.html',
    'https://katfile.com/b3ur5p9r36xx/JZIOK_0409.rar.html',
    'https://katfile.com/6lc99fpjcxqz/CHYTK_1027.rar.html',
    'https://turbobit.net/pdkqwexip2av.html',
    'https://turbobit.net/szchee5g1i5b/Psycho%20past%20v04.rar.html',
    'https://turbobit.net/z8qbwchcs7ci.html'

]

all_products = check_link_status(urls)
for url, status in all_products.items():
    print(f'{url} is {status}')
