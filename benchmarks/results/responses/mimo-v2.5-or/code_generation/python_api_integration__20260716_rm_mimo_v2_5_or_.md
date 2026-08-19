# MiMo-V2.5 (omnimodal) — code_generation/python_api_integration

- model_id: `xiaomi/mimo-v2.5`
- success: True  | final: 7.44 | quality: 8.32
- latency_total: 25.861s | tokens_per_second: 68.5
- input_tokens: 351 | output_tokens: 1772
- judge_score: 3.8 | justificación: 

## Respuesta completa

```python
import httpx
import time
from typing import List, Dict, Any

def get_products(token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos filtrados por precio mayor a 100 con manejo de errores y reintentos.
    
    Args:
        token: Token de autenticación Bearer
        
    Returns:
        Lista de diccionarios con 'id', 'name' y 'price' de productos con precio > 100
        
    Raises:
        ValueError: Si el token está vacío
        httpx.HTTPStatusError: Si hay errores HTTP después de los reintentos
        Exception: Para otros errores inesperados
    """
    if not token:
        raise ValueError("El token de autenticación no puede estar vacío")
    
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    timeout_seconds = 10
    
    for attempt in range(max_retries):
        try:
            # Realizar la petición GET con timeout
            with httpx.Client(timeout=timeout_seconds) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza HTTPStatusError para respuestas 4xx/5xx
                
                # Procesar la respuesta
                data = response.json()
                
                # Suponiendo que la respuesta tiene una clave 'products' con la lista
                # Ajustar según la estructura real de la API
                if isinstance(data, dict) and "products" in data:
                    products = data["products"]
                elif isinstance(data, list):
                    products = data
                else:
                    # Si la estructura no es la esperada, intentar procesar como lista directa
                    products = data
                
                # Filtrar productos con precio > 100 y extraer solo los campos necesarios
                filtered_products = []
                for product in products:
                    # Verificar que el producto tenga los campos necesarios
                    if all(key in product for key in ["id", "name", "price"]):
                        if product["price"] > 100:
                            filtered_products.append({
                                "id": product["id"],
                                "name": product["name"],
                                "price": product["price"]
                            })
                
                return filtered_products
                
        except httpx.TimeoutException:
            # Timeout específico
            print(f"Intento {attempt + 1} de {max_retries}: Timeout al conectar con la API")
        except httpx.HTTPStatusError as e:
            # Errores HTTP (4xx, 5xx)
            print(f"Intento {attempt + 1} de {max_retries}: Error HTTP {e.response.status_code}")
            # Si es error de autenticación (401/403), no reintentar
            if e.response.status_code in [401, 403]:
                raise
        except httpx.RequestError as e:
            # Errores de red (conexión, DNS, etc.)
            print(f"Intento {attempt + 1} de {max_retries}: Error de red: {str(e)}")
        except Exception as e:
            # Cualquier otro error inesperado
            print(f"Intento {attempt + 1} de {max_retries}: Error inesperado: {str(e)}")
            # Re-lanzar errores inesperados sin reintentar
            raise
            
        # Backoff exponencial: esperar 2^intentos segundos (1, 2, 4 segundos)
        if attempt < max_retries - 1:  # No esperar después del último intento
            wait_time = 2 ** attempt
            print(f"Esperando {wait_time} segundos antes del siguiente intento...")
            time.sleep(wait_time)
    
    # Si llegamos aquí, todos los intentos fallaron
    raise Exception(f"No se pudo obtener los productos después de {max_retries} intentos")

# Ejemplo de uso:
if __name__ == "__main__":
    try:
        # Reemplaza con tu token real
        token = "tu_token_de_autenticacion_aqui"
        products = get_products(token)
        print("Productos encontrados:")
        for product in products:
            print(f"  ID: {product['id']}, Nombre: {product['name']}, Precio: ${product['price']:.2f}")
    except Exception as e:
        print(f"Error general: {str(e)}")
```

## Características de la implementación:

1. **Autenticación Bearer**: Usa headers con `Authorization: Bearer {token}`

2. **Timeout de 10 segundos**: Configurado con `timeout=10` en el cliente httpx

3. **Retry con backoff exponencial**:
   - Máximo 3 intentos
   - Espera exponencial: 1s, 2s, 4s (2^attempt)
   - Maneja errores específicos: timeout, HTTP errors, errores de red

4. **Manejo de errores diferenciado**:
   - Timeout exceptions
   - HTTP errors (4xx/5xx)
   - Errores de red (conexión, DNS, etc.)
   - Errores inesperados (se re-lanzan sin reintento)

5. **Filtrado y transformación**:
   - Filtra productos con precio > 100
   - Extrae solo los campos `id`, `name`, `price`
   - Verifica la existencia de campos antes de acceder

6. **Flexibilidad en la estructura de respuesta**:
   - Maneja tanto respuestas tipo `{"products": [...]}` como listas directas
   - Validación de campos obligatorios

## Notas para uso:

- Reemplaza `"tu_token_de_autenticacion_aqui"` con tu token real
- La función asume que la API devuelve JSON con los campos `id`, `name`, `price`
- Ajusta la lógica de extracción de `products` si la API tiene una estructura diferente
- Los errores de autenticación (401/403) no se reintentan automáticamente