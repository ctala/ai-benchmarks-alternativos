# GPT-5.6 Terra Pro — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 8.42 | quality: 10.0
- latency_total: 18.051s | tokens_per_second: 162.5
- input_tokens: 4938 | output_tokens: 2933

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

**Conclusión:** con estos datos **no se puede saber si la secuencia de emails funcionó**.

Sí se observa una mejora coincidente con marzo:

- MRR: de **$4.100 a $5.300** (+$1.200; +29%).
- Altas de pago: de **9 a 14** (+5; +56% respecto a febrero).

Pero esa mejora no se puede atribuir a los emails porque hubo al menos dos cambios importantes casi al mismo tiempo:

1. Empezaste publicidad el 3 de marzo.
2. Un creador grande mencionó la comunidad el 12 de marzo.

Además, el MRR puede haber cambiado no solo por nuevas altas: también por bajas, upgrades/downgrades, descuentos, recuperaciones de pagos o cambios de precio. Por tanto, el +29% de MRR no equivale necesariamente al efecto de la secuencia.

### Qué haría falta para evaluar la secuencia

#### 1. Datos de atribución por usuario
Para cada persona que se convirtió a pago, necesitaríamos saber:

- Si recibió la secuencia y cuántos emails recibió antes de comprar.
- Fechas de envío, entrega, apertura y clic de cada email.
- Fecha de conversión.
- Fuente de adquisición: orgánico, publicidad, mención del creador, referido, directo, etc.
- Cuándo se registró en el plan gratuito.
- Si ya estaba cerca de pagar antes de recibir los emails.

Esto permitiría, por ejemplo, ver cuántas conversiones ocurrieron después de clicar un email. Pero incluso eso sería **atribución**, no una prueba definitiva de causalidad: quienes abren o hacen clic pueden ser usuarios que ya tenían más intención de comprar.

#### 2. La tasa de conversión, no solo el número de altas
Necesitamos el denominador:

- ¿Cuántos usuarios gratuitos eran elegibles para recibir la secuencia en febrero y marzo?
- ¿Cuántos recibieron cada email?
- ¿Qué porcentaje se convirtió a pago dentro de 7, 14 o 30 días?

Por ejemplo, 14 altas pueden ser excelentes si se enviaron emails a 100 personas, pero modestas si se enviaron a 10.000.

#### 3. Un grupo de control aleatorio
La forma más fiable sería un experimento:

- Asignar aleatoriamente a una parte de usuarios gratuitos a recibir la secuencia.
- Mantener a otra parte como grupo de control, sin secuencia (o con la comunicación anterior).
- Comparar las tasas de conversión en el mismo período y con la misma ventana temporal.

Ejemplo de métrica:

> Conversión a pago en 30 días = usuarios que pasan a pago / usuarios elegibles al inicio.

El efecto incremental sería:

> tasa de conversión del grupo con emails − tasa del grupo de control.

Como ambos grupos coexistirían durante la publicidad y la mención del creador, esos factores tenderían a afectar a ambos por igual. Eso sí permitiría estimar si la secuencia generó conversiones adicionales.

### Qué revisaría ahora

1. Graficar altas diarias de pago durante marzo, junto con:
   - inicio de publicidad (3 de marzo),
   - publicación del video (12 de marzo),
   - fechas de cada email de la secuencia.

2. Separar las conversiones por fuente de adquisición.

3. Ver cuántas altas ocurrieron:
   - tras un clic en email,
   - tras campañas publicitarias,
   - en los días posteriores al video,
   - sin fuente identificada.

4. Medir conversiones por cohorte de usuarios gratuitos: quienes entraron antes de marzo, quienes llegaron por publicidad y quienes llegaron tras el video no son necesariamente comparables.

5. Lanzar desde ahora un test A/B con grupo de control y definir por anticipado una ventana de medición, por ejemplo 30 días.

En resumen: **marzo fue mejor que febrero, pero no hay evidencia suficiente para concluir que los emails causaron la mejora**. La secuencia pudo haber ayudado, pero también pudo que la publicidad, la mención del creador o una combinación de las tres explicaran total o parcialmente el resultado.