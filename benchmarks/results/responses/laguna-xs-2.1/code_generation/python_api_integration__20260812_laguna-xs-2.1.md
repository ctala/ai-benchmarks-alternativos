# Poolside Laguna XS 2.1 — code_generation/python_api_integration

- model_id: `poolside/laguna-xs-2.1`
- success: True  | final: 9.14 | quality: 10.0
- latency_total: 23.715s | tokens_per_second: 193.4
- input_tokens: 126 | output_tokens: 4586
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, cubriendo todos los requisitos con implementaciones adecuadas y manejo de errores.

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

Aquí tienes la función que cumple con todos los requisitos:

```python
import httpx
import time
from typing import List, Dict, Any

def fetch_products(token: str) -> List[Dict[str, Any]]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    for attempt in range(3):
        try:
            response = httpx.get(url, headers=headers, timeout=10.0)
            response.raise_for_status()
            products = response.json()
            
            # Filtrar productos con precio > 100 y seleccionar campos requeridos
            return [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if p["price"] > 100
            ]
        except (httpx.TimeoutException, httpx.NetworkError) as e:
            if attempt < 2:
                wait_time = 2 ** attempt  # Backoff exponencial: 1, 2, 4 segundos
                time.sleep(wait_time)
            else:
                return []  # Retorna lista vacía si fallan todos los intentos
    
    return []  # Caso por si el bucle no se ejecuta (teóricamente imposible)
```

**Características implementadas:**

1. **Autenticación Bearer Token:** Se incluye en el header `Authorization`
2. **Timeout de 10 segundos:** Configurado en el cliente HTTP
3. **Filtro de productos:** Solo incluye aquellos con `price > 100`
4. **Estructura de retorno:** Lista de diccionarios con `{id, name, price}`
5. **Manejo de errores:** 
   - Captura `TimeoutException` y `NetworkError`
   - Implementa retry con backoff exponencial (1s, 2s, 4s)
   - Máximo 3 intentos
6. **Sin dependencias externas:** Solo usa `httpx` y módulos estándar de Python

**Ejemplo de uso:**
```python
products = fetch_products("mi_token_secreto")
print(products)
# Salida: [{'id': 1, 'name': 'Producto A', 'price': 150}, ...]
```