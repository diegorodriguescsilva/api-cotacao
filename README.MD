# Cotação de Moedas - Consulta via API

Este é um aplicativo simples em Python que permite consultar em tempo real a cotação de moedas estrangeiras e criptomoedas em relação ao Real brasileiro (BRL), utilizando a [AwesomeAPI de Moedas](https://docs.awesomeapi.com.br/api-de-moedas).

## O que essa aplicação resolve?

Muitas vezes, precisamos consultar rapidamente a cotação de moedas como o dólar (USD), euro (EUR) ou bitcoin (BTC), mas nem sempre temos uma ferramenta acessível, simples e confiável.  
Esta aplicação resolve esse problema permitindo:

- Consulta rápida pelo terminal
- Sem necessidade de acessar sites
- Retorno em tempo real via API
- Resultado direto: apenas o valor da moeda

---

# Estrutura do Projeto:

```
cotacao-moedas/
├── cotacao.py             # Script principal
├── requirements.txt       # Dependências
├── Dockerfile             # Para empacotar com Docker
└── .github/workflows/     # Pipeline CI com GitHub Actions
```

## Como usar

### Requisitos

- Python 3.8+
- Ou [Docker](https://www.docker.com/) instalado (opcional)

---

### Usando Python localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/cotacao-moedas.git
   cd cotacao-moedas
   '''
   
2. Crie e ative o ambiente virtual:

```
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```
pip install -r requirements.txt
```

4. Execute a aplicação:

```
python cotacao.py
```

# Usando o Docker:

1. Construa a imagem Docker:

```
docker build -t cotacao-app .
```

2. Rode a aplicação:

```
docker run -it cotacao-app
```

# Exemplo de uso:

1. Digite o par de moedas (ex: USD-BRL, EUR-BRL, BTC-BRL): USD-BRL
A cotação do USD-BRL é: R$ 5.3287

2. Se o par de moedas for inválido:

Digite o par de moedas (ex: USD-BRL, EUR-BRL, BTC-BRL): BRL
Não encontramos a moeda solicitada.

# Tecnologias usadas:

- Python 3
- Biblioteca requests
- Docker
- GitHub Actions (CI)

