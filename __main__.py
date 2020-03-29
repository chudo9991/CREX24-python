
import ast
import datetime
import base64
import hmac
from hashlib import sha512
from urllib.request import urlopen, Request
from urllib.error import HTTPError
import modify
import wallet
import orders
import getdata
import ema
import math
import buy
import sell
import time

def std(L): # рассчет среднеквадратичного отклонения
    stdOtkl=[]
    summa=0
    Sred=sum(L)/len(L)
    for i in L:
        stdOtkl.append(Sred-i)
    for i in stdOtkl:
        summa += math.pow(i,2)
    return math.sqrt(summa/len(L))

# ГЛАВНАЯ ПРОГРАММА НАЧИНАЕТСЯ ЗДЕСЬ
stopFlag=False # если этот флаг=Истина, ордера не выставляем

print("BTC доступно: ", "%.8f" % wallet.checkAmountOnWallet())
print("CREX доступно: ", "%.8f" % wallet.checkAmountOnWalletCREX())
startWallet=wallet.checkAmountOnWallet()
print("Запускаю основной цикл. Обновление раз в 30 секунд.")
print("Запускаю основной цикл. Торгуем на 3 минутах.")

while (True):

    data = getdata.getData()
    sred = ema.ema(data[-20:-1:], 0.5) #alpha была 0.5
    bol = (4*std(data[-20:-1:])/sred[-1])/2
    interval = abs(sred[-1] - sred[-1] * (1 + bol))

    # print ("болл", "%.6f" % bol)
    # print("интервал", "%.6f" % interval)

    # покупаем
    if (getdata.currentPriceBid()<sred[-1]-interval*0.7) and (stopFlag==False):
        buy.placeOrder(float(getdata.currentPriceBid()))
        stopFlag=True
        print("КУПИЛИ при значении: ", data[-1], " по цене ", getdata.currentPriceBid())
        sell.placeOrder(sred[-1]+interval)
        print("ОРДЕР НА ПРОДАЖУ по цене ", float(sred[-1]*(1+bol)))

    if orders.checkExistingOrders()!=0:
        stopFlag==True
    else:
        stopFlag=False
        print("В кошельке стало", "%.8f" % float(wallet.checkAmountOnWallet()), " BTC.")
        print("В кошельке стало", "%.8f" % float(wallet.checkAmountOnWalletCREX()), " CREX.")
    #         startWallet=wallet.checkAmountOnWallet()

    print(time.asctime()," ", end = '')
    print("stopflag: ", stopFlag, " ", end ='')
    print("BID: ", "%.6f" % getdata.currentPriceBid()," ", end = '')
    print("ASK: ", "%.6f" % getdata.currentPriceAsk(), " ", end='')
    print("EMA: ", "%.6f" % sred[-1]," ", end = '')
    print("Вбол: ", "%.6f" % (sred[-1]*(1+bol))," ", end = '')
    print("Нбол: ", "%.6f" % (sred[-1]*(1-bol)))

    time.sleep(10)
