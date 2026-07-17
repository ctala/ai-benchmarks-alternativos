# DeepSeek V4 Pro — code_generation/python_api_integration

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 8.04 | quality: 9.08
- latency_total: 44.117s | tokens_per_second: 67.5
- input_tokens: 110 | output_tokens: 2980
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import httpx
from time import sleep

def fetch_expensive_products(token: str) -> list[dict]:
    """
    Obtiene productos desde la API, filtra aquellos con precio > 100 y retorna
    una lista de diccionarios con {id, name, price}.

    Maneja errores de red y timeouts (10 s), reintentando hasta 3 veces
    con backoff exponencial.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_attempts = 3
    timeout = 10.0

    with httpx.Client(timeout=timeout) as client:
        for attempt in range(max_attempts):
            try:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza HTTPStatusError si 4xx/5xx

                data = response.json()
                if not isinstance(data, list):
                    raise ValueError("Respuesta inesperada: se esperaba una lista")

                # Filtrar y extraer solo campos requeridos
                result = []
                for product in data:
                    if not isinstance(product, dict):
                        continue
                    if not all(k in product for k in ("id", "name", "price")):
                        continue
                    if product["price"] > 100:
                        result.append({
                            "id": product["id"],
                            "name": product["name"],
                            "price": product["price"]
                        })
                return result

            except httpx.RequestError as exc:
                # Errores de red, timeout, DNS, etc.
                if attempt == max_attempts - 1:
                    raise
                # else: continuar al reintento

            except httpx.HTTPStatusError as exc:
                if exc.response.status_code >= 500:
                    # Error del servidor (5xx) -> reintentable
                    if attempt == max_attempts - 1:
                        raise
                    # else: continuar al reintento
                else:
                    # Error del cliente (4xx) -> no reintentar
                    raise

            # Backoff exponencial antes del siguiente intento
            if attempt < max_attempts - 1:
                wait = 2 ** attempt   # 1, 2, 4 segundos
                print(f"Intento {attempt + 1} fallido, reintentando en {wait}s...")
                sleep(wait)

    # Por seguridad, nunca debería llegar aquí
    raise RuntimeError("Se excedió el número máximo de reintentos")
```