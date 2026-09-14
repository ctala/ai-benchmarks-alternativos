# DeepSeek V4.1 Flash — code_generation/python_api_integration

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.1 | quality: 9.08
- latency_total: 48.191s | tokens_per_second: 147.9
- input_tokens: 136 | output_tokens: 7126
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

```python
import time
import httpx

def obtener_productos_caros(token: str, max_intentos: int = 3) -> list[dict]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)

    with httpx.Client(timeout=timeout) as client:
        for intento in range(1, max_intentos + 1):
            try:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()

                if not isinstance(data, list):
                    raise ValueError("La respuesta de /products no es una lista")

                resultado = []
                for item in data:
                    if not isinstance(item, dict):
                        continue

                    price = item.get("price")
                    if isinstance(price, (int, float)) and price > 100:
                        resultado.append({
                            "id": item.get("id"),
                            "name": item.get("name"),
                            "price": price,
                        })

                return resultado

            except httpx.RequestError as exc:
                # RequestError incluye TimeoutException y NetworkError.
                if intento == max_intentos:
                    raise RuntimeError(
                        f"Error de red o timeout tras {max_intentos} intentos"
                    ) from exc

                # Backoff exponencial: 1s, 2s, 4s...
                time.sleep(2 ** (intento - 1))
```

Notas:
- Usa `httpx.Client` con `timeout=10.0`.
- El token se envía como `Authorization: Bearer <token>`.
- Filtra productos con `price > 100`.
- Devuelve solo `{id, name, price}`.
- Reintenta hasta 3 veces con espera exponencial.
- Los errores de red/timeout se reintentan; si se agotan, se lanza `RuntimeError`.