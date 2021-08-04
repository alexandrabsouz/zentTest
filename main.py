import os
import time

from app.questoes import Questoes
from app.resultado import Resultado
from app.valores import Valores

while True:
    print('-=' * 60)
    titulo = '\033[34m'+'O quão ZEN você é?'+'\033[0;0m\n'
    print(titulo.center(120))
    questao   = Questoes()
    valor     = Valores()
    resultado = Resultado()
    soma = []
    print('Responda cada questão somente com a LETRA representante da sua escolha:')

    # Tratamento da questão 1 do questionário
    questao.primeira_questao()
    resposta_um = input('ESCOLHA: ').upper()
    while True:
        if resposta_um != 'A' and resposta_um != 'B' and resposta_um != 'C' and resposta_um != 'D':
            print('\033[31m'+'[ERRO] Opa! Você digitou errado, tente escolher entre A, B, C ou D'+'\033[0;0m')
            resposta_um = input('ESCOLHA: ').upper()
        else:
            break
    a = valor.primeira_questao(resposta_um)
    soma.append(a)
    os.system('clear') or None


    # Tratamento da questão 2 do questionário
    questao.segunda_questao()
    resposta_dois = input('ESCOLHA: ').upper()
    while True:
        if resposta_dois != 'A' and resposta_dois != 'B' and resposta_dois != 'C' and resposta_dois != 'D':
            print('\033[31m'+'[ERRO] Opa! Você digitou errado, tente escolher entre A, B, C ou D'+'\033[0;0m')
            resposta_dois = input('ESCOLHA: ').upper()
        else:
            break
    b = valor.segunda_questao(resposta_dois)
    soma.append(b)
    os.system('clear') or None


    # Tratamento da questão 3 do questionário
    questao.terceira_questao()
    resposta_tres = input('ESCOLHA: ').upper()
    while True:
        if resposta_tres != 'A' and resposta_tres != 'B' and resposta_tres != 'C' and resposta_tres != 'D':
            print('\033[31m'+'[ERRO] Opa! Você digitou errado, tente escolher entre A, B, C ou D'+'\033[0;0m')
            resposta_tres = input('ESCOLHA: ').upper()
        else:
            break
    c = valor.terceira_questao(resposta_tres)
    soma.append(c)
    os.system('clear') or None


    # Tratamento da questão 4 do questionário
    questao.quarta_questão()
    resposta_quatro = input('ESCOLHA: ').upper()
    while True:
        if resposta_quatro != 'A' and resposta_quatro != 'B' and resposta_quatro != 'C' and resposta_quatro != 'D':
            print('\033[31m'+'[ERRO] Opa! Você digitou errado, tente escolher entre A, B, C ou D'+'\033[0;0m')
            resposta_quatro = input('ESCOLHA: ').upper()
        else:
            break
    d = valor.quarta_questao(resposta_quatro)
    soma.append(d)
    os.system('clear') or None


    # Tratamento da questão 5 do questionário
    questao.quinta_questao()
    resposta_cinco = input('ESCOLHA: ').upper()
    while True:
        if resposta_cinco != 'A' and resposta_cinco != 'B' and resposta_cinco != 'C' and resposta_cinco != 'D':
            print('\033[31m'+'[ERRO] Opa! Você digitou errado, tente escolher entre A, B, C ou D'+'\033[0;0m')
            resposta_cinco = input('ESCOLHA: ').upper()
        else:
            break
    e = valor.quinta_questão(resposta_cinco)
    soma.append(e)
    os.system('clear') or None


    # Tratamento da questão 6 do questionário
    questao.sexta_questao()
    resposta_seis = input('ESCOLHA: ').upper()
    while True:
        if resposta_seis != 'A' and resposta_seis != 'B' and resposta_seis != 'C' and resposta_seis != 'D':
            print('\033[31m'+'[ERRO] Opa! Você digitou errado, tente escolher entre A, B, C ou D'+'\033[0;0m')
            resposta_seis = input('ESCOLHA: ').upper()
        else:
            break
    f = valor.sexta_questao(resposta_seis)
    soma.append(f)
    os.system('clear') or None


    # Tratamento da questão 7 do questionário
    questao.setima_questao()
    resposta_sete = input('ESCOLHA: ').upper()
    while True:
        if resposta_sete != 'A' and resposta_sete != 'B' and resposta_sete != 'C' and resposta_sete != 'D':
            print('\033[31m'+'[ERRO] Opa! Você digitou errado, tente escolher entre A, B, C ou D'+'\033[0;0m')
            resposta_sete = input('ESCOLHA: ').upper()
        else:
            break
    g = valor.setima_questão(resposta_sete)
    soma.append(g)
    os.system('clear') or None


    # Tratamento da questão 8 do questionário
    questao.oitava_questão()
    resposta_oito = input('ESCOLHA: ').upper()
    while True:
        if resposta_oito != 'A' and resposta_oito != 'B' and resposta_oito != 'C' and resposta_oito != 'D':
            print('\033[31m'+'[ERRO] Opa! Você digitou errado, tente escolher entre A, B, C ou D'+'\033[0;0m')
            resposta_oito = input('ESCOLHA: ').upper()
        else:
            break
    h = valor.oitava_questao(resposta_oito)
    soma.append(h)
    os.system('clear') or None


    # Tratamento da questão 9 do questionário
    questao.nona_questão()
    resposta_nove = input('ESCOLHA: ').upper()
    while True:
        if resposta_nove != 'A' and resposta_nove != 'B' and resposta_nove != 'C' and resposta_nove != 'D':
            print('\033[31m'+'[ERRO] Opa! Você digitou errado, tente escolher entre A, B, C ou D'+'\033[0;0m')
            resposta_nove = input('ESCOLHA: ').upper()
        else:
            break
    i = valor.nona_questão(resposta_nove)
    soma.append(i)
    os.system('clear') or None


    # Tratamento da questão 10 do questionário
    questao.decima_questao()
    resposta_dez = input('ESCOLHA: ').upper()
    while True:
        if resposta_dez != 'A' and resposta_dez != 'B' and resposta_dez != 'C' and resposta_dez != 'D':
            print('\033[31m'+'[ERRO] Opa! Você digitou errado, tente escolher entre A, B, C ou D'+'\033[0;0m')
            resposta_dez = input('ESCOLHA: ').upper()
        else:
            break
    j = valor.decima_questao(resposta_dez)
    soma.append(j)
    os.system('clear') or None

    
    # Tratamento da questão 11 do questionário
    questao.decima_primeira_questao()
    resposta_onze = input('ESCOLHA: ').upper()
    while True:
        if resposta_onze != 'A' and resposta_onze != 'B' and resposta_onze != 'C' and resposta_onze != 'D':
            print('\033[31m'+'[ERRO] Opa! Você digitou errado, tente escolher entre A, B, C ou D'+'\033[0;0m')
            resposta_onze = input('ESCOLHA: ').upper()
        else:
            break
    k = valor.decima_primeira_questao(resposta_onze)
    soma.append(j)
    os.system('clear') or None
    
    
    # Tratamento da questão 12 do questionário
    questao.decima_segunda_questao()
    resposta_doze = input('ESCOLHA: ').upper()
    while True:
        if resposta_doze != 'A' and resposta_doze != 'B' and resposta_doze != 'C' and resposta_doze != 'D':
            print('\033[31m'+'[ERRO] Opa! Você digitou errado, tente escolher entre A, B, C ou D'+'\033[0;0m')
            resposta_doze = input('ESCOLHA: ').upper()
        else:
            break
    l = valor.decima_segunda_questao(resposta_doze)
    soma.append(l)
    os.system('clear') or None
    
    
    # Tratamento da questão 13 do questionário
    questao.decima_terceira_questao()
    resposta_treze = input('ESCOLHA: ').upper()
    while True:
        if resposta_treze != 'A' and resposta_treze != 'B' and resposta_treze != 'C' and resposta_treze != 'D':
            print('\033[31m'+'[ERRO] Opa! Você digitou errado, tente escolher entre A, B, C ou D'+'\033[0;0m')
            resposta_treze = input('ESCOLHA: ').upper()
        else:
            break
    m = valor.decima_terceira_questao(resposta_treze)
    soma.append(m)
    os.system('clear') or None
    
    
    # Tratamento da questão 14 do questionário
    questao.decima_quarta_questao()
    resposta_quatorze = input('ESCOLHA: ').upper()
    while True:
        if resposta_quatorze != 'A' and resposta_quatorze != 'B' and resposta_quatorze != 'C' and resposta_quatorze != 'D':
            print('\033[31m'+'[ERRO] Opa! Você digitou errado, tente escolher entre A, B, C ou D'+'\033[0;0m')
            resposta_quatorze = input('ESCOLHA: ').upper()
        else:
            break
    n = valor.decima_quarta_questao(resposta_quatorze)
    soma.append(n)
    os.system('clear') or None

    print('Aguarde estamos calculando o resultados...')
    time.sleep(1)
    print('PRONTO!')
    os.system('clear') or None



    # Parte voltada para aprensentar e tratar o resultado 
    resultado_final = sum(soma)

    if 0 <= resultado_final <= 25:
        resultado.nunca_zen()

    if 25 < resultado_final <= 50:
        resultado.aspirante_zen()
        
    if 50 < resultado_final <= 75:
        resultado.aprendiz_zen()

    if 75 < resultado_final <= 100:
        resultado.monge_zen()

    if resultado_final > 100 :
        resultado.mestre_zen()
        
    time.sleep(20)

    os.system('clear') or None
    
    







