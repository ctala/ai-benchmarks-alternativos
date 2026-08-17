# MiniMax M2.5 — content_verificable/audiencia_que_ya_sabe

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 8.82 | quality: 10.0
- latency_total: 15.767s | tokens_per_second: 41.5
- input_tokens: 104 | output_tokens: 654
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza en la detección de problemas en workflows de n8n, ofreciendo consejos prácticos útiles para la audiencia experta.

## Respuesta completa

El workflow dice "success" y no hizo nada. Otra vez.

Esto nos pasa a todos, y es más común de lo que parece. El problema: n8n marca como exitoso todo lo que no explota. Un IF que no se cumple, un webhook que recibe vacío, un Error Trigger que nunca dispara... todo eso termina en ✓ verde.

**Por qué pasa**

El ejecutor de n8n distingue entre "el workflow corrió sin errores" y "el workflow hizo lo que debía". Son cosas distintas. Cuando una condición no se cumple, el flujo simplemente se bifurca y sigue su camino. No hay mensaje de error, no hay alerta. Solo un ✓ que te miente.

Otros casos típicos:

- Un nodo anterior falla silenciosamente porque pusiste "continue on fail" y no revisaste el output
- Tu workflow espera datos que nunca llegan (y el resto de nodos procesan vacío)
- Un Error Workflow que no está configurado, así que los errores pasan desapercibidos

**Cómo detectarlo**

1. **Añade nodos de verificación.** Un Count después de tu búsqueda principal. Si devuelve 0, que te avise.

2. **Monitorea ejecuciones vs. resultados útiles.** No basta con saber si corrió. Necesitas saber si procesó algo. Un simple IF después del paso crítico, con una alerta si no hubo "hits", salva horas de debug.

3. **Revisa los Output de los nodos.** Sempre. Especialmente los que dependen de datos externos.

El verde no significa que todo esté bien. Significa que no explotó. diferencia las dos cosas.