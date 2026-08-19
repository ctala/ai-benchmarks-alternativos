# Seed 2.0 Code — code_generation/python_api_integration

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.05 | quality: 9.72
- latency_total: 133.191s | tokens_per_second: 63.3
- input_tokens: 140 | output_tokens: 8425
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

Aquí tienes la función Python que cumple **todos los requisitos** usando `httpx` y bibliotecas estándar (sin dependencias externas adicionales):

---

### Código Final
```python
import httpx
import time
from typing import List, Dict


def obtener_productos_caros(token_bearer: str) -> List[Dict]:
    """
    Obtiene productos desde la API, filtra por precio > 100 y retorna datos estructurados.
    Maneja timeouts, errores de red y reintenta con BACKOFF EXPONENCIAL (máx 3 intentos).

    Args:
        token_bearer: Token de autenticación Bearer para la API.

    Returns:
        Lista de diccionarios con SOLO las claves `id`, `name`, `price` de productos caros.

    Raises:
        ValueError: Si el token está vacío o la respuesta tiene formato inválido.
        Exception: Si fallan todos los reintentos o hay errores de cliente HTTP NO reintentables.
    """
    # Configuraciones fijas (cumplen requisitos)
    URL_API = "https://api.example.com/products"
    MAX_INTENTOS = 3
    TIMEOUT_SEGUNDOS = 10.0  # Timeout de 10s (requisito 4)
    ENCABEZADOS = {"Authorization": f"Bearer {token_bearer.strip()}"}  # Autenticación Bearer (requisito 1)

    # Validación de entrada (evita tokens vacíos)
    if not token_bearer.strip():
        raise ValueError("El token Bearer no puede ser vacío o contener solo espacios.")

    # Bucle de REINTENTOS con BACKOFF EXPONENCIAL (requisito 5)
    for intento_actual in range(MAX_INTENTOS):
        try:
            # Crear cliente HTTPX con manejo seguro de conexiones
            with httpx.Client() as cliente:
                # Solicitud GET con timeout y autenticación (requisito 1)
                respuesta = cliente.get(
                    url=URL_API,
                    headers=ENCABEZADOS,
                    timeout=TIMEOUT_SEGUNDOS
                )

                # Verificar código de estado EXITOSO (2xx)
                respuesta.raise_for_status()  # Lanza error si es 4xx/5xx

                # Parsear respuesta a JSON (maneja errores de formato)
                productos = respuesta.json()

                # Validar que la respuesta sea una LISTA de productos
                if not isinstance(productos, list):
                    raise ValueError("La API no devolvió una lista de productos (formato inválido).")

                # FILTRAR productos con precio > 100 y TRANSFORMAR a dicts específicos (requisitos 2 y 3)
                productos_filtrados = []
                for producto in productos:
                    try:
                        # Extraer y validar precio (maneja int, float o string numérico)
                        precio_bruto = producto["price"]
                        if isinstance(precio_bruto, (int, float)):
                            precio = precio_bruto
                        elif isinstance(precio_bruto, str):
                            # Convertir string a número (mantiene int si es entero)
                            precio_temp = float(precio_bruto)
                            precio = int(precio_temp) if precio_temp.is_integer() else precio_temp
                        else:
                            continue  # Tipo de precio no válido, omitir producto

                        # Filtrar por precio > 100 (requisito 2)
                        if precio > 100:
                            # Crear dict con SOLO id, name, price (requisito 3)
                            producto_transformado = {
                                "id": producto["id"],
                                "name": producto["name"],
                                "price": precio
                            }
                            productos_filtrados.append(producto_transformado)

                    except (KeyError, TypeError, ValueError):
                        # Omitir productos mal formados (falta id/name/price, precio no numérico, etc.)
                        continue

                # Si llegamos aquí, TODO SALIÓ BIEN → retornar resultados
                return productos_filtrados

        # ---------------- MANEJO DE ERRORES (requisito 4) ----------------
        # Errores de TIMEOUT
        except httpx.TimeoutException:
            mensaje_error = f"Intento {intento_actual + 1}/{MAX_INTENTOS}: Timeout (máx {TIMEOUT_SEGUNDOS}s)"
        # Errores de RED (sin conexión, DNS fallido, etc.)
        except httpx.NetworkError:
            mensaje_error = f"Intento {intento_actual + 1}/{MAX_INTENTOS}: Error de red"
        # Errores de ESTADO HTTP (4xx/5xx)
        except httpx.HTTPStatusError as error:
            codigo_estado = error.response.status_code
            mensaje_error = f"Intento {intento_actual + 1}/{MAX_INTENTOS}: Error HTTP {codigo_estado}"

            # NO REINTENTAR errores de CLIENTE (4xx: token inválido, URL mal formada, etc.)
            if 400 <= codigo_estado < 500:
                raise Exception(f"Error de cliente NO reintentable: {mensaje_error}") from error

        # Errores de FORMATO de datos (JSON inválido, no es lista, etc.)
        except ValueError as error:
            mensaje_error = f"Intento {intento_actual + 1}/{MAX_INTENTOS}: Formato de datos inválido → {str(error)}"

        # ---------------- LÓGICA DE REINTENTO ----------------
        # Si NO es el ÚLTIMO intento → esperar con BACKOFF EXPONENCIAL
        if intento_actual < MAX_INTENTOS - 1:
            # Backoff exponencial: tiempo = 2^intento_actual segundos (1s, 2s para 3 intentos)
            tiempo_espera = 2 ** intento_actual
            print(f"{mensaje_error} → Reintentando en {tiempo_espera}s...")  # Opcional (para depuración)
            time.sleep(tiempo_espera)
        else:
            # ÚLTIMO intento fallido → lanzar excepción final
            raise Exception(f"Falló después de {MAX_INTENTOS} intentos. Último error: {mensaje_error}")
```

---

### Cumplimiento de Requisitos (Verificación)
| Requisito | Cumplimiento |
|-----------|--------------|
| 1. GET con Bearer Token | Usa `Authorization: Bearer {token}` en encabezados, valida token no vacío. |
| 2. Filtrar precio > 100 | Filtra productos después de validar que el precio sea numérico (maneja `int`, `float` o strings numéricos). |
| 3. Retornar `{id, name, price}` | Crea dicts **exclusivamente** con esas claves, omite productos que les falten. |
| 4. Manejar errores de red/timeout (10s) | Captura `httpx.TimeoutException` (timeout) y `httpx.NetworkError` (red), timeout establecido en **10s**. |
| 5. Retry con backoff exponencial (máx 3 intentos) | Bucle de 3 intentos, backoff = `2^intento_actual` (1s → 2s para reintentos), **no reintenta errores 4xx** (cliente) por ser no recuperables. |

---

### Características Adicionales (Buenas Prácticas)
- **Validación de entrada**: Verifica que el token no esté vacío.
- **Manejo de precios flexibles**: Acepta precios como `int`, `float` o strings numéricos (ej: `"250.5"`).
- **Omisión de productos mal formados**: No rompe si un producto falta `id`, `name` o `price` → lo omite y sigue.
- **Excepciones claras**: Diferencia entre errores recuperables (reintentables) y no recuperables (ej: token inválido).
- **Sin dependencias externas**: Usa solo `httpx` y bibliotecas estándar (`time`, `typing`).

---

### Ejemplo de Uso
```python
# Token de ejemplo (reemplázalo por el tuyo)
MI_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

try:
    productos = obtener_productos_caros(MI_TOKEN)
    print("Productos caros encontrados:")
    for p in productos:
        print(p)
except Exception as e:
    print(f"Error al obtener productos: {str(e)}")
```

---

### Notas Importantes
1. **Backoff Exponencial**: Para 3 intentos, los tiempos de espera son `1s` (primer fallo) y `2s` (segundo fallo) → no espera después del tercer fallo.
2. **Errores 4xx No Reintentables**: Si el token es inválido (401) o la URL es mala (404), no reintenta (no tiene sentido).
3. **Formato de Respuesta**: Supone que la API devuelve una **lista de productos** directamente en el JSON (formato común para endpoints `/products`). Si la API devuelve un dict con una clave como `data`, ajusta la línea `productos = respuesta.json()["data"]`.

Si necesitas modificar algo (ej: formato de respuesta, manejo de errores), avísame!