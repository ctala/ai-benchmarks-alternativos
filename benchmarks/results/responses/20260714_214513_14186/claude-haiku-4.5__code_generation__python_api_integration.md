# Claude Haiku 4.5 — code_generation/python_api_integration

- model_id: `anthropic/claude-haiku-4.5`
- success: True  | final: 8.13 | quality: 9.24
- latency_total: 9.504s | tokens_per_second: 195.5
- input_tokens: 123 | output_tokens: 1858
- judge_score: 4.6 | justificación: 

## Respuesta completa

```python
import httpx
import time
from typing import List, Dict, Optional
import random


def get_filtered_products(
    bearer_token: str,
    min_price: float = 100,
    max_retries: int = 3,
    timeout: float = 10.0
) -> List[Dict[str, any]]:
    """
    Obtiene productos de la API, filtra por precio y retorna lista simplificada.
    
    Args:
        bearer_token: Token Bearer para autenticación
        min_price: Precio mínimo para filtrar (default: 100)
        max_retries: Número máximo de intentos (default: 3)
        timeout: Timeout en segundos (default: 10)
    
    Returns:
        Lista de dicts con {id, name, price} para productos con precio > min_price
    
    Raises:
        httpx.HTTPError: Si falla después de todos los reintentos
        ValueError: Si el token está vacío
    """
    
    if not bearer_token:
        raise ValueError("Bearer token no puede estar vacío")
    
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    
    last_exception = None
    
    for attempt in range(max_retries):
        try:
            # Calcular backoff exponencial con jitter
            if attempt > 0:
                wait_time = (2 ** attempt) + random.uniform(0, 1)
                print(f"Intento {attempt + 1}/{max_retries}. Esperando {wait_time:.2f}s...")
                time.sleep(wait_time)
            
            print(f"Intentando GET a {url} (intento {attempt + 1}/{max_retries})...")
            
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza HTTPStatusError si status >= 400
            
            # Procesar respuesta exitosa
            data = response.json()
            
            # Validar que data sea una lista
            if not isinstance(data, list):
                raise ValueError(f"Respuesta esperada como lista, recibido: {type(data)}")
            
            # Filtrar y mapear productos
            filtered_products = [
                {
                    "id": product.get("id"),
                    "name": product.get("name"),
                    "price": product.get("price")
                }
                for product in data
                if isinstance(product, dict) 
                and product.get("price") is not None
                and float(product.get("price", 0)) > min_price
            ]
            
            print(f"✓ Éxito: {len(filtered_products)} productos encontrados")
            return filtered_products
        
        except httpx.TimeoutException as e:
            last_exception = e
            print(f"✗ Timeout en intento {attempt + 1}: {e}")
        
        except httpx.ConnectError as e:
            last_exception = e
            print(f"✗ Error de conexión en intento {attempt + 1}: {e}")
        
        except httpx.NetworkError as e:
            last_exception = e
            print(f"✗ Error de red en intento {attempt + 1}: {e}")
        
        except httpx.HTTPStatusError as e:
            # No reintentar si es error del cliente (4xx)
            if 400 <= e.response.status_code < 500:
                print(f"✗ Error HTTP {e.response.status_code}: {e}")
                raise
            
            last_exception = e
            print(f"✗ Error HTTP {e.response.status_code} en intento {attempt + 1}")
        
        except httpx.HTTPError as e:
            last_exception = e
            print(f"✗ Error HTTP en intento {attempt + 1}: {e}")
        
        except (ValueError, KeyError, TypeError) as e:
            print(f"✗ Error al procesar respuesta: {e}")
            raise
    
    # Si llegamos aquí, todos los reintentos fallaron
    print(f"\n✗ Falló después de {max_retries} intentos")
    raise httpx.HTTPError(
        f"No se pudo conectar a {url} después de {max_retries} intentos. "
        f"Último error: {last_exception}"
    )


# Ejemplo de uso
if __name__ == "__main__":
    # NOTA: Reemplazar con token válido
    TOKEN = "tu_bearer_token_aqui"
    
    try:
        products = get_filtered_products(
            bearer_token=TOKEN,
            min_price=100,
            max_retries=3,
            timeout=10.0
        )
        
        print("\nProductos filtrados:")
        for product in products:
            print(f"  - ID: {product['id']}, "
                  f"Nombre: {product['name']}, "
                  f"Precio: ${product['price']}")
    
    except ValueError as e:
        print(f"Error de validación: {e}")
    except httpx.HTTPError as e:
        print(f"Error HTTP: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
```

## Características principales:

### ✅ **Autenticación Bearer**
```python
headers = {
    "Authorization": f"Bearer {bearer_token}",
}
```

### ✅ **Filtrado de productos**
```python
if float(product.get("price", 0)) > min_price
```

### ✅ **Manejo de errores específicos**
- `TimeoutException`: Timeout después de 10s
- `ConnectError`: Errores de conexión
- `NetworkError`: Errores de red
- `HTTPStatusError`: Errores HTTP (reintenta 5xx, no 4xx)

### ✅ **Retry con backoff exponencial**
```python
wait_time = (2 ** attempt) + random.uniform(0, 1)
# Intento 1: ~1s
# Intento 2: ~2-3s  
# Intento 3: ~4-5s
```

### ✅ **Sin dependencias externas**
Solo usa `httpx` (ya especificado)

## Instalación:
```bash
pip install httpx
```

## Ejemplo con mock para testing:
```python
import httpx
from unittest.mock import patch

@patch('httpx.Client.get')
def test_get_filtered_products(mock_get):
    mock_response = httpx.Response(
        200,
        json=[
            {"id": 1, "name": "Producto A", "price": 150},
            {"id": 2, "name": "Producto B", "price": 50},
            {"id": 3, "name": "Producto C", "price": 200},
        ]
    )
    mock_get.return_value = mock_response
    
    result = get_filtered_products("token123")
    assert len(result) == 2  # Solo A y C
    assert result[0]["price"] == 150
```