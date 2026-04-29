# Gemma 4 31B (NIM) — code_generation/python_api_integration

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 7.7 | quality: 9.72
- latency_total: 82.099s | tokens_per_second: 10.7
- input_tokens: 115 | output_tokens: 881
- judge_score: 4.8 | justificación: 

## Respuesta completa

Para implementar esta funcionalidad con `httpx`, utilizaremos un bucle para manejar los reintentos y el cálculo de tiempo para el backoff exponencial.

Aquí tienes el código completo y profesional:

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos de la API, filtra los que cuestan más de 100 
    y retorna solo id, name y price.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    max_retries = 3
    timeout = 10.0
    
    # Usamos un cliente para optimizar las conexiones
    with httpx.Client() as client:
        for attempt in range(max_retries):
            try:
                response = client.get(
                    url, 
                    headers=headers, 
                    timeout=timeout
                )
                # Levanta excepción si el status code es 4xx o 5xx
                response.raise_for_status()
                
                # Si llegamos aquí, la petición fue exitosa
                products = response.json()
                
                # Filtrado y transformación en una sola comprensión de lista
                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products 
                    if p.get("price", 0) > 100
                ]

            except (httpx.RequestError, httpx.HTTPStatusError) as e:
                # Si es el último intento, lanzamos el error
                if attempt == max_retries - 1:
                    print(f"Error final tras {max_retries} intentos: {e}")
                    raise e
                
                # Backoff exponencial: 2^0=1s, 2^1=2s, 2^2=4s...
                wait_time = 2 ** attempt
                print(f"Intento {attempt + 1} fallido. Reintentando en {wait_time}s...")
                time.sleep(wait_time)

# Ejemplo de uso
if __name__ == "__main__":
    try:
        mi_token = "tu_token_aqui"
        resultado = get_expensive_products(mi_token)
        print(resultado)
    except Exception as e:
        print(f"La función falló: {e}")
```

### Explicación de los puntos clave:

1.  **Autenticación**: Se pasa el token en el header `Authorization` siguiendo el estándar `Bearer <token>`.
2.  **Filtrado y Mapeo**: Utilicé una *list comprehension* para hacer ambas tareas en un solo paso: verifica que el precio sea `> 100` y construye el nuevo diccionario solo con las llaves solicitadas.
3.  **Manejo de Errores y Timeout**:
    *   `timeout=10.0`: Limita la espera a 10 segundos.
    *   `response.raise_for_status()`: Asegura que errores como 404 o 500 sean capturados por el bloque `except`.
    *   `httpx.RequestError`: Captura problemas de red, DNS o timeouts.
4.  **Retry con Backoff Exponencial**:
    *   El bucle `for attempt in range(max_retries)` controla los intentos.
    *   `time.sleep(2 ** attempt)` implementa la espera exponencial (1s, 2s, 4s...), evitando saturar el servidor si este está caído.
5.  **Eficiencia**: El uso de `with httpx.Client()` es la forma recomendada de usar la librería para gestionar correctamente el pool de conexiones.