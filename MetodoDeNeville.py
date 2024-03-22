def MetodoDeInterpolacionNeville(x, y, value):
    n = len(x)
    p = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        p[i][i] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            p[i][i + j] = ((value - x[i + j]) * p[i][i + j - 1] + (x[i] - value) * p[i + 1][i + j]) / (x[i] - x[i + j])
    return p[0][n - 1]

# Solicitar al usuario los valores de entrada
num_points = int(input("Introduce el número de puntos: \n"))
x = []
y = []

print("Introduce los valores de x :")
for i in range(num_points):
    x_value = float(input(f"x[{i}]: "))
    
    x.append(x_value)
   
print("Introduce los valores de y :\n")
for i in range(num_points):
    y_value = float(input(f"y[{i}]: "))
    y.append(y_value)
    
value = float(input("Introduce el valor de x para interpolar: \n"))

# Realizar la interpolación
interpolated_value = MetodoDeInterpolacionNeville(x, y, value)
print(f"Valor interpolado en x={value} es {interpolated_value}")
