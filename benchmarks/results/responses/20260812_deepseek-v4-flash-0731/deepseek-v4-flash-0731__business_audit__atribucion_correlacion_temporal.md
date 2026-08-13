# DeepSeek V4 Flash 0731 — business_audit/atribucion_correlacion_temporal

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 9.17 | quality: 10.0
- latency_total: 14.827s | tokens_per_second: 67.2
- input_tokens: 314 | output_tokens: 997

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

Con los datos que me das, **no se puede concluir que la secuencia de emails funcionó**. Lo único que se puede decir es que el MRR subió y que hubo más altas en marzo que en febrero, pero hay al menos dos variables que se movieron a la vez y que explican igual de bien (o mejor) ese cambio:

- **Publicidad pagada desde el 3 de marzo ($400)**
- **Mención de un creador con audiencia grande el 12 de marzo**

Cualquiera de esas dos pudo generar las altas adicionales. También pudieron hacerlo los emails. Pero con un solo mes de datos y sin saber qué altas vinieron de qué canal, es imposible separar el efecto.

Además, ojo con lo que miden los números:

- **MRR**: sube por altas, pero también por upgrades de planes existentes, y baja por bajas o downgrades. Un +29% puede venir por muchas vías, no solo por conversiones de plan gratuito.
- **Altas**: 9 → 14 son 5 altas más. Es un cambio pequeño en términos absolutos. Con números tan bajos, una sola mención viral o un par de compras por anuncios ya explican el incremento sin necesidad de que los emails hayan hecho nada.

## Qué haría falta para estar seguros

1. **Atribución por fuente**: saber si cada nueva alta llegó por email, por anuncio, por el video del creador, por búsqueda orgánica, etc. Idealmente con UTM o preguntando al usuario.
2. **Grupo de control**: por ejemplo, retrasar la secuencia de emails a un subgrupo aleatorio de usuarios gratuitos y comparar conversión entre quienes la recibieron y quienes no. Eso aísla el efecto real.
3. **Datos de comportamiento dentro del email**: aperturas, clics, qué enlaces tocaron y si esos clics terminaron en pago.
4. **Serie temporal más larga y granularidad**: saber en qué días exactos de marzo ocurrieron las altas. Si todas fueron después del 12, apunta al creador. Si fueron repartidas durante todo el mes, puede que los emails ayudaran. Pero incluso eso no es prueba definitiva.
5. **Datos de churn y upgrades**: cuánto MRR se perdió y cuánto vino de clientes que ya pagaban un plan y subieron. Sin eso, el +29% puede estar inflado.

## Conclusión

Lo que tienes es una **correlación temporal**, no una causalidad demostrada. La respuesta honesta es: **no se puede saber si la secuencia funcionó**. Si necesitas decidir si mantenerla, mi recomendación es que no la juzgues por el MRR del mes, sino que montes un mínimo sistema de medición (atribución + grupo de control) antes de volver a lanzar algo así.