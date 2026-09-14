# Granite 4.2 8B — code_generation/python_api_integration

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 8.42 | quality: 9.52
- latency_total: 91.333s | tokens_per_second: 79.0
- input_tokens: 124 | output_tokens: 7219
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

def fetch_products(token: str) -> list[dict]:
    """
    Hace GET a https://api.example.com/products con autenticación Bearer token,
    filtra productos con precio > 100 y devuelve lista de dicts {id, name, price}.
    
    Maneja errores de red/timeout (10s por solicitud) con retry exponencial (máx. 3 intentos).
    Usa solo httpx y la librería estándar (time).
    
    Parámetros:
        token (str): Token Bearer para autenticación.
        
    Retorna:
        list[dict]: Lista de dicts con {id, name, price} para productos con price > 100.
        
    Lanza:
        RuntimeError si falla después de todos los intentos o si ocurre un error no retratable.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_attempts = 3
    
    for attempt in range(max_attempts):
        try:
            # Timeout total de 10 segundos por solicitud (incluye conexión y lectura)
            response = httpx.get(
                url,
                headers=headers,
                timeout=httpx.Timeout(10.0),
                follow_redirects=True
            )
            response.raise_for_status()  # Lanza HTTPError para 4xx/5xx
            
            data = response.json()
            
            # Validar que sea una lista (evita errores de iteración)
            if not isinstance(data, list):
                raise ValueError("Respuesta de API no es una lista")
            
            filtered = []
            for product in data:
                if not isinstance(product, dict):
                    continue  # Saltar elementos no-dict
                
                if 'price' not in product:
                    continue  # Saltar si falta precio
                
                try:
                    price = float(product['price'])
                except (TypeError, ValueError):
                    continue  # Saltar si precio no es convertible a float
                
                if price > 100:
                    # Incluir solo si tiene id y name (evita dicts incompletas)
                    if 'id' in product and 'name' in product:
                        filtered.append({
                            "id": product['id'],
                            "name": product['name'],
                            "price": price  # Devolver como float para consistencia
                        })
            
            return filtered
            
        except httpx.RequestError as e:
            # Retry solo para errores de red/timeout (RequestError incluye ConnectTimeout, ReadTimeout, NetworkError)
            if attempt < max_attempts - 1:
                # Backoff exponencial: 1s, 2s (1 * 2^0, 1 * 2^1)
                delay = 1 * (2 ** attempt)
                time.sleep(delay)
            else:
                # Último intento falló → lanzar error claro
                raise RuntimeError(
                    f"Falló obtener productos después de {max_attempts} intentos (timeout/error de red). "
                    f"Último error: {e}"
                ) from e
                
        except Exception as e:
            # No se retry para errores no-red (ej.: JSON mal formado, datos incorrectos)
            raise RuntimeError(
                f"Error inesperado al procesar la respuesta (no es retryable): {e}"
            ) from e
```

**Explicación breve (cumple todos los requisitos):**

1. **GET con Bearer token**: Usa `httpx.get` con `headers={"Authorization": "Bearer {token}"}`.
2. **Filtrado precio > 100**: Convierte `price` a `float` de forma segura (saltando valores no convertibles), verifica `price > 100`, y incluye solo productos con `id` y `name` presentes.
3. **Devuelve lista de dicts**: Cada dict tiene exactamente `{id, name, price}` (price como `float` para comparación numérica).
4. **Manejo de errores de red/timeout**: 
   - `timeout=httpx.Timeout(10.0)` asegura que cada solicitud tenga máximo 10 segundos.
   - `httpx.RequestError` captura errores de red/timeout (ej.: conexión fallida, timeout de lectura).
   - `response.raise_for_status()` detecta errores HTTP (4xx/5xx), pero **no se retry** para ellos (solo se retry para errores de red, como se especifica).
5. **Retry con backoff exponencial (máx. 3 intentos)**:
   - 3 intentos totales (primer intento + 2 retries).
   - Retraso: 1s después del primer fallo, 2s después del segundo fallo (`delay = 1 * 2^attempt`).
   - `time.sleep(delay)` está en el bucle de retry; si es el último intento y falla, se lanza `RuntimeError` claro.
   - Errores no-red (ej.: `JSONDecodeError`, datos mal formados) se lanzan inmediatamente sin retry (correcto según "errores de red y timeout").
6. **Sin dependencias externas**: Usa solo `httpx` (ya requerido) y `time` (estándar de Python).
7. **Código claro y seguro**: Validaciones básicas (tipo de respuesta, existencia de campos) para evitar `KeyError`/`TypeError` en procesamiento.

> **Nota**: El backoff es exacto (1s, luego 2s) para 3 intentos totales, como se describe ("max 3 intentos" + "backoff exponencial"). El timeout de 10 segundos se aplica a cada solicitud individual. Los errores de red (conexión, timeout) se retryan; errores de formato de datos se manejan inmediatamente (no se retry, ya que no son errores de red).