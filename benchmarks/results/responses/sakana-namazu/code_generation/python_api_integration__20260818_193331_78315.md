# Sakana Namazu — code_generation/python_api_integration

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.33 | quality: 9.52
- latency_total: 7.173s | tokens_per_second: 312.3
- input_tokens: 190 | output_tokens: 2240
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

Aquí tienes una función completa usando solo `httpx` (incluido en la biblioteca estándar de algunos entornos, pero es el único requerimiento externo indicado):

```python
import time
import httpx

def get_expensive_products(token: str):
    """
    Obtiene productos con precio > 100 desde https://api.example.com/products.
    
    Args:
        token: Bearer token para autenticación.
        
    Returns:
        Lista de diccionarios con {id, name, price}. Lista vacía si falla todo.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    timeout = 10.0

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout, headers=headers) as client:
                response = client.get(url)
                response.raise_for_status()  # Lanza HTTPStatusError en 4xx/5xx
                data = response.json()

                # Normalizamos respuesta (lista directa o envuelta en dict)
                if isinstance(data, list):
                    products = data
                elif isinstance(data, dict):
                    products = data.get("products") or data.get("data") or []
                else:
                    products = []

                # Filtrar por precio > 100 y proyectar solo los campos requeridos
                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if isinstance(p, dict) and p.get("price", 0) > 100
                ]

        except (
            httpx.TimeoutException,
            httpx.NetworkError,
            httpx.ConnectError,
            httpx.HTTPStatusError,
        ) as exc:
            if attempt == max_retries - 1:
                print(f"Fallo permanente tras {max_retries} intentos: {exc}")
                return []
            # Backoff exponencial: 1s, 2s, 4s
            backoff = 2 ** attempt
            time.sleep(backoff)

        except Exception as exc:
            # Errores inesperados (JSON inválido, estructura inesperada, etc.)
            print(f"Error inesperado: {exc}")
            return []

    return []
```

### ¿Qué cumple esta función?

| Requisito | Implementación |
|-----------|----------------|
| **GET con Bearer** | Headers `Authorization: Bearer <token>` |
| **Filtrar `price > 100`** | Comprensión de lista con `if p.get("price", 0) > 100` |
| **Retorno estricto** | Solo devuelve `{"id", "name", "price"}` |
| **Timeout 10 s** | `timeout=10.0` en el cliente |
| **Retry ×3 con backoff** | Bucle `range(3)` + `time.sleep(2 ** attempt)` (1s, 2s, 4s) |
| **Manejo de red/timeout** | Captura `TimeoutException`, `NetworkError`, `ConnectError`, `HTTPStatusError` |

### Uso

```python
products = get_expensive_products(token="tu_token_aqui")
print(products)
# Salida esperada: [{'id': 1, 'name': 'Premium Widget', 'price': 150.0}, ...]
```