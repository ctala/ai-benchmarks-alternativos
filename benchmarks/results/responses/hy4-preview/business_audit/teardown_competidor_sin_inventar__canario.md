# Tencent Hy4 preview — business_audit/teardown_competidor_sin_inventar

- model_id: `tencent/hy4-preview`
- success: True  | final: 2.56 | quality: 2.0
- latency_total: 293.238s | tokens_per_second: 52.1
- input_tokens: 213 | output_tokens: 15282

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista competitivo. Distingues SIEMPRE entre lo que sabes y lo que estás infiriendo, y marcas tu nivel de certeza.

**user:**

Hazme un teardown de un competidor. Esto es TODO lo que pude ver desde fuera (su página pública):

- Comunidad de pago sobre automatización, en una plataforma tipo membresía.
- Muestra '2.400 miembros' en la portada.
- Precio visible: $39/mes. No se ve si hay plan anual ni descuentos.
- Publican 3 posts por semana en el feed público.
- El fundador tiene 60.000 seguidores en una red social.
- Tienen 12 cursos listados, no se ve cuántos están terminados.

Quiero saber cuánto factura, qué tan sano es el negocio y cómo les compito.


## Respuesta completa

Voy a hacerlo como analista: separo **lo que sé**, **lo que calculo** y **lo que infiero**, y marco la certeza de cada cosa.

> **Leyenda de certeza**
> - **[HECHO]** = dato público que aportaste o que se deriva sin supuestos.
> - **[DERIVADO]** = matemática sobre hechos; alta certeza en el cálculo, pero no en que la realidad coincida.
> - **[INFERENCIA ALTA / MEDIA / BAJA]** = conclusión con supuestos explícitos.
> - **[HIPÓTESIS]** = especulación accionable; hay que validarla.

---

## 1. Mapa rápido: qué sabemos y qué no

| Dato | Qué es realmente | Certeza | Implicación |
|---|---|---|---|
| Comunidad de pago sobre automatización | Producto: membresía + comunidad + cursos | **[HECHO]** | Negocio recurrente, no venta única |
| “2.400 miembros” en portada | Número mostrado de cuentas en la plataforma | **[HECHO]** | No equivale a “2.400 pagando activos” |
| Precio visible $39/mes | Precio público mensual | **[HECHO]** | Techo de ARPU si todos pagan eso |
| No se ve plan anual ni descuentos | Ausencia de evidencia pública | **[HECHO]** | No significa que no exista; puede estar oculto en checkout |
| 3 posts/semana en feed público | Cadencia de contenido | **[HECHO]** | Señal de operación activa |
| Founder con 60.000 seguidores | Audiencia en una red social | **[HECHO]** | Ventaja de distribución, pero no sabemos engagement |
| 12 cursos listados | Biblioteca de productos | **[HECHO]** | No sabemos cuántos están terminados/actualizados |

**[HECHO lógico]**  
- “No se ve anual” ≠ “no existe”. Puede haber anual oculto, cupones, upsells, planes de equipo o B2B.  
- “2.400 miembros” es un **stock de cuentas**, no necesariamente suscriptores activos, ni mucho menos MRR.

---

## 2. ¿Cuánto factura?

### 2.1 El techo matemático

**[DERIVADO — Certeza alta en el cálculo, baja en que sea la realidad]**

Si los 2.400 fueran **suscriptores activos, pagando $39/mes, todos mensuales y sin descuentos**:

- **MRR bruto** = 2.400 × $39 = **$93.600/mes**
- **ARR bruto** = $93.600 × 12 = **$1.123.200/año**

Ese es el **techo absoluto**. Cada supuesto puede fallar.

---

### 2.2 Escenarios más realistas

Aquí ya entro en inferencia. El número real casi nunca es el techo.

| Escenario | Miembros que pagan | ARPU equivalente/mes | MRR bruto | ARR bruto | Certeza |
|---|---:|---:|---:|---:|---|
| **Techo puro** (todos activos, mensuales, sin descuento) | 2.400 | $39 | **$93.6k** | **$1.12M** | Alta en cálculo / **Baja** en realidad |
| **Base** (60–80% activos; puede haber mix anual con ligero descuento) | 1.440–1.920 | $32–$39 | **$46k–$75k** | **$552k–$900k** | **Media** |
| **Conservador** (40–60% activos; churn alto; impuestos/descuentos) | 960–1.440 | $30–$39 | **$29k–$56k** | **$350k–$675k** | **Media-Baja** |

**[INFERENCIA MEDIA]**  
Mi estimación actual más defendible es que están en el rango de:

> **$45.000–$75.000 MRR** → **$540.000–$900.000 ARR bruto**

con un techo matemático de **$93.6k MRR / $1.12M ARR** si no hay fugas.

---

### 2.3 Ojo con MRR vs. cash cobrado

**[HECHO]** No ves plan anual.  
**[INFERENCIA BAJA]** Podría no existir, o existir oculto.

Si existiera un plan anual, por ejemplo:

- 50% mensuales: 1.200 × $468/año = $561.600
- 50% anuales con 2 meses gratis: 1.200 × $390 = $468.000
- **Cash en 12 meses** ≈ **$1.03M**

Es decir: podrían estar cerca de **$1M en cash cobrado** en un año, aunque su MRR equivalente sea menor porque los anuales ya pagaron por adelantado.

También puede pasar lo contrario: que los 2.400 sean **acumulados históricos** y hoy solo queden 800–1.200 activos. En ese caso, facturarían bastante menos.

---

### 2.4 Neto, no bruto

**[INFERENCIA MEDIA-BAJA]**  
De ese bruto hay que restar:

- Pasarela de pago: ~3% + fijo (**~$3k–$4k/mes** si MRR es $93k).
- Plataforma de membresía: según herramienta, **~$100–$500/mes** si es plan profesional, o más si usan Kajabi/Circle con planes altos.
- Impuestos: si el precio incluye IVA/GST, el neto puede caer un 15–25%.
- Reembolsos y chargebacks.

**[DERIVADO]**  
En el escenario techo, el neto antes de impuestos probablemente quede en **~$85k–$90k MRR**. En el escenario base, **~$43k–$70k MRR**.

---

## 3. ¿Qué tan sano es el negocio?

### Señales positivas

- **[INFERENCIA MEDIA]** 2.400 miembros + 12 cursos indican tracción y producto ya construido.
- **[INFERENCIA MEDIA]** Founder con 60k seguidores = canal de adquisición orgánico si convierte bien.
- **[HECHO]** Publican 3 posts/semana: no es un proyecto abandonado.
- **[INFERENCIA MEDIA]** $39/mes con 12 cursos es percibido como “barato” si los cursos están buenos; eso facilita conversión inicial.

### Incógnitas críticas

1. **Churn**  
   **[INFERENCIA BAJA]** No lo sabemos. En comunidades de ticket bajo mensual, un churn mensual de 5–10% es común.  
   **[DERIVADO]** Si tuvieran 2.400 activos:
   - 5% churn = pierden **120 miembros/mes**
   - 10% churn = pierden **240 miembros/mes**

   Para mantenerse planos, necesitan reponer eso cada mes. Si solo tienen 1.200 activos, necesitan reponer 60–120/mes.

2. **Mix mensual/anual**  
   **[HECHO]** No se ve anual.  
   **[INFERENCIA MEDIA]** Si no tienen anual, el riesgo de churn es mayor y el cash flow es menos predecible. Si lo tienen oculto, su retención mejora.

3. **Costes y equipo**  
   **[INFERENCIA MEDIA]** Si es founder + algún contractor, los márgenes pueden ser altos (60–80% neto). Si tienen equipo de soporte, editores, community manager y ads, el margen baja fuerte.

4. **Dependencia del founder**  
   **[INFERENCIA MEDIA]** 60k seguidores y marca personal son una ventaja enorme, pero también un riesgo: si el founder deja de publicar o se quema, adquisición y retención sufren.

5. **Calidad real de los 12 cursos**  
   **[INFERENCIA BAJA]** Automatización cambia rápido (Make, Zapier, n8n, IA, APIs). Si los cursos están desactualizados, el churn subirá.

### Veredicto de salud

**[INFERENCIA MEDIA]**  
Parece un negocio **con tracción y probablemente rentable en caja**, pero **frágil**: ticket bajo, churn desconocido, dependencia del founder y de una sola audiencia.

No es una “máquina de dinero garantizada”. Es un negocio de membresía de bajo ticket que necesita volumen constante y retención fuerte.

---

## 4. Cómo les compito

Regla estratégica: **no compitas siendo “otra comunidad de automatización de $39 con 12 cursos”**. Ahí ya tienen escala y audiencia. Compite donde su tamaño no les sirva o donde tengan un punto ciego.

### 4.1 Ataca el empaquetado / monetización

**[HECHO]** No ves anual ni descuentos.  
**[HIPÓTESIS]** Puede que no lo tengan, o que lo oculten mal.

Movimientos:

- Lanza **plan anual** con 2 meses gratis: mejora cash flow y retención.
- Lanza **plan de equipos / B2B**. Automatización la compran empresas. Mientras ellos venden $39 a individuos, tú puedes vender:
  - $97–$297/mes por asiento de equipo
  - $3k–$15k por implementación / auditoría / DFY
- Crea un **tier premium** con soporte, Q&A en vivo, plantillas privadas o implementación asistida.

**[INFERENCIA MEDIA]**  
Si no monetizan anual ni B2B, ahí hay una palanca clara de ingresos que tú sí puedes capturar.

---

### 4.2 Ataca “resultados” vs. “contenido muerto”

12 cursos pueden ser mucho contenido… y poco consumo.

**[HIPÓTESIS]** Parte de esos cursos pueden estar desactualizados o sin terminar.

Tu propuesta:

- Onboarding de 30/60/90 días.
- Cohortes en vivo cada cierto tiempo.
- Plantillas listas para importar.
- Retos semanales con entregables.
- Office hours / soporte en vivo.
- Casos de éxito medibles: horas ahorradas, ROI, integraciones en producción.

**[INFERENCIA MEDIA]**  
Si su comunidad es pasiva, tú puedes posicionarte como “acompañamiento real”, no solo “biblioteca de videos”.

---

### 4.3 Ataca por nicho vertical

Automatización es gigante. Una comunidad generalista es difícil de mantener al día.

**[HIPÓTESIS]** Su contenido probablemente es generalista: “automatiza todo con IA”.

Tu movimiento:

- “Automatización para ecommerce”
- “Automatización para agencias”
- “Automatización para abogados / inmobiliarias / SaaS”
- “n8n + IA para operaciones internas”

La especialización permite cobrar más, reducir competencia directa y convertirse en referencia de un segmento.

---

### 4.4 Ataca por distribución propia

El founder tiene 60k seguidores, pero:

**[HECHO]** No sabemos engagement.  
**[INFERENCIA BAJA]** 60k seguidores no significan 60k compradores ni 60k personas activas.

Valida antes de asustarte:

- ¿Cuántos likes/comentarios tienen sus posts?
- ¿Sus 3 posts semanales tienen interacción real o parecen posts fantasma?
- ¿Venden desde una sola red?

Tu ventaja:

- Construye **SEO/YouTube**: automatización tiene mucha intención de búsqueda.
- Newsletter propia.
- Alianzas con herramientas (n8n, Make, Airtable, Zapier).
- Comunidad gratuita de captación.

---

### 4.5 No entres en guerra de precios

**[HECHO]** Su precio visible es $39/mes.

Si entras con algo similar a $39, compites por el usuario más sensible al precio y con menos compromiso.

Mejor:

- Mismo precio, pero **más resultado**: onboarding, plantillas, soporte.
- O precio más alto con más valor: $97/mes, $497/año, cohortes de $800–$2.000.
- O modelo híbrido: comunidad low-ticket + servicios DFY/consultoría high-ticket.

---

## 5. Matriz de ataque: “si confirmas X, haz Y”

| Si confirmas… | Ataca con… |
|---|---|
| No tienen plan anual | Lanza anual con descuento y mejora tu cash flow |
| No tienen plan de equipos/B2B | Vende a empresas: seats, facturación, implementación |
| Los 12 cursos están desactualizados | Posiciónate como “actualizado mensualmente” |
| La comunidad interna está fría | Vive de onboarding, retos y soporte en vivo |
| El founder concentra todo el marketing | Construye marca + equipo + alianzas, no dependas de una persona |
| Su audiencia tiene bajo engagement | Invierte en SEO/YouTube, donde la intención es mayor |
| Su churn es alto | Ataca con garantía de resultados o modelo de implementación |

---

## 6. Qué haría yo en los próximos 14 días para validar

Todo esto son inferencias. Para bajar la incertidumbre:

1. **Mystery shopping**: simula compra y captura el checkout.  
   Busca: plan anual, cupones, impuestos, garantía, reembolso, estado real de los 12 cursos.

2. **Wayback Machine + capturas semanales**:  
   Mide si “2.400 miembros” sube, baja o se queda plano. Eso te dice churn y crecimiento neto.

3. **BuiltWith / Wappalyzer**:  
   Identifica plataforma (Skool, Circle, Kajabi, Mighty…) y stack.

4. **Meta Ad Library / LinkedIn Ads**:  
   Si pagan publicidad, su CAC no es solo orgánico.

5. **LinkedIn**:  
   Busca empleados o colaboradores para estimar tamaño de equipo y costes fijos.

6. **Análisis del founder**:  
   No te quedes con “60k seguidores”. Mide crecimiento y engagement real.

7. **Busca quejas públicas**:  
   Reddit, X, YouTube, Trustpilot, comentarios. Palabras clave: *cancelé, no lo uso, desactualizado, no responden*.

8. **Mide interacción en su feed público**:  
   Si tienen 2.400 miembros pero sus posts tienen 5 likes, la comunidad está fría.

---

## TL;DR

- **Facturación**:  
  - Techo matemático: **$93.6k MRR / $1.12M ARR bruto**.  
  - Estimación realista: **$45k–$75k MRR / $540k–$900k ARR bruto**.  
  - Neto: menor por comisiones, plataforma e impuestos.  
  - Certeza: **media** en el rango, **baja** en la cifra exacta.

- **Salud**:  
  Negocio con tracción y probablemente rentable en caja, pero **frágil**: ticket bajo, churn desconocido, dependencia del founder y de una sola audiencia. Certeza: **media**.

- **Cómo competir**:  
  No clones su modelo. Ataca con:  
  1. Plan anual y B2B/equipos.  
  2. Resultados medibles y onboarding, no solo cursos.  
  3. Nicho vertical o herramienta específica.  
  4. Contenido actualizado y plantillas listas para usar.  
  5. Distribución propia: SEO/YouTube/newsletter/alianzas.  
  6. Modelo híbrido: comunidad + servicios DFY/consultoría.

Lo más importante: **valida si los 2.400 son activos y si realmente no tienen anual**. Esas dos respuestas cambian por completo la estrategia.