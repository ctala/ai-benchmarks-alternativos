# Devstral 2 (Dic 2025) — content_verificable/audiencia_que_ya_sabe

- model_id: `mistralai/devstral-2512`
- success: True  | final: 8.98 | quality: 10.0
- latency_total: 5.409s | tokens_per_second: 74.7
- input_tokens: 105 | output_tokens: 404
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza en las causas y soluciones, ofreciendo utilidad práctica para la audiencia experta.

## Respuesta completa

**¿Por qué tu workflow dice "success" pero no hizo nada?**

Si alguna vez has visto un workflow en n8n marcarse como *success* sin ejecutar ninguna acción, no estás solo. Este comportamiento puede ser frustrante, pero tiene explicación. Aquí te cuento por qué pasa y cómo detectarlo.

### **Causas comunes**
1. **Nodos condicionales que no se activan**: Si usas un *IF* o un *Switch* y ninguna condición se cumple, el workflow termina sin errores, pero sin hacer nada.
2. **Datos vacíos o filtrados**: Un *Set* o *Function* que devuelve `null` o un array vacío puede hacer que nodos posteriores no se ejecuten.
3. **Webhooks sin payload**: Si un webhook recibe una petición vacía o mal formada, el workflow puede completarse sin procesar datos.
4. **Errores silenciosos**: Algunos nodos (como HTTP Request) pueden fallar sin lanzar un error explícito si no están configurados para hacerlo.

### **Cómo detectarlo**
- **Revisa los logs de ejecución**: Fíjate en los datos de entrada/salida de cada nodo. Si un nodo no tiene salida, algo falló antes.
- **Usa nodos de depuración**: Un *Function* con `console.log()` o un *Set* que muestre variables clave te ayuda a rastrear el flujo.
- **Prueba con datos de ejemplo**: Ejecuta el workflow manualmente con payloads controlados para ver dónde se rompe.
- **Añade validaciones explícitas**: Usa un *IF* para verificar si los datos existen antes de continuar.

Si tu workflow sigue "mintiendo" con el *success*, revisa estos puntos. A menudo, el problema está en un nodo que no hace lo que esperabas. ¿Te ha pasado? ¡Cuéntame en los comentarios!