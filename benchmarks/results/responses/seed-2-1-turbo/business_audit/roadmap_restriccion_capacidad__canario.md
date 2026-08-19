# Seed 2.1 Turbo — business_audit/roadmap_restriccion_capacidad

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.29 | quality: 10.0
- latency_total: 105.698s | tokens_per_second: 75.4
- input_tokens: 302 | output_tokens: 7971

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

### Razonamiento previo (basado en tu capacidad REAL, no en suposiciones)
Primero, calculamos tu capacidad efectiva de construcción en el trimestre, para no engañarnos:
- 4h/día de construcción × 5 días/semana × 8 semanas = 160h brutas
- Le sumamos un 20% de colchón por interrupciones de soporte, scope creep o imprevistos (estándar para equipos de una persona) → **~128h de construcción efectiva en todo el trimestre**

Luego, convertimos los esfuerzos de las iniciativas (que están medidos en tiempo completo, 8h/día de construcción) a tu ritmo:
- A (3 meses full time): 480h de esfuerzo → te llevaría **6 meses a tu ritmo**, ni siquiera terminas un 25% en el trimestre. Riesgo altísimo de sobreesfuerzo (las reescrituras siempre duran más de lo estimado) y cero valor entregado en el corto plazo.
- B (1 semana full time): 40h de esfuerzo → te lleva **~2 semanas reales**. Impacto alto inmediato, sin invertir en adquisición.
- C (3 semanas full time): 120h de esfuerzo → pero depende de A terminado, así que está completamente bloqueado en este trimestre.
- D (2 semanas full time): 80h de esfuerzo → te lleva **~4,5 semanas reales**. Impacto medio, con beneficios secundarios que aumentan tu capacidad futura (reducción de soporte, mejor retención).

El principio rector para un fundador solo: **entrega valor medible lo más rápido posible, no te puedes permitir proyectos largos sin retorno en el corto plazo**.

---

### Plan del trimestre (orden de prioridad, semana a semana)
Es flexible, pero se apega a tu capacidad y maximiza el impacto en 8 semanas:

#### 📅 Semanas 1-2: Iniciativa B (Arreglar flujo de alta) → PRIORIDAD ABSOLUTA
**Por qué va primero**:
Es el ROI más alto de todas: pierdes el 60% de la gente en el paso 2, así que arreglarlo multiplica por 2-2.5 los usuarios que completan el alta sin invertir nada en adquisición. Más altas = más clientes = más ingresos = más feedback para validar el resto de iniciativas.

**Cómo ejecutarlo para no desviarte**:
- No hagas un flujo perfecto. Dedica las primeras 2 horas a analizar datos/feedback para saber exactamente qué causa el abandono (¿demasiados campos? ¿falta de explicación? ¿bugs?). Aplica el cambio de mayor impacto en menos tiempo (ej: reducir campos de 10 a 2, agregar un mensaje de contexto, arreglar un error de carga).
- **Hito fin de semana 2**: Tasa de abandono del paso 2 reducida al menos a la mitad (de 60% a 30% o menos).

#### 📅 Semanas 3-6.5: Iniciativa D (10 videos, entrega incremental)
**Por qué va después de B**:
Sinergia directa: B aumenta la cantidad de usuarios que se dan de alta, y D ayuda a retenerlos, reducir tu carga de soporte y traer más gente nueva. Si hicieras D primero, desperdiciarías parte de su impacto (la gente que llega se pierde en el alta rota).

**Cómo ejecutarlo para obtener valor ya, no al final**:
Ordena los videos por impacto, no por orden de lista:
1. **Primero 2-3 videos de soporte** (responden las preguntas más frecuentes): en la primera semana ya reduces las 2h/día que gastas en soporte. Si logras recortar 30min/día, pasas a tener 4.5h/día de construcción para siempre (un aumento de 12.5% de tu capacidad).
2. Luego 2-3 videos de onboarding: ayudan a que los nuevos usuarios (ahora más por B) entiendan el producto y se queden más.
3. Finalmente los videos de adquisición: traen más gente que se convierte bien gracias al alta arreglada.

No te obsesiones con la calidad de edición: el contenido vale más que la producción.
- **Hito fin de semana 3**: 3 videos de soporte publicados, consultas de esos temas reducidas en al menos 40%.
- **Hito fin de semana 6.5**: 10 videos completos.

#### 📅 Semanas 6.5-8: Spike de validación de A + mejoras incrementales de alto impacto
**Por qué NO empiezas A de lleno**:
Te llevaría 6 meses completos a tu ritmo (si no hay sobreesfuerzo, lo que es raro en reescrituras). No terminarías nada en el trimestre, y perderías la oportunidad de generar tracción con B y D.

**Qué haces en estas 1.5 semanas**:
1. **1 semana de spike de A**: Elige una parte pequeña y crítica de la plataforma (ej: el flujo de alta que acabas de arreglar, o el módulo de usuarios) y reescríbela en el nuevo framework. El objetivo no es construir, sino validar:
   - ¿Realmente es más rápido de desarrollar?
   - ¿Mejora la velocidad para el usuario?
   - ¿Hay problemas que no habías previsto?
   Con datos reales, decidirás en el próximo trimestre si vale la pena invertir 6 meses en la reescritura, o si es mejor seguir con el stack actual y hacer mejoras incrementales.
2. **0.5 semanas de mejoras pequeñas**: Arregla el bug más reportado por soporte, agrega una funcionalidad que pidan 3+ clientes, o mejora un poco más el flujo de alta. Sigue entregando valor hasta el último día.

- **Hito fin de trimestre**: Informe de validación de A (con esfuerzo real estimado para la reescritura completa) + 2-3 mejoras pequeñas implementadas.

---

### ¿Y qué pasa con C?
Como depende de A terminado, se pospone mínimo 2 trimestres (si es que decides hacer A). Pero antes de descartarlo del todo, pregúntate: **¿realmente no puedo hacer un MVP muy básico de panel de métricas con el stack actual?** Por ejemplo, un panel que muestre solo 2-3 métricas clave, usando herramientas que ya tienes. Si se puede, cambia el spike de A por este MVP de C: tiene impacto medio directo en los clientes, y si están dispuestos a pagar por ello, te da ingresos inmediatos para justificar proyectos más grandes después.

---

### Regla de oro para no desviarte
Cada semana tiene que haber algo de valor entregado a los usuarios. No pases más de 10 días sin que tus clientes noten un cambio positivo. Esto te mantiene motivado, te da feedback constante y evita que te pierdas en proyectos "para el futuro" que nunca llegan.