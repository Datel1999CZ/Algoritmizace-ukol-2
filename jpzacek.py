array = ["čočka", "pero", "škola", "pes", "kolo"]
arrayb = ["chlup", "deník"]
print(array)

#přidání prvku vítr
array.append("vítr")
print(array)

#odstranění druhého prvku
array.remove(array[1])
print(array)
#zaměnění páté hodnoty za slunce
array[4] = "slunce"
print(array)

#přidání 2 stringových hodnot do pole

array.extend(arrayb)
print(array)