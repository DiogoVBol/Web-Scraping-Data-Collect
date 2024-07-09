# %%
import requests
from bs4 import BeautifulSoup

url = "https://www.residentevildatabase.com/personagens/alex-wesker/" 

def get_content(url):
    
    cookies = {
        '_gid': 'GA1.2.1150280407.1720479941',
        '_ga_DJLCSW50SC': 'GS1.1.1720483927.2.1.1720484067.60.0.0',
        '_ga_D6NF5QC4QT': 'GS1.1.1720483927.2.1.1720484068.59.0.0',
        '_ga': 'GA1.2.1400588010.1720479941',
        '_gat_gtag_UA_29446588_1': '1',
        'FCNEC': '%5B%5B%22AKsRol_pX_KNloHJN_A8NO_srq5g2dpqNPJAmxR6M64DG9llpHdloYQ8lpg_M89obw9iLYk6ZuKbmmiE6PnVtIScVg_QdSGNXWs2aXN_Xk-z0OFsQAcdg8EOQJf-4jE5c_BeapetWpPfYGXAmFyWf8xQceoHEfRyxA%3D%3D%22%5D%5D',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,pt-PT;q=0.5',
        'cache-control': 'max-age=0',
        # 'cookie': '_gid=GA1.2.1150280407.1720479941; _ga_DJLCSW50SC=GS1.1.1720483927.2.1.1720484067.60.0.0; _ga_D6NF5QC4QT=GS1.1.1720483927.2.1.1720484068.59.0.0; _ga=GA1.2.1400588010.1720479941; _gat_gtag_UA_29446588_1=1; FCNEC=%5B%5B%22AKsRol_pX_KNloHJN_A8NO_srq5g2dpqNPJAmxR6M64DG9llpHdloYQ8lpg_M89obw9iLYk6ZuKbmmiE6PnVtIScVg_QdSGNXWs2aXN_Xk-z0OFsQAcdg8EOQJf-4jE5c_BeapetWpPfYGXAmFyWf8xQceoHEfRyxA%3D%3D%22%5D%5D',
        'priority': 'u=0, i',
        'referer': 'https://www.residentevildatabase.com/personagens/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    }

    response = requests.get(url, cookies=cookies, headers=headers)
    return response

# %%

response.status_code # Verificação por código 200 é OK

# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status


# %%

response.text # resposta em HTML


# %%

soup = BeautifulSoup(response.text) # Pegou a resposta que estava em HTLM e transformou em uma estrutura que podemos navegar
soup

# %%

"""
Para buscar algo na página usa soup.find()
"""

div_page = soup.find("div", class_ ="td-page-content") # Buscar um div
div_page = soup.find_all("p") # Buscar todos os parágrafos
div_page[1] # Quero apenas o segundo

# %%
paragrafo = div_page[1] 
ems = paragrafo.find_all("em") # Achar todos os "em"
ems # é uma lista

# %%
ems[0].text # ver o texto em str

# %%

ems[0].text # Retorna uma str do tipo: 'Ano de nascimento: 1974 (24 anos em 1998)' podemos splitar e jogar dentro de um dict

# Fazendo para 1 linha
chave, valor = ems[0].text.split(":")
data = {}
data[chave] = valor

data

# %%
# Fazendo para todas as linhas

data = {}

for i in ems:
    chave, valor = i.text.split(":")
    data[chave.strip(" ")] = valor.strip(" ")

data


# %%
# Consultas
data['Altura']

# %%
