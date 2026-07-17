# Mistral Small 4 — code_generation/python_api_integration

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 9.22 | quality: 9.72
- latency_total: 3.848s | tokens_per_second: 174.9
- input_tokens: 117 | output_tokens: 673
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes una función Python que cumple con todos los requisitos usando `httpx` para las peticiones HTTP y manejo de errores con retry con backoff exponencial:

```python
import httpx
import time
from typing import List, Dict, Optional

def get_expensive_products() -> Optional[List[Dict[str, str]]]:
    """
    Obtiene productos con precio > 100 desde la API, aplicando autenticación Bearer token,
    con manejo de errores de red, timeout y retry con backoff exponencial (max 3 intentos).

    Retorna:
        Lista de dicts con {id, name, price} para productos > 100, o None si falla.
    """
    url = "https://api.example.com/products"
    bearer_token = "tu_token_aqui"  # Reemplaza con tu token real
    timeout = 10.0
    max_retries = 3
    retry_delay = 1.0  # Tiempo inicial en segundos

    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/json"
    }

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza excepción si status es 4xx/5xx

                products = response.json()
                expensive_products = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if float(p.get("price", 0)) > 100
                ]

                return expensive_products

        except (httpx.RequestError, httpx.HTTPStatusError) as e:
            if attempt == max_retries - 1:
                print(f"Error después de {max_retries} intentos: {str(e)}")
                return None

            print(f"Intento {attempt + 1} falló: {str(e)}. Reintentando en {retry_delay}s...")
            time.sleep(retry_delay)
            retry_delay *= 2  # Backoff exponencial

    return None
```

### Características clave:
1. **Autenticación Bearer**: Incluye el token en los headers
2. **Filtrado**: Solo productos con precio > 100
3. **Formato de salida**: Lista de dicts con solo `{id, name, price}`
4. **Manejo de errores**:
   - Timeout de 10 segundos
   - Captura errores de red (`RequestError`) y HTTP (`HTTPStatusError`)
5. **Retry con backoff exponencial**:
   - Máximo 3 intentos
   - Tiempo de espera inicial de 1s, duplicándose en cada retry (1s, 2s, 4s)
6. **Sin dependencias externas**: Solo usa `httpx` estándar

### Uso:
```python
products = get_expensive_products()
if products is not None:
    print(products)
else:
    print("No se pudieron obtener los productos")
```