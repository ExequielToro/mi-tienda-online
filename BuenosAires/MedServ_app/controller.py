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
        #Agregar credenciales
        #ojo son las del vendedor de prueba no las credenciales mias como cliente
        #vendedor
        #{"id":773889678,"nickname":"TETE5286432","password":"qatest6632","site_status":"active","email":"test_user_14786185@testuser.com"}

        #comprador
        #{"id":773889678,"nickname":"TEST9GVLSYZE","password":"qatest6632","site_status":"active","email":"test_user_42921861@testuser.com"}

        #se debe ingresar con estas credenciales a la pagina y obtener un token como vendedor
        # https://www.mercado.cl/developers/es/guides
        #TEST-4113249211775140-060816-f22ac383ad0dc6dcdcec1fe81b61745b-773889678")


        sdk = mercadopago.SDK("TEST-20740088581424-061118-25aa2389f89bd2e80efcb1931e8ece4f-1396964436")

        # Crea un ítem en la preferencia
        preference_data = {
            "items": [
                {
                    "title": "Aire Acondicionado Nike",
                    "id":1,
                    "description": "Producto",
                    "quantity": 1,
                    "unit_price": 100000
                },
                {
                    "title": "Aire Acondicionado Wifi",
                    "id":2,
                    "description": "Producto",
                    "quantity": 1,
                    "unit_price": 150000
                }
            ],
            "back_urls":{
                "success": "http://127.0.0.1:8000/",
                "failure": "http://127.0.0.1:8000/",
                "pending": "http://127.0.0.1:8000/"
            },
            "auto_return": "approved"
        }

        preference_response = sdk.preference().create(preference_data)
        #preference = preference_response["response"]
        return preference_response