import requests

import random
import threading

def do_request():
    while True:

        url = 'https://www.senatranestadualgov.org/app/Ajax/ajaxForm/cadastro.php'

        url2 ='https://www.4devs.com.br/ferramentas_online.php'

        data_gerador ={
            'acao': 'gerar_cpf',
        'pontuacao': 'S',
        'cpf_estado': 'RJ'
        }


        cpf_gerador = requests.post(url2, data=data_gerador).text
        print(cpf_gerador)

        data = {
        'nome': "me contate por 202003130851@ALUNOS.ESTACIO.BR ",
        'email': str(random.randint(0,99999999)) +'@mail.com',
        'cpf': cpf_gerador,
        'dia': 3,
        'mes': 5,
        'ano': 1998,
        'telefone': '(22) 2222-2222',
        'cep': '22.222-222',
        'rua':  'rua como cu do dono',
        'numero': 222,
        'complemento': 2222,
        'bairro': 2222,
        'cidades': 'maceto cu do dono',
        'estados': 'rio de janeiro',
        'login': 'COMI O CU DO CHRISTIAN',
        'senha': 123,
        'c_senha': 123,
        'termos': 1,
        'direcionar':'-' ,
        'gravar': 1
        }

        response = requests.post(url,data=data).text
        print(response)

threads =[]

for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon= True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()