# Tencent Hy4 — code_generation/python_api_integration

- model_id: `tencent/hy4`
- success: True  | final: 8.25 | quality: 9.52
- latency_total: 35.492s | tokens_per_second: 97.8
- input_tokens: 129 | output_tokens: 3470
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

Aquí tienes la implementación. Usa únicamente `httpx` y `time` (de la librería estándar) para el backoff, sin recurrir a `tenacity` ni otras dependencias:

```python
import time
import httpx

def obtener_productos_caros(token: str) -> list[dict]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    max_intentos = 3
    timeout = 10.0   # segundos (aplica a connect/read/write/pool)
    delay_base = 1.0 # segundos

    # El Client reutiliza el pool de conexiones entre reintentos
    with httpx.Client(timeout=timeout) as client:
        for intento in range(max_intentos):
            try:
                resp = client.get(url, headers=headers)
                resp.raise_for_status()

                datos = resp.json()
                # Soporta tanto `[...]` como `{"products": [...]}`
                productos = datos if isinstance(datos, list) else datos.get("products", [])

                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in productos
                    if isinstance(p.get("price"), (int, float)) and p["price"] > 100
                ]

            except (httpx.RequestError, httpx.HTTPStatusError) as exc:
                # Un 401/403/404 no se arregla reintentando → se propaga ya
                if isinstance(exc, httpx.HTTPStatusError) and exc.response.status_code < 500:
                    raise

                # Último intento: fallamos de forma explícita
                if intento == max_intentos - 1:
                    raise RuntimeError(
                        f"Fallo definitivo tras {max_intentos} intentos: {exc}"
                    ) from exc

                # Backoff exponencial: 1s → 2s (3 intentos = 2 esperas)
                time.sleep(delay_base * (2 ** intento))

    return []  # Inalcanzable, pero satisface al type checker
```

### Detalles de diseño

| Requisito | Cómo se resuelve |
|---|---|
| **Bearer + GET** | `headers={"Authorization": f"Bearer {token}"}` en `client.get`. |
| **Timeout 10s** | `httpx.Client(timeout=10.0)` cubre `ConnectTimeout`, `ReadTimeout`, etc. |
| **Errores de red** | `httpx.RequestError` es la clase base de `ConnectError`, `NetworkError` y todos los timeouts. |
| **Retry ×3 + backoff** | `range(3)` con `time.sleep(1 * 2**intento)` → esperas de **1s** y **2s**. Sin librerías extra. |
| **Filtro + proyección** | List comprehension que valida el tipo de `price` (evita `TypeError` si viene como string) y devuelve solo las 3 claves pedidas. |
| **Robustez extra** | `raise_for_status()` reintenta solo **5xx**; un token inválido (401) falla rápido en vez de gastar 3 intentos. |

> **Nota:** asumí que el JSON puede venir como array directo o envuelto en `{"products": [...]}`. Si tu API usa otra clave (p. ej. `data`), basta con cambiar esa línea. Si prefieres que, en vez de lanzar `RuntimeError`, devuelva `[]` al agotar los reintentos, sustituye el `raise` final por `return []`.