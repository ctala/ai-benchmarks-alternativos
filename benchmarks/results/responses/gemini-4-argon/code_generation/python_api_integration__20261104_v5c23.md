# Gemini 4 Argon — code_generation/python_api_integration

- model_id: `google/gemini-4-argon`
- success: True  | final: 8.04 | quality: 9.48
- latency_total: 17.375s | tokens_per_second: 62.7
- input_tokens: 129 | output_tokens: 1090
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

Aquí tienes la función implementada utilizando únicamente `httpx` y módulos nativos de Python (`time` y `typing`).

```python
import time
from typing import Any, Dict, List
import httpx


def obtener_productos_caros(token: str) -> List[Dict[str, Any]]:
    """Obtiene productos desde la API, filtra aquellos con precio > 100

    y maneja reintentos con backoff exponencial.
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    max_intentos = 3
    timeout_segundos = 10.0

    # Usamos un Client para reutilizar la conexión entre posibles reintentos
    with httpx.Client(timeout=timeout_segundos) as client:
        for intento in range(max_intentos):
            try:
                response = client.get(url, headers=headers)

                # Lanza una excepción si el código de estado es 4xx o 5xx
                response.raise_for_status()

                # Si llegamos aquí, la petición fue exitosa; salimos del bucle
                productos = response.json()
                break

            except (httpx.RequestError, httpx.HTTPStatusError) as error:
                # Si es un error del cliente (4xx, ej. 401 Unauthorized), no tiene sentido reintentar
                if (
                    isinstance(error, httpx.HTTPStatusError)
                    and 400 <= error.response.status_code < 500
                ):
                    print(
                        f"Error del cliente ({error.response.status_code}). Abortando."
                    )
                    raise error

                # Si alcanzamos el máximo de intentos, relanzamos la última excepción
                if intento == max_intentos - 1:
                    print("Se alcanzó el número máximo de intentos.")
                    raise error

                # Cálculo de backoff exponencial: 1s, 2s, 4s... (2^0, 2^1, 2^2)
                tiempo_espera = 2**intento
                print(
                    f"Intento {intento + 1} falló ({error}). Reintentando en {tiempo_espera}s..."
                )
                time.sleep(tiempo_espera)

    # Si la API devuelve un diccionario que envuelve la lista (ej. {"data": [...]}),
    # asegúrate de ajustar la variable `productos`. Aquí asumimos que devuelve una lista directa.

    # Filtrado (precio > 100) y mapeo de claves ({id, name, price}) usando List Comprehension
    productos_filtrados = [
        {"id": prod["id"], "name": prod["name"], "price": prod["price"]}
        for prod in productos
        if prod.get("price", 0) > 100
    ]

    return productos_filtrados


# --- Ejemplo de uso ---
if __name__ == "__main__":
    MI_TOKEN = "eyJhbGciOiJIUzI1NiIsIn..."

    try:
        resultado = obtener_productos_caros(MI_TOKEN)
        print(f"Productos encontrados: {len(resultado)}")
        print(resultado)
    except Exception as e:
        print(f"La operación falló definitivamente: {e}")
```

### Detalles de la implementación:

1. **Petición y Autenticación:** Se utiliza `httpx.Client` pasando el header `Authorization: Bearer <token>`.
2. **Timeout:** Configurado directamente en el cliente con `timeout=10.0` segundos (afecta a conexión, lectura y escritura).
3. **Manejo de Errores:** 
   - `httpx.RequestError` captura cualquier problema de red, DNS o **Timeouts** (`httpx.TimeoutException` hereda de `RequestError`).
   - `httpx.HTTPStatusError` captura respuestas de error del servidor (4xx y 5xx) gracias a `response.raise_for_status()`.
   - *Optimización:* Si hay un error 4xx (por ejemplo, Token inválido - 401), el código **no** reintenta, ya que el resultado será el mismo. Solo reintenta en errores de red o errores 5xx del servidor.
4. **Backoff Exponencial:** Implementado manualmente con `time.sleep(2 ** intento)`. Esperará **1 segundo** tras el primer fallo, y **2 segundos** tras el segundo fallo. Al tercer fallo, lanzará el error.
5. **Filtrado y Formateo:** Se hace de manera eficiente ("Pythonic") usando una *list comprehension*, asegurando mediante `.get('price', 0)` que no falle si algún producto viene sin precio.