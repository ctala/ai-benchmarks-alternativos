# Gemini 3.8 Flash — business_audit/roadmap_restriccion_capacidad

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.66 | quality: 10.0
- latency_total: 13.616s | tokens_per_second: 122.7
- input_tokens: 242 | output_tokens: 1670

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

Primero, las matemáticas reales. La mayoría de los fundadores en solitario quiebran por no hacer esta cuenta:

* Tienes **4 horas/día** para construir.
* 8 semanas × 5 días = 40 días de trabajo.
* **Presupuesto total del trimestre: 160 horas.**
* Un "mes a tiempo completo" estándar son 160 horas. Por lo tanto, en todo el trimestre **solo tienes el equivalente a 1 mes de trabajo full-time tradicional**.

Con esta realidad, así queda el tablero:

---

### Lo que va a la basura (o al congelador)

* **A (Reescribir plataforma): CANCELADA.** Requiere ~3 meses full-time (480 horas). A tu ritmo actual te tomaría **tres trimestres enteros** sin lanzar nada más. Es la trampa clásica del fundador técnico: muerte por refactorización.
* **C (Panel de métricas): CANCELADA.** Depende de A, que no se va a hacer. Además, impacto medio frente a resolver fugas de negocio no justifica el esfuerzo.

---

### Tu plan de 8 semanas

Solo quedan **B** y **D**. Y el orden importa radicalmente: **no metes agua a un cubo agujereado.** Primero arreglas el embudo, luego atraes gente.

#### Semanas 1 y 2: Iniciativa B (Arreglar el alta)
* **Presupuesto:** ~40 horas (2 semanas a 4h/día).
* **Por qué:** Si el 60% se va en el paso 2, estás quemando cada visita o lead que consigues. Duplicar la conversión aquí tiene un impacto directo e inmediato en facturación.
* **Regla de PM:** No rediseñes todo el onboarding. Elimina campos, quita fricción en el paso 2, pon validaciones claras y mide. Termínalo y déjalo corriendo.

#### Semanas 3 a 6: Iniciativa D (10 Videos de contenido)
* **Presupuesto:** ~80 horas (4 semanas a 4h/día; tu estimación de 2 semanas full-time son 80 horas).
* **Por qué:** Con la fuga del paso 2 tapada, ahora sí tiene sentido empujar tráfico/adquisición. 
* **Distribución semanal sugerida:**
  * *Semana 3:* Guiones y estructura de los 10 videos.
  * *Semana 4 y 5:* Grabación por bloques (batching) y edición básica.
  * *Semana 6:* Publicación/programación y distribución.

#### Semanas 7 y 8: BUFFER (Margen de maniobra)
* **Presupuesto:** 40 horas.
* **Por qué:** Como trabajas solo, si te enfermas, si hay una caída de servidor o si el soporte explota (esas 2h diarias pasarán a 4h algún día), tu plan se romperá. Si no tienes este colchón, no llegarás al cierre del trimestre.
* **Si todo sale bien y sobra tiempo:** Mides los resultados del nuevo flujo de alta (B), iteras los detalles que fallen o automatizas parte de ese soporte diario que hoy te roba 2 horas.

---

### Resumen ejecutivo
1. **Semanas 1-2:** Arregla el paso 2 del alta (B).
2. **Semanas 3-6:** Produce los 10 videos (D).
3. **Semanas 7-8:** Colchón operativo y ajustes.
4. **A y C:** Prohibidas este trimestre.