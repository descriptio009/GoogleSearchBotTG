# -*- coding: utf-8 -*-
def google_t(name):
    name=name.replace(" ","%20")
    import requests
    from bs4 import BeautifulSoup
    #https://www.google.com/search?q=html&client=firefox-b-d&tbs=li:1&sxsrf=ALeKk02p_LnGycp2RIzRahOtlIFJV3HUhw:1602480671852&source=lnt&sa=X&ved=2ahUKEwiK09HZqa7sAhUtxosKHU06CbcQpwV6BAgiECk&biw=1440&bih=786
    html=requests.get('https://www.google.com/search?q='+name+'&client=firefox-b-d&tbs=li:1&sxsrf=ALeKk02p_LnGycp2RIzRahOtlIFJV3HUhw:1602480671852&source=lnt&sa=X&ved=2ahUKEwiK09HZqa7sAhUtxosKHU06CbcQpwV6BAgiECk&biw=1440&bih=786')
    html1=html.content
    open('log.html', 'w').write("SyntaxError: "+str(html1))
    soup = BeautifulSoup(html1, features=('html.parser'))
    soup = soup.find_all('div', {'class': 'kCrYT'})
    urls=[]
    i = 0
    b = 0
    while i < 10:
        try:
            for div in soup:
                for soup1 in div.find_all('a'):
                    a = str(soup1.get('href').replace('/url?q=',''))
                    i += 1
                    if i != b:
                        g = requests.get(a)
                        if str(g) == "<Response [200]>":
                            open('urls.txt', 'a+').write(a+"\n")
                            # print(str(i)+'good')
                            urls.append(a)
                            i += 1
                            b = i
                        else:
                            print(' ')
                    else:
                        print(' ')
        except Exception as e:
                            print(e)                
    return( urls )