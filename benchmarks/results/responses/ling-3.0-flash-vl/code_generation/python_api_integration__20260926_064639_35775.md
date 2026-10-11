# Ling 3.0 Flash VL — code_generation/python_api_integration

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 8.99 | quality: 9.52
- latency_total: 11.87s | tokens_per_second: 142.7
- input_tokens: 140 | output_tokens: 1694
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
import httpx
import time


def get_expensive_products(token: str) -> list[dict]:
    """
    Obtiene productos de la API, filtra los que tienen precio > 100
    y retorna una lista de dicts con {id, name, price}.

    Implementa reintentos con backoff exponencial (máx 3 intentos)
    y maneja errores de red y timeout (10 segundos).
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)
    max_attempts = 3

    for attempt in range(max_attempts):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()

            products = response.json()

            filtered = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if p.get("price", 0) > 100
            ]

            return filtered

        except httpx.TimeoutException as e:
            if attempt < max_attempts - 1:
                wait = 2 ** attempt  # 1s, 2s, 4s ...
                time.sleep(wait)
            else:
                raise RuntimeError(
                    f"Timeout después de {max_attempts} intentos"
                ) from e

        except httpx.TransportError as e:
            if attempt < max_attempts - 1:
                wait = 2 ** attempt
                time.sleep(wait)
            else:
                raise RuntimeError(
                    f"Error de red después de {max_attempts} intentos"
                ) from e

        except httpx.HTTPStatusError as e:
            raise RuntimeError(
                f"Error HTTP {e.response.status_code}: {e.response.text}"
            ) from e

        except httpx.JSONDecodeError as e:
            raise RuntimeError("Respuesta no es JSON válido") from e

        except KeyError as e:
            raise RuntimeError(
                f"Campo faltante en los datos del producto: {e}"
            ) from e

    # En caso de que el bucle termine sin retornar (por alguna lógica inesperada)
    raise RuntimeError("No se pudo obtener los productos")
```

### Explicación de los puntos clave:

| Requisito | Implementación |
|---|---|
| **GET con Bearer token** | Header `Authorization: Bearer {token}` en `client.get()` |
| **Filtro precio > 100** | List comprehension con `if p.get("price", 0) > 100` |
| **Retorno {id, name, price}** | Proyección explícita en el dict de la lista |
| **Timeout 10s** | `httpx.Timeout(10.0)` aplicado al cliente |
| **Retry con backoff exponencial** | `time.sleep(2 ** attempt)` → espera 1s, 2s y 4s entre intentos (máx 3) |
| **Sin dependencias externas** | Solo `httpx` y `time` (stdlib) |

### Uso:

```python
token = "tu_token_aqui"
try:
    productos = get_expensive_products(token)
    for p in productos:
        print(p)
except RuntimeError as e:
    print(f"Error: {e}")
```