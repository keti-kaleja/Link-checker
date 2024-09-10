from bs4 import BeautifulSoup
import requests

def check_link_status(urls):
    results = {}

    up_indicators = {
        'rapidgator.net': {'selector': 'div.text-block.file-descr', 'text': 'Downloading:'},
        'katfile.com': {'selector': 'div.panel', 'text': 'Download type:'},
        'turbobit.net': {'selector': 'div.file-header', 'text': 'Download file:'}
    }

    down_indicators = {
        'rapidgator.net': {'selector': 'div.main-block', 'text': '404 File not found'},
        'katfile.com': {'selector': 'img[alt="File has been removed"]', 'attribute': 'alt', 'text': 'File has been removed'},
        'turbobit.net': {'selector': 'h1', 'text': 'Searching for the file...Please wait…'}
    }

    for url in urls:
        try:
            response = requests.get(url)
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
                    for domain, config in down_indicators.items():
                        if domain in url:
                            indicator = soup.select_one(config['selector'])
                            if indicator:
                                if config.get('attribute'):
                                    attribute_value = indicator.get(config['attribute'])
                                    if attribute_value and config['text'] in attribute_value:
                                        results[url] = 'Down'
                                        classified = True
                                        break

                                elif config['text'] in indicator.text:
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
    'https://rapidgator.net/file/f7868d946fc34257b8cef78426bc2f19',
    'https://rapidgator.net/file/b2a2da47136afb64127030d747dfdb3b',
    'https://rapidgator.net/file/d91f6be71516f79207103072d3aa4708',
    'https://katfile.com/8md4j7yvel62',
    'https://katfile.com/aansaylix1kq/',
    'https://katfile.com/zbux6b0mta3s',
    'https://katfile.com/ybafbqs6ob3h',
    'https://katfile.com/aansaylix1kq/',
    'https://katfile.com/188cnv3mq729',
    'https://katfile.com/aansaylix1kg/24-02-24-marca.pdf.html',
    'https://turbobit.net/b2v6lmha8pid.html',
    'https://turbobit.net/19mb6ptq15jt.html',
    'https://turbobit.net/818c9qqoesxp.html',
    'https://rapidgator.net/file/341915b8acf25368fcef54e5ed03c072',
    'https://rapidgator.net/file/383c1000f897a4b11d44aa52b3a64bf0/Sanet.st.StardewValleyv1.6.3DINOByTES.rar.html',
    'https://rapidgator.net/file/78399f029680e279c2829cb36fef8b31/7823_StHaHD.part1.rar.html',
    'https://katfile.com/7vkysaonxahe/Shonen_Jump_2024-01.rar.html',
    'https://katfile.com/b3ur5p9r36xx/JZIOK_0409.rar.html',
    'https://katfile.com/aansaylix1kg/24-02-24-marca.pdf.html',
    'https://katfile.com/6lc99fpjcxqz/CHYTK_1027.rar.html',
    'https://turbobit.net/pdkqwexip2av.html',
    'https://turbobit.net/szchee5g1i5b/Psycho%20past%20v04.rar.html',
    'https://turbobit.net/z8qbwchcs7ci.html'
]

# Run the link status check
all_products = check_link_status(urls)

# Print the results
for url, status in all_products.items():
    print(f'{url} is {status}')
