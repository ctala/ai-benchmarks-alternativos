# MiniMax M2.7 (directo) — code_generation/python_api_integration

- model_id: `MiniMax-M2.7`
- success: True  | final: 8.04 | quality: 9.28
- latency_total: 42.663s | tokens_per_second: 48.0
- input_tokens: 133 | output_tokens: 2048
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

A continuación tienes una solución **completa** que cumple todos los puntos que pediste:

* GET contra la URL con autenticación **Bearer**.  
* Filtra los productos cuyo precio sea **> 100**.  
* Devuelve solo `id`, `name` y `price`.  
* Maneja errores de red y timeout (10 s por defecto).  
* Reintenta hasta **3 veces** con back‑off exponencial (se puede ajustar).

Usa **solo** `httpx` (y la biblioteca estándar de Python). No necesitas ninguna dependencia extra.

---

## Código

```python
import time
import random
from typing import List, Dict, Optional

import httpx


def fetch_filtered_products(
    url: str = "https://api.example.com/products",
    token: Optional[str] = None,
    timeout: float = 10.0,
    max_retries: int = 3,
    backoff_factor: float = 1.0,
) -> List[Dict]:
    """
    Obtiene los productos de ``url`` usando autenticación Bearer,
    filtra los que tengan precio > 100 y devuelve una lista de diccionarios
    con solo los campos ``id``, ``name`` y ``price``.

    La función reintenta automáticamente en caso de error de red o
    timeout, usando un back‑off exponencial (por defecto hasta 3 intentos).

    Parámetros
    ----------
    url : str
        Endpoint del API (por defecto ``https://api.example.com/products``).
    token : Optional[str]
        Token de acceso (Bearer). Si es ``None`` o vacío se lanza ``ValueError``.
    timeout : float
        Tiempo máximo (en segundos) que se esperará por la respuesta del
        servidor (por defecto 10 s).
    max_retries : int
        Número máximo de intentos antes de propagar la excepción
        (por defecto 3).
    backoff_factor : float
        Factor multiplicativo del intervalo exponencial. ``sleep = backoff_factor *
        2**intento`` (por defecto 1.0).

    Retorna
    -------
    List[Dict]
        Lista de diccionarios con las claves ``id``, ``name`` y ``price`` de
        los productos cuyo precio sea mayor a 100.

    Lanza
    -----
    ValueError
        Si no se proporciona un token o si la respuesta no es un JSON válido.
    RuntimeError
        Si se agotan todos los reintentos.
    """
    # ---------- 1️⃣ Validar token ----------
    if not token:
        raise ValueError("Se requiere un token Bearer.")

    headers = {"Authorization": f"Bearer {token}"}

    # ---------- 2️⃣ Petición con reintento ----------
    with httpx.Client(timeout=timeout) as client:
        for attempt in range(max_retries):
            try:
                response = client.get(url, headers=headers)
                response.raise_for_status()          # lanza HTTPStatusError si no 2xx
                break                               # ✅ Petición satisfactoria
            except (httpx.TimeoutException,
                    httpx.NetworkError,
                    httpx.HTTPStatusError) as exc:
                if attempt == max_retries - 1:
                    # Se han consumido todos los intentos
                    raise RuntimeError(
                        f"Falló después de {max_retries} intentos: {exc}"
                    ) from exc

                # Back‑off exponencial + un poco de jitter para evitar “thundering herd”
                sleep_time = backoff_factor * (2 ** attempt)
