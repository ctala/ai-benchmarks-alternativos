# Mistral Nemo — code_generation/python_api_integration

- model_id: `mistralai/mistral-nemo`
- success: True  | final: 7.28 | quality: 8.24
- latency_total: 16.413s | tokens_per_second: 27.1
- input_tokens: 105 | output_tokens: 445
- judge_score: 4.2 | justificación: 

## Respuesta completa

Aquí está una posible implementación de la función solicitada:
```python
import httpx
from typing import List, Dict
import time

def get_products() -> List[Dict[str, int]]:
    url = "https://api.example.com/products"
    headers = {"Authorization": "Bearer token"}
    retries = 3
    client = httpx.Client()

    for i in range(retries):
        try:
            response = client.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except (httpx.HTTPStatusError, httpx.ReadTimeout) as exc:
            print(f"Error en la solicitud GET: {exc}")
            time.sleep(2 ** i)  # backoff exponencial
            continue

        products = response.json()
        filtered_products = [{'id': p['id'], 'name': p['name'], 'price': p['price']} for p in products if p['price'] > 100]
        return filtered_products
    else:
        print("Se han agotado los intentos de solicitud GET.")
        return []
```
Explicación del código:

* Se importa la librería httpx y se definen los tipos de retorno y entrada de la función.
* Se define la URL del endpoint y los encabezados de autenticación.
* Se define el número máximo de intentos de solicitud GET y se crea un objeto cliente de httpx.
* Se itera sobre el número de intentos de solicitud GET, en caso de errores de red o timeout, se imprime el error, se espera un tiempo exponencialmente mayor en cada intento y se continúa con el siguiente intento.
* Si se realiza la solicitud GET con éxito, se analiza la respuesta JSON, se filtra la lista de productos para incluir solo aquellos con precio mayor a 100 y se devuelve una lista de diccionarios con solo los campos 'id', 'name' y 'price'.
* Si se agotan los intentos de solicitud GET, se imprime un mensaje de error y se devuelve una lista vacía.