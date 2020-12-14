import numpy
veces = int(input("¿Cuántas veces quiere que le salude? "))
print (veces)
a = "abca"
b = "aaaaaabcabc"
leta = list(a)
contat = numpy.zeros((len(leta),2))
letb = list(b)
contot = len(letb)
conpart = 0
for i in range(len(leta)):
  n = leta[i]
  for j in range(len(leta)):
    m = leta[j]
    print (i,j,n,m)
    if n == m:
      contat[i][1] = contat[i][1]+1
      print ('iguales en la cadena',i,j)
  for k in range(len(letb)):
    m = letb[k]
    #print (i,j)
    if n == m:
      contat[i][0] =contat[i][0]+1
      print (conpart,' encontrado en el otro vector',i,k,contat[i][0])
  conpart = int(contat[i][0]/contat[i][1])
  if contot > conpart:
       contot = conpart
  print("resultado",contot,contat[i][0],contat[i][1],n)
       

