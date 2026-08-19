# Seed 2.0 Code — business_audit/roadmap_restriccion_capacidad

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.27 | quality: 10.0
- latency_total: 116.86s | tokens_per_second: 61.3
- input_tokens: 302 | output_tokens: 7169

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres jefe de producto de una empresa de una sola persona. Priorizas con la capacidad real del equipo, no con la ideal.

**user:**

Soy fundador solo. Tengo 6 horas al día de trabajo enfocado y ya gasto 2 de esas 6 en soporte y operación diaria que no puedo delegar todavía. Me quedan ~4h/día reales para construir. Quedan 8 semanas hasta el cierre del trimestre.

Tengo cuatro iniciativas y quiero saber qué hago:

A) Reescribir la plataforma en otro framework. Impacto estimado: alto (velocidad y todo lo futuro). Esfuerzo: ~3 meses a tiempo completo.
B) Arreglar el flujo de alta, que hoy pierde al 60% de la gente en el paso 2. Impacto: alto. Esfuerzo: ~1 semana.
C) Añadir un panel de métricas para mis clientes. Impacto: medio. Esfuerzo: ~3 semanas. Depende de que A esté terminado.
D) Grabar 10 videos de contenido. Impacto: medio. Esfuerzo: ~2 semanas.

Ordename el trimestre.


## Respuesta completa

### Primero: Ajuste de capacidad REAL (no ideal)
Tus números son **no negociables** (fundador solo, sin margen para idealizaciones):
- Tiempo de construcción útil: `4h/día × 5d/sem × 8sem = 160 HORAS TOTALES`
- Los esfuerzos que diste están en **TIEMPO COMPLETO (8h/día)**. Para TI (solo 4h/día de construcción), te tomará el **DOBLE DE SEMANAS**:
  | Iniciativa | Esfuerzo TC (tu estimación) | Esfuerzo REAL para TI | Viabilidad en 8 semanas |
  |------------|-------------------------------|------------------------|--------------------------|
  | A          | 3 meses (12sem TC)           | 24sem (6 meses)        | ❌ IMPOSIBLE            |
  | B          | 1sem TC                       | 2sem                   | ✅ SÍ                    |
  | C          | 3sem TC                       | 6sem                   | ❌ DEPENDE DE A + PLAZO |
  | D          | 2sem TC                       | 4sem                   | ✅ SÍ                    |

### Regla de oro para fundadores solitarios:
> **Valor HOY > Valor MAÑANA** (si no te quedas sin ingresos para llegar a mañana)

---

## Cronograma del trimestre (100% viable, ajustado a tu capacidad)
### Semanas 1-2: Iniciativa B (Arreglar flujo de alta)
#### Por qué PRIMERO?
Es el único proyecto que genera **INGRESOS/USUARIOS INMEDIATOS**:
- Pierdes el 60% de **leads calificados** (que llegaron al alta) → duplicar la conversión aquí = duplicar tu base SIN GASTAR MÁS EN MARKETING.
- Es un "quick win" de ALTO IMPACTO sin riesgo.

#### Objetivo MEDIBLE:
Reducir la pérdida en el paso 2 de 60% a <30%.

#### Actividades diarias (4h/día, sin tocar soporte):
1. Analiza el problema (usa Hotjar/Google Analytics: ¿formulario muy largo? ¿bug de carga? ¿falta de info de precios?)
2. Arregla el punto crítico (ej: quita campos innecesarios, añade un mensaje de seguridad)
3. Testea con 5-10 leads reales.

---

### Semanas 3-6: Iniciativa D (Grabar 10 videos de contenido)
#### Por qué DESPUÉS de B?
Ahora que tu flujo de alta NO desperdicia tráfico, necesitas **más tráfico calificado**. Los videos tienen doble impacto:
1. Generan tráfico orgánico a mediano plazo.
2. Reducen tu carga de **soporte** (graba videos de preguntas frecuentes, así respondes con un video en lugar de 10min de chat → ahorras tiempo de tus 2h/día de soporte a futuro).

#### Objetivo MEDIBLE:
Tener 10 videos publicados (YouTube/LinkedIn/sitio) con palabras clave que buscan tus leads.

#### Truco para ahorrar tiempo (sin calidad perfecta):
Graba 2 videos por día: `1h de guion simple + 30min de grabación (cámara de celular) + 30min de edición básica (Canva)`. No necesitas cine, solo claridad.

---

### Semanas 7-8: Tiempo de optimización (NO A NI C)
Usa estas 80h (2sem × 4h/día × 5d) para **maximizar lo que ya hiciste** (no pierdas tiempo en proyectos sin valor inmediato):
1. **Optimiza B más**: Si la pérdida en el alta no bajó lo suficiente, añade un chat de soporte en el paso 2 o reduce más campos.
2. **Mejora D**: Añade subtítulos, thumbnails o descripciones SEO a los videos (aumenta las vistas en un 30% de media).
3. **Investigación de usuarios**: Entrevista a 5 leads que se fueron en el alta y 5 clientes que sí se quedaron → datos para optimizar en el próximo trimestre.
4. **Reduce soporte**: Crea plantillas de respuestas para preguntas frecuentes o un chatbot básico (ManyChat) → pasa de 2h/día de soporte a 1.5h/día (ganas tiempo de construcción para después).

---

## Lo que NUNCA haces en este trimestre (y por qué)
### 1. Iniciativa A (Reescribir plataforma)
- **Esfuerzo imposible**: Te tomaría 6 meses (no 8 semanas).
- **Sin valor inmediato**: La reescritura no genera ingresos hasta que esté 100% migrada → pierdes 8 semanas sin arreglar el embudo que te está quitando dinero.
- **Riesgo altísimo**: Scope creep, bugs ocultos, frustración → es el error más común de fundadores solitarios que quieren "mejorar el futuro" sin asegurar el presente.

### 2. Iniciativa C (Panel de métricas)
- **Depende de A**: No puedes hacerlo sin terminar la reescritura (imposible en este trimestre).
- **Impacto secundario**: Tus clientes no te van a dejar de pagar por no tener un panel de métricas si el flujo de alta es malo → prioriza lo que genera ingresos primero.

---

## Tips finales para no quemarte
1. **Medir TODO**: Usa Google Analytics para el flujo de alta, YouTube Analytics para los videos → no adivines, usa datos.
2. **No toques el soporte**: Tus 2h/día de soporte son irremovibles → no intentes "ahorrar" tiempo ahí para construir, porque te olvidarás de clientes y perderás ingresos.
3. **No te exijas perfección**: Los videos no necesitan cámara profesional, el flujo de alta no necesita ser "bonito" → necesita ser funcional.

Este es el único roadmap viable para tu capacidad real: genera valor inmediato, optimiza tu carga de trabajo y no te expone a riesgos innecesarios.