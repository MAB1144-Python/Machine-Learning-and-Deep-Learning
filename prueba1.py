veces = int(input("¿Cuántas veces quiere que le salude? "))
print (veces)
a = [1,2,3,3]
for i in range(len(a)):
  n = a[i]
  for j in range(i+1,len(a)):
    m = a[j]
    print (i,j)
    if n == m and i!=j:
     print ('iguales',i,j)
