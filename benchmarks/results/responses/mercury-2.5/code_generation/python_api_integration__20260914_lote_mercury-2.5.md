# Mercury 2.5 — code_generation/python_api_integration

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.15 | quality: 9.52
- latency_total: 3.444s | tokens_per_second: 567.6
- input_tokens: 96 | output_tokens: 1955
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



Aquí tienes una función Python que cumple con los requisitos usando solo `httpx` y librerías estándar:

```python
import httpx
import time

def obtener_productos_caros(token: str, timeout: int = 10, max_retries: int = 3) -> list:
    """
    Obtiene productos de la API, filtra aquellos con precio > 100 
    y retorna solo id, name y price. Incluye retry con backoff exponencial.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    delay = 1

    for intent in range(max_retries):
        try:
            with httpx.Client() as client:
                response = client.get(url, headers=headers, timeout=timeout)
                response.raise_for_status()
                data = response.json()
                
                # Filtrar y mapear solo los campos requeridos
                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in data 
                    if isinstance(p, dict) and p.get("price", 0) > 100
                ]
        except httpx.HTTPError:
            if intent == max_retries - 1:
                raise
            time.sleep(delay * (2 ** intent))
```

### Características:
- **Autenticación:** Usa encabezado `Authorization: Bearer`.
- **Timeout:** Configurado a 10 segundos.
- **Retry:** Máximo 3 intentos con backoff exponencial (1s, 2s, 4s).
- **Filtro:** Solo incluye productos con `price > 100`.
- **Salida:** Lista de diccionarios con `id`, `name` y `price`.

Asegúrate de tener instalado `httpx` (`pip install httpx`).