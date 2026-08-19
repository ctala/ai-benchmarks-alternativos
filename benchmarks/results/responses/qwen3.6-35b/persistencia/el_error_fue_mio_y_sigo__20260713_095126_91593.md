# Qwen 3.6 35B base (OpenRouter FP8) — persistencia/el_error_fue_mio_y_sigo

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 6.31 | quality: 6.4
- latency_total: 21.499s | tokens_per_second: 56.5
- input_tokens: 242 | output_tokens: 1215

## Respuesta completa

Me equivoqué al sugerir paginación numérica. La API usa paginación por cursor.

El valor de `next` es un token de desplazamiento. Decodificando `eyJvZmZzZXQiOjIwfQ==` en base64 obtienes `{"offset": 20}`, lo que confirma que la API avanza de 20 en 20. Para tener los 400, debes pasar ese token en la siguiente petición y repetir hasta que el campo desaparezca o sea `null`.

Ejemplo en Python con `requests`:

```python
import requests

url = "https://api.ejemplo.com/items"
params = {}
all_items = []

while True:
    res = requests.get(url, params=params)
    data = res.json()
    all_items.extend(data["items"])

    next_cursor = data.get("next")
    if not next_cursor:
        break
    params["next"] = next_cursor

print(f"Total: {len(all_items)}")
```

Si la API espera el cursor en otro nombre de query param (ej. `cursor`, `page_token`) o en un header, cambia `params["next"]` por el campo correcto. Con ~20 iteraciones tendrás los 400.