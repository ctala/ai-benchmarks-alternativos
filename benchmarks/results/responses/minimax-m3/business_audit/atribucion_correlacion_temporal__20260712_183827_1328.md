# MiniMax M3 — business_audit/atribucion_correlacion_temporal

- model_id: `minimax/minimax-m3`
- success: True  | final: 6.11 | quality: 6.0
- latency_total: 13.616s | tokens_per_second: 101.4
- input_tokens: 373 | output_tokens: 1380

## Respuesta completa

**Conclusión corta: con estos números, no se puede afirmar que la secuencia de emails funcionó.** Tampoco se puede afirmar que no funcionó. Lo que sí se puede decir es que la atribución que estás intentando hacer no se sostiene.

## Por qué no se puede saber

Tienes **dos confounders importantes** metidos en el mismo mes que los emails:

1. **El creador que te mencionó el 12 de marzo.** Una mención así suele generar un spike de tráfico y conversiones que puede explicar buena parte (o todo) del salto de 9 a 14 altas.
2. **La publicidad de $400.** También es un candidato perfectamente válido para explicar el aumento.

Los emails fueron una **causa concurrente más**, no la causa aislada. Estás viendo una foto del resultado agregado sin poder separar qué foto es de quién.

Además:

- **Muestras muy pequeñas.** Pasar de 9 a 14 altas no es estadísticamente concluyente ni en un sentido ni en otro.
- **No mencionas métricas de los emails**: tasa de entrega, apertura, clics, conversiones atribuidas al email. Sin eso, ni siquiera sabemos si los emails llegaron y fueron leídos.
- **El MRR +29% mezcla demasiadas cosas**: altas nuevas, posibles upgrades, expansión de revenue, cambios en churn. No es atribuible a un solo factor.

## Qué haría falta para estar seguros

En orden de importancia:

1. **Atribución por fuente.** Etiquetar de dónde vino cada alta: email, ad, mención del creador, orgánico. Sin esto, estás adivinando.
2. **Métricas internas de la secuencia**: aperturas, clics, y especialmente **cuántos de los 14 convirtieron y habían recibido la secuencia**. Esta es la pregunta clave y los datos que pasaste no la responden.
3. **Un grupo de control (holdout test)**: aunque sea un 10–20% de usuarios del plan gratuito que no reciban la secuencia, para comparar conversión contra los que sí la recibieron. Esto aísla el efecto del email del ruido externo.
4. **Observar abril**. Si el efecto del creador se diluye y la publicidad sigue corriendo pero las altas bajan respecto a marzo, tendrías una pista. Si se mantienen, es más probable que los emails estén haciendo algo.

## Lo que haría yo

No gastaría tiempo defendiendo ante el equipo que "los emails funcionaron" basándome en estos datos. Reportaría el crecimiento del 29% como **resultado del mes**, listando los tres factores (secuencia, ads, mención del creador), y propondría montar el holdout test este mes para tener una respuesta real en abril o mayo.

Decir "los emails funcionaron" con estos números es la respuesta cómoda, y es exactamente el tipo de conclusión que los datos no sostienen.