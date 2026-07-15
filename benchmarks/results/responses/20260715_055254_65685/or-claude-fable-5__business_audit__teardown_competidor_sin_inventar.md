# Claude Fable 5 — business_audit/teardown_competidor_sin_inventar

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 2.29 | quality: 2.0
- latency_total: 51.255s | tokens_per_second: 59.3
- input_tokens: 286 | output_tokens: 3040
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y bien estructurado que un emprendedor podría aplicar directamente.

## Respuesta completa

# Teardown competitivo: comunidad de automatización

Antes de empezar, mi convención de marcado:
- **[DATO]** = lo que me diste, verificable en su página
- **[INF-alta]** = inferencia con buen fundamento
- **[INF-media]** = inferencia razonable pero con supuestos importantes
- **[INF-baja]** = especulación informada, tómala con pinzas

---

## 1. Facturación estimada

**El número que NO debes usar:** 2.400 × $39 = **$93.600 MRR (~$1,1M/año)**. Es el techo teórico, no la realidad. **[INF-alta de que este número está inflado]**, por tres razones:

1. **El contador de "miembros" casi nunca es igual a "pagadores".** Muchas plataformas de membresía (Skool, Circle, etc.) muestran el total histórico o incluyen miembros gratuitos, en trial, comped y a veces ex-miembros. **[INF-alta]** — es práctica estándar del sector.
2. **Precio efectivo < precio de lista.** Si existió precio fundador, descuentos anuales no visibles, o promos, el ingreso medio por miembro baja. **[INF-media]** — no vemos plan anual, pero es raro que no exista alguno.
3. **Churn.** Comunidades de pago en nichos de "hacer dinero/productividad/automatización" suelen tener churn mensual de 5-15%. **[INF-media]** — benchmark del sector, no dato de ellos.

**Mis tres escenarios:**

| Escenario | Supuesto clave | MRR estimado | ARR |
|---|---|---|---|
| Optimista | 90% pagan, precio efectivo $36 | ~$78k | ~$930k |
| **Base [mi apuesta]** | 55-70% pagan, precio efectivo $32-35 | **~$45-55k** | **~$540-660k** |
| Conservador | Contador incluye muchos free/inactivos, 35-45% pagan | ~$28-38k | ~$340-450k |

**Mi lectura: probablemente facturan $500-650k anuales.** **[INF-media]** — el rango es amplio porque el dato del contador es ambiguo. Si pudieras verificar en la plataforma si existe un tier gratuito, esto se afina muchísimo.

---

## 2. ¿Qué tan sano es el negocio?

### Señales positivas
- **Conversión audiencia→miembro del ~4%** (2.400/60.000). Si el fundador es el canal principal de adquisición, es una tasa saludable; el benchmark típico de audiencia social a membresía de pago es 1-3%. **[INF-media]** — asume que la audiencia del fundador es la fuente principal, cosa que no sabemos.
- **CAC probablemente bajo o cero** si crecen orgánico vía el fundador. **[INF-media]**
- **Cadencia de 3 posts/semana pública** indica operación viva, no abandonada. **[DATO + INF-alta]**

### Señales de riesgo (las tuyas para atacar)
- **Riesgo de persona única.** El negocio parece depender del fundador como imán de adquisición. Si él se quema o pivota, el embudo se seca. **[INF-alta]**
- **12 cursos sin claridad de completitud.** Dos lecturas posibles: (a) catálogo amplio y maduro, o (b) muchos cursos a medias para inflar el valor percibido — patrón muy común en comunidades de pago. **[INF-baja]** — no tengo forma de saber cuál es sin entrar. *Esto es lo primero que verificaría comprando un mes.*
- **3 posts/semana es cadencia moderada, no de comunidad hiperactiva.** Ojo: solo vemos el feed *público*; dentro puede haber mucha más actividad. **[INF-baja]** — no concluyas nada fuerte de aquí.
- **Sin plan anual visible = poco cash flow anticipado y retención no "asegurada" por prepago.** **[INF-media]** — o simplemente no lo muestran en portada.

### Lo que NO sabemos y más importa
Churn real, engagement interno, cuánto tiempo llevan operando, si el contador crece o está estancado, tamaño de equipo. **Recomendación concreta: paga $39 un mes.** Es la inteligencia competitiva más barata que vas a conseguir: verás actividad real, calidad de cursos, y si el número de miembros se mueve.

---

## 3. Cómo competirles

Ordenado por lo que atacaría primero:

**a) Ataca la profundidad, no la amplitud.** Si mi inferencia sobre los cursos incompletos es correcta **[INF-baja, verificar]**, su promesa es "mucho contenido" y su debilidad es "poco resultado". Posiciónate como *un* camino completo con resultado medible ("automatiza tu primer proceso en 30 días") vs. su biblioteca de 12 cursos.

**b) Niche down.** "Automatización" es amplio. Ellos, con 2.400 miembros, probablemente son generalistas. Elige un vertical (automatización para agencias, para e-commerce, para operaciones de RRHH…) donde puedas ser *el* especialista. **[INF-alta de que un vertical bien elegido convierte mejor que competir de frente]**

**c) No compitas en precio a la baja de entrada.** $39/mes es precio medio. Bajar a $19 te posiciona como versión barata; considera lo contrario: precio superior con más acceso directo (calls, revisión de automatizaciones) que un fundador con 2.400 miembros ya no puede escalar. Su tamaño es tu ángulo: "aquí sí te responden". **[INF-media]**

**d) Construye tu propio embudo de audiencia antes de nada.** Su ventaja real no son los cursos ni la comunidad: son los 60.000 seguidores del fundador. **[INF-alta]** Sin un motor de adquisición propio, cualquier ventaja de producto tuya es invisible.

**e) Ofrece lo que ellos estructuralmente no muestran:** garantía de resultado, prueba gratuita real, o plan anual con descuento agresivo para asegurar retención — cosas ausentes o invisibles en su página. **[DATO sobre la ausencia + INF-baja sobre si existen internamente]**

---

## Resumen ejecutivo

| Pregunta | Respuesta corta | Certeza |
|---|---|---|
| ¿Cuánto facturan? | Probable $500-650k/año; techo $1,1M muy improbable | Media |
| ¿Es sano? | Operativo y con adquisición barata, pero dependiente del fundador y con retención desconocida | Media-baja |
| ¿Cómo compito? | Vertical específico + profundidad/resultado + acceso premium; y construye audiencia propia ya | Alta (en la lógica), media (en que funcione en tu caso) |

**Siguiente paso con mejor ROI:** gasta $39, entra un mes, y vuelve con datos de churn aparente, actividad interna y estado real de los cursos. Con eso convierto la mitad de mis inferencias en datos.