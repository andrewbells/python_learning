import urllib.request

def main():
    
    url = "http://www.friendsplace.ru/"
    #request = urllib.request.Request(url) '''optional line'''
    #===========================================================================
    response = urllib.request.urlopen(url)
    # print (response.getcode())
    # print (response.read().decode('utf-8'))
    #===========================================================================
    
    data = response.read().decode('utf-8')
    print (response.getcode(), data, end = '')
    
if __name__ == '__main__':
    main()