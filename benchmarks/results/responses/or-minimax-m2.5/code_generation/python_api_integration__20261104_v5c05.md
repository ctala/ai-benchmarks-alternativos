# MiniMax M2.5 — code_generation/python_api_integration

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 8.69 | quality: 9.52
- latency_total: 9.708s | tokens_per_second: 137.2
- input_tokens: 130 | output_tokens: 1332
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

# Solución en Python con httpx

Aquí tienes una función completa que cumple con todos los requisitos:

```python
import httpx
import time
import logging
from typing import List, Dict, Any

# Configurar logging básico
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_filtered_products(
    url: str = "https://api.example.com/products",
    token: str = "tu_bearer_token_aqui",
    max_retries: int = 3,
    timeout: float = 10.0,
    min_price: float = 100.0
) -> List[Dict[str, Any]]:
    """
    Realiza GET a la API, filtra productos por precio y retorna lista reducida.
    
    Args:
        url: Endpoint de la API
        token: Bearer token para autenticación
        max_retries: Máximo número de reintentos
        timeout: Timeout en segundos
        min_price: Precio mínimo para filtrar
    
    Returns:
        Lista de diccionarios con {id, name, price}
    
    Raises:
        httpx.HTTPStatusError: Si error HTTP (4xx/5xx)
        httpx.NetworkError: Si error de red
        httpx.TimeoutException: Si timeout
    """
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    
    def make_request_with_retry() -> httpx.Response:
        """Ejecuta la petición con retry y backoff exponencial."""
        
        last_exception = None
        
        for attempt in range(max_retries):
            try:
                # Calcular delay con backoff exponencial: 2^attempt segundos
                if attempt > 0:
                    delay = 2 ** attempt  # 2, 4, 8 segundos
                    logger.info(f"Reintento {attempt + 1}/{max_retries} tras {delay}s...")
                    time.sleep(delay)
                
                with httpx.Client(timeout=timeout) as client:
                    response = client.get(url, headers=headers)
                    response.raise_for_status()  # Lanza error si 4xx/5xx
                    return response
                    
            except httpx.TimeoutException as e:
                logger.warning(f"Timeout en intento {attempt + 1}: {e}")
                last_exception = e
                
            except httpx.NetworkError as e:
                logger.warning(f"Error de red en intento {attempt + 1}: {e}")
                last_exception = e
                
            except httpx.HTTPStatusError as e:
                # Errores 4xx/5xx no reintentamos (son errores del servidor/cliente)
                logger.error(f"Error HTTP: {e.response.status_code}")
                raise
                
            except httpx.RequestError as e:
                logger.warning(f"Error en request {attempt + 1}: {e}")
                last_exception = e
        
        # Si agotamos reintentos
        raise last_exception or Exception("Error desconocido después de reintentos")
    
    # Ejecutar request
    response = make_request_with_retry()
    products = response.json()
    
    # Filtrar productos con precio > min_price y seleccionar campos
    filtered = [
        {
            "id": product["id"],
            "name": product["name"],
            "price": product["price"]
        }
        for product in products
        if product.get("price", 0) > min_price
    ]
    
    logger.info(f"Productos filtrados: {len(filtered)} de {len(products)}")
    return filtered


# Ejemplo de uso
if __name__ == "__main__":
    try:
        results = fetch_filtered_products(
            url="https://api.example.com/products",
            token="mi_token_bearer"
        )
        print(f"Resultados: {results}")
        
    except httpx.HTTPStatusError as e:
        print(f"Error HTTP: {e}")
        
    except (httpx.NetworkError, httpx.TimeoutException) as e:
        print(f"Error de red: {e}")
        
    except Exception as e:
        print(f"Error inesperado: {e}")
```

## Puntos clave de la implementación:

| Requisito | Implementación |
|-----------|----------------|
| **GET con Bearer** | Header `Authorization: Bearer {token}` |
| **Filtro precio > 100** | List comprehension con `if product.get("price", 0) > min_price` |
| **Solo {id, name, price}** | Dict comprehension con solo esos keys |
| **Timeout 10s** | `httpx.Client(timeout=timeout)` |
| **Retry + backoff exponencial** | Loop con `delay = 2 ** attempt` (2s, 4s, 8s) |
| **Manejo de errores** | Except blocks para cada tipo de error |

## Notas:

- **Backoff exponencial**: `2 ** attempt` genera delays de 2, 4, 8 segundos
- **Errores no reintentados**: Los HTTP 4xx/5xx se lanzan inmediatamente (no tiene sentido reintentarlos)
- **Timeout**: Aplica tanto para conexión como para lectura
- **httpx.Client()**: Se usa como context manager para asegurar cierre de conexiones