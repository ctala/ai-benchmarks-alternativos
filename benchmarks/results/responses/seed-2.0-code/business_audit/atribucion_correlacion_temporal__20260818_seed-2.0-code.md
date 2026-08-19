# Seed 2.0 Code — business_audit/atribucion_correlacion_temporal

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.57 | quality: 10.0
- latency_total: 28.5s | tokens_per_second: 54.9
- input_tokens: 275 | output_tokens: 1566

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

### Conclusión: No se puede saber si la secuencia de emails funcionó  
El aumento de MRR (+29%) y de altas al plan pago (de 9 a 14) no se pueden atribuir exclusivamente a la secuencia de emails porque hay factores concurrentes que también podrían haber causado el uplift, y falta información para aislar el impacto de cada uno:  
1. **Confounders superpuestos en el tiempo**: La secuencia empezó el 1 de marzo, pero la publicidad el 3 y la mención del creador el 12. Cualquiera de estas tres acciones (o una combinación) podría haber impulsado las conversiones.  
2. **Datos agregados sin atribución**: No sabemos si las nuevas altas vinieron de usuarios que interactuaron con los emails, vieron la publicidad o conocieron la comunidad por el video del creador.


### Qué haría falta para estar seguros  
Para determinar si la secuencia de emails tuvo un impacto real, necesitarías:  
1. **Atribución individual**:  
   - Links trackeados (UTMs) o códigos de descuento exclusivos en la secuencia de emails para saber si las conversiones vienen de ahí.  
   - Seguimiento de interacciones: ¿Los usuarios que se convirtieron abrieron o clicaron los emails?  
   - Registro de origen de cada alta: ¿vinieron de ads, del video del creador o de la secuencia?  

2. **Grupo de control**:  
   Haber segmentado una muestra representativa de usuarios del plan gratuito para NO recibir la secuencia de emails. Así podrías comparar la tasa de conversión entre el grupo que recibió los emails (tratamiento) y el que no (control), aislando el efecto de la secuencia de otros factores (publicidad, mención del creador, que afectarían a ambos grupos por igual).  

3. **Desglose temporal de conversiones**:  
   Ver si las altas se concentraron después del 12 de marzo (cuando salió el video del creador), del 3 (publicidad) o si hubo un uplift en los primeros días de marzo (solo la secuencia de emails activa).  

4. **Contexto histórico**:  
   Confirmar si el crecimiento entre febrero y marzo es inusual (no explicable por estacionalidad o tendencias anteriores de la comunidad).  

5. **Análisis detallado de MRR**:  
   Saber si el aumento de MRR viene solo de nuevas altas, o también de upgrades de usuarios existentes. Si son upgrades, ¿se pueden vincular a interacciones con la secuencia de emails?