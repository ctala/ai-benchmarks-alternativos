# Mercury 3 — business_audit/atribucion_correlacion_temporal

- model_id: `inception/mercury-3`
- success: True  | final: 9.34 | quality: 10.0
- latency_total: 4.218s | tokens_per_second: 417.2
- input_tokens: 248 | output_tokens: 1760

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

## Conclusión

**No se puede saber si la secuencia de emails funcionó** con los datos que me pasaste. Los números muestran una mejora, pero hay al menos tres intervenciones distintas ocurriendo al mismo tiempo:

1. Secuencia de emails activada el 1 de marzo.
2. Publicidad pagada desde el 3 de marzo ($400).
3. Mención de un creador con audiencia grande el 12 de marzo.

Cualquiera de las tres, o una combinación, pudo generar el aumento de MRR y de altas. Los datos agregados no permiten separar el efecto de cada una.

## Por qué los datos no alcanzan

- **No hay grupo de control**: todos los usuarios del plan gratuito recibieron la secuencia, así que no sabemos qué habría pasado sin ella.
- **No hay datos de comportamiento**: no sabemos cuántos usuarios abrieron los emails, hicieron clic, ni cuántos se convirtieron después de recibirlos.
- **Las altas no están atribuidas**: las 14 altas de marzo pudieron venir de la publicidad, del video del creador, o de usuarios que ya estaban en el plan gratuito y se convirtieron por los emails. No lo podemos distinguir.
- **El MRR es una métrica acumulada**: el MRR de marzo incluye ingresos de altas de meses anteriores, posibles upgrades, cancelaciones, etc. Un aumento de $1.200 no se puede asignar directamente a los emails.
- **No hay denominador**: no sabemos cuántos usuarios del plan gratuito existían al 1 de marzo, así que no podemos calcular una tasa de conversión.
- **No hay definición de "funcionó"**: ¿era aumentar conversiones? ¿aumentar MRR? ¿mejorar retención? Cada definición requiere métricas distintas.

## Qué haría falta para estar seguros

1. **Definir la métrica principal** antes de lanzar (por ejemplo: tasa de conversión de gratuito a pago en 30 días).
2. **Aleatorizar**: dividir a los usuarios del plan gratuito en dos grupos: uno recibe la secuencia y otro no. Comparar tasas de conversión entre ambos. Es la única forma limpia de aislar el efecto.
3. **Si no se puede aleatorizar**, usar métodos cuasi-experimentales:
   - Comparar la evolución de conversiones de los usuarios que recibieron emails vs. usuarios similares que aún no los recibieron (por ejemplo, si la secuencia se envía por tandas).
   - Análisis de series temporales interrumpidas, controlando por el inicio de la publicidad y la mención del creador.
4. **Trackear eventos individuales**:
   - Quién recibió cada email, quién lo abrió, quién hizo clic.
   - Si el usuario se convirtió a pago y en qué fecha.
   - Fuente de adquisición del usuario (orgánica, publicidad, creador, etc.).
5. **Desglosar las altas por fuente y por fecha**: así podrías ver si las altas se concentran después del 12 de marzo (posible efecto del creador) o están distribuidas durante todo el mes.
6. **Incluir datos históricos**: tasa de conversión de meses anteriores, estacionalidad, y si este tipo de campañas ya se había hecho antes.
7. **Tener un tamaño de muestra suficiente** para que cualquier diferencia sea estadísticamente significativa.

En resumen: el aumento es real, pero **no podemos atribuirlo a los emails**. Si el equipo necesita saber si la secuencia funciona, lo correcto es diseñar un experimento controlado o al menos implementar un sistema de atribución por usuario antes del próximo lanzamiento.