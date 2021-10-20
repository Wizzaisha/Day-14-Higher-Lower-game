import random
from art import logo, vs
from game_data import data
from replit import clear


#Escoge una opcion de la data
def option():
  data_ran = random.choice(data)
  return data_ran

#Descripcion de la opcion escogida
def dict_variables(diccionario,otp):
  name = diccionario["name"]
  description = diccionario["description"]
  country = diccionario["country"]
  return f"Compare {otp}: {name}, a {description}, from {country}"

#Cantidad de followers
def followers(diccionario):
  return diccionario["follower_count"]

#Comparacion A y B
def compare(a, b, asnwer):
  if user_answer == "b":
    c = amount_followers_A
    a = amount_followers_B
    b = c
  if a > b:
    return True
  else:
    return False

#CODE HIGHER LOWER GAME

#Las 2 opciones, son de tipo diccionario
option_A = option()
option_B = option()

#Contador de score
score = 0

#Logo
print(logo)

#Loop para cuando sea correcta la desicion
result_compare = True
while result_compare:
  
  #Print del "Compare A"
  descript_A = dict_variables(option_A, "A")
  print(descript_A)

  #Cantidad de followers
  amount_followers_A = followers(option_A)
  
  #TEST
  print(amount_followers_A)

  #Versus
  print(vs)

  #Print del "Compare B"
  descript_B = dict_variables(option_B, "B")
  print(descript_B)

  #Cantidad de followers
  amount_followers_B = int(followers(option_B))

  #TEST
  print(amount_followers_B)

  #Pregunta de seleccionar una opcion
  user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

  #Comparacion de las opciones, devuelve TRUE o FALSE
  result_compare = compare(amount_followers_A, amount_followers_B, user_answer)
  
  #Respuesta correcta y continuacion del loop
  if result_compare or result_compare == result_compare:

    score += 1
    option_A = option_B
    option_B = option()

    #Imprimir_score
    clear()
    print(logo)
    print(f"You're right! Current score: {score}")

  else:
    result_compare = False

clear()
print(logo)
print(f"Sorry, that's wrong. Final score: {score}")