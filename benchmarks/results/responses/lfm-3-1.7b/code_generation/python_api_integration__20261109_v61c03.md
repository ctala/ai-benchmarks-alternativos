# LFM-3 1.7B — code_generation/python_api_integration

- model_id: `liquid/lfm-3-1.7b`
- success: True  | final: 8.55 | quality: 9.44
- latency_total: 25.508s | tokens_per_second: 291.4
- input_tokens: 115 | output_tokens: 7433
- judge_score: 4.6 | justificación: 

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

Aquí tienes una implementación completa usando **`httpx`**, sin importar ninguna librería externa más allá de lo necesario para el tipo hintado (`typing`).  

La función `get_products`:

* Envía un GET a la URL indicada con el encabezado **Bearer <token>**.  
* Solicita un timeout de **10 segundos** por petición.  
* Intenta hasta **3 veces** (con retrocesión exponencial: 1 s, 2 s, 4 s entre intentos).  
* Si la respuesta contiene un campo `"price"`, convierte su valor a `float` y conserva el registro solo cuando `price > 100`.  
* Devuelve una lista de diccionarios con las claves `{ "id", "name", "price" }`.  
* Gestiona excepciones de red (`ConnectTimeout`, `ReadTimeout`) y otros errores inesperados, y lanza una excepción tras agotar los intentos.

```python
import time
import httpx
from typing import List, Dict

# Parámetros configurables dentro de la función o como constantes globales
MAX_RETRIES = 3          # número máximo de intentos de retry
TIMEOUT_SECONDS = 10     # tiempo de espera de cada solicitud (segundos)


def get_products(token: str, url: str = "https://api.example.com/products") -> List[Dict]:
    """
    Obtiene productos desde la API especificada, filtrando aquellos cuyo precio sea mayor a 100.

    Parameters
    ----------
    token : str
        Token Bearer para autenticación (encabezado Authorization: Bearer <token>).
    url : str, opcional
        URL del endpoint (por defecto https://api.example.com/products).

    Returns
    -------
        Lista de diccionarios con las claves ``id``, ``name`` y ``price`` que cumplen
        ``price > 100``.

    Raises
    ------
        ValueError
            Si se pasa una cadena vacía o ``None`` para ``token``.
        RuntimeError
            Si todas las tres intentas fallan.
    """
    if not token:
        raise ValueError("Se debe proporcionar un token válido (Bearer)")

    headers = {"Authorization": f"Bearer {token}"}

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            # Realiza la petición con timeout y verifica el código HTTP
            response = httpx.get(
                url,
                headers=headers,
                timeout=TIMEOUT_SECONDS,
                raise_for_status=True,
            )

            # El contenido puede estar en formato JSON. Intentamos parsediarlo;
            # si falla, continuamos con la representación textual.
            try:
                json_data = response.json()
            except httpx.HTTPException:
                # Si hay problema con la deserialización, trataremos como dato bruto
                json_data = response.text

            # Aseguramos que teníamos al menos una lista; si es un objeto singular,
            # convertimos en una lista de un único elemento.
            if isinstance(json_data, dict):
                json_data = [json_data]

            # Filtra y transforma los elementos que tienen precio > 100
            filtered_items = []
            for entry in json_data:
                price_raw = entry.get("price")
                if price_raw is None:
                    continue
                try:
                    price = float(price_raw)
                except (ValueError, TypeError):
                    # Valor no numérico → ignoramos
                    continue

                if price > 100:
                    filtered_items.append({
                        "id": entry.get("id"),
                        "name": entry.get("name"),
                        "price": price,
                    })

            return filtered_items

        except httpx.ConnectTimeout:
            # Error de conexión (pérdida de paquete, firewall, etc.)
            if attempt < MAX_RETRIES:
                wait = 2 ** (attempt - 1)   # 1 s, 2 s, 4 s …
                time.sleep(wait)
            else:
                raise   # agotamos los intentos

        except httpx.ReadTimeout:
            # Tiempo de espera de lectura (buffering, servidor lento, etc.)
            if attempt < MAX_RETRIES:
                wait = 2 ** (attempt - 1)
                time.sleep(wait)
            else:
                raise

        except httpx.HTTPError as exc:
            # Errores del servidor (4xx/5xx). Se trata como fallo permanente;
            # no se reintentará.
            raise RuntimeError(
                f"Error HTTP {exc.response.status_code} al obtener productos para {url}"
            ) from exc

        except Exception as exc:   # cualquier otro error inesperado (ej. parsing)
            # Se considera un fallo y se abandona la retry
            break

    # Si salimos del bucle sin devolver, todos los intentos fallaron
    raise RuntimeError(f"No se pudo obtener los productos después de {MAX_RETRIES} intentos")
```

### Uso rápido

```python
my_token = "your-bearer-token-here"
products = get_products(token=my_token)
print(products)
```

El resultado será una lista como:

```python
[
    {"id": 101, "name": "Laptop", "price": 1299.99},
    {"id": 204, "name": "Mouse", "price": 29.99},   # se excluye porque price ≤ 100
    ...
]
``` 

Con esto cumples con los cinco puntos solicitados:  

1. **GET** a la URL con autenticación `Bearer token`.  
2. **Filtro** de productos con `price > 100`.  
3. **Devolver** lista de dicts con solo `{id, name, price}`.  
4. **Manejo de errores/network** y timeout de 10 s.  
5. **Retry** con retrocesión exponencial (máximo 3 intentos).