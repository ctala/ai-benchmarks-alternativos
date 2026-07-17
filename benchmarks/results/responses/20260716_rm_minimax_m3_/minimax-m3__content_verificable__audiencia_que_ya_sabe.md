# MiniMax M3 — content_verificable/audiencia_que_ya_sabe

- model_id: `minimax/minimax-m3`
- success: True  | final: 8.86 | quality: 10.0
- latency_total: 12.95s | tokens_per_second: 146.0
- input_tokens: 260 | output_tokens: 1891
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para expertos en n8n, abordando directamente el problema y ofreciendo soluciones prácticas.

## Respuesta completa

# Tu workflow dijo "Success". No hizo nada.

Esto me ha mordido demasiadas veces. El run sale verde, el icono feliz, el cliente tranquilo. Y cuando vas a mirar, nada se escribió, nada se envió, nada cambió en producción.

**¿Por qué pasa?** Tres patrones principales:

**1. Ramas que nunca se ejecutan.** Un IF con la condición al revés, un Switch sin default que matchea cualquier cosa, un Merge en modo "Append" que descarta items. La rama "feliz" simplemente no corre. n8n marca Success porque las ramas existentes terminaron sin error.

**2. Datos vacíos propagados.** Un Code node que devuelve `[]`, un HTTP Request mal parametrizado que responde 200 con body vacío, un Webhook que recibe `{test: true}` en producción. El nodo siguiente recibe cero items y sale por la ruta vacía.

**3. Errores tragados silenciosamente.** `Continue on Fail` activado a nivel workflow + nodo que falla sin reventar la ejecución. Success de cara, cero efectos de facto.

**Cómo detectarlo sin volverte paranoico:**

- **Nodo centinela** al final de cada rama crítica: Set → Postgres, una fila en una hoja, un POST a un endpoint propio. Si no aparece, esa rama no corrió aunque el workflow diga success.
- **Revisa la pestaña Executions** y expande nodo por nodo. Un nodo sin datos de salida = la rama murió silenciosamente.
- **Compara executions vs. triggers esperados.** Si cuadran los runs pero no los efectos downstream, el fantasma está en tu branching.
- **Valida el response después del nodo.** Un 200 con `body.results = []` no es éxito: es vacío.

**Regla de oro:** "Success" en n8n significa "ningún nodo lanzó un throw", no "se hizo lo que querías". Diseña en consecuencia.