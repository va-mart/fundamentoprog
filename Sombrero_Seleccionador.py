# Write code below 💖
gryffindor = 0
ravenclaw = 0
hufflepuff = 0 
slytherin = 0
answer = int(input("""Q1) Prefieres el amanecer o el anochecer
    1) amanecer
    2) anochecer
    """))
if answer == 1:
  gryffindor += 1 
  ravenclaw += 1
elif answer == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print("Respuesta incorrecta")
answer = int(input("""Q2) Cuando mueras, te gustaria que las personas te recuerden como:
    1) El Bueno
    2) El Grandioso
    3) El Sabio
    4) El Audaz
    """))
if answer == 1:
  hufflepuff += 2
elif answer == 2:
  slytherin += 2
elif answer == 3:
  ravenclaw += 2
elif answer == 4:
  gryffindor += 2
else:
  print("Respuesta incorrecta")

answer = int(input("""Q3) Que clase de instrumento de gusta escuchar?
    1) El violin
    2) La trompeta
    3) El piano
    4) La bateria
    """))
if answer == 1:
  slytherin += 4
elif answer == 2:
  hufflepuff += 4
elif answer == 3:
  ravenclaw += 4
elif answer == 4:
  gryffindor += 4
else:
  print("Respuesta incorrecta")
print(
  """🦁 Gryffindor: """,gryffindor,
  """🦅 Ravenclaw: """,ravenclaw,
  """🦡 Hufflepuff: """,hufflepuff,
  """🐍 Slytherin: """,slytherin,
  )