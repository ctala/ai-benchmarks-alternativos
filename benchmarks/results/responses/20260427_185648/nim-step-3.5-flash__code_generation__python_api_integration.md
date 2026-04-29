# Step 3.5 Flash (NIM) — code_generation/python_api_integration

- model_id: `stepfun-ai/step-3.5-flash`
- success: True  | final: 7.6 | quality: 9.72
- latency_total: 41.407s | tokens_per_second: 31.3
- input_tokens: 118 | output_tokens: 1295
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes una función Python que cumple con todos los requisitos usando solo `httpx`:

```python
import httpx
from typing import List, Dict
import time

def fetch_filtered_products(
    bearer_token: str,
    url: str = "https://api.example.com/products",
    timeout: float = 10.0,
    max_retries: int = 3
) -> List[Dict[str, float]]:
    """
    Obtiene productos desde una API, filtra por precio > 100 y retorna lista simplificada.
    
    Args:
        bearer_token: Token de autenticación Bearer
        url: URL de la API (por defecto la especificada)
        timeout: Timeout en segundos (por defecto 10)
        max_retries: Número máximo de reintentos (por defecto 3)
    
    Returns:
        Lista de diccionarios con claves: id, name, price
    
    Raises:
        httpx.RequestError: Si fallan todos los reintentos
    """
    headers = {"Authorization": f"Bearer {bearer_token}"}
    
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza error para códigos 4xx/5xx
                
                products = response.json()
                
                # Filtrar y mapear productos
                filtered = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if p.get("price", 0) > 100
                ]
                
                return filtered
                
        except (httpx.RequestError, httpx.TimeoutException) as e:
            if attempt == max_retries - 1:
                raise  # Reintentos agotados
            
            # Backoff exponencial: 2^attempt segundos (1, 2, 4...)
            backoff = 2 ** attempt
            time.sleep(backoff)
    
    return []  # No debería llegar aquí, pero por seguridad


# Ejemplo de uso:
if __name__ == "__main__":
    try:
        token = "tu_token_aqui"
        result = fetch_filtered_products(token)
        print(f"Productos encontrados: {len(result)}")
        for product in result[:3]:  # Muestra los primeros 3
            print(product)
    except httpx.RequestError as e:
        print(f"Error después de reintentos: {e}")
```

### Características principales:

1. **Autenticación Bearer**: Incluye el token en el encabezado `Authorization`.
2. **Filtrado de precio**: Solo incluye productos con `price > 100`.
3. **Estructura simplificada**: Retorna solo `{id, name, price}`.
4. **Manejo de errores**: Captura errores de red y timeouts.
5. **Retry con backoff exponencial**:
   - Intentos: 1, 2, 4 segundos de espera entre reintentos
   - Máximo 3 intentos (configurable)
6. **Sin dependencias externas**: Solo usa `httpx` (instalable via `pip install httpx`).

### Notas importantes:

- **Validación de datos**: Usa `p.get("price", 0)` para evitar `KeyError` si falta el campo.
- **Timeouts**: Configurable mediante el parámetro `timeout`.
- **Códigos HTTP**: `raise_for_status()` maneja errores 4xx/5xx.
- **Tipo de retorno**: Especificado con `List[Dict[str, float]]` (ajusta `float` si `price` es otro tipo).
- **Thread-safe**: Cada llamada crea su propio `httpx.Client`.

### Instalación:
```bash
pip install httpx
```

### Posibles mejoras (según necesidades):
- Agregar logging de reintentos.
- Soportar paginación si la API la requiere.
- Validar tipos de datos más estrictamente.
- Parámetro para personalizar la condición de filtrado (ej: `min_price`).