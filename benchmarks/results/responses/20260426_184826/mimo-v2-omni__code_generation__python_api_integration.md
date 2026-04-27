# MiMo-V2-Omni (multimodal) — code_generation/python_api_integration

- model_id: `xiaomi/mimo-v2-omni`
- success: True  | final: 7.51 | quality: 8.88
- latency_total: 15.254s | tokens_per_second: 116.4
- input_tokens: 354 | output_tokens: 1775
- judge_score: 4.2 | justificación: 

## Respuesta completa

```python
import httpx
from typing import List, Dict, Optional
import time

def fetch_products(token: str, base_url: str = "https://api.example.com/products") -> List[Dict]:
    """
    Obtiene productos de la API, filtra los que tienen precio > 100 y retorna
    una lista simplificada con id, name y price.
    
    Args:
        token: Token de autenticación Bearer
        base_url: URL base de la API (opcional)
    
    Returns:
        Lista de diccionarios con productos filtrados
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    
    max_retries = 3
    timeout = httpx.Timeout(10.0)  # Timeout de 10 segundos
    
    for attempt in range(max_retries):
        try:
            # Realizar petición GET
            with httpx.Client(timeout=timeout) as client:
                response = client.get(base_url, headers=headers)
                response.raise_for_status()  # Lanza excepción para códigos 4xx/5xx
                
                # Procesar respuesta
                products = response.json()
                
                # Filtrar productos con precio > 100 y extraer campos requeridos
                filtered_products = []
                for product in products:
                    if product.get("price", 0) > 100:
                        filtered_products.append({
                            "id": product.get("id"),
                            "name": product.get("name"),
                            "price": product.get("price")
                        })
                
                return filtered_products
                
        except httpx.TimeoutException:
            print(f"Timeout en intento {attempt + 1}/{max_retries}")
            if attempt < max_retries - 1:
                # Backoff exponencial: 2^attempt segundos (1, 2, 4)
                wait_time = 2 ** attempt
                print(f"Reintentando en {wait_time} segundos...")
                time.sleep(wait_time)
            else:
                print("Se agotaron los reintentos por timeout")
                return []
                
        except httpx.HTTPStatusError as e:
            print(f"Error HTTP {e.response.status_code}: {e.response.text}")
            return []
            
        except httpx.RequestError as e:
            print(f"Error de conexión en intento {attempt + 1}/{max_retries}: {e}")
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                print(f"Reintentando en {wait_time} segundos...")
                time.sleep(wait_time)
            else:
                print("Se agotaron los reintentos por error de conexión")
                return []
                
        except Exception as e:
            print(f"Error inesperado: {e}")
            return []
    
    return []

# Ejemplo de uso:
if __name__ == "__main__":
    TOKEN = "tu_token_aquí"
    productos = fetch_products(TOKEN)
    print(f"Productos encontrados: {len(productos)}")
    for producto in productos:
        print(f"  - {producto['name']}: ${producto['price']}")
```

**Características implementadas:**

1. **Autenticación Bearer**: Usa el token en el header de autorización
2. **Filtrado**: Solo incluye productos con `price > 100`
3. **Estructura de respuesta**: Retorna `{id, name, price}` como diccionarios
4. **Manejo de errores**:
   - Timeout de 10 segundos configurado
   - Captura específica de `TimeoutException` y `RequestError`
   - Manejo de errores HTTP (4xx, 5xx)
   - Manejo de excepciones inesperadas
5. **Retry con backoff exponencial**:
   - Máximo 3 intentos
   - Espera de 2^attempt segundos (1s, 2s, 4s)
   - Solo reintenta en errores de red/timeout

**Nota**: Para usar esta función, necesitarás instalar `httpx`:
```bash
pip install httpx
```

La función es robusta y maneja los casos de error comunes mientras mantiene un código limpio y bien estructurado.