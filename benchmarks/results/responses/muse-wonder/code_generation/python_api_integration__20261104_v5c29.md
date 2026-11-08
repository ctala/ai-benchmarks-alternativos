# Muse Wonder — code_generation/python_api_integration

- model_id: `meta/muse-wonder`
- success: True  | final: 7.84 | quality: 9.28
- latency_total: 11.956s | tokens_per_second: 138.8
- input_tokens: 100 | output_tokens: 1659
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

```python
import time
import httpx


def obtener_productos_caros(token: str) -> list[dict]:
    """
    Obtiene productos desde la API, filtra los que tienen precio > 100
    y retorna solo los campos id, name y price.

    Incluye timeout de 10 segundos y reintentos con backoff exponencial.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_intentos = 3
    ultimo_error = None

    for intento in range(max_intentos):
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()

            productos = response.json()

            # Por si la API devuelve {"products": [...]} en lugar de [...]
            if isinstance(productos, dict):
                productos = productos.get("products", [])

            return [
                {
                    "id": p["id"],
                    "name": p["name"],
                    "price": p["price"],
                }
                for p in productos
                if p.get("price", 0) > 100
            ]

        except httpx.HTTPStatusError as e:
            ultimo_error = e
            # Solo reintentar en errores del servidor (5xx)
            if e.response.status_code < 500 or intento == max_intentos - 1:
                raise

        except (httpx.TimeoutException, httpx.RequestError) as e:
            # Incluye errores de red, conexión y timeout
            ultimo_error = e
            if intento == max_intentos - 1:
                raise

        # Backoff exponencial: 1s, 2s, 4s...
        if intento < max_intentos - 1:
            espera = 1 * (2 ** intento)
            time.sleep(espera)

    # Nunca debería llegar aquí, pero por seguridad
    raise RuntimeError("No se pudieron obtener los productos") from ultimo_error


# Ejemplo de uso
if __name__ == "__main__":
    token = "tu_token_aqui"
    productos = obtener_productos_caros(token)
    print(productos)
```