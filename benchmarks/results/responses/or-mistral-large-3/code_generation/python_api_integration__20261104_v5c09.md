# Mistral Large 3 675B — code_generation/python_api_integration

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 8.71 | quality: 9.72
- latency_total: 10.502s | tokens_per_second: 110.6
- input_tokens: 105 | output_tokens: 1162
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

Aquí tienes una función Python que cumple con todos los requisitos solicitados, utilizando `httpx` para las peticiones HTTP y manejando los errores, timeouts y retries con backoff exponencial:

```python
import httpx
import asyncio
from typing import List, Dict, Optional

async def get_filtered_products(
    token: str,
    base_url: str = "https://api.example.com/products",
    min_price: float = 100.0,
    timeout: int = 10,
    max_retries: int = 3
) -> Optional[List[Dict[str, str | float]]]:
    """
    Obtiene productos de una API con autenticación Bearer token,
    filtra aquellos con precio > min_price y retorna una lista simplificada.

    Args:
        token: Bearer token para autenticación
        base_url: URL de la API (por defecto: "https://api.example.com/products")
        min_price: Precio mínimo para filtrar productos (por defecto: 100)
        timeout: Timeout en segundos para la petición (por defecto: 10)
        max_retries: Número máximo de intentos (por defecto: 3)

    Returns:
        Lista de diccionarios con {id, name, price} de productos filtrados,
        o None si ocurre un error después de los reintentos.
    """
    headers = {"Authorization": f"Bearer {token}"}
    retry_delay = 1  # segundos iniciales para el backoff

    async with httpx.AsyncClient(timeout=timeout) as client:
        for attempt in range(max_retries):
            try:
                response = await client.get(base_url, headers=headers)
                response.raise_for_status()  # Lanza excepción para códigos 4xx/5xx

                products = response.json()
                if not isinstance(products, list):
                    raise ValueError("La respuesta de la API no es una lista de productos")

                # Filtrar y simplificar productos
                filtered_products = [
                    {
                        "id": product.get("id"),
                        "name": product.get("name"),
                        "price": product.get("price")
                    }
                    for product in products
                    if isinstance(product.get("price"), (int, float)) and product.get("price") > min_price
                ]

                return filtered_products

            except httpx.HTTPStatusError as e:
                if e.response.status_code == 401:
                    print("Error: Token no válido o no autorizado")
                    return None
                elif e.response.status_code == 404:
                    print("Error: Recurso no encontrado")
                    return None
                else:
                    print(f"Intento {attempt + 1}: Error HTTP {e.response.status_code} - {e}")

            except httpx.RequestError as e:
                print(f"Intento {attempt + 1}: Error de red - {e}")

            except (ValueError, KeyError) as e:
                print(f"Intento {attempt + 1}: Error en el formato de la respuesta - {e}")
                return None

            # Backoff exponencial (solo si no es el último intento)
            if attempt < max_retries - 1:
                await asyncio.sleep(retry_delay)
                retry_delay *= 2  # Duplica el tiempo de espera para el próximo intento

    print(f"Error: No se pudo completar la petición después de {max_retries} intentos")
    return None

# Ejemplo de uso (requiere asyncio.run si se ejecuta fuera de un entorno asíncrono)
if __name__ == "__main__":
    import asyncio

    async def main():
        token = "tu_token_aqui"
        products = await get_filtered_products(token)
        if products is not None:
            print(f"Productos encontrados: {len(products)}")
            for product in products:
                print(product)
        else:
            print("No se pudieron obtener los productos")

    asyncio.run(main())
```

### Características principales:

1. **Autenticación Bearer Token**: Se incluye en los headers de la petición.
2. **Filtrado de productos**: Solo se incluyen productos con precio > 100 (configurable).
3. **Formato de salida**: Lista de diccionarios con solo `id`, `name` y `price`.
4. **Manejo de errores**:
   - Errores HTTP (4xx, 5xx)
   - Errores de red (timeout, conexión fallida)
   - Errores en el formato de la respuesta
5. **Retry con backoff exponencial**:
   - Hasta 3 intentos (configurable)
   - Tiempo de espera inicial de 1 segundo, duplicándose en cada intento
6. **Timeout**: 10 segundos por defecto (configurable)
7. **Uso de httpx**: Cliente HTTP asíncrono moderno (puedes usar la versión síncrona si prefieres)

### Notas:
- La función es asíncrona (usa `async/await`). Si necesitas una versión síncrona, puedes reemplazar `httpx.AsyncClient` con `httpx.Client` y eliminar los `await`.
- El ejemplo de uso al final muestra cómo llamar a la función desde un contexto asíncrono.
- Los mensajes de error se imprimen por consola, pero podrías modificarlos para usar logging si lo prefieres.