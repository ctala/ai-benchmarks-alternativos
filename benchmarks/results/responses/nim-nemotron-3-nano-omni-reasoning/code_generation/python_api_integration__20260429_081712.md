# Nemotron 3 Nano Omni 30B-A3B Reasoning (NIM) — code_generation/python_api_integration

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning`
- success: True  | final: 7.78 | quality: 9.52
- latency_total: 5.141s | tokens_per_second: 263.8
- input_tokens: 121 | output_tokens: 1356
- judge_score: 4.8 | justificación: 

## Respuesta completa

**Código**

```python
import time
from typing import List, Dict, Any

import httpx


def get_expensive_products(
    token: str,
    *,
    max_attempts: int = 3,
    timeout: float = 10.0,
    backoff_factor: float = 0.5,
) -> List[Dict[str, Any]]:
    """
    Obtiene los productos cuya precio es mayor a 100.

    Parámetros
    ----------
    token : str
        Token Bearer de autenticación.
    max_attempts : int, opcional
        Número máximo de intentos (incluye el intento inicial). Por defecto 3.
    timeout : float, opcional
        Tiempo máximo de espera para la respuesta HTTP (segundos). Por defecto 10.
    backoff_factor : float, opcional
        Factor de back‑off exponencial (en segundos). Los tiempos de espera
        entre intentos son: backoff_factor * (2 ** (intento‑1)).
        Por defecto 0.5 → 0.5 s, 1 s, 2 s.

    Returns
    -------
    List[Dict[str, Any]]
        Lista de diccionarios con los campos ``id``, ``name`` y ``price`` de
        los productos que cumplen el filtro.

    Raises
    ------
    httpx.HTTPError
        Si después de ``max_attempts`` la petición sigue fallando.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    # Cliente httpx reutilizable (más eficiente que crear uno por llamada)
    client = httpx.Client(timeout=timeout)

    for attempt in range(1, max_attempts + 1):
        try:
            response = client.get(url, headers=headers)
            # Si el código HTTP no es 2xx, lo consideramos error
            response.raise_for_status()
        except (httpx.RequestError, httpx.TimeoutException) as exc:
            # Error de red o timeout → reintentar
            if attempt == max_attempts:
                # Último intento → lanzar la excepción para que el llamador la maneje
                raise
            # Esperar antes del reintento (backoff exponencial)
            sleep_time = backoff_factor * (2 ** (attempt - 1))
            time.sleep(sleep_time)
            continue
        except httpx.HTTPStatusError as exc:
            # Errores de HTTP (p.ej. 4xx/5xx) no se reintentan, se propagan
            raise

        # --- Procesar la respuesta exitosa ---
        try:
            data = response.json()
        except ValueError as exc:
            # Si la respuesta no es JSON, considerarlo error
            raise RuntimeError("Respuesta no es JSON") from exc

        # Se asume que la API devuelve una lista de objetos con los campos
        # id, name y price. Si la estructura es diferente, habría que ajustarla.
        filtered = [
            {"id": item["id"], "name": item["name"], "price": item["price"]}
            for item in data
            if isinstance(item, dict) and item.get("price") is not None and item.get("price") > 100
        ]

        return filtered

    # Si se sale del bucle sin return, algo salió mal (debería haber lanzado)
    raise RuntimeError("No se pudo obtener la lista de productos después de varios intentos")
```

**Explicación paso a paso**

1. **Autenticación**  
   Se agrega el encabezado `Authorization: Bearer <token>` a la solicitud `GET`.

2. **Timeout**  
   El cliente `httpx.Client` se crea con `timeout=10.0` s, lo que cubre el requisito de manejo de timeout.

3. **Manejo de errores de red**  
   - `httpx.RequestError` y `httpx.TimeoutException` se capturan para volver a intentar.  
   - Si se supera el número máximo de intentos (`max_attempts`) se vuelve a lanzar la excepción, permitiendo que quien invoque la función trate el fallo.

4. **Retry con back‑off exponencial**  
   - En cada reintento se espera `backoff_factor * (2 ** (attempt‑1))` segundos.  
   - Con los valores por defecto (`0.5`) los tiempos de espera son: 0.5 s, 1 s, 2 s → máximo 3 intentos.

5. **Filtrado**  
   Después de una respuesta exitosa (`2xx`) se parsea el JSON y se construye una lista de diccionarios con solo los campos `id`, `name` y `price`, manteniendo aquellos cuya `price` sea mayor que 100.

6. **Retorno**  
   La función devuelve directamente la lista filtrada. Si después de los reintentos no se obtiene respuesta válida, se lanza una excepción `RuntimeError`.

**Uso rápido**

```python
token = "mi_token_secreto"
try:
    productos_caros = get_expensive_products(token)
    print(productos_caros)
except Exception as e:
    print(f"Error al obtener productos: {e}")
```

El código solo depende de la biblioteca estándar `time` y de `httpx`, cumpliendo con la restricción de **no usar dependencias externas adicionales**.