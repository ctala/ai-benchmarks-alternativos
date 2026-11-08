# Qwen 3.8 Max 0902 — business_audit/teardown_competidor_sin_inventar

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 5.09 | quality: 6.0
- latency_total: 279.757s | tokens_per_second: 41.6
- input_tokens: 231 | output_tokens: 11627

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

# Teardown competitivo con datos públicos

**Advertencia de método:** con lo que me diste no puedo saber la facturación real ni la salud exacta del negocio. Puedo darte una estimación por escenarios, separando **hechos observables**, **inferencias** y **supuestos**. Marcaré nivel de certeza así:

- **Alta:** dato observable o cálculo aritmético directo.
- **Media:** inferencia razonable basada en patrones típicos de membresías/comunidades.
- **Baja:** hipótesis estratégica; requiere validación.

---

## 1) Lo que sé con certeza alta

| Dato observado | Lectura inicial | Certeza |
|---|---|---|
| Comunidad de pago sobre automatización | Hay intención de monetización recurrente | Alta |
| Plataforma tipo membresía | Probablemente usan Circle, Skool, Kajabi, Discord pago, Memberstack, etc. | Alta en formato; baja en herramienta exacta |
| Muestra “2.400 miembros” en portada | Es una métrica de prueba social | Alta como número visible; baja sobre qué significa exactamente |
| Precio visible: $39/mes | Precio de entrada conocido | Alta |
| No se ve plan anual ni descuentos | Puede no existir, estar oculto en checkout o no ser prioritario | Media-baja |
| 3 posts por semana en feed público | Cadencia de contenido activo | Alta en cadencia; baja en engagement real |
| Fundador con 60.000 seguidores en una red | Tienen canal de distribución propio | Alta |
| 12 cursos listados | Hay biblioteca de contenido | Alta como listado; baja en calidad/completitud |

---

## 2) Lo que no sé y es crítico

No puedo afirmar sin datos adicionales:

1. **Cuántos de esos 2.400 miembros son realmente pagos.**
2. **Cuántos son miembros activos vs registrados históricos.**
3. **Si el contador incluye trials, free tier, antiguos miembros o cuentas duplicadas.**
4. **Churn mensual**, es decir, cuántos se dan de baja cada mes.
5. **Ingresos reales por anualidades, descuentos, upsells, afiliados o servicios.**
6. **Costos del equipo, ads, herramientas, producción de contenido.**
7. **Engagement real de la comunidad.**
8. **Si los 12 cursos están completos, actualizados y generan retención.**
9. **Si el fundador es el único motor de ventas o hay sistema.**
10. **Si el negocio depende de publicidad pagada o de audiencia orgánica.**

**Conclusión rápida:** puedo estimar facturación, pero no afirmarla.

---

# 3) Estimación de facturación

## Techo máximo simple

Si todos los miembros visibles fueran pagos activos a $39/mes:

> **2.400 × $39 = $93.600/mes**  
> **$93.600 × 12 = $1.123.200/año**

Ese es el **techo bruto simple**, asumiendo que:

- 2.400 = miembros pagos activos.
- Todos pagan $39/mes.
- No hay descuentos, trials, cuentas gratis, miembros regalados, cuentas de equipo o planes anuales que cambien el ingreso mensual reconocido.

**Certeza del techo:** baja como realidad; alta como cálculo máximo.

---

## Escenarios de facturación

### Escenario conservador

**Supuesto:** los 2.400 miembros incluyen usuarios no pagos, trials, miembros antiguos, cuentas duplicadas o free tier.  
**Rango de miembros pagos:** 30%–50%  
**Miembros pagos estimados:** 720–1.200  
**Precio efectivo:** $30–$36/mes por descuentos, anualidades, promociones o impagos.

| Miembros pagos | Precio efectivo | MRR bruto | ARR bruto |
|---:|---:|---:|---:|
| 720 | $30 | $21.600/mes | $259.200/año |
| 1.200 | $36 | $43.200/mes | $518.400/año |

**Facturación estimada conservadora:**  
**$21k–$43k MRR**  
**$260k–$520k ARR**

**Certeza:** media-baja, pero es un escenario prudente si el número público no refleja solo pagos activos.

---

### Escenario base

**Supuesto:** la comunidad es de pago y el número mostrado es bastante cercano a miembros reales, pero no todos están activos o pagan tarifa completa.  
**Rango de miembros pagos:** 60%–80%  
**Miembros pagos estimados:** 1.440–1.920  
**Precio efectivo:** $35–$39/mes.

| Miembros pagos | Precio efectivo | MRR bruto | ARR bruto |
|---:|---:|---:|---:|
| 1.440 | $35 | $50.400/mes | $604.800/año |
| 1.920 | $39 | $74.880/mes | $898.560/año |

**Facturación estimada base:**  
**$50k–$75k MRR**  
**$600k–$900k ARR**

**Certeza:** media-baja.  
Si tuviera que apostar con los datos actuales, este sería mi rango central si el negocio parece activo y el contador no es puramente inflado.

---

### Escenario optimista

**Supuesto:** 2.400 miembros son mayormente pagos activos y el precio es $39/mes sin descuentos relevantes.  
**Miembros pagos:** 90%–100%  
**Precio:** $39/mes.

| Miembros pagos | Precio | MRR bruto | ARR bruto |
|---:|---:|---:|---:|
| 2.160 | $39 | $84.240/mes | $1.010.880/año |
| 2.400 | $39 | $93.600/mes | $1.123.200/año |

**Facturación estimada optimista:**  
**$84k–$94k MRR**  
**$1.0M–$1.12M ARR**

**Certeza:** baja. Es posible, pero no debería asumirse sin verificar.

---

## Mi estimación resumida

| Escenario | MRR estimado | ARR estimado | Certeza |
|---|---:|---:|---|
| Conservador | $21k–$43k | $260k–$520k | Media-baja |
| Base | $50k–$75k | $600k–$900k | Media-baja |
| Optimista | $84k–$94k | $1.0M–$1.12M | Baja |

### Mi apuesta informada

**Si los 2.400 miembros son mayormente pagos:**  
**$50k–$80k MRR.**

**Si los 2.400 incluyen gratis, trials, antiguos miembros o vanity metric:**  
**$20k–$45k MRR.**

**Certeza general de la estimación:** baja.  
No porque el cálculo sea difícil, sino porque la variable clave —miembros pagos reales— no está confirmada.

---

# 4) Ingresos netos aproximados

La facturación bruta no es lo que se llevan a casa. Hay que descontar:

| Concepto | Impacto estimado | Certeza |
|---|---:|---|
| Pasarela de pago | 2.5%–4% | Alta |
| Plataforma de membresía | $100–$1.000+/mes o % según proveedor | Media |
| Impuestos según país | Variable | Alta que existe; baja en monto |
| Reembolsos | 1%–5% típico en infoproductos | Baja |
| Afiliados, si existen | 10%–50% de comisión sobre ventas referidas | Baja |
| Equipo/contratistas | Variable | Baja |
| Publicidad | Variable | Baja |

Para un MRR bruto de $75.000:

- Después de pasarela y plataforma, quizá queden **$67k–$72k**.
- Después de equipo, herramientas, ads y producción, el margen real puede caer mucho.
- Si es un negocio tipo creador solo o equipo pequeño, el margen puede ser alto.
- Si tienen equipo de contenido, soporte, ads y comunidad, el margen baja.

**Certeza:** baja.

---

# 5) Unit economics aproximados

## Precio medio

ARPU visible: **$39/mes**.

Si el precio real efectivo baja por descuentos o anualidades, podríamos hablar de **$30–$39/mes**.

## Conversión desde la audiencia del fundador

El fundador tiene 60.000 seguidores.

Si 2.400 fueran pagos:

> 2.400 / 60.000 = **4%**

Eso sería una conversión alta, pero no imposible si la audiencia es muy fiel y el producto está muy alineado.

Si solo 1.200 fueran pagos:

> 1.200 / 60.000 = **2%**

Eso es más razonable.

Si solo 720 fueran pagos:

> 720 / 60.000 = **1.2%**

También razonable.

**Inferencia:** el negocio probablemente depende mucho del fundador como canal de adquisición.  
**Certeza:** media.

---

## LTV estimado

LTV = ingreso medio mensual × vida media del cliente.

| Churn mensual | Vida media aprox. | LTV bruto a $39 |
|---:|---:|---:|
| 5% | 20 meses | $780 |
| 8% | 12.5 meses | $487 |
| 10% | 10 meses | $390 |
| 15% | 6.7 meses | $260 |
| 20% | 5 meses | $195 |

**Lectura:**

- Con churn de 8%–10%, el negocio puede ser sano si el CAC no es muy alto.
- Con churn de 15%–20%, necesita adquirir miembros constantemente.
- Si pagan ads, un churn alto puede volver el modelo frágil.

**Certeza:** baja porque no conocemos churn real.

---

## CAC máximo razonable

Con LTV bruto de $390 y buscando un ratio sano de 3:1:

> CAC objetivo máximo: **$130 aproximadamente**.

Si el LTV es $260:

> CAC objetivo máximo: **$85 aproximadamente**.

Si el LTV es $780:

> CAC objetivo máximo: **$260 aproximadamente**.

Esto sin contar costos operativos.

**Certeza:** media como marco, baja para este caso concreto.

---

# 6) Señales de salud del negocio

## Señales positivas

| Señal | Interpretación | Certeza |
|---|---|---|
| Precio visible de $39/mes | Oferta clara y monetización activa | Alta |
| 2.400 miembros visibles | Prueba social relevante | Alta como dato visible |
| Fundador con 60k seguidores | Canal propio de distribución | Alta |
| 3 posts/semana | Actividad pública constante | Alta |
| 12 cursos listados | Biblioteca de contenido amplia | Alta como listado |
| Nicho de automatización | Demanda empresarial/profesional relevante | Media |

**Lectura positiva:**  
Parece un negocio con audiencia, oferta y contenido. Si la mayoría de esos 2.400 son pagos, probablemente sea un negocio sano o al menos con tracción real.

**Certeza:** media.

---

## Señales de riesgo

| Riesgo | Por qué importa | Certeza |
|---|---|---|
| No se sabe si 2.400 son pagos | Puede inflar percepción de tamaño | Alta como riesgo |
| No se ve plan anual | Puede haber poca optimización de retención/cash | Media |
| No se sabe cuántos cursos están terminados | Puede haber deuda de producto | Media |
| Dependencia del fundador | Si el fundador deja de publicar, ventas pueden caer | Media |
| Comunidad de $39/mes | Precio bajo si requiere mucho soporte | Media |
| No se ve engagement real | Puede haber comunidad fría | Media |
| Nicho automatización puede estar saturado | Necesita diferenciación clara | Media |
| Posible churn alto en membresías educativas | Riesgo de ingresos recurrentes frágiles | Media-baja |

**Lectura de riesgo:**  
El negocio puede estar vivo, pero no sabemos si es robusto. La clave está en retención, engagement y costo de adquisición.

---

## Score rápido de salud

Esto es subjetivo, pero útil:

| Área | Puntuación estimada | Certeza |
|---|---:|---|
| Demanda | 7/10 | Media |
| Distribución | 8/10 | Media-alta |
| Monetización | 7/10 | Media |
| Retención | 4/10 | Baja |
| Producto | 6/10 | Baja |
| Margen | 7/10 | Baja |
| Riesgo fundador | 6/10 riesgo | Media |
| **Salud general estimada** | **6.5/10** | Baja-media |

**Interpretación:**  
No parece un negocio muerto. Parece tener tracción. Pero no puedo afirmar que sea sólido sin ver retención, engagement y costos.

---

# 7) Cómo competirles

## Regla principal

No les competiría frontalmente con “otra comunidad de automatización por $39/mes” si no tienes audiencia comparable.

**Mejor estrategia:** atacar por un flanco donde ellos sean débiles o genéricos.

---

## A) Estrategia de posicionamiento

### Opción 1: Nicho vertical

En vez de:

> “Comunidad de automatización”

Usar:

> “Automatización para [sector específico]”

Ejemplos:

- Automatización para agencias.
- Automatización para e-commerce.
- Automatización para inmobiliarias.
- Automatización para clínicas.
- Automatización para equipos de ventas.
- Automatización para operaciones/finance.
- Automatización para creadores de contenido.

**Ventaja:** reduces competition and increase perceived relevance.  
**Certeza estratégica:** alta.

---

### Opción 2: Vender resultado, no acceso

Ellos probablemente venden:

- Comunidad.
- Cursos.
- Información.
- Automatización general.

Tú puedes vender:

- Implementación.
- Plantillas listas.
- Workflows descargables.
- Casos de uso por rol.
- Retos de 30 días.
- Certificación.
- “Tu primer sistema automatizado en X días”.

Ejemplo de promesa:

> “Implementa tu primer sistema de automatización en 14 días, aunque no sepas programar.”

**Ventaja:** más tangible que “acceso a comunidad”.  
**Certeza estratégica:** alta.

---

### Opción 3: Subir de precio y dar más acompañamiento

Si ellos cobran $39/mes y parecen low-touch, tú puedes cobrar:

- $79/mes
- $99/mes
- $149/mes
- $299/mes
- $500–$2.000 por cohortes
- $2.000–$10.000 por done-for-you

No compitas por ser más barato. Compite por ser más específico, más acompañado o más orientado a resultados.

**Certeza:** media-alta si el nicho tiene poder adquisitivo.

---

### Opción 4: Modelo híbrido comunidad + servicio

Una membresía educativa sufre churn. Un servicio híbrido puede retener mejor.

Ejemplos:

- Comunidad + oficina mensual.
- Comunidad + auditoría trimestral.
- Comunidad + plantillas nuevas cada mes.
- Comunidad + implementación guiada.
- Comunidad + soporte técnico.
- Comunidad + certificación.

**Ventaja:** aumenta LTV y reduce churn.  
**Certeza:** media-alta.

---

## B) Estrategia de oferta

### Oferta recomendada si empiezas

No lanzaría solo “comunidad a $39”.

Lanzaría una escalera:

| Nivel | Oferta | Precio sugerido | Objetivo |
|---|---|---:|---|
| Gratis | Lead magnet, mini-curso, plantilla, newsletter | $0 | Captar leads |
| Entrada | Plantillas + recursos + comunidad básica | $19–$49/mes | Validar demanda |
| Core | Comunidad + retos + plantillas + cursos | $79–$149/mes | Retención |
| Premium | Cohorte en vivo + acompañamiento | $299–$999 | Margen |
| Done-for-you | Implementación personalizada | $1.500–$10.000 | Alto ticket |

**Certeza:** media como estructura; debe validarse con entrevistas y preventa.

---

## C) Estrategia de contenido

Ellos publican 3 posts/semana en feed público. No necesitas publicar más solamente. Necesitas publicar mejor y con más intención de conversión.

### Tipos de contenido que les pueden atacar

1. **Casos reales**
   - “Cómo automaticé X proceso.”
   - “Antes/después.”
   - “Cuánto tiempo ahorra.”

2. **Plantillas descargables**
   - Lead magnets concretos.
   - Workflows listos.
   - Checklists de implementación.

3. **Errores comunes**
   - “Por qué tu automatización falla.”
   - “No automatices esto sin antes arreglar aquello.”

4. **Comparativas**
   - Herramienta A vs herramienta B.
   - Cuándo usar cada una.
   - Costo real de implementación.

5. **Mini implementaciones**
   - Videos cortos mostrando procesos.
   - Tutoriales de 5–10 minutos.
   - Casos por industria.

6. **Prueba social**
   - Testimonios.
   - Capturas de resultados.
   - Métricas de ahorro de tiempo.
   - Casos de alumnos/clientes.

**Certeza:** alta como táctica general.

---

## D) Estrategia de pricing

Si ellos están en $39/mes, tienes tres caminos:

### Camino 1: Precio similar, pero más específico

Cobras $39–$49/mes, pero con una promesa más clara:

> “Automatización para agencias que quieren ahorrar 10 horas al mes.”

**Riesgo:** margen bajo si requiere soporte.  
**Certeza:** media.

---

### Camino 2: Precio mayor, más acompañamiento

Cobras $99–$199/mes e incluyes:

- Llamadas mensuales.
- Revisión de workflows.
- Plantillas premium.
- Comunidad más curada.
- Soporte más rápido.

**Ventaja:** necesitas menos clientes.  
**Certeza:** media-alta en B2B.

---

### Camino 3: Alto ticket

Cobras $1.000–$5.000 por:

- Implementación.
- Diagnóstico.
- Setup de automatización.
- Formación al equipo.
- Mantenimiento.

**Ventaja:** monetizas mejor desde el inicio.  
**Riesgo:** ventas más lentas.  
**Certeza:** media-alta si el cliente tiene presupuesto.

---

## E) Dónde atacar sus debilidades probables

| Debilidad posible | Cómo atacarla | Certeza |
|---|---|---|
| Comunidad genérica | Especialízate en un vertical | Media-alta |
| Cursos sin terminar | Vende implementación guiada o retos | Media |
| Precio bajo con poco soporte | Ofrece acompañamiento premium | Media |
| Dependencia del fundador | Construye marca con múltiples voces/casos | Media |
| No se ve plan anual | Lanza anual con incentivo | Media |
| No se ven resultados concretos | Publica casos medibles | Alta |
| Feed público limitado | Crea contenido más profundo y accionable | Media |
| Audiencia amplia | Ataca un dolor más específico | Alta |

---

# 8) Plan para competir en 90 días

## Días 1–15: Investigación y validación

Objetivo: reducir incertidumbre.

Acciones:

1. Seguir al fundador durante 2 semanas.
2. Registrar cuántas veces publica.
3. Ver qué contenidos generan más interacción.
4. Revisar si el contador de miembros cambia.
5. Entrar a su página de pago si es público.
6. Buscar testimonios.
7. Buscar reviews externas.
8. Revisar si hacen webinars, lanzamientos o ads.
9. Entrevistar a 5–10 personas del nicho.
10. Preguntar:
   - ¿Qué quieren automatizar?
   - ¿Qué han intentado?
   - ¿Pagarían por comunidad, curso o implementación?
   - ¿Cuánto pagarían?
   - ¿Qué les frustra de las soluciones actuales?

**Certeza:** alta que esto mejorará tu estrategia.

---

## Días 16–30: Definir el ángulo

Elige una hipótesis:

- Vertical específico.
- Rol específico.
- Resultado específico.
- Nivel de acompañamiento.
- Precio.

Ejemplo:

> “Ayudo a agencias a automatizar onboarding de clientes y reporting en 30 días.”

Mejor que:

> “Comunidad de automatización.”

**Certeza:** alta.

---

## Días 31–60: Lanzar oferta mínima viable

No necesitas 12 cursos.

Necesitas:

1. Una promesa clara.
2. Una landing simple.
3. Un lead magnet.
4. Una oferta de preventa.
5. 10 cupos beta.
6. Precio de validación.
7. Llamadas de venta o formulario.

Ejemplo de oferta beta:

> “Programa de 30 días para implementar tu primer sistema de automatización. Incluye plantillas, comunidad y 2 llamadas en vivo. Precio fundador: $99/mes o $299 trimestre.”

**Certeza:** media-alta como enfoque de validación.

---

## Días 61–90: Conseguir prueba social

Objetivo: obtener 3–10 casos.

Acciones:

1. Acompañar a los primeros usuarios.
2. Documentar resultados.
3. Pedir testimonios.
4. Publicar casos.
5. Iterar la oferta.
6. Subir precio cuando haya prueba.
7. Crear contenido basado en objeciones reales.

**Certeza:** alta que esto importa.

---

# 9) Qué datos necesitas para afinar el teardown

Si quieres convertir esto en un análisis más preciso, necesitarías:

| Dato | Para qué sirve | Cómo obtenerlo éticamente |
|---|---|---|
| Número real de miembros pagos | Calcular MRR real | Trial, encuesta, entrevista, observación |
| Evolución del contador de miembros | Ver crecimiento/estancamiento | Capturas semanales |
| Nivel de actividad en comunidad | Estimar retención | Entrar como usuario si es público/pago |
| Cantidad de cursos completos | Evaluar producto | Trial o acceso |
| Testimonios y casos | Evaluar satisfacción | Página pública |
| Precio anual oculto | Calcular ingreso efectivo | Checkout |
| Herramienta usada | Estimar costos | Inspección pública |
| Ads activos | Ver si compran tráfico | Meta Ads Library, TikTok Creative Center |
| Equipo visible | Estimar costos | LinkedIn, página “sobre nosotros” |
| Publicaciones del fundador | Ver dependencia | Seguimiento público |
| Reviews externas | Ver reputación | Trustpilot, Reddit, X, YouTube |
| Churn | Salud real | Solo interno; difícil desde fuera |

**Importante:** todo debe hacerse con información pública o acceso legítimo. Nada de cuentas falsas, engaño o violación de términos.

---

# 10) Conclusión ejecutiva

## Facturación estimada

No se puede saber con certeza, pero con los datos públicos:

- **Techo máximo:** $93.6k MRR / $1.12M ARR.
- **Escenario conservador:** $21k–$43k MRR / $260k–$520k ARR.
- **Escenario base:** $50k–$75k MRR / $600k–$900k ARR.
- **Escenario optimista:** $84k–$94k MRR / $1.0M–$1.12M ARR.

**Mi apuesta:** si los 2.400 son mayormente pagos, probablemente estén entre **$50k y $80k MRR**.  
Si el número incluye no pagos, podrían estar entre **$20k y $45k MRR**.

**Certeza:** baja-media.

---

## Salud del negocio

Probablemente tienen:

- Buena distribución por el fundador.
- Oferta clara.
- Prueba social visible.
- Contenido activo.
- Potencial de margen alto si son lean.

Pero les falta confirmar:

- Retención.
- Engagement.
- Miembros reales pagos.
- Completitud del producto.
- Dependencia del fundador.
- Costos de adquisición.

**Salud estimada:** 6.5/10, con certeza baja-media.

---

## Cómo competir

No competiría frontalmente con una comunidad genérica de automatización a $39/mes.

Competiría así:

1. **Elige un nicho específico.**
2. **Vende resultado, no solo acceso.**
3. **Ofrece plantillas, implementación y acompañamiento.**
4. **Cobra más si el cliente es B2B.**
5. **Construye prueba social rápida.**
6. **Crea contenido orientado a casos y dolores concretos.**
7. **Ataca su posible debilidad: genericidad, cursos incompletos o falta de resultados medibles.**
8. **No dependas solo de precio bajo.**

**Frase estratégica:**  
Si ellos venden “aprende automatización”, tú vende “implementa automatización con resultado medible en 30 días”.