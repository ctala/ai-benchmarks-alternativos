# GPT-OSS 120B — code_generation/python_api_integration

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.61 | quality: 9.52
- latency_total: 47.592s | tokens_per_second: 37.3
- input_tokens: 150 | output_tokens: 1776
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

**Código completo (sin dependencias externas, solo httpx y la biblioteca estándar)**  

```python
import time
from typing import List, Dict, Any

import httpx


def get_filtered_products(
    bearer_token: str,
    *,
    url: str = "https://api.example.com/products",
    price_threshold: float = 100.0,
    timeout: float = 10.0,
    max_retries: int = 3,
    backoff_factor: float = 1.0,
) -> List[Dict[str, Any]]:
    """
    Obtiene la lista de productos desde `url` usando autenticación Bearer,
    filtra los que tengan `price` mayor que `price_threshold` y devuelve
    únicamente los campos ``id``, ``name`` y ``price``.

    Parámetros
    ----------
    bearer_token: str
        Token JWT (u otro) que se enviará en el encabezado
        ``Authorization: Bearer <token>``.
    url: str (opcional)
        Endpoint del API. Por defecto ``https://api.example.com/products``.
    price_threshold: float (opcional)
        Precio mínimo para que un producto sea incluido en el resultado.
    timeout: float (opcional)
        Tiempo máximo (en segundos) que esperará cada petición antes de
        lanzar ``httpx.TimeoutException``.
    max_retries: int (opcional)
        Número máximo de intentos en caso de error de red o timeout.
    backoff_factor: float (opcional)
        Factor de crecimiento exponencial del “sleep” entre reintentos.
        El tiempo de espera será ``backoff_factor * (2 ** intento)`` segundos.

    Retorna
    -------
    List[Dict[str, Any]]
        Lista de diccionarios con las claves ``id``, ``name`` y ``price``.

    Excepciones
    ----------
    httpx.HTTPStatusError
        Si el servidor responde con un código de estado 4xx/5xx después
        de agotar los reintentos.
    RuntimeError
        Si se supera el número máximo de reintentos sin obtener una respuesta
        válida (por ejemplo, por errores de red persistentes).
    """
    headers = {"Authorization": f"Bearer {bearer_token}"}
    # Configuramos un cliente con timeout global (puede sobrescribirse por request)
    client = httpx.Client(timeout=timeout)

    attempt = 0
    while attempt < max_retries:
        try:
            response = client.get(url, headers=headers)
            # Levanta excepción para códigos 4xx/5xx
            response.raise_for_status()

            # Suponemos que la respuesta es JSON con una lista bajo la clave "data"
            # o directamente una lista. Ajuste según la estructura real.
            payload = response.json()
            if isinstance(payload, dict) and "data" in payload:
                products = payload["data"]
            else:
                products = payload  # asume que ya es una lista

            # Filtrado y proyección
            filtered = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if isinstance(p, dict) and p.get("price", 0) > price_threshold
            ]
            return filtered

        except (httpx.RequestError, httpx.TimeoutException) as exc:
            # Errores de red, DNS, timeout, etc.
            attempt += 1
            if attempt >= max_retries:
                raise RuntimeError(
                    f"Error de red después de {max_retries} intentos: {exc}"
                ) from exc

            # Back‑off exponencial
            sleep_seconds = backoff_factor * (2 ** (attempt - 1))
            print(
                f"[{attempt}/{max_retries}] Error de conexión ({exc}). "
                f"Reintentando en {sleep_seconds:.1f}s..."
            )
            time.sleep(sleep_seconds)

        except httpx.HTTPStatusError as exc:
            # El servidor respondió pero con código de error.
            # No reintentamos en la mayoría de los casos 4xx, pero sí podemos
            # intentar en 5xx (errores temporales del servidor).
            status = exc.response.status_code
            attempt += 1
            if 500 <= status < 600 and attempt < max_retries:
                sleep_seconds = backoff_factor * (2 ** (attempt - 1))
                print(
                    f"[{attempt}/{max_retries}] HTTP {status} del servidor. "
                    f"Reintentando en {sleep_seconds:.1f}s..."
                )
                time.sleep(sleep_seconds)
                continue
            # Si llegamos aquí, el error es definitivo.
            raise

        finally:
            # No cerramos el cliente aquí porque lo reutilizamos entre reintentos.
            pass

    # Si el bucle termina sin `return`, algo inesperado ocurrió.
    raise RuntimeError("No se pudo obtener la lista de productos.")


# ----------------------------------------------------------------------
# Ejemplo de uso
# ----------------------------------------------------------------------
if __name__ == "__main__":
    # Reemplaza esto por tu token real
    TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

    try:
        productos = get_filtered_products(TOKEN)
        print(f"Se obtuvieron {len(productos)} productos con precio > 100:")
        for p in productos:
            print(p)
    except Exception as e:
        print(f"Fallo al obtener los productos: {e}")
```

---

### Detalles de la solución

| Requisito | Cómo se cumple |
|-----------|----------------|
| **GET con Bearer token** | Se añaden los encabezados `Authorization: Bearer <token>` al cliente `httpx`. |
| **Filtrar precio > 100** | Después de parsear el JSON se crea una lista por comprensión que solo incluye los productos cuyo campo `price` supera el umbral (`price_threshold`). |
| **Retornar solo id, name, price** | La comprensión de listas construye diccionarios con esas tres claves exclusivamente. |
| **Manejo de errores de red y timeout (10 s)** | `httpx.Client(timeout=10.0)` lanza `httpx.RequestError` o `httpx.TimeoutException`; ambos son capturados y tratados. |
| **Retry con backoff exponencial (máx 3 intentos)** | Un bucle `while` controla los intentos. Entre cada reintento se espera `backoff_factor * 2**(attempt-1)` segundos (1 s → 2 s → 4 s por defecto). |
| **Sin dependencias externas** | Sólo se usan `httpx` (ya requerida) y módulos estándar (`time`, `typing`). |

---

#### Personalizaciones rápidas

- **Cambiar el umbral de precio** → pasar `price_threshold=150` al llamar la función.  
- **Modificar la URL o los parámetros de la petición** → usar el argumento `url=`.  
- **Ajustar el número máximo de reintentos** → `max_retries=5`.  
- **Cambiar el factor de back‑off** → `backoff_factor=0.5` (esperas: 0.5 s, 1 s, 2 s).  

Con este bloque de código tienes una solución lista para usar en cualquier proyecto que necesite consumir el endpoint indicado de forma robusta y sin dependencias adicionales. ¡Éxitos!