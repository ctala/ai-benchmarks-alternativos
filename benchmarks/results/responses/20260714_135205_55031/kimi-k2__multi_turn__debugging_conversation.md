# Kimi K2 — multi_turn/debugging_conversation

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 7.28 | quality: 7.5
- latency_total: 8.982s | tokens_per_second: 31.6
- input_tokens: 386 | output_tokens: 284
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda y clara, ofreciendo una estrategia de reintento bien estructurada con backoff exponencial y jitter, que es directamente aplicable y útil para resolver el problema de la API.

## Respuesta completa

Ahi esta el problema - el retry infinito te esta baneando. Necesitas limitar los intentos y agregar backoff exponencial.

**Estructura basica de retry:**

```
intentos: max 3-5
delay inicial: 1 segundo
backoff: multiplicar x2 cada intento
```

**Logica:**

```
intento = 0
max_intentos = 3
delay = 1

mientras intento < max_intentos:
    intentar request
    si exito: retornar respuesta
    
    si error 429:
        intento += 1
        si intento >= max_intentos: lanzar error
        esperar delay segundos
        delay *= 2  # 1, 2, 4 segundos
        
    si otro error: lanzar error inmediatamente
```

**Puntos clave:**

- **Nunca** retry sin limite
- **Solo** retry 429, 503, 502 - errores 4xx definitivos (400, 401, 403) no retry
- **Jitter**: agregar random 0-1s al delay para evitar thundering herd

¿En que lenguaje lo estas implementando? Te doy codigo especifico.