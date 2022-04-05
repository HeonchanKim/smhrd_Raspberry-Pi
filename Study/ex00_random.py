import random
예진반 = ['김헌찬','제동현','김소원','유주영','전채원']
#randint  이상,이하
#result = 예진반[random.randint(0,4)]
#result = 예진반[random.randrange(5)]
result = random.choice(예진반)
print(result)

