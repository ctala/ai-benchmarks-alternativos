# KAT Coder Pro v2.5 — code_generation/python_api_integration

- model_id: `kwaipilot/kat-coder-pro-v2.5`
- success: True  | final: 7.94 | quality: 9.08
- latency_total: 16.042s | tokens_per_second: 92.9
- input_tokens: 113 | output_tokens: 1491
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



<!DOCTYPE python>
def fetch_filtered_products(token: str) -> list[dict]:
    """
    Obtiene productos de la API, filtra por precio > 100 y retorna
    una lista de diccionarios con id, name y price.
    Maneja errores de red con reintentos y backoff exponencial.
    """
    import httpx
    import time
    from typing import List, Dict

    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    base_delay = 1  # segundos

    for attempt in range(max_retries):
        try:
            with httpx.Client() as client:
                response = client.get(url, headers=headers, timeout=10.0)
                response.raise_for_status()
                data = response.json()

                # Soporta respuesta como lista directa o bajo clave 'products'
                if isinstance(data, dict) and "products" in data:
                    products = data["products"]
                elif isinstance(data, list):
                    products = data
                else:
                    products = []

                filtered = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if isinstance(p.get("price"), (int, float)) and p["price"] > 100
                ]
                return filtered

        except (httpx.RequestError, httpx.TimeoutException, httpx.HTTPStatusError, KeyError, TypeError) as e:
            if attempt == max_retries - 1:
                raise RuntimeError(f"Failed after {max_retries} attempts: {e}")
            delay = base_delay * (2 ** attempt)
            time.sleep(delay)

    return []