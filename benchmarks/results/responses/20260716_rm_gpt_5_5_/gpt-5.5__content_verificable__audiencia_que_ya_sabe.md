# GPT-5.5 — content_verificable/audiencia_que_ya_sabe

- model_id: `gpt-5.5`
- success: True  | final: 8.32 | quality: 10.0
- latency_total: 11.264s | tokens_per_second: 50.4
- input_tokens: 101 | output_tokens: 568
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, abordando directamente el problema con soluciones prácticas y ejemplos específicos.

## Respuesta completa

Un workflow en n8n puede terminar en verde y aun así no haber hecho nada útil. No es un bug: normalmente significa que **no hubo una excepción no controlada**, no que el objetivo de negocio se haya cumplido.

Casos típicos:

- Un `IF`, `Switch` o filtro deja pasar **0 items** y el resto del flujo simplemente no se ejecuta.
- Un nodo tiene `Continue On Fail` activado y el error queda convertido en dato.
- Una API responde `200`, `202` o `204`, pero no crea/actualiza nada.
- Un `Merge`, `Split in Batches` o paginación termina con una colección vacía.
- Un nodo hace “upsert”, pero todos los registros ya existían y no hubo cambios.
- Estás validando que “la llamada funcionó”, no que “el efecto ocurrió”.

La forma práctica de detectarlo es tratar el éxito como una condición explícita, no como el estado final de la ejecución.

Algunas defensas útiles:

1. **Cuenta items en puntos críticos**  
   Después de filtros, búsquedas o merges, calcula `items.length`. Si esperabas al menos uno, falla el workflow.

2. **Añade nodos de aserción**  
   Un `IF` con condición tipo: “si `updated_count === 0`, lanzar error”. Puedes usar `Stop and Error` para que el verde no maquille un no-op.

3. **Comprueba efectos, no respuestas**  
   Después de escribir en Airtable, Sheets, Postgres, HubSpot, etc., haz una lectura de verificación. Si el registro no cambió, eso no es success.

4. **Loguea métricas de negocio**  
   No solo “execution finished”. Guarda: recibidos, filtrados, creados, actualizados, ignorados, errores.

5. **Diferencia vacío esperado vs vacío sospechoso**  
   Un cron que no encuentra nada puede ser correcto. Un webhook de pedido que no crea pedido, no.

En n8n, verde significa “no explotó”. Tu trabajo es definir qué significa “hizo algo”.