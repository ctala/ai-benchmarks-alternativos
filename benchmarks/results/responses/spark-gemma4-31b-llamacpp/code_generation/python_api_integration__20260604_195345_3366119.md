# Gemma 4 31B (Spark llama-server Q4_K_M) — code_generation/python_api_integration

- model_id: `gemma-4-31B-it-Q4_K_M.gguf`
- success: True  | final: 8.02 | quality: 9.72
- latency_total: 87.677s | tokens_per_second: 9.9
- input_tokens: 117 | output_tokens: 865
- judge_score: 4.8 | justificación: 

## Respuesta completa

Para implementar esta funcionalidad, utilizaremos `httpx` junto con el módulo estándar `time` para gestionar el backoff exponencial.

Aquí tienes el código completo y detallado:

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    max_retries = 3
    timeout = 10.0
    
    # Usamos un cliente para reutilizar conexiones
    with httpx.Client(timeout=timeout) as client:
        for attempt in range(max_retries):
            try:
                response = client.get(url, headers=headers)
                
                # Lanza excepción si el status code es 4xx o 5xx
                response.raise_for_status()
                
                # Si llegamos aquí, la petición fue exitosa
                products = response.json()
                
                # 2. Filtro de precio > 100 y 3. Proyección de campos {id, name, price}
                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products 
                    if p.get("price", 0) > 100
                ]

            except (httpx.RequestError, httpx.HTTPStatusError) as exc:
                # Manejo de errores de red, timeout y errores HTTP
                is_last_attempt = attempt == max_retries - 1
                
                if is_last_attempt:
                    print(f"Error final después de {max_retries} intentos: {exc}")
                    raise exc
                
                # 5. Backoff exponencial: 2^attempt segundos (1s, 2s, 4s...)
                wait_time = 2 ** attempt
                print(f"Intento {attempt + 1} fallido. Reintentando en {wait_time}s...")
                time.sleep(wait_time)

# Ejemplo de uso
if __name__ == "__main__":
    TOKEN = "tu_token_aqui"
    try:
        result = get_expensive_products(TOKEN)
        print("Productos filtrados:", result)
    except Exception as e:
        print("No se pudieron obtener los productos:", e)
```

### Explicación de los puntos solicitados:

1.  **Autenticación Bearer**: Se implementa pasando el header `Authorization: Bearer <token>` en la petición GET.
2.  **Filtro de precio**: Se utiliza una *list comprehension* que evalúa `if p.get("price", 0) > 100`. El uso de `.get()` evita que el código rompa si un producto no tiene la clave "price".
3.  **Retorno simplificado**: En la misma *list comprehension*, se crean nuevos diccionarios conteniendo únicamente las llaves `id`, `name` y `price`.
4.  **Errores y Timeout**: 
    *   Se define `timeout=10.0` en el cliente de `httpx`.
    *   Se capturan `httpx.RequestError` (problemas de red/DNS/timeout) y `httpx.HTTPStatusError` (errores del servidor como 500 o 404 mediante `raise_for_status()`).
5.  **Retry con Backoff Exponencial**: 
    *   Se implementa un bucle `for` hasta el máximo de intentos.
    *   `time.sleep(2 ** attempt)` calcula el tiempo de espera exponencialmente ($2^0=1$, $2^1=2$, $2^2=4$).