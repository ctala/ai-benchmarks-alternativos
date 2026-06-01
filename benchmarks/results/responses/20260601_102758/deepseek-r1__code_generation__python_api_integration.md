# DeepSeek R1 (reasoning) — code_generation/python_api_integration

- model_id: `deepseek/deepseek-r1`
- success: True  | final: 7.36 | quality: 9.48
- latency_total: 72.368s | tokens_per_second: 25.4
- input_tokens: 111 | output_tokens: 1837
- judge_score: 4.8 | justificación: 

## Respuesta completa

Para resolver el problema, vamos a crear una función en Python que utilice la biblioteca `httpx` para realizar una solicitud GET a la API especificada, con autenticación Bearer token. La función filtrará los productos con precio mayor a 100 y devolverá una lista de diccionarios con los campos `id`, `name` y `price`. Además, manejará errores de red y timeout, e implementará un mecanismo de reintento con backoff exponencial (hasta 3 intentos).

### Solución
```python
import httpx
import time

def get_products(token: str) -> list[dict]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0, connect=10.0)
    max_retries = 3
    backoff_factor = 0.5  # Factor para el cálculo del tiempo de espera exponencial
    
    for attempt in range(max_retries):
        try:
            # Realizar la solicitud GET con timeout
            with httpx.Client() as client:
                response = client.get(url, headers=headers, timeout=timeout)
                response.raise_for_status()  # Lanza excepción para códigos HTTP 4xx/5xx
                data = response.json()
            
            # Verificar si la respuesta es una lista o un diccionario con clave 'products'
            if isinstance(data, list):
                products = data
            elif isinstance(data, dict) and "products" in data:
                products = data["products"]
            else:
                # Si la estructura no es reconocida, retornar lista vacía
                return []
            
            # Filtrar productos con precio > 100 y seleccionar campos requeridos
            filtered_products = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if p.get("price", 0) > 100
            ]
            
            return filtered_products
        
        except (httpx.NetworkError, httpx.TimeoutException) as e:
            # Calcular tiempo de espera exponencial (0.5, 1, 2 segundos)
            wait_time = backoff_factor * (2 ** attempt)
            time.sleep(wait_time)
        except (httpx.HTTPStatusError, ValueError, KeyError, TypeError) as e:
            # Errores no reintentables (respuesta HTTP no exitosa, JSON inválido, estructura incorrecta)
            break
    
    # Retornar lista vacía después de fallar todos los reintentos o por error no reintentable
    return []
```

### Explicación
1. **Autenticación Bearer Token**: Se incluye el token en los headers de la solicitud HTTP.
2. **Timeout**: Se configura un timeout de 10 segundos para la conexión y la lectura.
3. **Reintentos con Backoff Exponencial**:
   - Se realizan hasta 3 intentos en caso de errores de red o timeout.
   - El tiempo de espera entre reintentos sigue una secuencia exponencial: 0.5s, 1s, 2s.
4. **Manejo de Errores**:
   - **Errores Reintentables**: `NetworkError` (problemas de red) y `TimeoutException`.
   - **Errores No Reintentables**: Errores HTTP (4xx/5xx), JSON inválido, o estructura de datos inesperada.
5. **Procesamiento de la Respuesta**:
   - Si la respuesta es una lista, se usa directamente.
   - Si es un diccionario, se busca la clave `"products"`.
   - Se filtran los productos con `price > 100` y se extraen los campos `id`, `name`, `price`.
6. **Salida**: Lista de diccionarios con los campos requeridos o lista vacía en caso de error.

Esta solución cumple con todos los requisitos especificados utilizando únicamente la biblioteca `httpx` y la biblioteca estándar de Python.