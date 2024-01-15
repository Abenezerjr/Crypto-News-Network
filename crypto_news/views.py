from django.shortcuts import render
import requests
import json


# Create your views here.


def home(request):
    # for crypto price data
    price_api_request = requests.get(
        'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,SOL,USDC,BNB,XRP,USDT&tsyms=USD')
    price = json.loads(price_api_request.content)
    # for crypto news
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)
    context = {
        'api': api,
        'price': price,
    }

    return render(request, 'crypto_news/home.html', context)


def price(request):
    if request.method == "POST":
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote +
            "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        quote = request.POST['quote']
        context = {
            "quote": quote,
            'crypto': crypto,

        }
        return render(request, 'crypto_news/price.html', context)
    else:
        notfound = "enter  a crypto currency symbol in the form above"
        context = {
            'notfound': notfound
        }

        return render(request, 'crypto_news/price.html',context)
