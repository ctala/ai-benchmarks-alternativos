# MiMo-V2-Pro — code_generation/python_api_integration

- model_id: `xiaomi/mimo-v2-pro`
- success: True  | final: 7.63 | quality: 9.52
- latency_total: 16.13s | tokens_per_second: 67.9
- input_tokens: 353 | output_tokens: 1095
- judge_score: 4.8 | justificación: 

## Respuesta completa

# Función Python con httpx y retry

```python
import httpx
import time
from typing import Optional


def get_expensive_products(
    token: str,
    min_price: float = 100,
    base_url: str = "https://api.example.com",
    max_retries: int = 3,
    timeout: float = 10.0,
) -> list[dict]:
    """
    Obtiene productos con precio mayor a min_price desde la API.

    Args:
        token:       Bearer token de autenticación.
        min_price:   Precio mínimo para filtrar (default 100).
        base_url:    URL base de la API.
        max_retries: Número máximo de reintentos.
        timeout:     Timeout en segundos por request.

    Returns:
        Lista de dicts con {id, name, price} de productos filtrados.

    Raises:
        httpx.HTTPStatusError: Si la API retorna un error HTTP tras agotar reintentos.
        httpx.RequestError:    Si hay error de red tras agotar reintentos.
    """

    url = f"{base_url}/products"
    headers = {"Authorization": f"Bearer {token}"}

    last_exception: Optional[Exception] = None

    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza excepción en 4xx/5xx

                products = response.json()

                # Filtrar y extraer solo los campos necesarios
                filtered = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if p.get("price", 0) > min_price
                ]

                return filtered

        except (httpx.TimeoutException, httpx.NetworkError, httpx.HTTPStatusError) as exc:
            last_exception = exc
            print(f"⚠️  Intento {attempt}/{max_retries} falló: {type(exc).__name__}: {exc}")

            # Si no es el último intento, esperar con backoff exponencial
            if attempt < max_retries:
                wait_time = 2 ** (attempt - 1)  # 1s, 2s, 4s...
                print(f"   Reintentando en {wait_time}s...")
                time.sleep(wait_time)

    # Si llegamos aquí, todos los intentos fallaron
    raise last_exception  # type: ignore[misc]
```

## Ejemplo de uso

```python
if __name__ == "__main__":
    try:
        productos = get_expensive_products(token="mi_token_secreto_123")

        print(f"\n✅ Productos con precio > 100 encontrados: {len(productos)}")
        for p in productos:
            print(f"   - {p['name']}: ${p['price']}")

    except httpx.HTTPStatusError as e:
        print(f"❌ Error HTTP {e.response.status_code}: {e.response.text}")

    except httpx.RequestError as e:
        print(f"❌ Error de conexión: {e}")
```

## Flujo de retry visualizado

```
Intento 1 ──→ ¿Éxito? ──→ ✅ Retornar resultado
    │
    ❌ Falló
    │
    ▼ Espera 1s (2⁰)
    │
Intento 2 ──→ ¿Éxito? ──→ ✅ Retornar resultado
    │
    ❌ Falló
    │
    ▼ Espera 2s (2¹)
    │
Intento 3 ──→ ¿Éxito? ──→ ✅ Retornar resultado
    │
    ❌ Falló
    │
    ▼ Re-lanzar excepción
```

## Puntos clave

| Aspecto | Detalle |
|---|---|
| **Timeout** | 10s por request, configurable |
| **Backoff** | Exponencial: 1s → 2s → 4s |
| **Excepciones capturadas** | `TimeoutException`, `NetworkError`, `HTTPStatusError` |
| **Filtrado** | Usa `get("price", 0)` para evitar `KeyError` si falta el campo |
| **Sin dependencias extra** | Solo `httpx` (instalar con `pip install httpx`) |