# Claude Fable 5 — code_generation/python_api_integration

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 7.73 | quality: 9.52
- latency_total: 18.439s | tokens_per_second: 68.1
- input_tokens: 154 | output_tokens: 1255
- judge_score: 4.8 | justificación: 

## Respuesta completa

# Función con httpx, retry y backoff exponencial

```python
import time
import httpx


def obtener_productos_caros(
    token: str,
    url: str = "https://api.example.com/products",
    max_intentos: int = 3,
    timeout: float = 10.0,
) -> list[dict]:
    """
    Obtiene productos con precio > 100 desde la API.

    Args:
        token: Bearer token para autenticación.
        url: Endpoint de la API.
        max_intentos: Número máximo de intentos (default 3).
        timeout: Timeout en segundos por request (default 10).

    Returns:
        Lista de dicts con las claves: id, name, price.

    Raises:
        RuntimeError: Si todos los intentos fallan.
        httpx.HTTPStatusError: Si la API responde con error 4xx (no se reintenta).
    """
    headers = {"Authorization": f"Bearer {token}"}
    ultimo_error: Exception | None = None

    for intento in range(1, max_intentos + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()

            productos = response.json()

            return [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in productos
                if p.get("price", 0) > 100
            ]

        except httpx.HTTPStatusError as exc:
            # Errores 4xx: no tiene sentido reintentar (token inválido, URL mal, etc.)
            if exc.response.status_code < 500:
                raise
            ultimo_error = exc

        except (httpx.TimeoutException, httpx.NetworkError) as exc:
            # Timeout o error de red: candidatos a retry
            ultimo_error = exc

        # Backoff exponencial: 1s, 2s, 4s... (no espera después del último intento)
        if intento < max_intentos:
            espera = 2 ** (intento - 1)
            time.sleep(espera)

    raise RuntimeError(
        f"Fallo tras {max_intentos} intentos. Último error: {ultimo_error}"
    ) from ultimo_error
```

## Ejemplo de uso

```python
try:
    productos = obtener_productos_caros(token="mi-token-secreto")
    for p in productos:
        print(f"{p['id']}: {p['name']} - ${p['price']}")
except RuntimeError as e:
    print(f"Error de red persistente: {e}")
except httpx.HTTPStatusError as e:
    print(f"Error de la API: {e.response.status_code}")
```

## Detalles de diseño

| Requisito | Implementación |
|---|---|
| Timeout 10s | `httpx.Client(timeout=timeout)` — aplica a conexión, lectura y escritura |
| Retry x3 | Bucle `for` con contador de intentos |
| Backoff exponencial | `2 ** (intento - 1)` → espera 1s, luego 2s |
| Errores de red | Captura `httpx.TimeoutException` y `httpx.NetworkError` |
| Errores 4xx | **No se reintentan** (un 401 nunca se arreglará solo); los 5xx sí |

**Nota:** si necesitas versión asíncrona, cambia a `httpx.AsyncClient`, marca la función como `async def` y usa `await asyncio.sleep(espera)` en lugar de `time.sleep`.