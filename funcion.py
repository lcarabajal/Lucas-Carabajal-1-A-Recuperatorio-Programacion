#Lucas Carabajal Division 1-A
#1.Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto y devuelva el valor del producto con un 
#aumento del 5%. Realizar la llamada desde el main.

def aplicarAumento(precioProducto:float)->float:
    
    aumento = precioProducto*5/100
    
    precioAumentado = precioProducto + aumento
    
    return precioAumentado
    