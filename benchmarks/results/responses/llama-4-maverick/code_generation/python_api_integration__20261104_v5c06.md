# Llama 4 Maverick — code_generation/python_api_integration

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 8.76 | quality: 9.52
- latency_total: 8.066s | tokens_per_second: 83.4
- input_tokens: 102 | output_tokens: 673
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Escribe una funcion Python que:
1. Haga GET a https://api.example.com/products con autenticacion Bearer token
2. Filtre productos con precio > 100
3. Retorne una lista de dicts con solo {id, name, price}
4. Maneje errores de red y timeout (10 segundos)
5. Incluya retry con backoff exponencial (max 3 intentos)

Usa httpx y no dependencias externas adicionales.


## Respuesta completa

### Función Python para obtener productos con filtro de precio

A continuación, te presento una función Python que cumple con los requisitos solicitados:

```python
import httpx
import logging
from typing import List, Dict

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def obtener_productos(token: str) -> List[Dict]:
    """
    Obtiene productos de la API con precio > 100 y retorna una lista de dicts con id, name y price.

    Args:
    - token (str): Token de autenticación Bearer.

    Returns:
    - List[Dict]: Lista de diccionarios con id, name y price de los productos filtrados.
    """

    # Configuración de la solicitud HTTP
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)  # Timeout de 10 segundos

    # Función para realizar la solicitud con retry y backoff exponencial
    transport = httpx.HTTPTransport(retries=3)
    client = httpx.Client(transport=transport, timeout=timeout)

    try:
        # Realizar solicitud GET con autenticación Bearer
        response = client.get(url, headers=headers)

        # Verificar si la respuesta fue exitosa
        response.raise_for_status()

        # Procesar la respuesta JSON
        productos = response.json()

        # Filtrar productos con precio > 100 y seleccionar campos id, name y price
        productos_filtrados = [
            {"id": p["id"], "name": p["name"], "price": p["price"]}
            for p in productos
            if p.get("price", 0) > 100
        ]

        return productos_filtrados

    except httpx.HTTPError as exc:
        logger.error(f"Error HTTP: {exc}")
    except httpx.TimeoutException as exc:
        logger.error(f"Timeout: {exc}")
    except Exception as exc:
        logger.error(f"Error inesperado: {exc}")

    return []

# Ejemplo de uso
if __name__ == "__main__":
    token = "tu_token_de_autenticacion"
    productos = obtener_productos(token)
    logger.info(productos)
```

### Explicación

1.  La función `obtener_productos` toma un token de autenticación Bearer como argumento y realiza una solicitud GET a la URL especificada con autenticación Bearer.
2.  Utiliza la biblioteca `httpx` para realizar la solicitud HTTP y configura un timeout de 10 segundos.
3.  Implementa retry con backoff exponencial utilizando `httpx.HTTPTransport` con `retries=3`.
4.  Filtra los productos con precio > 100 y selecciona solo los campos `id`, `name` y `price`.
5.  Maneja errores de red y timeout, y registra los errores utilizando la biblioteca `logging`.
6.  La función retorna una lista de diccionarios con los productos filtrados.

Puedes probar esta función proporcionando un token de autenticación válido y verificando los resultados. Recuerda reemplazar `"tu_token_de_autenticacion"` con tu token real en el ejemplo de uso.