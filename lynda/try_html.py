from urllib.request import urlopen


def main():
    webUrl = urlopen('http://friendsplace.ru')
    data = webUrl.read()
    print (data)


if __name__ == '__main__':
    main()
