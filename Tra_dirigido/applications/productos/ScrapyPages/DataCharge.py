from django.db import transaction
import logging
from applications.productos.models import Productos
from applications.historial_precio.models import Historial_precio
from django.db import IntegrityError


def saveProductsAndPrices(listaProductosRepeat):
    listaProductos = delProductsRepeated(listaProductosRepeat)

    productObjects = []
    historyPricesObjects = []

    for producto in listaProductos:

        if producto["almacen"] == "Exito":
            product_object = Productos(producto["id"], producto["almacen"], producto["descripcion"][:100], producto["categoria"],producto["marca"], producto["descripcion"][:100], )
        else:
            product_object = Productos(producto["id"], producto["almacen"], producto["nombre"][:100],producto["categoria"],producto["marca"], producto["descripcion"][:100], )

        producto_insertar = Productos.objects.filter(productId=producto["id"],store=producto["almacen"])
        if not producto_insertar.exists():
            productObjects.append(product_object)

        if producto["almacen"] == "Exito":
            history_prices_object = Historial_precio(productId=product_object, price=producto["precio"],priceUnit=producto["precio"])
        else:
            history_prices_object = Historial_precio(productId=product_object, price=producto["precio"],
                                                     priceUnit=producto["precioUnitario"])
        historyPricesObjects.append(history_prices_object)

    logger = logging.getLogger(__name__)

    try:
        with transaction.atomic():
            for product_object in productObjects:
                try:
                    product_object.save()
                except Exception as e:
                    # Manejar la excepción de clave única violada (puedes personalizar según tus necesidades)
                    logger.warning(f"Error al insertar producto {product_object}: {e}")

            for history_prices_object in historyPricesObjects:
                try:
                    history_prices_object.save()
                except Exception as e:
                    # Manejar la excepción de clave única violada (puedes personalizar según tus necesidades)
                    logger.warning(f"Error al insertar historial de precios {history_prices_object}: {e}")

    except Exception as e:
        logger.error(f"Error al ejecutar bulk_create: {e}")



def delProductsRepeated(lista):
    # Crear un conjunto para rastrear productId únicos
    seen_product_ids = set()

    # Crear una lista filtrada de diccionarios únicos
    diccionarios_unicos = []

    for diccionario in lista:
        product_id = diccionario["id"]
        if product_id not in seen_product_ids:
            seen_product_ids.add(product_id)
            diccionarios_unicos.append(diccionario)

    return diccionarios_unicos



