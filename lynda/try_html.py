from urllib.request import urlopen


def main():
    webUrl = urlopen('http://rambler.ru')
    data = webUrl.read()
    address = 'C:/andrey/website_html.txt'
    f = open(address, 'w+')
    f.write(str(data))
    f.close()
    print ('Your html is saved in ', address)


if __name__ == '__main__':
    main()
