# MiniMax M3 — business_audit/atribucion_correlacion_temporal

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.66 | quality: 8.4
- latency_total: 13.963s | tokens_per_second: 92.0
- input_tokens: 373 | output_tokens: 1284
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando un análisis detallado y práctico sobre la imposibilidad de atribuir el crecimiento a la secuencia de correos electrónicos sin más datos.

## Respuesta completa

## Conclusión corta: no se puede saber

Los datos que me pasás muestran crecimiento, pero **no permiten atribuir ese crecimiento a la secuencia de emails**. Hay al menos tres causas mezcladas en marzo y no hay forma de separarlas con lo que tenemos.

## Por qué los números no bastan

Los eventos relevantes de marzo fueron tres, casi simultáneos:

| Evento | Fecha | Efecto esperado |
|---|---|---|
| Secuencia de 5 emails | 1 marzo | Mejora conversión free → pago |
| Publicidad paga ($400) | 3 marzo | Más usuarios free entrando al funnel |
| Mención de creador grande | 12 marzo | Pico de tráfico orgánico/free |

Las conversiones subieron de 9 a 14 (+55%) y el MRR +29%. Pero cualquiera de las tres cosas —o las tres juntas— pudo causarlo. Incluso es plausible que el video del 12 de marzo haya traído tantos usuarios nuevos al plan gratuito que la secuencia los convirtió, sin que la secuencia en sí haya mejorado la tasa de conversión.

**Dato clave que falta: de dónde vinieron los 14 nuevos pagos.** Si la mayoría venía de usuarios que se registraron después del 12 de marzo, es más probable que el mérito sea del video. Si muchos eran usuarios free preexistentes a marzo, la secuencia es candidata más fuerte.

## Qué haría falta para estar seguros

1. **Grupo de control (holdout test):** dejar a un % de usuarios free sin recibir la secuencia (idealmente 10-20%), comparar conversión contra los que sí la recibieron. Esto es lo único que aísla el efecto del email.
2. **Atribución por fuente de registro:** taggear a cada usuario según cómo llegó (ad, referencia del video, orgánico, etc.) y cruzar con si convirtió.
3. **Separar nuevos free de usuarios preexistentes:** la secuencia apunta a gente ya dentro, así que hay que distinguir conversión de "viejos free" vs. "free que entraron este mes y convirtieron rápido".
4. **Medir conversión por cohorte, no solo totales:** febrero convirtió al X% de sus free, marzo al Y%. Si Y es claramente mayor con tamaño de muestra razonable, es indicio —no prueba— de que algo funcionó.

## Lo que sí te puedo decir (con cuidado)

- No hay señal de que la secuencia haya *dañado*: el negocio creció.
- Tampoco hay señal de que haya *sido necesaria*: con la mención del creador, probablemente habría crecido igual o más.
- El testeo serio conviene hacerlo en un mes "limpio" (sin viralidad ni cambios grandes) o con un grupo de control activo, porque abril o mayo van a traer nuevos confounders y vas a seguir sin poder aislar el efecto.

Si querés, podemos diseñar cómo correr un A/B test simple sobre esa misma secuencia a partir de ahora para tener la respuesta que hoy no se puede dar.