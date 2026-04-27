# Gemini 3.1 Pro — code_generation/python_api_integration

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 6.42 | quality: 7.48
- latency_total: 18.805s | tokens_per_second: 108.7
- input_tokens: 105 | output_tokens: 2044
- judge_score: 4.0 | justificación: 

## Respuesta completa

Aquí tienes la función implementada en Python cumpliendo con todos tus requisitos. 

Utiliza la librería `httpx` para las peticiones y la librería estándar `time` para implementar el *exponential backoff*.

### Código de la función

```python
import time
import httpx
from typing import List, Dict, Any

def get_expensive_products(token: str) -> List[Dict[