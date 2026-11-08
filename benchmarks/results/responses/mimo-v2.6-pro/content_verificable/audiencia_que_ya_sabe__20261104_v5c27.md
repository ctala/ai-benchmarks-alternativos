# MiMo V2.6 Pro — content_verificable/audiencia_que_ya_sabe

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 8.72 | quality: 10.0
- latency_total: 23.094s | tokens_per_second: 21.1
- input_tokens: 107 | output_tokens: 488

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Tu workflow dice 'success' y no hizo nada. Y ni te enteraste.**

Ejecutaste. Corrió. Status: 200. Todo verde. ¿Seguro?

Es el fallo silencioso más caro de n8n. El workflow termina sin error porque, técnicamente, no hay error. Hay un array vacío, un `null` que pasó como válido, un filtro que descartó todo antes del nodo que importa. n8n ve ejecución completa. Tú ves trabajo hecho. Nadie hizo nada.

Tres escenarios donde esto ocurre constantemente:

**1. El filtro elimina todo y nadie lo nota.**
`If` o `Filter` con condición que matchea cero items. El downstream simplemente no se ejecuta — no falla, no avisa. Verifica con un nodo final que compruebe `items.length > 0` y lance un error explícito.

**2. El HTTP node devuelve 200 con un body basura.**
APIs que responden `{"data": [], "status": "ok"}` cuando no encuentran nada. Tu workflow sigue adelante como si hubiera procesado records. Valida la estructura del response con `IF` antes de continuar.

**3. El `Set` / `Code` node fabrica datos.**
Un error de sintaxis en expresión devuelve `undefined`, y el nodo lo escribe silencioso como string. Revisa los outputs node por node en la pestaña de datos. No en la interfaz — en los datos.

**Cómo blindarlo:**

Añade un nodo `Check` al final de cada rama crítica. Una expresión mínima:

```js
if (!items.length) throw new Error('Rama vacía')
```

Y activa los **workflow error triggers**. Pero eso cubre errores reales. Para los falsos positivos, necesitas validación *explícita de output*.

Un workflow que no falla no es un workflow que funciona.

— Nos vemos el jueves.