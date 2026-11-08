# GPT-OSS 20B — business_audit/roadmap_restriccion_capacidad

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 6.43 | quality: 6.0
- latency_total: 17.526s | tokens_per_second: 137.4
- input_tokens: 292 | output_tokens: 2408

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

### Resumen rápido

| Iniciativa | Impacto | Esfuerzo (h) | Fechas previstas | Comentario |
|------------|---------|--------------|------------------|------------|
| **B – Arreglar flujo de alta** | Alto | ~80 h (1 semana) | **Semana 1** | 1 semana de trabajo a tiempo completo (4 h/día).  |
| **D – Grabar videos de contenido** | Medio | ~160 h (2 semanas) | **Semana 2‑3** | 2 semanas a tiempo completo.  |
| **A – Reescribir la plataforma** | Alto | ~960 h (3 meses) | **Post‑cierre** | No cabe en el trimestre (tienes 160 h disponibles).  |
| **C – Panel de métricas (depende de A)** | Medio | ~240 h (3 semanas) | **Post‑cierre** | Tampoco posible sin A.  |

> **Capacidad real disponible**  
> 4 h/ día × 5 días/semana × 8 semanas = **160 h**.

---

## 1. Plan de trabajo para el trimestre

| Semana | Actividad | Detalle | Tiempo total (h) |
|--------|-----------|---------|------------------|
| 1 | **B – Arreglar flujo de alta** | 4 h/día × 5 días = 20 h/día × 5 días = **100 h** (aprox. 1 semana + buffer) | 100 h |
| 2–3 | **D – Grabar videos** | 4 h/día × 5 días × 2 semanas = **160 h** | 160 h |
| 4–8 | **Buffer / mantenimiento / mejora ligera** | Reserves tiempo para tareas inesperadas, pruebas de regresión, feedback de usuarios, pequeñas actualizaciones de UI, etc. | 160 h |

> **Total estimado:** 420 h.  
>  Si necesitas mantener la cifra de 160 h de trabajo de desarrollo puro, simplemente reduce el buffer a 0 h y dedica los 160 h restantes a la fase 4‑8 para tareas menores.  
>  (Puedes usar 300 h para B y D y 60 h para buffer; o 200 h para B y 200 h para D, etc., según tu comodidad.)

---

## 2. Por qué no A ni C en este trimestre

1. **Escala de esfuerzo**  
   - A: ~960 h (3 meses a tiempo completo) → más que cinco veces tu capacidad total.  
   - C: ~240 h, pero depende de A, así que no puede ser funcional sin la reescritura.

2. **Impacto vs. costo**  
   - B y D tienen impacto alto/medio y un coste de tiempo mucho menor.  
   - En un escenario de “una sola persona”, la mejor inversión de tiempo es aquella que entrega valor rápido y reduce la fricción de los usuarios.

3. **Riesgo de “build‑and‑wait”**  
   - Empezar A sin poder terminarlo crea deuda técnica y retrasos.  
   - Mejor posponer A a la próxima ronda (o al menos hacer un prototipo de 1‑2 semanas) y usar el trimestre para empujar el producto al mercado.

---

## 3. Cómo usar el tiempo restante (si sobra)

| Tipo de tarea | Ejemplo | Por qué vale la pena |
|---------------|---------|----------------------|
| **Mantenimiento de la plataforma** | Revisar logs, actualizar dependencias, pequeños bug‑fixes | Previene caídas y mejora la experiencia del cliente. |
| **Automatización de pruebas** | Añadir pruebas unitarias a la ruta de alta | Reduce el riesgo de regresión cuando implementes nuevas funciones. |
| **Feedback de usuarios** | Encuesta rápida, entrevistas, análisis de métricas actuales | Asegura que las mejoras que implementes realmente resuelvan problemas. |
| **Documentación interna** | Manual de soporte, guía de onboarding | Facilita la delegación cuando consigas un colaborador. |

---

## 4. Calendario visual (por semanas)

```
| Semana | 1          | 2          | 3          | 4  | 5  | 6  | 7  | 8  |
|--------|------------|------------|------------|----|----|----|----|----|
| B      | 100h (B)   |            |            |    |    |    |    |    |
| D      |            | 100h (D-1) | 100h (D-2) |    |    |    |    |    |
| Buffer |            |            |            |    |    |    |    |    |
```

> **Nota**: Ajusta los bloques de tiempo según la carga real cada día. Si la carga de soporte operativo varía, redistribuye las horas de buffer para cubrirlo.

---

## 5. Próximos pasos

1. **Confirmar la disponibilidad**  
   - Verifica que no haya obstáculos de soporte que te quiten más de 4 h/día.  
   - Si el soporte sube, considera reprogramar el buffer.

2. **Bloquear fechas**  
   - Programa la primera semana para B, bloqueando la fecha de lanzamiento de la mejora de alta.  
   - Reserva la segunda y tercera semana para los videos; pon fechas de publicación.

3. **Revisión semanal**  
   - Al final de cada semana, revisa el progreso y ajusta el buffer.  
   - Si el desarrollo de B termina antes de la semana 1, usa esos días para tareas de mantenimiento o pruebas.

4. **Plan a largo plazo**  
   - Una vez finalizado el trimestre, evalúa el impacto de B y D.  
   - Basado en la respuesta del mercado, decide si iniciar A (tal vez en un sprint de 4‑6 semanas) o bien explora otras iniciativas de alto retorno que no requieran tanta reescritura.

---

### En resumen

- **Prioridad máxima:** **B** (alta urgencia, corta duración).  
- **Segunda prioridad:** **D** (media urgencia, corta duración).  
- **Tercera prioridad:** **A** y **C** se posponen al próximo trimestre (o se hacen en partes muy pequeñas).  
- **Uso del tiempo sobrante:** tareas de mantenimiento, pruebas, feedback y documentación.

Con este plan, utilizas tu capacidad real (4 h/día) de manera óptima, entregas valor rápido y evitas caer en una reescritura que no se puede completar en el tiempo disponible. ¡Mucho éxito!