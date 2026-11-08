# Nemotron 3 Ultra 550B — business_audit/atribucion_correlacion_temporal

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.49 | quality: 10.0
- latency_total: 41.106s | tokens_per_second: 31.5
- input_tokens: 243 | output_tokens: 1296

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

**Conclusión: No se puede saber. Los datos no sostienen que la secuencia de emails funcionó.**

---

### Por qué no se puede atribuir el crecimiento a los emails

Tienes **tres intervenciones simultáneas** en una ventana de 12 días:

| Fecha | Intervención | Canal |
|-------|--------------|-------|
| 1 mar | Secuencia de 5 emails (a usuarios *ya existentes* en plan gratuito) | Retención/activación interna |
| 3 mar | Publicidad pagada ($400/mes) | Adquisición *nueva* (tráfico frío) |
| 12 mar | Mención de creador con audiencia grande | Adquisición *nueva* (tráfico de referencia/viral) |

El MRR subió $1.200 (+29%) y las altas pagadas subieron 5 (de 9 a 14, +55%). **Cualquiera de las tres —o la combinación— puede explicar todo, parte o nada del incremento.** No hay grupo de control, no hay staggering, no hay tracking de atribución por canal.

---

### Qué sería *mínimamente* necesario para tener una evidencia razonable

1. **Fuente de atribución por alta**  
   Cada usuario que pasa a plan pago debe tener registrado: `utm_source`, `referrer`, `primer_email_click`, `fecha_primera_visita`, etc. Si no lo tienes, estás ciego.

2. **Cohorte de comparación para los emails**  
   - Opción A (ideal): A/B test — 50% de los gratuitos reciben la secuencia, 50% no.  
   - Opción B (cuasi-experimento): Lanzar la secuencia en oleadas semanales y comparar conversión de cada oleada vs. la anterior.  
   - Opción C (mínimo viable): Comparar la conversión de *usuarios gratuitos preexistentes* (los únicos que recibieron los emails) contra su baseline histórico, **excluyendo** a los usuarios nuevos traídos por ads y video.

3. **Desglose de las 14 altas de marzo**  
   - ¿Cuántos venían de la base gratuita previa al 1 mar?  
   - ¿Cuántos entraron por ads (UTM / landing page)?  
   - ¿Cuántos entraron tras el video (referrer / pico de tráfico 12–14 mar)?  
   Sin ese desglose, cualquier número que te dé es especulación.

4. **Curva de conversión temporal**  
   Gráfico diario de altas pagadas del 1 al 31 mar.  
   - Si el pico es 12–15 mar → video.  
   - Si hay subida sostenida desde el 3–4 mar → ads.  
   - Si hay subida escalonada coincidiendo con envíos de emails (días 1, 3, 5, 7, 9) *solo en usuarios gratuitos antiguos* → emails.  
   Si no tienes serie diaria por cohorte, no puedes ver el patrón.

5. **Coste por adquisición (CAC) por canal**  
   - Ads: $400 / altas_vía_ads.  
   - Video: $0 / altas_vía_video (pero incontrolable).  
   - Emails: coste fijo de herramienta + tiempo / altas_vía_email.  
   Sin atribución, no sabes rentabilidad.

---

### Qué puedes hacer *hoy* con lo que tienes

1. **Etiqueta retroactivamente** las 14 altas de marzo revisando:
   - ¿Tenían cuenta gratuita antes del 1 mar? → candidatos a email.
   - ¿Su primera sesión tiene UTM de ads? → ads.
   - ¿Su referrer es YouTube / el canal del creador / aterrizaron 12–14 mar? → video.
   - ¿Ninguna de las anteriores? → orgánico / directo / desconocido.

2. **Calcula la conversión de la base gratuita preexistente**:  
   `usuarios_gratis_28feb → cuántos pagaron en marzo`.  
   Compáralo con la misma métrica en meses anteriores (enero, diciembre). Si no tienes histórico, anótalo para el mes que viene.

3. **Detén una variable el mes que viene** (si puedes):  
   - Mantén ads, apaga emails → mides ads + video.  
   - O apaga ads, mantén emails → mides emails + video.  
   - Mejor: apaga video (no controlable), testea emails vs. ads con UTM limpios.

---

### En una frase
**Subió el MRR, pero con tres palancas movidas a la vez no sabes cuál —si alguna— la movió.**  
Si tu jefe o socio te pide confirmar que los emails funcionaron, la respuesta honesta es: **«No lo sabemos; el experimento está contaminado.»**