from bs4 import BeautifulSoup
import requests

def check_link_status(urls):
    results = {}
    buy_button= 'Buy it now'

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        buy_it_now = soup.find('span', class_='ux-call-to-action__text')

        if buy_it_now and buy_it_now.text == buy_button:
            results[url] = 'Online'
        else:
            results[url] = 'Offline'

    return results

urls = [
     'https://www.ebay.co.uk/itm/37538540?itmmeta=01Hsh=item5762F8IyVc18WO2K0fnj8YpKu1gOsM6X95vPR9XOh1v9le%2FN7RdDkW67zHbbBeQlqo3QhngWcKbhsFMlCGmAHM4jsydYBkAOoEqbVwQ2fdI3T3IAI%2B%2FjzIUrEb8fXukyMnojxoKXuJe%2BLlU2kGGFYiZXxqUZfus2npeXd5dRRKIoL0oWiHjIocnap8Vv%7Ctkp%3ABk9SR6q-94XgYw',
     'https://www.ebay.co.uk/itm/375385403889?itmmeta=01HW05XVWA5128W2N02Q0VC6A2&hash=item5766b6b1f1:g:moAAAOSwUoFmIngx&itmprp=enc%3AAQAJAAAA4GGBk5dKMu7ajIa%2B6Y0ivcAwUnWZZoGy0Q4G66LD3vQjhITlHze1GJniXVWmn5rC6TyF0fqIP2lfq3nfXWmUUOj3KZ8TBxVE5730mlxRXlUBolgKulSF%2F8IyVc18WO2K0fnj8YpKu1gOsM6X95vPR9XOh1v9le%2FN7RdDkW67zHbbBeQlqo3QhngWcKbhsFMlCGmAHM4jsydYBkAOoEqbVwQ2fdI3T3IAI%2B%2FjzIUrEb8fXukyMnojxoKXuJe%2BLlU2kGGFYiZXxqUZfus2npeXd5dRRKIoL0oWiHjIocnap8Vv%7Ctkp%3ABk9SR6q-94XgYw',
     'https://www.ebay.co.uk/itm/375383065700?itmmeta=01HW05XVWATEPFYHR9QYFC6Y9V&hash=item5766930464:g:JvkAAOSwDnJmIj~S&itmprp=enc%3AAQAJAAAAwDADEJDSGRPo%2Fm30%2BLmWiLBFU7QYt7h0GS%2BxkH9Ig1wkgojeucIAAWgktW5UIhBaULom%2BorOFyDbDD5xDxNMwxrSp4XvSif2CCTCD2ckgfVZT%2Bp9%2B28VMzLl2ToV%2Bv%2FoTss%2F2lyz%2FNhsZwzHY1t6FXxFsEzvslQQ0yHgZmHOF9fqbyirdfTYdlzMoqus1bbULBqCqTEoYy7dRDBbWm9wgAYOJde4rWdvP4xy%2BtSFBzTgKHBgmE9YcBoV7g8IaVGRog%3D%3D%7Ctkp%3ABk9SR6q-94XgYw',
     'https://www.ebay.co.uk/itm/374661038830?itmmeta=01HW05XVWKBKGQTBEX1X5DVMXG&hash=item573b89c2ee:g:gggAAOSw84JlG-8y&itmprp=enc%3AAQAJAAAA4MigDTZUYsadRoO6Gn3dCxOm%2FL1SOD8ivBD0RYfxR8MB3sh%2FDkfEApwFrcJ9UlZeJtOYVjcpZV9ah6tXsLyAgJ3QtnLKJsj%2FHB1npNThmq0lP8l3ayyz%2FLOjZhSQRF2Hn1oiYKynVek%2FxjvSQYlFaJyjXE8N%2BVvYdSqjP%2BzoiQdV4bk6FitqdsWNsYl3tpDqjVI6XpYqc65JSrQA7qSabvcfVH0WLZ0UEdcIMQW%2BFw0jKzNqKVY8%2FWlhgPlKTEvKFL1Wr9V9vi5WVISpFPsJVyejT%2Bk5zVZClJXZaHOoDdKd%7Ctkp%3ABFBMkL_3heBj'
]

all_products = check_link_status(urls)
for url, status in all_products.items():
    print(f'{url} is {status}')
