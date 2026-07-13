# GPT-5.6 Luna — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 6.0 | quality: 6.0
- latency_total: 5.976s | tokens_per_second: 123.2
- input_tokens: 224 | output_tokens: 736

## Respuesta completa

## Conclusión

**No se puede saber si la secuencia de emails funcionó a partir de estos datos.**

Sí se observa una mejora en marzo:

- MRR: de $4.100 a $5.300, un aumento de $1.200 o 29%.
- Altas al plan pago: de 9 a 14, un aumento del 56%.

Pero en el mismo período ocurrieron dos acciones relevantes:

- Publicidad desde el 3 de marzo, con un gasto de $400.
- Mención de un creador con una audiencia grande el 12 de marzo.

Por tanto, el aumento podría deberse a:

- la secuencia de emails;
- la publicidad;
- la mención del creador;
- una combinación de las tres;
- variación normal de un mes a otro;
- cambios en cancelaciones, upgrades o composición de los planes.

Además, **más altas no implica necesariamente que la secuencia haya generado más MRR**: habría que saber el valor de los planes contratados, las bajas y los upgrades.

## Qué haría falta para estar seguros

Lo ideal sería un experimento controlado:

1. Tomar usuarios gratuitos elegibles.
2. Asignarlos aleatoriamente a:
   - grupo tratamiento: recibe la secuencia;
   - grupo control: no recibe la secuencia, o recibe una comunicación neutra.
3. Medir en ambos grupos, durante un período definido:
   - conversión a pago;
   - tiempo hasta la conversión;
   - MRR generado por usuario;
   - cancelaciones y retención.
4. Comparar la diferencia entre ambos grupos.

Por ejemplo, si el 8% del grupo con emails se convierte y el 5% del grupo control, esa diferencia sería evidencia del efecto de la secuencia, siempre que haya suficientes usuarios y el resultado sea estadísticamente consistente.

También necesitaría:

- quién recibió cada email y quién lo abrió o hizo clic;
- fechas exactas de altas y conversiones;
- fuente de cada usuario: orgánico, publicidad, creador o email;
- número de usuarios gratuitos elegibles antes y durante marzo;
- altas, bajas y upgrades diarios;
- planes contratados y MRR por usuario;
- datos de varios meses anteriores para estimar la variación normal.

Si no hubo grupo control, todavía se puede hacer un análisis exploratorio segmentando por fuente y comparando cohortes, pero **no permitiría atribuir causalmente el resultado a los emails**. Mi conclusión actual sería: **marzo fue mejor que febrero, pero la efectividad de la secuencia es indeterminada**.