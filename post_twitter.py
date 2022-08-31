#!/usr/bin/env python
# -*- coding: utf-8 -*-

from asyncio.log import logger
from msilib.schema import File
import tweepy, time
from respondtotweet import respondToTweet
import settings
import random




pessoas = ["Pinto","Mito","Beta", "Artin", "Drasso", "Yudi", "Livia", "Theo", "amor", "Dartnes","Xuxa"]
materiaopt = ["Calculo 1", "Genetica", "Fisica", "bve", "DCE 420"]
horaopt = ["1","2","3","4","5","6","7","8","9","10","11"]
jogoopt = ["rocket league", "cs", "minecraft", "valorant","aram", "cassino brasil", "fifinha"]
cenarioopt = ["na hora da aula", "amanha", "de noite", "depois do jogo"]
timeopt = ["Atletico", "galao", "galo", "cruzeiro", "curintia", "flamengo", "Cuiabayern", "Marseille", "psg", "Real Madrid","Chelsea", "Clube Atletico Dinheiro"]
jogadoropt = ["Marcos Leonardo","Ngapandouetnbu","Jo77","Jamerson","Allan Kardec","Lakaka","Werner","Hulk", "Nacho","Havertz", "Everson", "Rudiger", "Wellington Rato", "Edu 99", "Sasha", "Mane", "Salah", "Ademir", "Azpilipueta", "Fabio", "Pedrinho", "Luan", "Kepa Barrizalabala","Harry cane"]
tecnicopt = ["SAMPAOLI","PEZOLANO","ANTONIO CONTE","ARTIN TUCHEL","YUDI CONFIANTE :)","TUCHEL","LAMPARD","CUQUINHA FEDAPUTA","RENATOP GAUCHO","ROGERIO CENI","JOSE MOURINHO","DUDAMEL" ]
 
CONSUMER_KEY = settings.ENV['CONSUMER_KEY']
CONSUMER_SECRET = settings.ENV['CONSUMER_SECRET']
ACCESS_KEY = settings.ENV['ACCESS_KEY']
ACCESS_SECRET = settings.ENV['ACCESS_SECRET']


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


n=0
while n<10:
    respondToTweet()
    jogador2 = random.choice(jogadoropt)
    cenario = random.choice(cenarioopt)
    jogador = random.choice(jogadoropt)
    pessoa = random.choice(pessoas)
    time1 = random.choice(timeopt)
    jogo = random.choice(jogoopt)
    hora = random.choice(horaopt)
    materia = random.choice(materiaopt)
    tecnico = random.choice(tecnicopt)
    f1 = ["E apagar o bot em?","Cheiro de 2° Brasileiro\n Cheiro (2°) Supercopa de convidado\n Cheiro na CDB\n Cheiro na liberta\n Cheiro no carioca","As camisas vão chegar e "+str(pessoa)+" ainda não pediu","lei 171","Bob Marley sitou","Renato Gaucho são meus ovos","Ce esqueceu q sou FalaBoulos13","Harry cane em 10 anos de tottenham","Caroninha pro boulos? 😃","É porque falaram que ta vergonhoso","Fazer um DME aqui no fifa",  "Mas e porque do nada apareceu um carro atras", "Vô na bbt rapidao" , "Eu nn fui bem nessa por estar doente e tals, na proxima nn tem desculpa nn, vo amassar","Arbitragem nojenta!" ,"Bom noite" , "Oieee" , "Isso n e vida nao" , "Era msg pra aninha" ,"SI" , "Ai minha bet" , "Eu odeio estudar antecipado",]
    f2 = ["O " +str(pessoa) + ", eu tenho mewtwo de armadura ce tem?","O "+str(pessoa) + " qual a boa de hoje?","O "+str(pessoa) +" , voce viu quem veio pro " + str(time1)+"?","O "+str(pessoa) + " , qq ce me diz de " +str(jogador)+ " q jogou no " +str(time1)+"?","O "+ str(pessoa) + " , me lembra de montar bet "+str(cenario), "O "+str(pessoa) +" , estamos de moto hj?", "só jogar um " +str(jogo) +" e vou de neneca",]
    f3 = ["Depois eu falo q "+str(time1)+ " é um time imundo, boulos nn entende nada",str(tecnico)+" terminou a 3 pontos do líder com "+str(jogador)+ " e " +str(jogador2)+" no ataque",str(tecnico) +" DEIXOU O "+str(time1),"Pq jogamos um "+str(jogo)+" lendario ontem a noite","Fui dormir " + str(hora)+ " da manha", "Tenho que estudar "+str(materia), str(time1) +" nn foda minha bet",]
    f4 = [r"C:\Users\pedro\OneDrive\Área de Trabalho\bot-twitter\svd_images\svd6.jpg",r"C:\Users\pedro\OneDrive\Área de Trabalho\bot-twitter\svd_images\svd5.jpg",r"C:\Users\pedro\OneDrive\Área de Trabalho\bot-twitter\svd_images\cf22485e-f8b7-448c-827b-76f28ccb5a1c.jpg", r"C:\Users\pedro\OneDrive\Área de Trabalho\bot-twitter\svd_images\randomb1.jpg", r"C:\Users\pedro\OneDrive\Área de Trabalho\bot-twitter\svd_images\random2.jpg",r"C:\Users\pedro\OneDrive\Área de Trabalho\bot-twitter\svd_images\random3.jpg",r"C:\Users\pedro\OneDrive\Área de Trabalho\bot-twitter\svd_images\nathangalo.jpg",r"C:\Users\pedro\OneDrive\Área de Trabalho\bot-twitter\svd_images\hulkgol.jpg",r"C:\Users\pedro\OneDrive\Área de Trabalho\bot-twitter\svd_images\svd1.jpg",r"C:\Users\pedro\OneDrive\Área de Trabalho\bot-twitter\svd_images\svd2.jpg",r"C:\Users\pedro\OneDrive\Área de Trabalho\bot-twitter\svd_images\svd3.jpg",r"C:\Users\pedro\OneDrive\Área de Trabalho\bot-twitter\svd_images\svd4.jpg",]
    esclh = [f1,f2,f3,f4]
    carai = random.choice(esclh)
    hihi = random.choice(carai)
    print(n)
    if carai == f4:
        if hihi ==  r"C:\Users\pedro\OneDrive\Área de Trabalho\bot-twitter\svd_images\random3.jpg":
            media = api.media_upload(hihi)
            tweet = ''
            api.update_status(status=tweet, media_ids=[media.media_id])
        elif hihi == r"C:\Users\pedro\OneDrive\Área de Trabalho\bot-twitter\svd_images\nathangalo.jpg":
            media = api.media_upload(hihi)
            tweet = ''
            api.update_status(status=tweet, media_ids=[media.media_id])
        elif hihi == r"C:\Users\pedro\OneDrive\Área de Trabalho\bot-twitter\svd_images\cf22485e-f8b7-448c-827b-76f28ccb5a1c.jpg":
            media = api.media_upload(hihi)
            tweet = ''
            api.update_status(status=tweet, media_ids=[media.media_id])
        elif hihi == r"C:\Users\pedro\OneDrive\Área de Trabalho\bot-twitter\svd_images\randomb1.jpg":
            media = api.media_upload(hihi)
            tweet = ''
            api.update_status(status=tweet, media_ids=[media.media_id])
        elif hihi == r"C:\Users\pedro\OneDrive\Área de Trabalho\bot-twitter\svd_images\random2.jpg":
            media = api.media_upload(hihi)
            tweet = ''
            api.update_status(status=tweet, media_ids=[media.media_id])
        elif hihi == r"C:\Users\pedro\OneDrive\Área de Trabalho\bot-twitter\svd_images\hulkgol.jpg":
            media = api.media_upload(hihi)
            tweet = 'EU TE AMO HULK PARAIBA EU TE AMO 🐔🐔🐔'
            api.update_status(status=tweet, media_ids=[media.media_id])
        elif hihi == r"C:\Users\pedro\OneDrive\Área de Trabalho\bot-twitter\svd_images\bomdia-deyverson.jpg":
            media = api.media_upload(hihi)
            tweet = 'Bom dia'
            api.update_status(status=tweet, media_ids=[media.media_id])
        else:
            media = api.media_upload(hihi)
            tweet = 'servidos pivetes?'
            api.update_status(status=tweet, media_ids=[media.media_id])
    else:
        api.update_status(hihi)
    n=n+1
    time.sleep(1800)