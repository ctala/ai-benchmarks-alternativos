# Llama 3.1 8B Instant (Groq) — code_generation/python_api_integration

- model_id: `llama-3.1-8b-instant`
- success: True  | final: 7.99 | quality: 8.68
- latency_total: 1.268s | tokens_per_second: 558.3
- input_tokens: 136 | output_tokens: 708
- judge_score: 4.2 | justificación: 

## Respuesta completa

A continuación, te muestro una función que cumple con los requisitos establecidos:

```python
import httpx
import time

def get_productos():
    # Configuración de tokens y URL
    url = "https://api.example.com/products"
    token = "TU_TOKEN_AQUI"  # Reemplaza con tu token de autenticación
    
    # Configuración de retry con backoff exponencial
    max_intentos = 3
    backoff_exp = 2  # Factor de backoff exponencial
    backoff_initial = 0.5  # Tiempo inicial en segundos

    # Configuración de timeout
    timeout = 10  # Tiempo de espera en segundos

    # Intentos de conexión
    for intento in range(max_intentos):
        try:
            # Configuración de headers con token
            headers = {"Authorization": f"Bearer {token}"}
            
            # Realización de GET con retry y timeout
            response = httpx.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()  # Lanza error si la respuesta no es 200
            
            # Filtro de productos con precio > 100
            productos = [p for p in response.json() if p['price'] > 100]
            
            # Retorno de lista con id, name y price
            return [{k: p[k] for k in ['id', 'name', 'price']} for p in productos]
        
        except httpx.HTTPError as e:
            # Manejo de errores HTTP
            print(f"Error HTTP: {e}")
            if intento < max_intentos - 1:
                # Espera antes de intentarlo nuevamente
                tiempo_espera = backoff_exp ** intento * backoff_initial
                print(f"Intentando de nuevo en {tiempo_espera} segundos...")
                time.sleep(tiempo_espera)
        
        except httpx.TimeoutException:
            # Manejo de timeout
            print("Timeout excedido. Intentando de nuevo...")
            if intento < max_intentos - 1:
                # Espera antes de intentarlo nuevamente
                tiempo_espera = backoff_exp ** intento * backoff_initial
                print(f"Intentando de nuevo en {tiempo_espera} segundos...")
                time.sleep(tiempo_espera)
        
        except Exception as e:
            # Manejo de errores generales
            print(f"Error general: {e}")

# Llamada a la función
productos = get_productos()
print(productos)
```

En este ejemplo, la función `get_productos` realiza un GET a la URL especificada con autenticación Bearer token. Si el servidor devuelve una respuesta no 200, lanza un error HTTP. Si el servidor no responde dentro del tiempo de espera, lanza un timeout. En ambos casos, la función intenta nuevamente con un backoff exponencial. Si se alcanza el número máximo de intentos, la función devuelve None.

La lista de productos se filtra para incluir solo aquellos con precio mayor a 100. La lista resultante se devuelve con solo los campos id, name y price.

Recuerda reemplazar `TU_TOKEN_AQUI` con tu token de autenticación real.