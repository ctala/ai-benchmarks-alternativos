# Nemotron 3 Nano Omni 30B-A3B Reasoning — code_generation/python_api_integration

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- success: True  | final: 8.78 | quality: 9.72
- latency_total: 25.103s | tokens_per_second: 57.2
- input_tokens: 118 | output_tokens: 1436
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(
    token: str,
    *,
    timeout: float = 10.0,
    max_retries: int = 3,
    base_backoff: float = 0.5,
) -> List[Dict[str, Any]]:
    """
    Obtiene los productos cuya precio es mayor a 100.

    Parámetros
    ----------
    token : str
        Token de autorización Bearer.
    timeout : float, opcional
        Tiempo máximo (en segundos) para la petición HTTP. Default 10 s.
    max_retries : int, opcional
        Número máximo de intentos (incluye el intento inicial). Default 3.
    base_backoff : float, opcional
        Retraso base para el back‑off exponencial (segundos). Default 0.5 s.

    Returns
    -------
    List[Dict[str, Any]]
        Lista de diccionarios con los campos ``id``, ``name`` y ``price`` de
        los productos que cumplen la condición ``price > 100``.
        Si todos los intentos fallan, devuelve una lista vacía.

    Notas
    -----
    - Se usa ``httpx`` (sin dependencias externas adicionales).
    - El back‑off exponencial se calcula como ``base_backoff * 2**(attempt-1)``.
    - Se capturan ``httpx.RequestError`` (errores de red) y
      ``httpx.HTTPStatusError`` (códigos de estado no exitosos).
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}

    for attempt in range(1, max_retries + 1):
        try:
            # Cliente con timeout definido
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                # Lanza excepción si el código de estado no es 2xx
                response.raise_for_status()
                # Se asume que la respuesta JSON contiene una lista de productos
                products = response.json()

            # Filtrar productos con precio > 100
            result = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if isinstance(p.get("price"), (int, float)) and p["price"] > 100
            ]
            return result

        except (httpx.RequestError, httpx.HTTPStatusError) as exc:
            # Si es el último intento, propagamos la excepción para que el llamador
            # pueda decidir qué hacer (por ejemplo, registrar o re‑intentar a nivel superior).
            if attempt == max_retries:
                raise  # o bien: return [] si se prefiere silenciar el error
            # Retraso exponencial antes del siguiente intento
            backoff = base_backoff * (2 ** (attempt - 1))
            time.sleep(backoff)

    # Nunca debería llegar aquí porque el bucle termina con return o raise,
    # pero lo dejamos por completitud.
    return []
```

### Uso rápido

```python
if __name__ == "__main__":
    token = "mi_token_secreto"
    try:
        productos_caros = get_expensive_products(token)
        print(productos_caros)
    except Exception as e:
        print(f"Error al obtener los productos: {e}")
```

Esta función cumple con todos los requisitos:

1. **GET** a `https://api.example.com/products` con autenticación **Bearer**.
2. **Filtra** los productos cuyo `price` sea mayor que 100.
3. Devuelve una lista de diccionarios con sólo los campos `{id, name, price}`.
4. **Maneja** errores de red y timeout (10 s por defecto).
5. **Retry** con back‑off exponencial (0.5 s, 1 s, 2 s) y máximo 3 intentos.  

Solo se emplea la biblioteca estándar `httpx`; no se añaden dependencias externas.