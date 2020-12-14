veces = int(input("¿programa para saber cuando estan bien cerrados los (), {} y []? "))
#print (veces)
listado = "([]{})"
a = list(listado)
print (a)
largo = int(len(a)/2)
#print ("la mitad del largo es ",largo)
band = False
for i in range(largo):
  e1 = a[i]
  ultimo = largo*2-i
  #print (i, ultimo)
  e2 = a[ultimo-1]
  #print (e1," == ",e2)
  if e1 == '(' and e2 == ')' and i!= ultimo:
     band = True
     continue
  elif e1 == '{' and e2 == '}' and i!= ultimo:
     band = True
     continue
  elif e1 == '[' and e2 == ']' and i!= ultimo:
     band = True
     continue
  else:
     band = False
     break
#print("va a evaluar de la froma dos")
largo = (largo)*2
if largo%2 == 0 and band != True:#si es multiplo de 2
 for i in range(0,largo,2):#este rango corre de dos en dos
  e1 = a[i]
  ultimo = largo*2-i
  #print (i, ultimo)
  e2 = a[i+1]
  #print (e1," == ",e2)
  if e1 == '(' and e2 == ')' and i!= ultimo:
     #print("caso 1")
     band = True
  elif e1 == '{' and e2 == '}' and i!= ultimo:
     #print("caso 2")
     band = True
  elif e1 == '[' and e2 == ']' and i!= ultimo:
     #print("caso 3")
     band = True
  else:
     band = False
     break 
if band:
   print("escrito de forma correcta")
else:
   print("escrito de forma incorrecta")  
