# Seed 2.0 Code — business_audit/atribucion_correlacion_temporal

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.36 | quality: 10.0
- latency_total: 62.151s | tokens_per_second: 76.0
- input_tokens: 275 | output_tokens: 4723

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

### Conclusión Final: **No se puede saber si la secuencia de emails funcionó**
Razones clave (confusión causal múltiple y datos insuficientes, alineados con tu contexto):
1. **Tres intervenciones concurrentes en marzo** que podrían haber causado el aumento de métricas, sin forma de aislar su efecto individual:
   - Secuencia de emails (1 mar, dirigido a usuarios gratuitos [¿existentes o nuevos? No se especifica])
   - Publicidad pagada (3 mar, $400: atrae tráfico nuevo)
   - Mencion de creador (12 mar, audiencia grande: atrae tráfico nuevo y recuerda a usuarios existentes)
2. **Métricas sin desglose granular**:
   - No sabes si las 14 altas de marzo provienen de **usuarios gratuitos EXISTENTES (público objetivo de la secuencia)** o de **usuarios NUEVOS (llegados por ads/creador)**. Si son todos nuevos, la secuencia no tuvo relevancia.
   - No mencionas **churn de MRR, ampliaciones o downgrades** de planes pagos: el aumento de $1200 en MRR podría deberse a la falta de churn en marzo (vs churn en febrero) o a ampliaciones de usuarios pagos existentes, no a las altas de plan pago.
3. **Sin grupo de control o segmentación aleatoria**: No hay un subgrupo de usuarios gratuitos que NO haya recibido la secuencia para comparar su tasa de conversión, por lo que no se puede atribuir el aumento de altas (si hubiera) a la secuencia.

---

### Qué haría falta para estar SEGUROS (medidas concretas, jerarquizadas por facilidad):
#### 1. **Primero: Desglosar datos existentes (sin experimentos nuevos, lo más rápido)**
   a. **Fecha exacta de cada alta al pago (marzo)**:
      - Si >80% de altas son POST 12 mar: El creador es el factor principal.
      - Si hay altas entre 2-3 mar (solo secuencia activa): Posible señal, pero sin control no es concluyente.
   b. **Origen de cada alta al pago**:
      - Clasificar cada alta como:
        1. Usuario gratuito EXISTENTE (registrado antes del 1 mar, público objetivo de la secuencia)
        2. Usuario gratuito NUEVO (registrado en mar, llegado por ads/creador)
        3. Usuario pago DIRECTO (sin pasar por gratuito)
      - Si la tasa de conversión de **usuarios gratuitos existentes (pre-mar)** subió MUCHO más en mar vs feb (ej: 2% → 8%), podría haber un efecto, pero sin control sigue siendo especulativo.
   c. **Desglose del MRR**:
      - Cuánto del aumento de $1200 corresponde a:
        1. Altas de plan pago
        2. Menos churn (vs feb)
        3. Ampliaciones de planes pagos existentes
      - Esto elimina si el MRR subió por razones no relacionadas con la secuencia.

#### 2. **Segundo: Experimento controlado (para confirmar, en la próxima o retroactivamente si se puede segmentar)**
   - **Segmentación ALEATORIA EX-ANTE** (si se hubiera hecho al lanzar la secuencia, o para usuarios gratuitos pendientes):
     - Dividir a TODOS los usuarios gratuitos (elegibles) en dos grupos:
       - **Grupo Tratamiento**: Recibe la secuencia de 5 emails (igual a la lanzada)
       - **Grupo Control**: NO recibe la secuencia (recibe emails habituales o ninguno)
     - Mantener igual para AMBOS grupos: Publicidad, menciones de creadores, cualquier otra intervención.
     - La diferencia de **tasa de conversión a plan pago** entre Tratamiento y Control SÓLO se deberá a la secuencia (porque todos los demás factores son iguales).

#### 3. **Tercero: Control de variables coexistentes (para eliminar ruido)**
   - Registrar el volumen de tráfico nuevo por canal (ads vs creador vs orgánico) y su tasa de conversión a pago.
   - Ver si la tasa de conversión de usuarios gratuitos existentes (público de la secuencia) no se correlaciona con picos de tráfico por ads o creador (si se correlaciona, el efecto es de esas intervenciones, no de la secuencia).

---

### Ejemplo hipotético en el que SÍ se podría concluir que funcionó:
Si después de desglosar:
- 11 de las 14 altas de mar son de **usuarios gratuitos existentes (pre-mar)**
- Estas 11 altas se distribuyen entre el 2 y el 11 de mar (antes del creador)
- La tasa de conversión de estos usuarios pasó de 2% en feb a 8% en mar
- Y al lanzar un grupo control aleatorio, la tasa de conversión del Tratamiento es 8% vs 2% del Control

Entonces SÍ se podría afirmar que la secuencia funcionó. Pero con los datos que tienes ahora, no se puede saber.