# Nemotron Nano 9B v2 — code_generation/python_api_integration

- model_id: `nvidia/nemotron-nano-9b-v2:free`
- success: True  | final: 8.83 | quality: 9.72
- latency_total: 157.259s | tokens_per_second: 33.7
- input_tokens: 114 | output_tokens: 5305
- judge_score: 4.8 | justificación: 

## Respuesta completa



Aquí tienes la implementación de la función en Python que cumple con todos los requisitos especificados:

```python
import httpx
import time

def get_expensive_products(bearer_token):
    """
    Obtiene productos con precio > 100 de una API con autenticación Bearer.
    
    Args:
        bearer_token (str): Token de autenticación Bearer
    
    Returns:
        list: Lista de diccionarios con {id, name, price} de productos filtrados
    """
    for attempt in range(3):
        try:
            response = httpx.get(
                'https://api.example.com/products',
                headers={'Authorization': f'Bearer {bearer_token}'},
                timeout=10
            )
            response.raise_for_status()  # Lanza error para códigos 4xx/5xx
            
            products = response.json()
            filtered_products = [
                {'id': p['id'], 'name': p['name'], 'price': p['price']}
                for p in products
                if p.get('price', 0) > 100
            ]
            return filtered_products
            
        except (httpx.TimeoutException, httpx.ConnectError) as e:
            # Reintento con backoff exponencial
            wait_time = 2 ** attempt
            time.sleep(wait_time)
            
        except httpx.HTTPStatusError as e:
            # Error HTTP no retryable (ej: token inválido)
            return []
            
    # Si todos los reintentos fallan
    return []
```

### Características principales:

1. **Autenticación Bearer**: Se incluye el token en el encabezado `Authorization` usando el formato `Bearer <token>`.

2. **Filtrado de productos**: Solo se devuelven productos con precio mayor a 100, extraiendo solo los campos `id`, `name` y `price`.

3. **Manejo de errores**:
   - **Timeout**: Se maneja con `timeout=10` y se captura `TimeoutException`.
   - **Errores de conexión**: Se captura `ConnectError`.
   - **Errores HTTP**: Se captura `HTTPStatusError` y se retorna una lista vacía sin reintentar.

4. **Retry con backoff exponencial**:
   - Máximo 3 intentos.
   - Espera 1, 2 y 4 segundos entre reintentos (2^0, 2^1, 2^2).

5. **No dependencias externas**: Solo usa `httpx` (librería estándar) y `time` (módulo estándar de Python).

### Uso ejemplo:

```python
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxxxx"
result = get_expensive_products(token)
print(result)
```

### Notas:
- Si el token es inválido (respuesta 401/403), se retorna una lista vacía en el primer intento.
- Si hay errores de red/timeout, se realizan hasta 3 intentos con backoff.
- Si no hay productos con precio > 100, se retorna una lista vacía.
