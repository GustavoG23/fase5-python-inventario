# Matriz de inventario
inventario = [
    ["A01", "Mouse", 3, 10],
    ["A02", "Teclado", 12, 10],
    ["A03", "Monitor", 2, 5],
    ["A04", "USB", 20, 15],
    ["A05", "Impresora", 1, 4]
]

# Función para calcular cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Mostrar lista de pedidos
print("LISTA DE REABASTECIMIENTO")

for articulo in inventario:
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    pedido = calcular_pedido(stock_actual, stock_minimo)

    print("Artículo:", nombre)
    print("Cantidad a pedir:", pedido)
    print("---------------------")
