from datetime import datetime

agora = datetime.now()

dia = agora.day
mes = agora.month
ano = agora.year
horas = agora.hour
minutos = agora.minute

print(f"Hoje é {dia}/{mes}/{ano} e agora são {horas}:{minutos}")

#Outra forma

print(agora.strftime("Hojé é %d/%m/%Y e agora são %H:%M"))