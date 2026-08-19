# DeepSeek V3 — code_generation/python_api_integration

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 8.87 | quality: 9.72
- latency_total: 15.155s | tokens_per_second: 71.3
- input_tokens: 116 | output_tokens: 1081
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import httpx
import time
from typing import List, Dict, Optional

def fetch_products_with_retry(
    token: str,
    timeout: int = 10,
    max_retries: int = 3
) -> List[Dict[str, any]]:
    """
    Obtiene productos de la API, filtra por precio > 100 y retorna datos específicos.
    
    Args:
        token: Token de autenticación Bearer
        timeout: Tiempo máximo de espera en segundos (default: 10)
        max_retries: Número máximo de reintentos (default: 3)
    
    Returns:
        Lista de diccionarios con {id, name, price} de productos con precio > 100
    
    Raises:
        httpx.RequestError: Si fallan todos los reintentos
    """
    
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    # Configuración de reintento con backoff exponencial
    base_delay = 1  # segundos
    last_exception = None
    
    for attempt in range(max_retries):
        try:
            # Intento de conexión
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza excepción para códigos 4xx/5xx
                
                # Procesar respuesta
                products = response.json()
                
                # Filtrar y transformar datos
                filtered_products = []
                for product in products:
                    # Verificar que tenga los campos necesarios
                    if all(key in product for key in ['id', 'name', 'price']):
                        try:
                            price = float(product['price'])
                            if price > 100:
                                filtered_products.append({
                                    'id': product['id'],
                                    'name': product['name'],
                                    'price': price
                                })
                        except (ValueError, TypeError):
                            # Saltar productos con precio inválido
                            continue
                
                return filtered_products
                
        except (httpx.RequestError, httpx.HTTPStatusError) as e:
            last_exception = e
            
            # Si no es el último intento, esperar y reintentar
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt)  # Backoff exponencial
                print(f"Intento {attempt + 1} falló. Reintentando en {delay} segundos...")
                time.sleep(delay)
            else:
                print(f"Todos los {max_retries} intentos fallaron.")
                raise
    
    # Nunca debería llegar aquí, pero por seguridad
    raise last_exception or httpx.RequestError("Error desconocido")


# Ejemplo de uso:
def main():
    # Token de ejemplo - reemplazar con token real
    token = "tu_token_aqui"
    
    try:
        products = fetch_products_with_retry(token)
        print(f"Productos encontrados: {len(products)}")
        for product in products:
            print(f"ID: {product['id']}, Nombre: {product['name']}, Precio: ${product['price']:.2f}")
            
    except httpx.RequestError as e:
        print(f"Error al obtener productos: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
```

**Características implementadas:**

1. **Autenticación Bearer**: Incluye el token en los headers
2. **Filtro de precio**: Solo productos con precio > 100
3. **Estructura de datos**: Retorna lista de dicts con solo {id, name, price}
4. **Manejo de errores**:
   - Timeout configurable (10 segundos por defecto)
   - Errores de red (RequestError)
   - Errores HTTP (HTTPStatusError)
   - Validación de tipos de datos
5. **Retry con backoff exponencial**:
   - 3 intentos máximo
   - Delays: 1s, 2s, 4s (exponencial)
   - Solo reintenta en errores de red/HTTP
6. **Validaciones adicionales**:
   - Verifica que los productos tengan los campos requeridos
   - Convierte precio a float para comparación
   - Maneja precios inválidos silenciosamente

**Uso:**
```python
# Llamada básica
products = fetch_products_with_retry("mi_token")

# Con timeout personalizado
products = fetch_products_with_retry("mi_token", timeout=15)

# Con diferente número de reintentos
products = fetch_products_with_retry("mi_token", max_retries=5)
```