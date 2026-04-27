# MiMo V2.5-Pro (Xiaomi) — code_generation/python_api_integration

- model_id: `mimo-v2.5-pro`
- success: True  | final: 7.93 | quality: 9.52
- latency_total: 23.316s | tokens_per_second: 56.1
- input_tokens: 355 | output_tokens: 1307
- judge_score: 4.8 | justificación: 

## Respuesta completa

# Función con `httpx`, filtros y retry con backoff exponencial

```python
import httpx
import time


def get_expensive_products(bearer_token: str) -> list[dict]:
    """
    Obtiene productos con precio > 100 desde la API,
    con reintentos y backoff exponencial.

    Args:
        bearer_token: Token de autenticación Bearer.

    Returns:
        Lista de dicts con {id, name, price} de productos con precio > 100.

    Raises:
        httpx.HTTPStatusError: Si tras los reintentos la API sigue respondiendo con error.
        httpx.RequestError:    Si tras los reintentos persiste un error de red.
    """

    url = "https://api.example.com/products"
    max_retries = 3
    base_delay = 1  # segundo base para el backoff

    headers = {"Authorization": f"Bearer {bearer_token}"}

    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza excepción para 4xx/5xx

            # Parsear y filtrar en una sola pasada
            products = response.json()
            return [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if p.get("price", 0) > 100
            ]

        except httpx.TimeoutException:
            # Timeout de conexión o lectura
            error_type = "Timeout"
        except httpx.HTTPStatusError:
            # Respuesta HTTP con código de error (4xx, 5xx)
            error_type = f"HTTP {response.status_code}"
        except httpx.RequestError:
            # Error de red (DNS, conexión rechazada, etc.)
            error_type = "Error de red"

        # Si no es el último intento, esperar con backoff exponencial
        if attempt < max_retries:
            delay = base_delay * (2 ** (attempt - 1))  # 1s → 2s → 4s
            print(f"[Intento {attempt}/{max_retries}] {error_type}. "
                  f"Reintentando en {delay}s...")
            time.sleep(delay)
        else:
            print(f"[Intento {attempt}/{max_retries}] {error_type}. "
                  f"Se agotaron los reintentos.")
            raise  # Re-lanza la última excepción capturada
```

---

## Cómo funciona, paso a paso

```
Intento 1          Intento 2          Intento 3
   │                  │                  │
   ▼                  ▼                  ▼
 GET /products     GET /products     GET /products
   │                  │                  │
 ¿Éxito?           ¿Éxito?           ¿Éxito?
   │ Sí → return     │ Sí → return     │ Sí → return
   │ No              │ No              │ No
   ▼                  ▼                  ▼
 esperar 1s        esperar 2s        raise (último intento)
```

### Desglose de cada requisito

| # | Requisito | Implementación |
|---|-----------|----------------|
| 1 | GET con Bearer token | `headers = {"Authorization": f"Bearer {bearer_token}"}` |
| 2 | Filtrar precio > 100 | List comprehension con `if p.get("price", 0) > 100` |
| 3 | Solo `{id, name, price}` | Dict literal `{"id": ..., "name": ..., "price": ...}` |
| 4 | Timeout de 10 s | `httpx.Client(timeout=10.0)` + catch `TimeoutException` |
| 5 | Retry con backoff | Loop `for attempt in range(1, 4)` con `delay = 1 * 2^(attempt-1)` |

---

## Ejemplo de uso

```python
if __name__ == "__main__":
    try:
        productos = get_expensive_products(bearer_token="mi_token_secreto_123")
        for p in productos:
            print(f"  #{p['id']}  {p['name']:30s}  ${p['price']:.2f}")
        print(f"\nTotal productos caros: {len(productos)}")
    except (httpx.HTTPStatusError, httpx.RequestError) as e:
        print(f"No se pudo obtener los productos: {e}")
```

**Salida esperada (ejemplo):**
```
  #42  Monitor 4K UltraWide             $599.99
  #87  Teclado mecánico premium         $149.00

Total productos caros: 2
```

---

## Notas importantes

- **`httpx.Client` en un `with`**: garantiza que la conexión TCP se cierre correctamente, incluso si hay excepciones.
- **`p.get("price", 0)`**: evita `KeyError` si algún producto no tiene el campo `price`.
- **`raise` sin argumentos** en el último `except`: re-lanza la excepción original con su traceback intacto, lo que facilita el debugging.
- **No se usa `tenacity` ni `backoff`**: el retry manual cumple el requisito de no dependencias externas adicionales a `httpx`.