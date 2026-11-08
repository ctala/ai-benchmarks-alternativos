# Granite 4.2 8B — code_generation/python_api_integration

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 8.42 | quality: 9.52
- latency_total: 79.872s | tokens_per_second: 90.2
- input_tokens: 124 | output_tokens: 7202
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

```python
import httpx
import time

def get_products(token: str) -> list[dict]:
    """
    Hace GET a https://api.example.com/products con autenticación Bearer,
    filtra productos con precio > 100, devuelve lista de dicts {id, name, price},
    maneja errores de red/timeout (10s) con retry exponencial (máx 3 intentos).
    
    Args:
        token (str): Token Bearer para autenticación.
        
    Returns:
        list[dict]: Lista de dicts con solo {'id', 'name', 'price'} para productos con precio > 100.
        
    Raises:
        httpx.RequestError: Si falla todas las intentos después de retry.
        Exception: Para errores HTTP no reintentables (ej. 404, 500 si no es red) o errores de formato.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)  # Timeout total de 10 segundos
    max_attempts = 3
    
    for attempt in range(max_attempts):
        try:
            response = httpx.get(url, headers=headers, timeout=timeout)
            
            # Verificar código de estado HTTP 200 (no reintentar errores HTTP como 4xx/5xx)
            if response.status_code == 200:
                data = response.json()
                
                # Validar que sea una lista
                if not isinstance(data, list):
                    raise Exception("Respuesta no es una lista de productos")
                
                filtered = []
                for product in data:
                    if not isinstance(product, dict):
                        continue
                    price = product.get('price')
                    if price is None:
                        continue
                    try:
                        price_val = float(price)
                    except (TypeError, ValueError):
                        continue  # Saltar si precio no es numérico
                    
                    if price_val > 100:
                        # Incluir solo {id, name, price} (usar .get para evitar KeyError si falta alguno)
                        filtered.append({
                            'id': product.get('id'),
                            'name': product.get('name'),
                            'price': product['price']  # Mantener el valor original (int/float/string del API)
                        })
                return filtered
            
            # Para códigos HTTP != 200 (ej. 404, 500), no reintentar (no es error de red)
            raise Exception(f"HTTP {response.status_code}: {response.text}")
        
        except httpx.RequestError as e:
            # Error de red/timeout (conexión fallida, timeout de conexión/lectura, etc.)
            if attempt < max_attempts - 1:
                delay = 2 ** attempt  # Backoff exponencial: 1s (attempt 0), 2s (attempt 1), 4s (attempt 2)
                time.sleep(delay)
            else:
                # Último intento falló: re-lanzar el error
                raise  # Propaga el error de red después de todos los intentos
        except Exception as e:
            # Errores no relacionados con red (ej. JSON mal formado, respuesta no es lista, HTTP 4xx/5xx)
            # No se reintentan (estos no son errores de red)
            raise e
```

**Explicación breve de cumplimiento de requisitos:**

1. ✅ **GET con Bearer token**: Usa `headers = {"Authorization": f"Bearer {token}"}` en `httpx.get`.
2. ✅ **Filtrar precio > 100**: Convierte `price` a `float` de forma segura (maneja strings numéricos o valores no numéricos), verifica `price_val > 100`, y solo incluye `id`, `name`, `price` en el dict de salida.
3. ✅ **Retornar lista de dicts `{id, name, price}`**: Construye cada dict con `.get()` para evitar KeyError y solo incluye las tres claves.
4. ✅ **Manejar errores de red y timeout (10s)**: 
   - `timeout=httpx.Timeout(10.0)` asegura que la solicitud no exceda 10 segundos.
   - `httpx.RequestError` captura errores de red/timeout (conexión fallida, timeout de conexión/lectura, etc.).
5. ✅ **Retry con backoff exponencial (máx 3 intentos)**:
   - 3 intentos totales (inicial + 2 reintentos).
   - Backoff: 1s (primera retry), 2s (segunda retry), 4s (tercera retry) usando `delay = 2 ** attempt`.
   - Solo se reintentan errores de red (`httpx.RequestError`); errores HTTP (ej. 404, 500) o errores de formato (JSON mal formado) se re-lanzan inmediatamente sin retry (correcto, ya que no son errores de red).
   - El `time.sleep(delay)` se usa solo entre intentos (no antes del primer intento).

**Notas clave:**
- No se usan dependencias externas además de `httpx` (solo `httpx` y la librería estándar `time`).
- Los errores HTTP (ej. 404, 500) **no se reintentan** (es correcto: los retries son para errores de red/timeout, no para errores de negocio o respuestas no válidas).
- La lógica de filtrado es robusta: verifica que `price` exista, sea numérico, y usa `float()` para comparación segura (ej. `"150"` → `150.0`).
- El código es claro, con comentarios explicativos y seguimiento de flujo lógico.

> 💡 **Uso en práctica**:  
> ```python
> try:
>     products = get_products("tu_token_bearer")
>     print(products)  # Lista de dicts con solo id, name, price > 100
> except Exception as e:
>     print(f"Error después de todos los intentos: {e}")
> ```