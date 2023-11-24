#Izveidojiet Python programmu, kas pārbauda, vai ievadītais skaitlis ir nepāra, izmantojot if priekšrakstu.

skaitlis=[1,2,3,4,5,6,7,8,9,10,11,12]
nepara_skaitlis=list(filter(lambda x:x%2==0, skaitlis))
print(nepara_skaitlis)