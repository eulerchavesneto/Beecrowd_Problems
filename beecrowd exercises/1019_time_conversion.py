segundos = int(input())

horas = int(segundos / 3600)
resto = segundos - (horas * 3600)
minutos = int(resto / 60)
segundos = int(resto % 60)

print(f'{horas}:{minutos}:{segundos}')


