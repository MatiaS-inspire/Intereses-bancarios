from re import I
# Caso 2 - Debería dar 20.866,93 --- La diferencia es de 2.866,93

Dinero_bolsillo = 18000
Interes_anual = 0.03
Cantidad_años = 5

for i in range(Cantidad_años):
  Dinero_bolsillo = Dinero_bolsillo + (Dinero_bolsillo * Interes_anual) # La variable acumuladora va en el primer termino para que se repita en cada caso
  print(int(Dinero_bolsillo))
