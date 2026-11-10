# GPT-OSS 120B — code_generation/python_api_integration

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.88 | quality: 9.48
- latency_total: 11.794s | tokens_per_second: 147.8
- input_tokens: 163 | output_tokens: 1743
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
"""
Módulo: product_api.py

Contiene una única función pública ``get_expensive_products`` que:

1. Hace una petición **GET** a ``https://api.example.com/products`` usando
   autenticación *Bearer token*.
2. Filtra los productos cuyo ``price`` sea mayor a 100.
3. Devuelve una lista de diccionarios con únicamente las claves
   ``id``, ``name`` y ``price``.
4. Gestiona errores de red y *timeout* (máximo 10 s por intento).
5. Implementa reintentos con back‑off exponencial (máximo 3 intentos).

Solo se usa la librería estándar y **httpx** (no se añaden dependencias
externas).
"""

from __future__ import annotations

import time
from typing import List, Dict

import httpx

# --------------------------------------------------------------------------- #
# Constantes de configuración (pueden sobrescribirse al llamar a la función)
# --------------------------------------------------------------------------- #
BASE_URL = "https://api.example.com"
ENDPOINT = "/products"
TIMEOUT = 10.0                     # segundos
MAX_RETRIES = 3
INITIAL_BACKOFF = 1.0              # segundos (se duplica en cada intento)


def _build_headers(token: str) -> Dict[str, str]:
    """Construye los encabezados HTTP con el token Bearer."""
    return {"Authorization": f"Bearer {token}"}


def _filter_product(product: dict) -> bool:
    """
    Devuelve ``True`` si el producto cumple con los criterios de filtrado.
    En este caso, que el precio sea mayor a 100.
    """
    try:
        return float(product.get("price", 0)) > 100
    except (TypeError, ValueError):
        # Si el precio no es numérico, lo descartamos.
        return False


def _extract_fields(product: dict) -> dict:
    """
    Devuelve un nuevo diccionario con solo los campos requeridos.
    Si alguno falta, se coloca ``None``.
    """
    return {
        "id": product.get("id"),
        "name": product.get("name"),
        "price": product.get("price"),
    }


def get_expensive_products(token: str) -> List[Dict[str, object]]:
    """
    Obtiene la lista de productos de la API, filtra los cuyo precio sea > 100
    y devuelve sólo los campos ``id``, ``name`` y ``price``.

    Parameters
    ----------
    token: str
        Token de autorización Bearer.

    Returns
    -------
    List[Dict[str, object]]
        Lista de productos filtrados.

    Raises
    ------
    RuntimeError
        Si después de los reintentos la petición sigue fallando.
    """
    url = f"{BASE_URL}{ENDPOINT}"
    headers = _build_headers(token)

    backoff = INITIAL_BACKOFF
    attempt = 0

    while attempt < MAX_RETRIES:
        attempt += 1
        try:
            # httpx.Client se abre y cierra automáticamente con ``with``.
            with httpx.Client(timeout=TIMEOUT) as client:
                response = client.get(url, headers=headers)

            # Si la API devolvió un código de error (4xx/5xx) lanzamos excepción.
            response.raise_for_status()

            # Se asume que la respuesta es JSON y contiene una lista bajo
            # la clave "data" o directamente una lista.
            payload = response.json()
            if isinstance(payload, dict) and "data" in payload:
                products = payload["data"]
            else:
                products = payload  # tipo list

            # Filtrado y extracción de campos.
            result = [
                _extract_fields(p)
                for p in products
                if isinstance(p, dict) and _filter_product(p)
            ]
            return result

        # ------------------------------------------------------------------- #
        # Manejo de errores que disparan un re‑intento
        # ------------------------------------------------------------------- #
        except (httpx.RequestError, httpx.TimeoutException) as exc:
            # Errores de red, DNS, timeout, etc.
            if attempt == MAX_RETRIES:
                raise RuntimeError(
                    f"Error de red después de {MAX_RETRIES} intentos: {exc}"
                ) from exc
            # Esperamos antes del siguiente intento
            time.sleep(backoff)
            backoff *= 2  # back‑off exponencial

        # ------------------------------------------------------------------- #
        # Errores HTTP (códigos 4xx/5xx) – no se re‑intentan porque la
        # petición llegó al servidor y el servidor respondió con error.
        # ------------------------------------------------------------------- #
        except httpx.HTTPStatusError as exc:
            raise RuntimeError(
                f"Respuesta HTTP inesperada: {exc.response.status_code} "
                f"{exc.response.text}"
            ) from exc

        # ------------------------------------------------------------------- #
        # Cualquier otro error inesperado
        # ------------------------------------------------------------------- #
        except Exception as exc:  # pragma: no cover
            raise RuntimeError(f"Error inesperado: {exc}") from exc


# --------------------------------------------------------------------------- #
# Ejemplo de uso (solo se ejecuta cuando el archivo se llama directamente)
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    # Sustituye por un token válido antes de probar.
    SAMPLE_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

    try:
        products = get_expensive_products(SAMPLE_TOKEN)
        print(f"Se obtuvieron {len(products)} productos > 100 $:")
        for p in products:
            print(p)
    except RuntimeError as e:
        print(f"Fallo al obtener los productos: {e}")
```

### Qué hace el código paso a paso  

| Paso | Acción | Detalle |
|------|--------|---------|
| 1 | Construye la URL completa y los encabezados | `Authorization: Bearer <token>` |
| 2 | Entra en un bucle de reintentos (`MAX_RETRIES = 3`) | Usa `backoff` exponencial: 1 s → 2 s → 4 s |
| 3 | Ejecuta la petición con `httpx.Client(timeout=10)` | Si ocurre `RequestError` o `TimeoutException` se reintenta |
| 4 | Verifica código HTTP (`raise_for_status`) | Si el servidor responde con 4xx/5xx se lanza `RuntimeError` sin re‑intento |
| 5 | Analiza el JSON devuelto | Acepta tanto `{ "data": [...] }` como una lista directa |
| 6 | Filtra productos cuyo `price` > 100 | Usa `_filter_product` (convierte a `float` y protege contra valores no numéricos) |
| 7 | Extrae solo los campos requeridos | `id`, `name`, `price` mediante `_extract_fields` |
| 8 | Devuelve la lista resultante | Si todo salió bien, se sale del bucle y la función termina |

### Por qué no se usan dependencias externas  

* `httpx` ya incluye manejo de timeout, excepciones de red y un cliente HTTP completo.  
* El back‑off exponencial se implementa con la función estándar `time.sleep`.  
* Todo el resto (tipado, lógica de filtrado) es código puro de Python.

Con esto tienes una solución lista para ser importada en cualquier proyecto que ya cuente con `httpx`. ¡A probarla!