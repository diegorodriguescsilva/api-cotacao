import requests

moeda = input("Digite o par de moedas (ex: USD-BRL, EUR-BRL, BTC-BRL): ")

url = f'https://economia.awesomeapi.com.br/last/{moeda}'
requisicao = requests.get(url)
resultado = requisicao.json()

moeda_sem_hifen = moeda.replace("-", "").upper()

if moeda_sem_hifen in resultado:
    valor = resultado[moeda_sem_hifen]
    print(f"💵 A cotação do {moeda} é: R$ {valor['bid']}")
else:
    print("⚠️ Não encontramos a moeda solicitada.")
