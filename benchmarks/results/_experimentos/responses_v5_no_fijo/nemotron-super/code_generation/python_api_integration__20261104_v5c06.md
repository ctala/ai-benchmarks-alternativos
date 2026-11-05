# Nemotron 3 Super — code_generation/python_api_integration

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 8.53 | quality: 9.28
- latency_total: 11.745s | tokens_per_second: 91.8
- input_tokens: 118 | output_tokens: 1078
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
from typing import List, Dict, Any

def get_expensive_products(bearer_token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos desde https://api.example.com/products, filtra aquellos con precio > 100
    y devuelve una lista de diccionarios con los campos {id, name, price}.

    Parámetros
    ----------
    bearer_token: str
        Token de autorización Bearer que se enviará en el encabezado ``Authorization``.

    Retorna
    -------
    List[Dict[str, Any]]
        Lista de productos que cumplen el filtro. Cada elemento tiene la forma:
        {"id": <int|str>, "name": <str>, "price": <float|int>}.
        Si tras los reintentos no se pudo obtener una respuesta válida, se devuelve una lista vacía.

    Notas
    -----
    * Se utiliza ``httpx`` exclusivamente (no se requieren otras dependencias externas).
    * Timeout de petición: 10 segundos.
    * Política de reintentos: hasta 3 intentos con back‑off exponencial (1 s, 2 s, 4 s).
    * Se capturan errores de red, timeout y respuestas HTTP no exitosas.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    timeout = httpx.Timeout(10.0, read=10.0, write=10.0, connect=10.0)

    max_attempts = 3
    backoff_factor = 1  # segundos

    for attempt in range(1, max_attempts + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                # Lanza excepción para códigos 4xx/5xx
                response.raise_for_status()
                data = response.json()

                # Asumimos que la API devuelve una lista de productos
                if not isinstance(data, list):
                    raise ValueError("Respuesta inesperada: se esperaba una lista de productos")

                filtered = []
                for item in data:
                    try:
                        price = float(item.get("price", 0))
                        if price > 100:
                            filtered.append({
                                "id": item.get("id"),
                                "name": item.get("name"),
                                "price": price
                            })
                    except (TypeError, ValueError):
                        # Si el precio no es numérico, simplemente lo ignoramos
                        continue

                return filtered

        except (httpx.RequestError, httpx.HTTPStatusError, ValueError) as exc:
            # Si ya hemos agotado los intentos, salimos y devolvemos lista vacía
            if attempt == max_attempts:
                # Aquí podrías logar el error si tuvieras un logger configurado
                # logger.error(f"Fallo después de {max_attempts} intentos: {exc}")
                return []
            # Esperamos antes del siguiente intento con back‑off exponencial
            wait_time = backoff_factor * (2 ** (attempt - 1))
            time.sleep(wait_time)
            # Continuamos al siguiente intento
``` 

**Cómo usarlo**

```python
token = "mi_token_secreto"
result = get_expensive_products(token)
print(result)
```

La función cumple con todos los puntos solicitados:

1. GET a `https://api.example.com/products` con encabezado `Authorization: Bearer <token>`.
2. Filtra solo los productos cuyo campo `price` sea mayor a 100.
3. Devuelve una lista de diccionarios con `{id, name, price}`.
4. Maneja errores de red, timeout y códigos HTTP no exitosos.
5. Implementa hasta 3 reintentos con back‑off exponencial (1 s, 2 s, 4 s).  
6. Sólo depende de `httpx` (no se requieren otras librerías externas).