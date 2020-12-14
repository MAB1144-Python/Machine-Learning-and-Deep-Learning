pala = "oeaaao"
a = list(pala)
larg = int(len(a)/2)
print (larg)
corre = 1
if len(a)-larg*2 > 0:
  corre = 0
for i in range(larg):
  n = a[i]
  m = a[larg*2-i-corre]
  print (i,n,m)
  if n == m :
     print ('iguales')
