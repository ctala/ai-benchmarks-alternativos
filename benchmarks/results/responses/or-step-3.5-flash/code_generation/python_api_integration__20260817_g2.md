# Step 3.5 Flash — code_generation/python_api_integration

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 8.35 | quality: 9.12
- latency_total: 37.859s | tokens_per_second: 54.1
- input_tokens: 118 | output_tokens: 2048
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
from typing import List, Dict

def fetch_filtered_products(token: str) -> List[Dict[str, float]]:
    """
    Obtiene productos de la API, filtra por precio > 100 y retorna {id, name, price}.
    Implementa retry con backoff exponencial (max 3 intentos) y maneja errores de red/timeout.
    
    Args:
        token: Bearer token para autenticación.
        
    Returns:
        Lista de diccionarios con claves 'id', 'name', 'price'.
        
    Raises:
        httpx.RequestError: Si fallan todos los reintentos.
        ValueError: Si el formato de respuesta es inválido.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    base_delay = 1  # segundos base para backoff exponencial
    
    for attempt in range(max_retries):
        try:
            # Intento de solicitud con timeout de 10 segundos
            response = httpx.get(
                url,
                headers=headers,
                timeout=10.0
            )
            response.raise_for_status()  # Lanza error para códigos 4xx/5xx
            
            products = response.json()
            
            # Validar estructura esperada (lista de diccionarios)
            if not isinstance(products, list):
                raise ValueError("La respuesta no es una lista de productos")
            
            # Filtrar y transformar
            result = []
            for p in products:
                # Validar campos requeridos
                if not all(k in p for k in ("id", "name", "price")):
                    continue
                try:
                    price = float(p["price"])
                    if price > 100:
                        result.append({
                            "id": p["id"],
                            "name": p["name"],
                            "price": price
                        })
                except (ValueError, TypeError):
                    continue  # Ignorar productos con precio inválido
            
            return result
            
        except (httpx.RequestError, httpx.TimeoutException) as e:
            # Si es el último intento, propagar error
            if attempt == max_retries - 1:
                raise