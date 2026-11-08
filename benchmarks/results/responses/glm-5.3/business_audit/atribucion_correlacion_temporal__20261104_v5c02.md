# GLM 5.3 — business_audit/atribucion_correlacion_temporal

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.27 | quality: 10.0
- latency_total: 73.799s | tokens_per_second: 66.3
- input_tokens: 235 | output_tokens: 4895

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de datos de una empresa pequeña. Tu trabajo es proteger al equipo de conclusiones que los datos no sostienen. Prefieres decir 'no se puede saber' antes que dar una respuesta cómoda pero falsa.

**user:**

Tengo una comunidad de pago online. Te paso los números y quiero que me digas si la secuencia de emails automáticos que lancé funcionó.

- El 1 de marzo activé una secuencia de 5 emails para los usuarios del plan gratuito.
- MRR al 28 de febrero: $4.100
- MRR al 31 de marzo: $5.300 (+29%)
- Altas al plan pago en febrero: 9
- Altas al plan pago en marzo: 14

Contexto adicional: también el 3 de marzo empecé a pagar publicidad ($400 en el mes), y el 12 de marzo un creador con audiencia grande mencionó la comunidad en un video.

¿La secuencia de emails funcionó? Dame tu conclusión y qué haría falta para estar seguros.


## Respuesta completa

## Conclusión directa: no se puede saber

Con estos datos es imposible distinguir si la secuencia de emails aportó todo, algo, o nada. Y no es una respuesta cómoda, pero es la honesta. Te explico por qué y qué haría falta.

### Por qué estos datos no alcanzan

**1. Tres intervenciones en 11 días.** Emails (1 mar), publicidad (3 mar), mención del creador (12 mar). Todo lo que subió en marzo tiene al menos tres padres posibles. El mes no fue un experimento, fue un cóctel.

**2. Volúmenes demasiado chicos.** 9 vs 14 altas. Con números de ese tamaño, un salto así ocurre por puro azar con bastante frecuencia (la variación mensual esperada ronda ±3). Incluso sin confusores, esto no alcanzaría para afirmar efecto.

**3. Los agregados no descomponen.** El MRR subió $1.200, pero no sabemos cuánto vino de altas nuevas, upgrades o menos churn. Y de las 14 altas, no sabemos cuántas eran usuarios gratuitos previos (expuestos a los emails) versus gente nueva que llegó por los ads o el video y compró directamente.

Lo único que los datos sostienen: **marzo fue un buen mes en conjunto**. Eso es todo. (Ojo: la misma incertidumbre aplica a los $400 de publicidad — tampoco puedes saber si funcionaron.)

### Qué revisar hoy con datos que probablemente ya tienes

- **Para cada una de las 14 altas:** ¿era usuario gratuito antes del 1 de marzo? ¿Cuándo se registró? ¿De dónde vino (UTM, referral)?
- **Del lado de emails:** quién abrió/clickeó y cuándo, cruzado con la fecha de conversión. ¿Las conversiones se agrupan en los días posteriores a cada email, o después del 12 de marzo?
- **Tasa de conversión gratuito→pago:** tamaño del pool gratuito en febrero vs. marzo. Si el video infló el pool, el conteo bruto de altas engaña; la tasa es lo comparable.
- **Descomposición del MRR:** altas nuevas, upgrades, churn.

**Cómo lo interpretarías:** si la mayoría de las 14 altas eran gratuitos previos al 1 de marzo, con actividad de email antes de convertir y conversiones dentro de la ventana de la secuencia → evidencia razonable (no prueba) de que la secuencia aportó. Si la mayoría se registró después del 3 o del 12 de marzo desde tráfico nuevo → el mérito probablemente es de los otros canales.

### Para la próxima (esto es lo importante)

- **Grupo de control.** Antes de lanzar cualquier campaña, excluye aleatoriamente al 10–20% de los usuarios gratuitos de la secuencia. La diferencia de conversión entre grupos es la única medida limpia que existe.
- **No apiles lanzamientos.** Emails, ads y colaboración en el mismo mes hicieron imposible la atribución. Sepáralos 3–4 semanas entre sí.
- **Trackear la fuente desde el primer click** (UTMs en ads y en el link del video si es posible).

Una última nota honesta: incluso el análisis retrospectivo tendrá zonas grises. Alguien que llegó por el video, se hizo gratuito y convirtió tras el email 2 tiene mérito compartido. La atribución perfecta no existe; el holdout sí te da una respuesta defendible.