class Producto:
    id_producto=0
    nombre=''
    precio=''
    stock = ''
    btu=''
    marca=''
    def __init__(self, id_producto,nombre,marca,btu,precio,stock,):
        self.id_producto=id_producto
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
        self.btu=btu
        self.marca=marca

    def libroArr(self):
        return{
            'codigo':self.id_producto,
            'nombre':self.nombre,
            'precio':self.precio,
            'stock':self.stock,
            'btu':self.btu,
            'marca':self.marca

        }
    def __str__(self):
        return   'codigo:'+self.id_producto +' nombre:'+self.nombre+' precio:'+self.precio+' stock:'+self.stock+ ' btu:'+self.btu+ ' marca:'+self.marca