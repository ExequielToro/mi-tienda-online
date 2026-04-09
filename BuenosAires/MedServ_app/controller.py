from zeep import Client
from .producto import Producto
import mercadopago


class Controller:
    wsdl = 'http://localhost:8080/AIREACON/servicioLibreria?wsdl'
    
    cliente = Client(wsdl)
    
    def buscarTodo(self):
        listaProducto = []
        lista = self.cliente.service.consultarProducto()
        for i in range(len(lista)):
            producto = Producto(
                lista[i]['id_producto'],
                lista[i]['nombre'],
                lista[i]['precio'],
                lista[i]['stock'],
                lista[i]['btu'],
                lista[i]['marca']
            )
            listaProducto.append(producto)
        return listaProducto
    
    def buscarUnaBodega(self, cod):
        producto = self.cliente.service.consultarunProducto(cod)
        return producto
    
    def actualizarStock(self, cod, stock,precio):
        resultado = self.cliente.service.actualizarStockProducto(cod, stock,precio)
        return resultado
    
    def sumar(self):
        resultado = self.cliente.service.sumar(3, 4)
        return resultado
    

    
    def eliminarProducto(self, id_producto):
        resultado = self.cliente.service.eliminarProducto(id_producto)
        return resultado
    
    def IngresarProducto(self, precio_producto, btu, marca, nombre, stock):
        resultado = self.cliente.service.ingresarProducto(precio_producto, btu, marca, nombre, stock)
        return resultado


    
    def pagar(self):
        sdk = mercadopago.SDK("TEST-20740088581424-061118-25aa2389f89bd2e80efcb1931e8ece4f-1396964436")

        preference_data = {
            "items": [
                {
                    "title": "Aire Acondicionado Nike",
                    "id": 1,
                    "description": "Producto",
                    "quantity": 1,
                    "unit_price": 100000
                }
            ],
            "back_urls": {
                "success": "http://127.0.0.1:8000/",
                "failure": "http://127.0.0.1:8000/",
                "pending": "http://127.0.0.1:8000/"
            },
            
        }

        preference_response = sdk.preference().create(preference_data)

        print("MP RAW:", preference_response)  # 👈 DEBUG REAL

        # 👇 cubrir ambos casos (SDK viejo y nuevo)
        if "response" in preference_response:
            return preference_response["response"]
        else:
            return preference_response