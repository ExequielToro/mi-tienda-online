# Tienda Online con Integración Java

**Tienda Online** es una plataforma de ventas en línea para cualquier tipo de producto. Solo necesitas personalizar las características de los productos y listo.  
Está desarrollada con **Django**, permitiendo a los usuarios navegar, agregar productos al carrito y realizar compras. Además, los administradores pueden gestionar productos mediante un CRUD completo.  
Esta tienda está **integrada con un sistema externo** mediante **microservicios SOAP**, desarrollados en Java.

---

## Arquitectura del Proyecto

El sistema está dividido en dos partes principales:

1. **Sistema de Bodega (Java + SOAP + Oracle)**  
   Proyecto independiente que expone microservicios SOAP para realizar operaciones CRUD sobre productos.  
   [Repositorio del sistema de bodega](https://github.com/ExequielToro/sistema-microservicios-soap)

2. **Tienda Online (Django + HTML + CSS + JavaScript)**  
   Este repositorio contiene el frontend y backend de la tienda, que consume los servicios SOAP para mostrar y gestionar productos.

---

## Tecnologías Utilizadas

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python, Django  
- **Servicios:** Consumo de WSDL (SOAP) generado en Java  
- **Pasarela de pagos:** Mercado Pago  
- **Base de datos:** SQLite (en Django) y Oracle (en sistema de bodega)  
- **Control de versiones:** Git y GitHub  

---

## Estructura del Proyecto

- `tienda/`: Proyecto principal de Django  
- `templates/`: Vistas HTML  
- `static/`: Archivos CSS y JS  
- `soap/`: Módulo para consumir servicios SOAP  
- `carrito/`: Gestión del carrito de compras  
- `usuarios/`: Registro e inicio de sesión de usuarios  

---

## Próximas mejoras

-Validación avanzada de datos desde los servicios SOAP
-Filtros y buscador de productos
-Historial de pedidos por usuario
-Seguridad mejorada y despliegue para producción
-Seguimiento del los productos
-Agregar empleadores,sucursales,vendedores,proveedores,etc 

---

## Instalación y Ejecución

1.- Descargar los instaladores(visual studio code)
2.- Abrir terminal o cmd
3.- Verificar si esta instaldo Python
4.- Instalar Django
5.- Crear un entorno virtual
6.- Instalar dependecias django 
7.- Configurar proyecto (manage.py)
8.- Aplicar migraciones
9.- Creación de superusuario
10.- Levantar el servidor
   
** Autor

Pablo Toro - Ingeniero en Informática
Este proyecto forma parte de mí experiencia profesional y está en constante mejora
