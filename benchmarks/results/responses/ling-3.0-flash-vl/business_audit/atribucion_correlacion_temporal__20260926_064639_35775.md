# Ling 3.0 Flash VL — business_audit/atribucion_correlacion_temporal

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 9.32 | quality: 10.0
- latency_total: 15.507s | tokens_per_second: 130.5
- input_tokens: 286 | output_tokens: 2024

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

## Conclusión: No se puede saber.

Los datos **no permiten afirmar** que la secuencia de emails funcionó. Lo que sí se puede decir es que hubo un aumento notable en marzo (MRR +29%, altas +56% respecto a febrero), pero ese aumento coincide en el tiempo con **al menos otras dos intervenciones simultáneas**, y no hay forma de separar sus efectos con la información disponible.

---

### Por qué no se puede atribuir el resultado a los emails

**1. Confusores simultáneos graves**

| Intervención | Fecha | Impacto potencial |
|---|---|---|
| Secuencia de 5 emails | 1 de marzo | Desconocido |
| Publicidad pagada ($400) | 3 de marzo | Desconocido |
| Mención de creador con audiencia grande | 12 de marzo | Probablemente significativo |

Tres cosas cambiaron en el mismo mes. Cualquiera de ellas —o la combinación— podría explicar el aumento. No hay forma de desagregar con los datos actuales.

**2. No hay grupo de control**

No se tiene un cohorte de usuarios gratuitos que **no** recibieran los emails. Sin eso, no hay base de comparación para aislar el efecto de la secuencia.

**3. Métricas insuficientes**

- No se sabe cuántos usuarios gratuitos había en total → no se puede calcular tasa de conversión.
- No se sabe si las 14 altas de marzo son 100% nuevos usuarios o incluyen renovaciones.
- No hay datos de engagement de los emails (aperturas, clics).
- No hay datos de origen de las altas (¿vino del email, del anuncio o del video?).

**4. El confusor más fuerte: el creador**

Un creador con "audiencia grande" mencionando la comunidad el 12 de marzo es, por sí solo, un evento que podría generar un pico de altas significativo. Esto no es un ruido menor — es probablemente el candidato más fuerte para explicar parte o la totalidad del aumento.

---

### Lo que haría falta para estar seguros

| Dato | Para qué sirve |
|---|---|
| **Cohorte de control** (usuarios gratuitos que no recibieron emails) | Aislar el efecto de la secuencia |
| **Datos de engagement de los emails** (aperturas, clics) | Saber si los emails fueron siquiera leídos |
| **Desglose de altas por fuente** (email, anuncio, referencia orgánica, creador) | Atribuir cada alta a su origen |
| **Tamaño del parque de usuarios gratuitos** | Calcular tasa de conversión real |
| **Datos de la publicidad** (impresiones, clics, conversiones) | Evaluar si el anuncio tuvo impacto |
| **Tráfico referido del video del creador** | Medir su contribución concreta |
| **Comparación mes a mes con estacionalidad** | Entender si febrero fue atípico |

---

### ¿Qué haría en tu lugar?

1. **No comunicar internamente** que la secuencia de emails "funcionó". Eso no está demostrado y puede llevar a decisiones equivocadas (por ejemplo, invertir más en emails cuando el verdadero motor fue el creador).
2. **Configurar tracking de fuentes** desde ya: un UTM diferente para cada canal (emails, anuncios, enlace del creador) y una pregunta de onboarding tipo *"¿cómo nos conociste?"*.
3. **Hacer un experimento controlado** el próximo mes: dividir a los usuarios gratuitos en dos grupos, uno que reciba la secuencia y otro que no, y comparar tasas de conversión.
4. **Si necesitas una respuesta ahora**: lo más honesto es decir *"marzo fue un buen mes con múltiples iniciativas; no podemos atribuir el resultado a ninguna en particular todavía, y estamos poniendo tracking para poderlo determinar en el próximo ciclo"*.

La diferencia entre un analista que protege al equipo y uno que no, es exactamente esta: decir **"no se puede saber"** hoy es más útil que decir **"sí funcionó"** con datos que no lo confirman.