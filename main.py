# coding=utf8
import requests
from bs4 import BeautifulSoup

text = 'ここにDebankのHistoryのテーブルいれる'
soup = BeautifulSoup(text, "html.parser")
divs = soup.select('div')[0]
print ('Time, URL, action, volume, ticker1, volume, ticker2, buffer, buffer2,gas, gas-ticker, gasfee')
for div in divs:
    #print (div)
    time = div.select_one('div > :nth-child(1) > :nth-child(1) ')
    #print (time.text)

    csv = time.text + ","
    tx = div.select_one('div > :nth-child(1) > :nth-child(2) > a ')
    tx_link = tx.get('href')
    #print (tx_link)
    csv = csv + tx_link + ","
    #2段目
    #Eventによって階層が変わるからその処理　これは後で実装
    event = div.select_one(':nth-child(2)> :nth-child(2) > :nth-child(1)')
    #print(event.text)
    csv = csv + event.text + ","
    aite = div.select_one(':nth-child(2)> :nth-child(2) > :nth-child(1) ')
    #print (aite)

    #3段目
    content = div.select_one(':nth-child(3)')
    #print (content.text)
    content1 = div.select_one(':nth-child(3)>:nth-child(1) >:nth-child(1)')
    content2 = div.select_one(':nth-child(3)>:nth-child(1) >:nth-child(2)')
    '''
    content3 = div.select_one(':nth-child(3)>:nth-child(1) >:nth-child(3)')
    content4 = div.select_one(':nth-child(3)>:nth-child(1) >:nth-child(4)')
    
    if content3:
        print (content3.text)
    if content4:
        print (content4.text)
    '''
    content3 = ''
    for i in range(3,10):
        contentover3 = div.select_one(':nth-child(3)>:nth-child(1) >:nth-child(' + str(i) + ')')
        if contentover3:
            c3text = contentover3.text
            c3text = (c3text.replace(',', ''))
            content3 = content3 + c3text



    if(content1 and  content1.text):
        volticker1 = content1.text
        #print(content1.text )
        target = ' '
        idx = volticker1.find(target)
        vol =volticker1[:idx]
        vol = (vol.replace(',', ''))
        ticker = volticker1[idx + 1:]
        ticker = (ticker.replace(',', ''))
        csv = csv +  vol + "," +  ticker + ","
        #print (vol)
        #rint (ticker)
    else:
        csv = csv + "," + ","

    if (content2 and content2.text):
        #print(content2.text )
        volticker2 = content2.text
        target = ' '
        idx = volticker2.find(target)
        vol = volticker2[:idx]
        vol = (vol.replace(',', ''))
        ticker = volticker2[idx + 1:]
        ticker = (ticker.replace(',', ''))
        csv = csv + vol + "," + ticker + ","
        #print (vol)
        #print (ticker)
    else:
        csv = csv + "," + ","

    if (content3):
        csv = csv + content3 + "," + ","
    else:
        csv = csv + "," + ","

    #4段目
    #gas = div.select_one(':nth-child(4) > :nth-child(1) > span')
    if(div.select_one(':nth-child(4) > :nth-child(1)')):
        gas= div.select_one(':nth-child(4) > :nth-child(1)')
        try:
            gas_text = gas.text
            gas_text = gas_text.strip("Gas Fee")
            #print ("gasis" + str(gas.text))
            target = ' '
            idx = gas_text.find(target)
            gasfee = gas_text[:idx]
            eth = 'ETH'
            idx = gas_text.find(target)
            feedoller = gas_text[idx + len(target):]
            #print (gasfee)
            #print (eth)
            #print (feedoller)
            csv = csv + gasfee + "," + eth + "," + feedoller

        except NameError:
            #print("変数が存在しません")
            csv = csv + "," + ","

    csv = csv
    print(csv)
