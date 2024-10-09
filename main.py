import random
array = [1, 13, 32, 45, 57, 69, 78, 81, 100]

arraylength = len(array)
firstnum = array[0]
middlenum = array[int(arraylength/2)]
lastnum = array[-1]

print("První, prostřední a poslední čísla jsou: ", firstnum ,",", middlenum ,",", lastnum) 

array[5] = 34

print("Indexová hodnota sedmého pole je: ", array[7])

print("Délka pole je: ", arraylength)

arraymax = max(array)
arraymin = min(array)

print("Minimální a maximální hodnota pole je: ", arraymin,",",arraymax)


arrayb = [10, 15, 43, 86, 55, 61, 79, 24]

arraysum = sum(arrayb)

print("Součet čísel v druhém poli je: ", arraysum)

arrayindexsum = arrayb[1] + arrayb[5]
print("Indexový součet 1 a 5 hodnoty pole 2 je: ", arrayindexsum)