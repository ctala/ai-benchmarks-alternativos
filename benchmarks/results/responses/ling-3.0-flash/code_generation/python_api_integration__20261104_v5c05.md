# Ling 3.0 Flash — code_generation/python_api_integration

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 8.69 | quality: 9.52
- latency_total: 45.045s | tokens_per_second: 44.7
- input_tokens: 140 | output_tokens: 2014
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


def get_products(token: str) -> list[dict]:
    """
    Obtiene productos de la API, filtra los de precio > 100,
    y retorna una lista de dicts con {id, name, price}.

    Implementa reintentos con backoff exponencial (máx. 3 intentos)
    y timeout de 10 segundos.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}

    for attempt in range(1, 4):  # máximo 3 intentos
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                products = response.json()

            # Filtrar precio > 100 y proyectar solo los campos necesarios
            filtered_products = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if p.get("price", 0) > 100
            ]

            return filtered_products

        except (
            httpx.TimeoutException,
            httpx.NetworkError,
            httpx.HTTPStatusError,
            httpx.JSONDecodeError,
            KeyError,
        ) as e:
            if attempt == 3:
                # Último intento: propagar la excepción
                raise RuntimeError(
                    f"Error al obtener productos después de 3 intentos: {e}"
                ) from e

            # Backoff exponencial: 1s, 2s, 4s, ...
            backoff = 2 ** (attempt - 1)
            time.sleep(backoff)

    # Línea de seguridad (nunca debería llegar aquí)
    raise RuntimeError("No se pudieron obtener los productos.")


# --- Ejemplo de uso ---
if __name__ == "__main__":
    try:
        productos = get_products(token="mi-token-secreto")
        for p in productos:
            print(p)
    except RuntimeError as e:
        print(f"Error final: {e}")
```

### Explicación de los puntos clave

| Requisito | Implementación |
|---|---|
| **GET + Bearer token** | `client.get(url, headers={"Authorization": f"Bearer {token}"})` |
| **Filtrar precio > 100** | List comprehension con `if p.get("price", 0) > 100` |
| **Solo {id, name, price}** | Proyección explícita en el dict de la comprensión |
| **Timeout 10s + errores** | `timeout=10.0` en el cliente + manejo de `httpx.TimeoutException`, `httpx.NetworkError`, `httpx.HTTPStatusError`, `httpx.JSONDecodeError` |
| **Retry backoff exponencial** | Loop de 3 intentos con `time.sleep(2 ** (attempt - 1))` → espera 1s, luego 2s |
| **Sin dependencias externas** | Solo `httpx` + `time` (stdlib) |

### Comportamiento del backoff

```
Intento 1 → fallo → esperar 1 segundo  (2^0)
Intento 2 → fallo → esperar 2 segundos (2^1)
Intento 3 → fallo → lanzar RuntimeError
Intento 3 → éxito  → retornar resultado
```