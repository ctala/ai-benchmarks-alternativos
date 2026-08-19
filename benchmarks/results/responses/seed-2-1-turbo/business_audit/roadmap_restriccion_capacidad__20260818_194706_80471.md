# Seed 2.1 Turbo — business_audit/roadmap_restriccion_capacidad

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 149.819s | tokens_per_second: 54.7
- input_tokens: 302 | output_tokens: 8192

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

### Resumen ejecutivo de 10 segundos
Empieza por arreglar el flujo de alta (B), luego graba los videos de contenido (D), y usa el tiempo restante para iterar y mejorar de forma incremental. **No toques la reescritura (A) ni el panel de métricas (C) en este trimestre**: A no se termina y no genera valor inmediato, y C depende de A.

---

### Paso previo: Calculamos tu capacidad REAL (no ideal)
Tienes 4h/día de construcción = 20h/semana = 160h totales en 8 semanas. Pero como fundador solo, **nunca planifiques al 100%**: reserva un 20% para imprevistos (bugs, soporte extra por más usuarios, reuniones con clientes, etc.). Quedan 128h útiles para iniciativas planificadas.

Ajustamos los esfuerzos (asumimos que tus estimaciones son de persona-full-time, el estándar más común; si son en tu propio ritmo de 4h/día, multiplica los plazos por la mitad):
- A: 3 meses full time = 480h → te llevaría 24 semanas (6 meses) a tu ritmo. No entra en el trimestre, ni por cerca.
- B: 1 semana full time = 40h → 2 semanas a tu ritmo.
- C: 3 semanas full time = 120h → 6 semanas a tu ritmo. Depende de A, así que no se puede hacer sin ella.
- D: 2 semanas full time = 80h → 4 semanas a tu ritmo.

---

### Plan del trimestre, ordenado por ROI real
#### Fase 1: Semanas 1-2 → Arreglar flujo de alta (B)
**Por qué va primero, sin dudas**:
Es el quick win con mayor impacto de toda la lista. Hoy pierdes el 60% de los usuarios en el paso 2: por cada 100 personas que empiezan el alta, solo 40 llegan a usar el producto. Si reducen la fuga al 20% (objetivo realista en 2 semanas), pasan 80 usuarios → **duplicas tus usuarios activos (y tus ingresos, si es de pago) en 14 días**. Nada más se acerca a ese retorno.

Además, todo lo que hagas después valdrá el doble: si traes usuarios con contenido, no se perderán en el alta. Si haces mejoras del producto, más gente las usará.

**Cómo hacerlo para no perder tiempo**:
No te obsesiones con un flujo perfecto. Identifica las 2-3 causas principales de la fuga (mira datos de embudo, habla con 3-5 usuarios que abandonaron, prueba el flujo tú mismo) y arregla solo esas.

**Punto de control al final de la fase**:
Si la fuga bajó al 30% o menos, pasas a la siguiente fase. Si no, dedica 1 semana más (usa el colchón) a iterar: vale más la pena reducir la fuga 10 puntos más que pasar a contenido.

---

#### Fase 2: Semanas 3-6 → Grabar 10 videos de contenido (D)
**Por qué después de B**:
El impacto de D (tráfico nuevo, reconocimiento de marca, reducción de soporte) se multiplica por el arreglo del alta. Cada usuario que llegue por los videos tiene muchas más probabilidades de quedarse, así que el tiempo que inviertas aquí rinde más que si lo hicieras antes.

A diferencia de la reescritura (A), D genera valor de forma incremental: no necesitas los 10 videos terminados para ver resultados. Sube 2 por semana y ya empiezas a atraer usuarios.

**Cómo optimizar el esfuerzo**:
No hagas videos perfectos. Prioriza temas que resuelvan los problemas más comunes de tus usuarios (o las preguntas que más te llegan en soporte): así, además de atraer usuarios nuevos, reduces el tiempo de soporte (te devuelve tiempo en el futuro).

**Punto de control semanal**:
Si un tema funciona mucho (más vistas, más usuarios que llegan al alta), haz más videos de ese tema en lugar de seguir la lista inicial de 10.

---

#### Fase 3: Semanas 7-8 → Tiempo de iteración y mejora incremental (NO empieces A)
Te quedan 2 semanas de margen (más si tus estimaciones eran en tu propio ritmo). **No inviertas este tiempo en empezar la reescritura**:
- Las reescrituras completas son el error número 1 de fundadores técnicos: siempre tardan más de lo esperado, y son proyectos "todo o nada" que no generan valor hasta que están terminados. Para un equipo de una persona, la supervivencia y los ingresos inmediatos son más importantes que una mejora de velocidad que solo verás en 6 meses.
- Si empiezas A, te quedarás a mitad de camino cuando termine el trimestre, y no tendrás nada que mostrar por el tiempo invertido si surge una urgencia o una oportunidad.

**Qué hacer en este tiempo, en orden de prioridad**:
1. **Iterar en B**: Si la fuga del alta sigue siendo alta, sigue mejorando. Cada punto porcentual que reduces es ingresos directos.
2. **Reducir deuda técnica de forma incremental**: Si el framework actual te frena en algo específico (por ejemplo, los tiempos de carga son lentos, o te cuesta añadir funcionalidades), arregla solo esa parte, no toda la plataforma. Así te acercas a poder hacer C sin invertir 3 meses en una reescritura.
3. **Validar la demanda de C**: Habla con 5-10 clientes