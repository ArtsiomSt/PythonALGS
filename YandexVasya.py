import re
import math

class bludo:
    def __init__(self, name, amount, amount_of_ingr, belk=0, jir=0, ugl=0, ener=0):
        self.name = name
        self.amount = amount
        self.amount_of_ingr = amount_of_ingr
        self.ingridients_needed = []
        self.belk = belk
        self.jir = jir
        self.ugl = ugl
        self.ener = ener


class ingridient:
    def __init__(self, name='NULL', price=0, amount_per_one=0, amount_for_stats=0, si='NULL', si1 = 'NULL', belk=0, jir =0, ugle=0, energy=0):
        self.name = name
        self.price = price
        self.amount_per_one_packet = amount_per_one
        self.amount_for_stats = amount_for_stats
        self.si = si
        self.si1 = si1
        self.belk = belk
        self.jir = jir
        self.ugle = ugle
        self.energy = energy


class amount_of_ingridients:
    def __init__(self, name, amount_for_bludo, si):
        self.name = name
        self.amount_for_bludo = amount_for_bludo
        self.si = si

class name_plus_packs:
    def __init__(self, name, packs):
        self.name = name
        self.packs = packs


amount_of_bludes = int(input())
bludes = []
ingridients = []
ingridients_need = []
one_string = ''
is_there_a_blude = False
price = 0
name_price = []

for item in range(amount_of_bludes):
    one_string = input()
    sep = re.split(' ', one_string)
    current_bludo = bludo(sep[0], int(sep[1]), int(sep[2]))
    n = current_bludo.amount_of_ingr
    for item_1 in range(n):
        one_string = input()
        sep = re.split(' ', one_string)
        cur_ingridient_1 = amount_of_ingridients(sep[0], int(sep[1]), sep[2])
        cur_ingridient = amount_of_ingridients(sep[0], int(sep[1]), sep[2])
        current_bludo.ingridients_needed.append(cur_ingridient_1)
        cur_ingridient.amount_for_bludo *=current_bludo.amount
        counter = 0
        if ingridients_need:
            for item in ingridients_need:
                if cur_ingridient.name == item.name:
                    break
                else:
                    counter += 1
            if counter < len(ingridients_need):
                ingridients_need[counter].amount_for_bludo = ingridients_need[counter].amount_for_bludo+cur_ingridient.amount_for_bludo
            else:
                ingridients_need.append(cur_ingridient)
        else:
            ingridients_need.append(cur_ingridient)
    bludes.append(current_bludo)

k = int(input())

for item in range(k):
    one_string = input()
    sep = re.split(' ', one_string)
    current_ingr = ingridient()
    current_ingr.name = sep[0]
    current_ingr.price = int(sep[1])
    current_ingr.amount_per_one_packet = int(sep[2])
    current_ingr.si = sep[3]
    ingridients.append(current_ingr)

m = int(input())

for item in range(m):
    one_string = input()
    sep = re.split(' ', one_string)
    counter = 0
    for item1 in ingridients:
        if item1.name == sep[0]:
            break
        else:
            counter += 1
    if (counter < len(ingridients)):
        ingridients[counter].amount_for_stats = int(sep[1])
        ingridients[counter].si1 = sep[2]
        ingridients[counter].belk = float(sep[3])
        ingridients[counter].jir = float(sep[4])
        ingridients[counter].ugle = float(sep[5])
        ingridients[counter].energy = float(sep[6])

for item in ingridients_need:
    counter = 0
    for item1 in ingridients:
        if item.name == item1.name:
            break
        else:
            counter += 1
    if item.si != ingridients[counter].si:
        if (item.si == 'ml' or item.si == 'g') and (ingridients[counter].si == 'kg' or ingridients[counter].si == 'l'):
            packs = math.ceil(item.amount_for_bludo/(ingridients[counter].amount_per_one_packet*1000))
        elif (item.si == 'l' or item.si == 'kg') and (ingridients[counter].si == 'g' or ingridients[counter].si == 'ml'):
            packs = math.ceil((item.amount_for_bludo*1000)/ingridients[counter].amount_per_one_packet)
        elif (item.si == 'cnt') and (ingridients[counter].si == 'tens'):
            packs = math.ceil(item.amount_for_bludo/(ingridients[counter].amount_per_one_packet*10))
        elif (item.si == 'cnt') and (ingridients[counter].si == 'cnt'):
            packs = math.ceil((item.amount_for_bludo*10)/ingridients[counter].amount_per_one_packet)
    else:
        packs = math.ceil(item.amount_for_bludo/ingridients[counter].amount_per_one_packet)

    price += ingridients[counter].price*packs
    cur_packets = name_plus_packs(ingridients[counter].name, packs)
    name_price.append(cur_packets)

for item in ingridients:
    counter = 0
    for item_1 in ingridients_need:
        if item.name == item_1.name:
            break
        else:
            counter += 1
    if counter < len(ingridients_need):
        pass
    else:
        cur_packets = name_plus_packs(item.name, 0)
        name_price.append(cur_packets)


counter_1 = 0
for blude in bludes:
    for item in blude.ingridients_needed:
        counter = 0
        for item1 in ingridients:
            if item.name == item1.name:
                break
            else:
                counter += 1
        if (ingridients[counter].si1 == 'kg' or ingridients[counter].si1 == 'l') and (item.si == 'g' or item.si == 'ml'):
            k = item.amount_for_bludo/(1000*ingridients[counter].amount_for_stats)
        elif (ingridients[counter].si1 == 'g' or ingridients[counter].si1 == 'ml') and (item.si == 'kg' or item.si == 'l'):
            k = item.amount_for_bludo*1000/ingridients[counter].amount_for_stats
        elif ingridients[counter].si1 == 'tens' and item.si == 'cnt':
             k = item.amount_for_bludo/(10*ingridients[counter].amount_for_stats)
        else:
            k = item.amount_for_bludo/ingridients[counter].amount_for_stats
        bludes[counter_1].belk += ingridients[counter].belk*k
        bludes[counter_1].jir += ingridients[counter].jir*k
        bludes[counter_1].ugl += ingridients[counter].ugle*k
        bludes[counter_1].ener += ingridients[counter].energy*k
    counter_1 += 1


print(price)
for item in name_price:
    print(item.name+' ' + str(item.packs))

for item in bludes:
    print(item.name, end=' ')
    print(item.belk, end=' ')
    print(item.jir, end=' ')
    print(item.ugl, end=' ')
    print(item.ener, end=' ')
    print()
