# Solar Pro 4 — business_audit/roadmap_restriccion_capacidad

- model_id: `upstage/solar-pro4`
- success: True  | final: 7.66 | quality: 8.0
- latency_total: 17.876s | tokens_per_second: 55.2
- input_tokens: 323 | output_tokens: 987

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

Con 4 horas/día reales de construcción y 8 semanas de runway, no tienes margen para proyectos de 3 meses. Tu ventana de entrega es ~224 horas (8 semanas × 5 días × 4h). Cualquier iniciativa que rompa esa frontera te dejará al cierre del trimestre sin entregables visibles.

Aquí tienes el orden y la disciplina necesaria:

### Orden del trimestre
1. **B) Arreglar el flujo de alta (Semana 1-2)**  
   Prioridad cero. Un 60% de fuga en el paso 2 es un escape de ingresos, no un "bug de UX". Impacto alto, esfuerzo bajo. Lo arreglas primero porque libera capacidad de soporte (menos tickets de "no me funciona") y sube la conversión inmediata.
2. **D) 10 videos de contenido (Semana 3-5)**  
   Impacto medio, esfuerzo medio, pero es independiente y de entrega rápida. Los videos alimentan la tubería, mejoran posicionamiento y, si están bien enfocados, pueden reducir soporte futuro. Los grabas en el hueco que queda tras B.
3. **C) Panel de métricas (Semana 6-8)**  
   Impacto medio, entrega visible al cierre del trimestre. Solo lo tocas si B y D están estables. Si el panel requiere infraestructura que A aún no provee, lo haces con un MVP autocontenido (query directo, datos crudos, sin depender del reescritura).
4. **A) Reescribir el framework (Nunca en este trimestre)**  
   3 meses a tiempo completo = ~480-500 horas. Tienes ~224. No cabe. Además, un rewrite sin problema de negocio urgente es la forma más segura de quemar un trimestre sin métricas que lo justifiquen. Déjalo en "evaluar en Q1 siguiente" o descompónlo en micro-decisiones que puedas tomar sin reescribir todo.

### Ruta de 8 semanas (orientativa)
- **S1-2:** B. Foco total en el paso 2. Mide tasa de conversión paso 1→2 y 2→final. Si baja de 60% de fuga a <25%, el esfuerzo ya se paga.
- **S3-5:** D. 10 videos, publicados de a 2/semana. No los dejes para la semana 8. Empieza a validar qué resuena.
- **S6-8:** C. Panel MVP para clientes. Si hay dependencia técnica con A, haz una capa ligera que entregues sin bloquearte. Cierra el trimestre con un entregable que los clientes puedan usar.
- **Reserva:** 10-15% del tiempo para imprevistos y para la operación que no puedes delegar. Si el soporte crece, protege B y D; C puede esperar o reducirse.

### Criterios de decisión en el camino
- Si B no baja la fuga en 2 semanas, no avanzas: analizas hipótesis, no code.
- Si D genera tráfico/leads measurable, priorizas mantenerlo sobre C.
- Si C se vuelve bloqueado por A, lo haces con lo que tienes. No esperas al rewrite para entregar valor.
- A solo se mueve si, a mitad de trimestre, tienes evidencia clara de que la plataforma actual limita ingresos o crecimiento de forma medible, y puedes reescribir por fases sin parar B/C/D.

### Regla de oro para este trimestre
Entrega valor que afecte conversión o retención antes que arquitectura. Con 4 horas diarias, tu ventaja no es la velocidad de código, es la disciplina de no empezar lo que no cabe. Ordena por impacto/effort y por independencia. Al cierre, quieres poder decir: "menos fuga en alta, más contenido activo, y un panel que los clientes usan". El rewrite puede esperar a que el negocio te lo pida con números, no con intuición.