# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests


def get_data() -> str:
    url = "https://www.zhonghuadiancang.com/lishizhuanji/mingshi/4380.html"

    response = requests.get(url)

    html = response.content.decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')

    title: str = soup.find('h1').get_text().strip()
    text: str = soup.find('div', {'id': 'content', 'class': 'panel-body'}).get_text().strip()

    return title, text


def main():

    try:
        title, text = get_data()
        print(title)
        print(text)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()





