# Seed 2.0 Code — business_audit/atribucion_correlacion_temporal

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.3 | quality: 10.0
- latency_total: 113.55s | tokens_per_second: 53.9
- input_tokens: 275 | output_tokens: 6116

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

### Conclusión inequívoca: No se puede saber si la secuencia de emails funcionó
La correlación temporal (lanzaste la secuencia → aumentó el MRR/altas) no es causalidad, porque hay **factores confundidores muy fuertes** que superponen su efecto al de los emails, y faltan datos clave para aislar el impacto real de la secuencia.

---

### Por qué los datos que compartiste no son suficientes
1. **Confundidores superpuestos (no lanzaste solo la secuencia):**
   Tres días después de activar los emails empezaste publicidad pagada, y 12 días después un creador con audiencia grande te mencionó. Ambos son canales que generan directamente tráfico y conversiones (tanto de usuarios nuevos que llegan al pago, como de usuarios que pasan por el gratuito). No hay forma de separar cuánto del aumento viene de los emails, cuánto de la publicidad y cuánto de la mención.

2. **Falta de grupo control:**
   No hay un subgrupo de usuarios del plan gratuito que **no haya recibido la secuencia** para comparar sus tasas de conversión. Por ejemplo, si hubieras dividido aleatoriamente a los gratuitos en dos grupos (A: recibe emails, B: no), podrías ver si A tuvo más altas. Sin eso, no sabes si el aumento es por los emails o por algo más.

3. **No hay segmentación de los datos:**
   - No sabes si las 14 altas de marzo son de **usuarios gratuitos existentes al 28/02** (potencialmente alcanzados por la secuencia) o de **usuarios nuevos en marzo** (probablemente atraídos por publicidad o la mención).
   - No sabes si el aumento de MRR viene solo de altas nuevas, o de **menos cancelaciones** o **cambios de plan** (ej: usuarios que pasaron de un plan básico a uno premium).
   - No hay métricas de la secuencia: ¿cuántos abrieron los emails? ¿cuántos hicieron clic en el enlace al pago? ¿cuántos de los que pasaron a pago interactuaron con la secuencia?

4. **Falta de contexto histórico:**
   No sabes si el +29% de MRR o el paso de 9 a 14 altas es **atípico** o parte de una tendencia que ya venías teniendo. Por ejemplo, si en enero hubo 13 altas, febrero 9 (una baja temporal) y marzo 14 (regreso a la media), el aumento no tiene nada que ver con los emails.

---

### Qué hace falta para estar seguros (ordenados por viabilidad)
#### 1. Segmentar datos existentes (retrospectivo, sin costo)
Primero, desglosa lo que ya tenés para eliminar confusiones:
- Divide las 14 altas de marzo en:
  ✅ Altas de **usuarios gratuitos al 28/02** (potencialmente alcanzados por la secuencia).
  ❌ Altas de **usuarios nuevos en marzo** (atraídos por publicidad o la mención).
- Dentro de los primeros, ver si interactuaron con la secuencia: ¿abrieron al menos un email? ¿hicieron clic en el enlace al pago?
- Desglosa el aumento de MRR: ¿viene de altas nuevas, menos cancelaciones o cambios de plan?
- Ver el origen de tráfico de las altas (si tenés UTMs, cookies o datos de búsqueda): ¿vienen de publicidad, de búsquedas del creador, o de clics en tus emails?

#### 2. Comparar con la tendencia histórica (retrospectivo, sin costo)
Trae datos de altas y MRR de los **3-6 meses anteriores a febrero** para ver si marzo es un valor atípico (ej: venías creciendo un 10% mensual y marzo fue un 29%) o parte de una tendencia.

#### 3. Buscar un grupo control natural (retrospectivo, si existe)
¿Hubo algún subgrupo de usuarios gratuitos al 28/02 que **no recibió la secuencia**? Por ejemplo:
- Usuarios que desactivaron las comunicaciones por email.
- Usuarios que se inscribieron el 28/02 por la tarde y no fueron incluidos en la segmentación inicial.
- Un error de automatización que dejó a un grupo sin emails.
Si existe ese grupo, compara su tasa de conversión a pago con la de los que sí recibieron la secuencia.

#### 4. Prueba A/B real (prospectivo, definitivo)
Esta es la única forma de estar 100% seguros. Pasos:
1. Divide **aleatoriamente** a todos los nuevos usuarios del plan gratuito en dos grupos iguales y balanceados (mismo perfil, misma fuente de tráfico):
   - **Grupo Tratamiento:** Recibe la secuencia de 5 emails.
   - **Grupo Control:** No recibe la secuencia (o recibe un email neutro sin oferta de pago).
2. Asegúrate de que ambos grupos estén expuestos a los **mismos estímulos externos** (misma publicidad, mismas menciones) para aislar el efecto de los emails.
3. Medir durante 4-6 semanas la **tasa de conversión a plan pago** de cada grupo y el MRR por usuario.
4. Si la diferencia entre grupos es **estadísticamente significativa** (no es por azar), entonces podés confirmar que la secuencia funcionó.

---

### Ejemplo de caso en el que SÍ se podría confirmar el efecto
> Después de segmentar:
> - 8 de las 14 altas de marzo son de **usuarios gratuitos al 28/02**, TODOS los cuales abrieron al menos 3 emails y hicieron clic en el enlace al pago.
> - Las 6 altas restantes son de usuarios nuevos que llegaron por la mención del creador (verificados por búsquedas de su nombre).
> - Además, había un grupo control natural de 200 usuarios gratuitos al 28/02 que no recibieron la secuencia, y solo 1 pasó a pago (tasa del 0,5%), mientras que los que sí la recibieron tuvieron una tasa del 4% (diferencia estadísticamente significativa).
> 
> En ese caso, sí se podría decir que la secuencia funcionó.

Sin estos datos, no hay forma de atribuir el aumento a los emails.