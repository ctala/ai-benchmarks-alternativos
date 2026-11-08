# DeepSeek V4 Pro (0813) — code_generation/python_api_integration

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 7.79 | quality: 9.08
- latency_total: 46.144s | tokens_per_second: 67.8
- input_tokens: 189 | output_tokens: 3127
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

def obtener_productos_caros(
    token: str,
    precio_minimo: float = 100.0,
    intentos_maximos: int = 3
) -> list[dict]:
    """
    Obtiene productos desde la API y retorna solo los que tienen precio > precio_minimo.
    Incluye timeout de 10s, reintentos con backoff exponencial y manejo de errores de red/timeout.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout_segundos = 10.0
    backoff_base = 1.0  # segundos

    for intento in range(intentos_maximos):
        try:
            with httpx.Client(timeout=timeout_segundos, headers=headers) as client:
                respuesta = client.get(url)
                respuesta.raise_for_status()
                data = respuesta.json()

                # Algunas APIs devuelven {"products": [...]} o {"items": [...]}
                if isinstance(data, dict):
                    productos = data.get("products", data.get("items", []))
                else:
                    productos = data

                return [
                    {
                        "id": producto["id"],
                        "name": producto["name"],
                        "price": producto["price"],
                    }
                    for producto in productos
                    if float(producto.get("price", 0)) > precio_minimo
                ]

        except httpx.RequestError:
            # httpx.RequestError cubre errores de red y timeouts
            if intento == intentos_maximos - 1:
                raise
            time.sleep(backoff_base * (2 ** intento))

        except (KeyError, TypeError, ValueError):
            # Errores de formato/datos: no se reintenta
            raise

    return []
```

La función usa únicamente `httpx` y `time` de la biblioteca estándar, sin dependencias externas adicionales. Si después de los 3 intentos sigue fallando por red/timeout, se lanza la excepción original.