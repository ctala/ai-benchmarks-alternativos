# Step 3.5 Flash — code_generation/python_api_integration

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 8.65 | quality: 9.48
- latency_total: 25.53s | tokens_per_second: 64.2
- input_tokens: 118 | output_tokens: 1639
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

Aquí tienes la función implementada con `httpx`:

```python
import httpx
import time
from typing import List, Dict

def fetch_filtered_products(token: str) -> List[Dict[str, float]]:
    """
    Obtiene productos con precio > 100 usando autenticación Bearer.
    
    Args:
        token: Token de autenticación Bearer
        
    Returns:
        Lista de diccionarios con {id, name, price}
        
    Raises:
        httpx.RequestError: Si fallan todos los reintentos
        ValueError: Si la respuesta no tiene el formato esperado
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    base_delay = 1  # segundos
    
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                
                products = response.json()
                if not isinstance(products, list):
                    raise ValueError("La respuesta no es una lista de productos")
                
                filtered = []
                for p in products:
                    try:
                        price = float(p.get("price", 0))
                        if price > 100:
                            filtered.append({
                                "id": p["id"],
                                "name": p["name"],
                                "price": price
                            })
                    except (KeyError, TypeError, ValueError):
                        # Ignorar productos con datos inválidos
                        continue
                
                return filtered
                
        except (httpx.RequestError, httpx.TimeoutException) as e:
            if attempt == max_retries - 1:
                raise
            
            # Backoff exponencial: 1, 2, 4 segundos
            delay = base_delay * (2 ** attempt)
            time.sleep(delay)
    
    # Este punto no debería reacharse
    raise httpx.RequestError("Se agotaron los reintentos sin éxito")


# Ejemplo de uso:
if __name__ == "__main__":
    try:
        token = "tu_token_aqui"
        result = fetch_filtered_products(token)
        print(f"Productos encontrados: {len(result)}")
        for p in result[:3]:  # Mostrar primeros 3
            print(f"  - {p['name']}: ${p['price']}")
    except Exception as e:
        print(f"Error: {e}")
```

### Características clave:

1. **Autenticación Bearer**: Token pasado en header `Authorization`
2. **Filtrado**: Solo productos con `price > 100`
3. **Estructura de salida**: Lista de diccionarios con solo `{id, name, price}`
4. **Manejo de errores**:
   - `httpx.RequestError` y `httpx.TimeoutException` (timeout de 10s configurado en el cliente)
   - Reintentos con backoff exponencial (1s, 2s, 4s)
   - Máximo 3 intentos
5. **Robustez**:
   - Validación de que la respuesta es una lista
   - Manejo de productos con datos inválidos (los ignora silenciosamente)
   - `response.raise_for_status()` para códigos HTTP no exitosos

### Notas:

- La función asume que la API devuelve una lista de objetos JSON con campos `id`, `name` y `price`.
- Los productos con `price` no numérico o faltante se descartan.
- Solo se reintenta en errores de red/timeout, no en errores HTTP 4xx/5xx (que se propagan inmediatamente).
- Usa `httpx.Client` como context manager para cerrar conexiones automáticamente.

### Instalación requerida:
```bash
pip install httpx
```

Esta implementación es completamente autocontenida y no requiere dependencias externas adicionales a `httpx`.