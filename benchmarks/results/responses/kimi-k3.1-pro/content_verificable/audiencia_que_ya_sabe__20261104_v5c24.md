# Kimi K3.1 Pro — content_verificable/audiencia_que_ya_sabe

- model_id: `moonshotai/kimi-k3.1-pro`
- success: True  | final: 7.85 | quality: 10.0
- latency_total: 143.007s | tokens_per_second: 27.6
- input_tokens: 204 | output_tokens: 3945

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

## El check verde también puede ser un *no-op*

En n8n, `success` significa que la ejecución terminó sin un error no controlado. No certifica que hubiera trabajo, que los items tomaran la rama correcta ni que el destino persistiera algo.

Los agujeros habituales:

- Un **Filter/IF/Switch** deja cero items; los nodos siguientes no se ejecutan y todo queda verde.
- **Continue On Fail** o una salida de error convierte la excepción en un camino válido, pero sin efecto ni alerta.
- La API responde `200` con errores en el body —GraphQL y endpoints bulk son clásicos—; el nodo HTTP celebra y nadie revisa el payload.
- Un cursor, una ventana temporal o un filtro de origen devuelven vacío: ejecución impecable, trabajo inexistente.
- Si respondes inmediatamente al caller, ese `200` confirma recepción, no finalización.

La defensa es medir resultados, no nodos:

1. **Contabiliza** `received`, `eligible`, `written`, `skipped` y `failed`; cada descarte necesita `reason`. Al final, valida invariantes como `received = written + skipped + failed`.
2. **Inspecciona respuestas de negocio** y, en escrituras críticas, haz *read-after-write* o confirma los IDs devueltos. Un `2xx` no basta.
3. **Convierte las violaciones en error real**: `Stop and Error`, alerta con execution ID. Un *no-op* legítimo debe reportar `skipped_empty` o `no_input`, nunca camuflarse de éxito operativo.
4. **Mira desde fuera**: alerta sobre ejecuciones exitosas con cero escrituras, caídas frente a la línea base y ausencia de heartbeats. Si el trigger deja de disparar, tus contadores internos tampoco te salvarán.

El verde es telemetría de ejecución. La evidencia es otra cosa: «37 recibidos, 35 persistidos, 2 duplicados».