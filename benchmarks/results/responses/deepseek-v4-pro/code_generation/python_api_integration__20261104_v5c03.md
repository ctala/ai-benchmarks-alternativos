# DeepSeek V4 Pro — code_generation/python_api_integration

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 7.83 | quality: 9.08
- latency_total: 30.142s | tokens_per_second: 79.9
- input_tokens: 110 | output_tokens: 2407
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
from typing import List, Dict

def obtener_productos_caros(token: str) -> List[Dict]:
    """
    Obtiene productos con precio > 100 desde la API, usando autenticación Bearer.
    
    Args:
        token: Token de acceso Bearer.
    
    Returns:
        Lista de diccionarios con las claves 'id', 'name' y 'price' de cada producto
        cuyo precio sea superior a 100.
    
    Raises:
        Exception: Si después de 3 intentos (con backoff exponencial) la petición sigue fallando.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_intentos = 3
    retraso_base = 2  # segundos

    for intento in range(max_intentos):
        try:
            with httpx.Client(timeout=10) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza HTTPStatusError si 4xx/5xx
                
                datos = response.json()
                # Se asume que la respuesta puede ser una lista directa o un dict con clave 'products'
                if isinstance(datos, dict) and "products" in datos:
                    datos = datos["products"]
                if not isinstance(datos, list):
                    # Si no se puede interpretar como lista, devolvemos vacío
                    return []

                # Filtrado y mapeo a solo {id, name, price}
                resultado = []
                for producto in datos:
                    if isinstance(producto, dict) and producto.get("price", 0) > 100:
                        resultado.append({
                            "id": producto.get("id"),
                            "name": producto.get("name"),
                            "price": producto.get("price"),
                        })
                return resultado

        except (httpx.HTTPStatusError, httpx.RequestError) as e:
            # Para errores HTTP de cliente (4xx) no reintentamos
            if isinstance(e, httpx.HTTPStatusError) and e.response.status_code < 500:
                raise
            if intento == max_intentos - 1:
                raise  # Se agotaron los reintentos, relanzamos la última excepción
            
            # Backoff exponencial: 2^0=1s, 2^1=2s, 2^2=4s
            retraso = retraso_base ** intento
            time.sleep(retraso)

    return []  # Nunca debería llegar aquí, pero por completitud
```