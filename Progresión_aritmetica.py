
Dinero_invertido = 18000
Interes_anual = 0.03
Cantidad_años = 5

# Caso 1 - Debería dar $20.700

Interes_total = Interes_anual * Cantidad_años
Dinero_obtenido = Dinero_invertido + (Dinero_invertido * Interes_total)
print(int(Dinero_obtenido))
