from bs4 import BeautifulSoup as BeSoup
import requests
import lxml
import os


def get_data():
    headers = (
        {

            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        }
    )

    # r = requests.get(url="https://2gis.ru/search/книжные%20магазины%20в%20Приморском%20крае?m=135.639737%2C44.225779%2F6.97", headers=headers)
    #
    # if not os.path.exists("data"):
    #     os.mkdir("data")
    # with open("data/page_1.html", "w", encoding="utf-8") as file:
    #     file.write(r.text)

    with open("data/page_1.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeSoup(src, "lxml")

    for i in range(2, 6):
        url = f"https://2gis.ru/search/книжные%20магазины%20в%20Приморском%20крае?m=135.639737%2C44.225779%2F6.97/vladivostok/search/%D0%BA%D0%BD%D0%B8%D0%B6%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%B0%D0%B3%D0%B0%D0%B7%D0%B8%D0%BD%D1%8B%20%D0%B2%20%D0%9F%D1%80%D0%B8%D0%BC%D0%BE%D1%80%D1%81%D0%BA%D0%BE%D0%BC%20%D0%BA%D1%80%D0%B0%D0%B5/page/{i}"
        print(url)
def main():
    get_data()


if __name__ == '__main__':
    main()






















