# height at least 137 cm, cost 10 credis
# ask users their height and how many credits do they have
# height and credits enough -> Enjoy the ride
# enough credits but short -> not tall enough to ride
# tall enough but not credits -> you don't have enought credits
# do not meet either requirement

print('Welcome to The Cyclone, Coney Island.\n', 'We need you to answer a couple questions before proceeding.')
height = int(input('What is your height? Please write it in cm: '))
credits = int(input('How many credits do you have?: '))

if height >= 137 and credits >= 10:
  print('Enjoy the ride!')
elif height < 137 and credits >= 10:
  print("You're not tall enough to ride.")
elif height >= 137 and credits < 10:
  print("You don't have enough credits.")
else:
  print("You don't meet either requirement") 
