# Qwen3-Coder-Next (OpenRouter FP8) — code_generation/python_api_integration

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 8.09 | quality: 9.52
- latency_total: 5.245s | tokens_per_second: 139.2
- input_tokens: 112 | output_tokens: 730
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes una función Python que cumple con todos los requisitos usando `httpx`, sin dependencias externas adicionales:

```python
import httpx
import time
from typing import List, Dict, Any


def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos cuyo precio > 100 desde la API, con autenticación Bearer.
    
    Args:
        token (str): Token Bearer para autenticación.
    
    Returns:
        List[Dict[str, Any]]: Lista de productos filtrados con 'id', 'name' y 'price'.
    
    Raises:
        httpx.HTTPError: Si fallan todos los reintentos o hay error de red/HTTP.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    max_retries = 3
    base_delay = 1.0  # segundos
    
    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=httpx.Timeout(10.0)) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                products = response.json()
                
                # Filtrar productos con precio > 100 y extraer campos necesarios
                result = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if isinstance(p, dict) and p.get("price", 0) > 100
                ]
                return result
                
        except (httpx.TimeoutException, httpx.NetworkError, httpx.HTTPStatusError) as e:
            if attempt == max_retries:
                # Último intento fallido: relanzar excepción
                raise e
            # Esperar con backoff exponencial antes de reintentar
            delay = base_delay * (2 ** (attempt - 1))
            time.sleep(delay)
    
    # Nunca debería llegar aquí, pero por seguridad
    raise httpx.HTTPError("Error inesperado durante los intentos")
```

### Notas importantes:
- ✅ Usa `httpx` con timeout de 10 segundos (`httpx.Timeout(10.0)`).
- ✅ Autenticación `Bearer` mediante cabecera `Authorization`.
- ✅ Filtra productos con `price > 100` (incluye comprobación segura con `get()` para evitar KeyError).
- ✅ Devuelve lista de dicts con solo `id`, `name`, `price`.
- ✅ Maneja errores de red (`NetworkError`), timeout (`TimeoutException`) y errores HTTP (`HTTPStatusError`).
- ✅ Retry con **backoff exponencial**: 1s → 2s (2¹⁻¹ y 2²⁻¹), total 2 intentos extras tras el primero → 3 intentos en total.
- ✅ No usa dependencias externas adicionales (solo `httpx`, `time`, `typing` — este último es estándar).

> ⚠️ Asegúrate de instalar `httpx` si aún no lo tienes:
> ```bash
> pip install httpx
> ```

¿Te gustaría que también incluyera logging o que devolviera `None` en lugar de lanzar excepciones?