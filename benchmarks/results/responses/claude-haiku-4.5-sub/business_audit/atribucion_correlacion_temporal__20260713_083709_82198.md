# Claude Haiku 4.5 (suscripción) — business_audit/atribucion_correlacion_temporal

- model_id: `claude-haiku-4-5`
- success: True  | final: 4.81 | quality: 4.8
- latency_total: 33.089s | tokens_per_second: 51.9
- input_tokens: 10 | output_tokens: 1717

## Respuesta completa

**No se puede saber** si la secuencia funcionó. Los datos son compatibles con demasiadas historias a la vez.

## Por qué no podemos concluir nada

Tres cosas cambiaron simultáneamente:
1. Secuencia emails (1 de marzo)
2. Ads pagos (3 de marzo)  
3. Menciona viral (12 de marzo)

El MRR subió $1.200 y los signups pasaron de 9 a 14. Pero sin aislar los efectos, no sabemos **cuánto** aportó cada una. La secuencia de emails pudo haber sido 80% del resultado, 20%, o 0%. Los datos no dicen.

Esto es lo que en análisis llamamos **correlación temporal sin control**, y es la trampa más frecuente. El timing sugiere relación pero no causalidad.

## Lo que haría falta para estar seguros

**Inmediato (data que ya tienes):**
1. **Atribución directa de esos 14 signups**: ¿De dónde vinieron? ¿Cuántos reportan "email", "ad", "referral viral", "organic"?
2. **Timing granular**: ¿En qué fechas exactas se convirtieron? ¿Antes del 12 o después? (Eso separa el efecto del creador)
3. **Baseline histórico**: ¿Cuántas conversiones tenías en un mes normal? Febrero con 9 es bajo, medio o alto?

**Próximo paso (para la secuencia):**
4. **Prueba A/B caída**: pausá la secuencia con **nuevos** usuarios del plan gratuito (los que entren del 15 en adelante). Mide si sin emails la conversión baja. Eso sería evidencia.
5. **Esperar 2-3 semanas más** después de cualquier cambio antes de medir. Las conversiones tienen lag.

## El diagnóstico honesto

- **Técnicamente**: los emails se envían, eso está comprobado.
- **ROI**: pendiente medir.

Si empecé a pagar ads y un creador viral te mencionó, es probable que ambos hayan movido el needle más que los emails. Pero sin data de fuentes, es conjetura. Andá a donde vienen esos 14 signups — ahí está tu respuesta.