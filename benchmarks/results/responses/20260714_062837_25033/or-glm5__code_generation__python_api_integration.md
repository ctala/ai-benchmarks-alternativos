# GLM 5 — code_generation/python_api_integration

- model_id: `z-ai/glm-5`
- success: True  | final: 8.38 | quality: 9.72
- latency_total: 45.77s | tokens_per_second: 52.1
- input_tokens: 106 | output_tokens: 2386
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes la función implementada usando `httpx` y la librería estándar `time` para el manejo de los reintentos:

```python
import httpx
import time

def obtener_productos_caros(token: str) -> list[dict]:
    """
    Obtiene productos con precio mayor a 100, con reintentos y backoff exponencial.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_intentos = 3
    timeout = 10.0

    for intento in range(1, max_intentos + 1):
        try:
            # 1. Petición GET con autenticación y timeout
            response = httpx.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()  # Lanza excepción si el status es 4xx o 5xx
            
            data = response.json()

            # 2. Filtrar productos con precio > 100
            # 3. Retornar lista de dicts con {id, name, price}
            productos_filtrados = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in data
                if isinstance(p, dict) and p.get("price", 0) > 100
            ]
            
            return productos_filtrados

        # 4. Manejar errores de red y timeout
        except (httpx.TimeoutException, httpx.NetworkError) as e:
            print(f"Error de conexión/timeout en intento {intento}: {e}")
            
            # Si ya alcanzamos el máximo de intentos, lanzamos la excepción
            if intento == max_intentos:
                raise
            
            # 5. Backoff exponencial (2^intento: 2s, 4s, 8s...)
            espera = 2 ** intento
            print(f"Reintentando en {espera} segundos...")
            time.sleep(espera)

# Ejemplo de uso (comentado para que no falle si copias y pegas):
# try:
#     token_valido = "mi_token_secreto"
#     resultado = obtener_productos_caros(token_valido)
#     print(resultado)
# except Exception as e:
#     print(f"Falló definitivamente: {e}")
```

### Detalles de la implementación:

1.  **Autenticación**: Se inyecta el header `Authorization: Bearer {token}`.
2.  **Filtrado y Transformación**: Se utiliza una *list comprehension* para filtrar por precio y crear el nuevo diccionario con solo las claves requeridas en un solo paso.
3.  **Manejo de Errores**: Se capturan explícitamente `httpx.TimeoutException` y `httpx.NetworkError` (que incluye errores de conexión, lectura, etc.).
4.  **Retry con Backoff**: El bucle `for` controla los intentos. Si ocurre un error, se calcula el tiempo de espera como $2^{intento}$ (ej. intento 1 = 2s, intento 2 = 4s) antes de volver a intentar. Si se agotan los intentos, se relanza la excepción para que el llamador sepa que falló.