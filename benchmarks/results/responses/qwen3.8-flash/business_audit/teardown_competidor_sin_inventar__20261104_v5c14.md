# Qwen 3.8 Flash — business_audit/teardown_competidor_sin_inventar

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 4.47 | quality: 4.0
- latency_total: 95.755s | tokens_per_second: 132.5
- input_tokens: 231 | output_tokens: 12683

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

# Teardown competitivo con datos públicos limitados

## 1. Resumen rápido

**Lo más probable:** si los 2.400 miembros son realmente pagantes a $39/mes, el techo de facturación es aproximadamente **$93.600 MRR** y **$1.123.200 ARR**.

Pero como no puedes ver churn, miembros activos, planes anuales, descuentos, reembolsos, lifetime deals o si los 2.400 incluyen free/trials, el rango razonable sería:

| Escenario | Supuesto | MRR estimado | ARR estimado |
|---|---:|---:|---:|
| Techo visible | 2.400 miembros pagantes a $39/mes | $93.600 | $1.123.200 |
| Escenario probable alto | 80% de los miembros pagantes | $74.880 | $898.560 |
| Escenario probable medio | 60% de los miembros pagantes | $56.160 | $673.920 |
| Escenario bajo | 40% de los miembros pagantes | $37.440 | $449.280 |

**Mi lectura:** negocio **potencialmente sano**, pero con riesgos importantes por dependencia del fundador, posible deuda de contenido y falta de visibilidad de planes anuales/retención.

---

## 2. Datos observados vs. inferencias

| Dato observado | Qué sabemos con certeza | Qué podemos inferir | Certeza de la inferencia |
|---|---|---|---|
| Comunidad de pago sobre automatización | El posicionamiento es pago + nicho técnico/operativo | Vende a profesionales, founders, marketers, ops, agencias, ecommerce o equipos que quieren automatizar procesos | Alta |
| Plataforma tipo membresía | Hay una infraestructura de comunidad, no solo cursos sueltos | El modelo busca recurrencia, no solo venta única de curso | Alta |
| Muestra 2.400 miembros en portada | Es un número público, no una auditoría | Puede ser total de miembros, miembros históricos, free + paid, o solo paid. No podemos confirmarlo | Baja |
| Precio visible: $39/mes | Hay una oferta mensual a $39 | Si todos los miembros pagan esa tarifa, el techo de revenue es alto; si hay free, trials, descuentos o planes anuales, el revenue real puede bajar | Media |
| No se ve plan anual ni descuentos | En la página pública no aparece | Puede que no tengan anual, o que esté oculto en checkout, upsell, campaña o sección privada | Media |
| Publican 3 posts/semana en feed público | Hay actividad visible de contenido | Cadencia moderada. No sabemos si el feed privado tiene más actividad ni si los miembros interactúan | Media |
| Fundador con 60.000 seguidores | Tiene audiencia propia | La adquisición probablemente depende mucho del fundador. Esto es una fuerza, pero también un riesgo de concentración | Alta |
| 12 cursos listados | Hay catálogo de contenido formativo | Puede ser una fortaleza si están terminados y actualizados, o un riesgo si son cursos inacabados, desactualizados o sin implementación | Baja |

---

## 3. Estimación de facturación

### 3.1 Techo visible

Si asumimos el escenario más favorable:

- 2.400 miembros pagantes.
- Todos pagan $39/mes.
- No hay descuentos.
- No hay free members.
- No hay churn visible en el número.
- No hay lifetime deals.

Entonces:

**2.400 × $39 = $93.600 MRR**

**$93.600 × 12 = $1.123.200 ARR**

Este es el **techo visible**, no una confirmación.

---

### 3.2 Escenarios más realistas

Como “miembros” puede incluir free, trials, inactivos, cancelados históricos o cuentas duplicadas, conviene usar escenarios.

| % de miembros realmente pagantes | Miembros pagantes | MRR | ARR |
|---:|---:|---:|---:|
| 100% | 2.400 | $93.600 | $1.123.200 |
| 80% | 1.920 | $74.880 | $898.560 |
| 60% | 1.440 | $56.160 | $673.920 |
| 50% | 1.200 | $46.800 | $561.600 |
| 40% | 960 | $37.440 | $449.280 |

**Mi rango probable:** entre **$500k y $950k ARR**, si el número público de 2.400 miembros incluye free, trials o miembros inactivos.

**Rango optimista:** alrededor de **$1.1M ARR**, si la mayoría son pagantes y no hay grandes descuentos.

---

### 3.3 Efecto de un plan anual oculto

Si tuvieran plan anual con descuento, la facturación mensual equivalente podría bajar, aunque el cash upfront mejoraría.

Ejemplo:

- 30% de los miembros pagan anual a $390/año.
- 70% pagan mensual a $39/mes.
- 2.400 miembros pagantes.

MRR equivalente:

- Anual: $390 / 12 = $32,50/mes.
- Mensual: $39/mes.
- ARPU mensual promedio:  
  0,3 × $32,50 + 0,7 × $39 = $37,05.

MRR equivalente:

**2.400 × $37,05 = $88.920 MRR**

ARR:

**$88.920 × 12 = $1.067.040 ARR**

Es decir, aunque el número de miembros sea el mismo, un plan anual puede reducir ligeramente el MRR reportado, pero mejorar caja y retención.

---

## 4. ¿Qué tan sano parece el negocio?

### Veredicto general

**Negocio potencialmente sano, pero frágil en algunos puntos.**

No parece un negocio débil: tiene audiencia, precio recurrente, comunidad de nicho y contenido formativo. Pero tampoco parece un negocio con moat fuerte si depende mucho del fundador, tiene cursos sin evidencia de finalización y no muestra claramente planes anuales, retención o resultados.

---

## 5. Scorecard de salud del negocio

| Dimensión | Lectura | Nota | Certeza |
|---|---|---:|---:|
| Modelo de negocio | Comunidad de pago recurrente + cursos. Buena estructura para LTV | 8/10 | Alta |
| Precio | $39/mes es viable para nicho profesional. No parece barato | 7/10 | Alta |
| Tracción visible | 2.400 miembros es una base interesante | 7/10 | Media |
| Calidad del número de miembros | Desconocido: ¿paid, free, trials, inactivos? | 4/10 | Baja |
| Adquisición | Fundador con 60k seguidores puede traer tráfico constante | 7/10 | Alta |
| Dependencia del fundador | Riesgo alto: si el fundador deja de publicar, el negocio puede resentirse | 4/10 | Media |
| Contenido | 12 cursos listados pueden ser fortaleza o deuda | 5/10 | Baja |
| Cadencia pública | 3 posts/semana es razonable, pero no garantiza comunidad activa | 6/10 | Media |
| Retención | No hay datos de churn, renovación, comentarios, testimonios o engagement interno | 3/10 | Baja |
| Moat competitivo | Comunidad + fundador + contenido. Replicable si no hay resultados demostrables | 5/10 | Media |
| Salud global estimada | **6,5/10** | 6,5/10 | Media-baja |

---

## 6. Señales positivas

### 6.1 Precio recurrente en nicho técnico

**[Dato]** $39/mes.

**[Inferencia]** No están compitiendo en el rango $10-$19/mes, que suele ser más volátil y con más churn. $39/mes implica que esperan valor profesional.

**[Certeza]** Alta.

---

### 6.2 Comunidad de automatización

**[Dato]** Comunidad de pago sobre automatización.

**[Inferencia]** El nicho tiene dolor real: procesos manuales, herramientas desconectadas, pérdida de tiempo, errores operativos, falta de SOPs, necesidad de escalar sin contratar.

**[Certeza]** Alta.

---

### 6.3 Fundador con audiencia

**[Dato]** 60.000 seguidores.

**[Inferencia]** Tienen un canal de distribución propio. Esto reduce dependencia de ads y mejora CAC si la audiencia está calificada.

**[Certeza]** Alta.

---

### 6.4 Catálogo de cursos

**[Dato]** 12 cursos listados.

**[Inferencia]** Pueden justificar una membresía continua si los cursos están actualizados, son accionables y tienen implementación.

**[Certeza]** Media-baja, porque no sabemos si están terminados.

---

## 7. Señales de riesgo

### 7.1 “2.400 miembros” puede ser un vanity metric

**[Dato]** La portada muestra 2.400 miembros.

**[Inferencia]** Ese número puede incluir:

- miembros free,
- trials,
- miembros históricos,
- cancelados,
- cuentas inactivas,
- miembros con descuentos,
- miembros de planes anuales más baratos.

**[Certeza]** Baja, pero el riesgo es alto.

---

### 7.2 No se ve plan anual

**[Dato]** Solo se ve $39/mes.

**[Inferencia]** Si no tienen plan anual visible, pueden estar perdiendo:

- caja upfront,
- mayor retención,
- menos churn mensual,
- mejor LTV,
- oportunidades de upsell.

**[Certeza]** Media.

---

### 7.3 12 cursos sin evidencia de finalización

**[Dato]** 12 cursos listados, pero no se ve cuántos terminados.

**[Inferencia]** Puede haber “course debt”: el usuario paga para entrar, ve muchos cursos, pero si están incompletos, desactualizados o sin implementación, la percepción de valor cae.

**[Certeza]** Baja.

---

### 7.4 Dependencia del fundador

**[Dato]** Fundador con 60k seguidores.

**[Inferencia]** La adquisición probablemente depende de una sola persona. Si cambia algoritmo, si deja de publicar, si hay saturación de audiencia o si la plataforma social cambia, el crecimiento puede frenarse.

**[Certeza]** Alta.

---

### 7.5 Actividad pública no garantiza comunidad sana

**[Dato]** 3 posts/semana en feed público.

**[Inferencia]** Una comunidad puede tener pocos posts del fundador y mucha conversación entre miembros, o puede tener 3 posts/semana y casi ningún engagement.

**[Certeza]** Baja.

---

## 8. Análisis de retención probable

No podemos saber churn exacto, pero podemos estimar presión operativa.

Si tuvieran 2.400 miembros pagantes a $39/mes:

| Churn mensual | Miembros que necesitan reponer/mes | MRR en riesgo/mes |
|---:|---:|---:|
| 2% | 48 | $1.872 |
| 5% | 120 | $4.680 |
| 7% | 168 | $6.552 |
| 10% | 240 | $9.360 |
| 15% | 360 | $14.040 |

### Interpretación

- Churn de **2%-4%** sería excelente para una comunidad de pago.
- Churn de **5%-7%** es aceptable en membresías de contenido, pero exige adquisición constante.
- Churn de **10%+** empieza a ser preocupante si no hay resultados claros, comunidad activa o implementación.
- Churn de **15%+** puede indicar que el valor percibido no justifica el precio.

**[Certeza]** Baja, porque no tenemos churn real.

---

## 9. Análisis de adquisición probable

El fundador tiene 60.000 seguidores. Supongamos que no todos son leads calificados.

| Conversión mensual de seguidores a miembros | Nuevos miembros/mes |
|---:|---:|
| 0,1% | 60 |
| 0,2% | 120 |
| 0,3% | 180 |
| 0,5% | 300 |

Para mantener 2.400 miembros con churn de 5%, necesitarían aproximadamente **120 nuevos miembros/mes**.

Eso equivale a una conversión mensual de:

**120 / 60.000 = 0,2% de seguidores.**

Es una conversión plausible si:

- la audiencia está calificada,
- hay lista de email,
- hay contenido educativo,
- hay testimonios,
- hay free community o lead magnet,
- el fundador tiene engagement real.

Pero si la audiencia es generalista, el engagement bajo o la oferta no está bien segmentada, puede ser difícil sostener.

**[Certeza]** Media-baja.

---

## 10. Análisis de contenido y producto

### 10.1 3 posts/semana

**[Dato]** 3 posts/semana en feed público.

**[Inferencia]** Cadencia moderada. No es una señal de abandono, pero tampoco indica alta actividad comunitaria.

Para una comunidad de 2.400 miembros, lo importante no es solo el contenido del fundador, sino:

- comentarios,
- preguntas,
- wins de miembros,
- casos de uso,
- templates compartidos,
- discusiones entre miembros,
- lives,
- onboarding,
- member spotlights.

**[Certeza]** Media.

---

### 10.2 12 cursos

**[Dato]** 12 cursos listados.

**[Inferencia]** Pueden ser una ventaja si:

- están terminados,
- son actualizados,
- tienen ejercicios,
- tienen plantillas,
- tienen implementaciones,
- tienen casos reales,
- tienen rutas claras por nivel,
- tienen soporte o comunidad asociada.

Pueden ser una debilidad si:

- hay muchos cursos incompletos,
- están desactualizados,
- son contenido genérico,
- no tienen outcomes,
- no tienen aplicación práctica,
- generan overwhelm en el miembro.

**[Certeza]** Baja.

---

## 11. Diagnóstico competitivo

### Lo que probablemente hacen bien

1. **Tienen un nicho claro:** automatización.
2. **Tienen precio recurrente:** $39/mes.
3. **Tienen audiencia propia:** fundador con 60k seguidores.
4. **Tienen catálogo de contenido:** 12 cursos.
5. **Tienen plataforma de membresía:** infraestructura para recurrencia.

### Lo que probablemente no están demostrando

1. **No se ve plan anual.**
2. **No se sabe si los 2.400 miembros son realmente pagantes.**
3. **No se sabe si los cursos están terminados.**
4. **No se ve métrica de engagement interno.**
5. **No se ve prueba de resultados o casos de éxito.**
6. **No se sabe si tienen churn alto o bajo.**
7. **No se sabe si la comunidad es activa o solo un repositorio de cursos.**

### Conclusión

Es un negocio con **buena base comercial**, pero con **riesgo de producto y retención**. Si la comunidad está activa y los cursos funcionan, puede ser un negocio sólido. Si no, puede estar sobreviviendo con la audiencia del fundador y contenido no necesariamente terminado.

---

# 12. Cómo les compites

No te recomiendo competir solo con “más cursos” o “precio más bajo”. La mejor estrategia es atacar las brechas visibles:

1. **Falta de plan anual.**
2. **Posible deuda de contenido.**
3. **Dependencia del fundador.**
4. **Falta de resultados demostrables.**
5. **Comunidad posiblemente poco activa.**
6. **Oferta genérica si no se segmenta.**

---

## 13. Estrategia de posicionamiento

### Posicionamiento recomendado

**“Menos cursos, más implementación.”**

Si tu competidor vende 12 cursos, tú puedes vender:

- automatizaciones terminadas,
- plantillas,
- SOPs,
- workflows listos,
- soporte,
- accountability,
- resultados medibles.

### Frase de posicionamiento

> “No te damos 12 cursos para que los veas. Te ayudamos a automatizar 5 procesos en 30 días.”

### Diferenciación

| Competidor probable | Tú |
|---|---|
| Comunidad + cursos | Comunidad + implementación |
| 12 cursos listados | 5 resultados claros |
| $39/mes | $39/mes o $390/año |
| Contenido teórico | Templates, checklists, casos |
| Fundador como único motor | Sistema + comunidad + coaches |
| Valor difuso | ROI medible |

---

## 14. Oferta competitiva

### Estructura sugerida

Puedes crear una membresía con tres niveles:

### Nivel 1: Comunidad básica

**$39/mes o $390/año**

Incluye:

- acceso a comunidad,
- 1 live semanal,
- biblioteca de templates,
- 1 challenge mensual,
- feed activo,
- recursos descargables.

---

### Nivel 2: Implementación guiada

**$79/mes o $790/año**

Incluye:

- todo lo anterior,
- cohortes mensuales,
- revisión de workflows,
- plantillas premium,
- office hours,
- casos de éxito,
- rutas por vertical.

---

### Nivel 3: Done-with-you premium

**$149/mes o $1.490/año**

Incluye:

- todo lo anterior,
- sesiones 1 a 1,
- auditoría de automatizaciones,
- implementación de 1-2 workflows,
- SOPs personalizados,
- soporte prioritario.

---

## 15. Pricing competitivo

Si ellos cobran $39/mes, no compitas con $19/mes. Eso destruye margen y atrae churn.

### Opción A: igualar precio pero subir valor

**$39/mes**

Pero con:

- plan anual visible,
- resultados más claros,
- comunidad más activa,
- templates más útiles,
- implementación.

### Opción B: crear plan anual agresivo

**$390/año**

Eso equivale a $32,50/mes.

Ventajas:

- mejora caja,
- reduce churn,
- da percepción de descuento,
- facilita renovación anual.

### Opción C: premium por implementación

**$79/mes**

Justificación:

- no solo contenido,
- sino acompañamiento,
- templates,
- revisión de workflows,
- accountability.

### Mi recomendación

Lanza con:

- **$39/mes** como entrada.
- **$390/año** como oferta principal visible.
- **$79/mes** o **$790/año** para implementación guiada.

---

## 16. Diferenciación por nicho

Si tu competidor dice “automatización”, tú puedes segmentar más.

### Nichos posibles

1. Automatización para agencias de marketing.
2. Automatización para ecommerce.
3. Automatización para SaaS.
4. Automatización para founders solopreneurs.
5. Automatización para equipos de operaciones.
6. Automatización para creadores.
7. Automatización con IA para PYMEs.
8. Automatización para servicios profesionales.
9. Automatización para lead generation.
10. Automatización para soporte al cliente.

### Ejemplo

No compitas con:

> “Comunidad de automatización.”

Compite con:

> “Comunidad de automatización para agencias que quieren ahorrar 20 horas/semana.”

O:

> “Automatización para ecommerce: workflows listos para postventa, inventario, soporte y marketing.”

El nicho reduce la sensación de contenido genérico y aumenta la percepción de valor.

---

## 17. Cómo atacar sus posibles debilidades

### Debilidad 1: No se ve plan anual

**Tu movimiento:**

- mostrar plan anual claro,
- descuento visible,
- garantía,
- onboarding anual,
- beneficios de renovación.

Ejemplo:

> “Mensual: $39. Anual: $390, ahorras 17%.”

---

### Debilidad 2: 12 cursos sin finalización visible

**Tu movimiento:**

- no lanzar 12 cursos,
- lanzar 1 o 2 rutas terminadas,
- mostrar progreso,
- incluir ejercicios,
- incluir plantillas,
- incluir casos reales.

Ejemplo:

> “Ruta de 30 días: automatiza 3 procesos de tu negocio.”

---

### Debilidad 3: Posible comunidad poco activa

**Tu movimiento:**

- onboarding obligatorio,
- preguntas de introducción,
- wins de la semana,
- challenges,
- lives,
- member spotlights,
- recompensas por participación.

---

### Debilidad 4: Dependencia del fundador

**Tu movimiento:**

- crear sistema de contenido,
- coaches,
- curadores,
- community managers,
- rutas claras,
- biblioteca de casos.

---

### Debilidad 5: Falta de resultados medibles

**Tu movimiento:**

- publicar casos con métricas:
  - horas ahorradas,
  - leads gestionados,
  - errores reducidos,
  - tiempo de respuesta,
  - ingresos recuperados,
  - procesos automatizados.

Ejemplo:

> “Cómo una agencia redujo 12 horas/semana con 4 automatizaciones.”

---

## 18. Contenido competitivo

### No copies “3 posts/semana”

Copia la cadencia, pero mejora la intención.

### Contenido recomendado

| Tipo de contenido | Frecuencia | Objetivo |
|---|---:|---|
| Caso real | 1/semana | Prueba de valor |
| Template descargable | 1/semana | Lead magnet |
| Mini-tutorial | 2/semana | Autoridad |
| Live Q&A | 1/semana | Comunidad |
| Member spotlight | 1/semana | Retención |
| Antes/después de proceso | 2/semana | Diferenciación |
| Errores comunes en automatización | 1/semana | SEO/educación |

---

## 19. Producto mínimo competitivo

No necesitas 12 cursos. Necesitas una promesa clara.

### MVP sugerido

**“Automatización en 30 días”**

Incluye:

1. 1 diagnóstico inicial.
2. 3 workflows recomendados.
3. 1 plantilla de SOP.
4. 1 checklist de implementación.
5. 1 live semanal.
6. 1 comunidad de soporte.
7. 1 biblioteca de integraciones.
8. 1 tracker de horas ahorradas.

### Promesa

> “En 30 días automatizas al menos 3 procesos que hoy te quitan tiempo.”

---

## 20. Estrategia de adquisición

### Canales recomendados

1. **YouTube/Shorts**
   - tutoriales cortos de automatización.
   - casos reales.
   - errores comunes.

2. **LinkedIn/X**
   - frameworks visuales.
   - antes/después.
   - plantillas.

3. **SEO**
   - “cómo automatizar [proceso]”
   - “plantillas de automatización para [vertical]”
   - “workflow de [herramienta]”
   - “automatizar [proceso] con [herramienta]”

4. **Lead magnet**
   - biblioteca de 10 workflows.
   - checklist de automatización.
   - template de SOP.
   - calculadora de horas ahorradas.

5. **Partnerships**
   - herramientas de automatización,
   - agencias,
   - comunidades de founders,
   - newsletters de ops/IA.

6. **Free community**
   - comunidad gratuita como embudo.
   - después upsell a paid.

---

## 21. Estrategia de retención

La retención será tu ventaja si su negocio depende de contenido no validado.

### Onboarding

Primeros 7 días:

1. Bienvenida.
2. Pregunta de introducción.
3. Objetivo del miembro.
4. 1 template inicial.
5. 1 live de bienvenida.
6. 1 reto de 7 días.
7. 1 caso de éxito.

### Retención semanal

- live semanal,
- win de la semana,
- template semanal,
- Q&A,
- member spotlight,
- challenge mensual.

### Retención mensual

- actualización de workflows,
- revisión de herramientas,
- casos nuevos,
- rutas de aprendizaje,
- recompensas por participación.

### Retención por resultado

Mide:

- procesos automatizados,
- horas ahorradas,
- leads gestionados,
- errores reducidos,
- ingresos recuperados,
- tiempo de respuesta.

Si el miembro ve resultados, renueva.

---

## 22. Plan de ataque: 30/60/90 días

### Días 1-30: validar y posicionarte

Objetivo: no construir 12 cursos, sino validar una promesa.

Acciones:

1. Definir nicho exacto.
2. Entrevistar a 10 personas.
3. Identificar 3 procesos más dolorosos.
4. Crear 1 lead magnet.
5. Montar landing simple.
6. Ofrecer prueba o pre-sale.
7. Conseguir 10-20 primeros miembros.

Métricas:

- leads,
- conversión,
- precio aceptado,
- objeciones,
- primeras implementaciones.

---

### Días 31-60: lanzar una oferta clara

Objetivo: vender una membresía con resultados visibles.

Acciones:

1. Abrir comunidad.
2. Lanzar plan anual.
3. Crear 1 ruta de 30 días.
4. Publicar 3 casos.
5. Hacer 1 live/semana.
6. Crear 10 templates.
7. Medir engagement.

Métricas:

- MRR,
- churn,
- DAU/WAU,
- comentarios,
- completions,
- testimonios.

---

### Días 61-90: diferenciarte por implementación

Objetivo: pasar de “contenido” a “resultado”.

Acciones:

1. Publicar casos con métricas.
2. Crear biblioteca de workflows.
3. Lanzar challenge de implementación.
4. Abrir nivel premium.
5. Crear programa de referidos.
6. Documentar SOPs de la comunidad.
7. Reducir dependencia del fundador.

Métricas:

- LTV,
- CAC,
- churn,
- NPS,
- resultados reportados,
- renovaciones anuales.

---

## 23. Qué no hacer contra este competidor

### Error 1: lanzar 12 cursos sin terminar

Si ellos tienen 12 cursos listados, tú no necesitas imitar eso. La percepción de “demasiado contenido” puede generar overwhelm.

### Error 2: competir solo por precio

Bajar a $19/mes puede parecer atractivo, pero suele aumentar churn y atraer usuarios menos comprometidos.

### Error 3: copiar su posicionamiento genérico

Si ellos dicen “automatización”, tú necesitas ser más específico: vertical, herramienta, resultado, proceso.

### Error 4: depender solo de tu audiencia

Si compites con un fundador con 60k seguidores, necesitas construir sistemas: SEO, email, partnerships, casos, comunidad, contenido evergreen.

### Error 5: vender comunidad sin onboarding

Una comunidad sin onboarding se siente vacía. El miembro nuevo debe entender qué hacer en sus primeros 7 días.

---

## 24. Métricas que debes vigilar para medir si realmente están sanos

| Métrica | Qué mirar | Señal positiva | Señal negativa |
|---|---|---|---|
| Miembros públicos | Crecimiento o estancamiento | Aumenta con contenido visible | Número fijo sin actividad |
| Comentarios | Actividad en posts | Miembros comentan y aportan | Solo likes o respuestas del fundador |
| Testimonios | Prueba social | Casos con resultados | Solo felicitaciones genéricas |
| Posts públicos | Cadencia | 3/semana sostenido | Irregular |
| Cursos | Estado visible | Terminados y actualizados | Incompletos o desactualizados |
| Fundador | Frecuencia | Publica y responde | Deja de publicar |
| Precio | Planes | Anual visible, tiers claros | Solo mensual |
| Comunidad | Interacción | Conversaciones entre miembros | Feed unidireccional |

---

## 25. Veredicto final

### ¿Cuánto facturan?

No se puede afirmar con certeza.

**Techo visible:**  
**$1.123.200 ARR** si los 2.400 miembros son pagantes y todos pagan $39/mes.

**Rango probable:**  
Entre **$500k y $950k ARR**, si el número de miembros incluye free, trials, inactivos o descuentos.

**Certeza:** Baja sobre la cifra exacta; media sobre el rango.

---

### ¿Qué tan sano es el negocio?

Es un negocio **potencialmente sano**, pero con riesgos.

**Fortalezas:**

- nicho claro,
- precio recurrente,
- audiencia del fundador,
- plataforma de membresía,
- catálogo de contenido.

**Debilidades visibles:**

- no se ve plan anual,
- no se sabe si los cursos están terminados,
- no se sabe si los 2.400 miembros son pagantes,
- no se ve churn,
- no se ve engagement interno,
- alta dependencia del fundador.

**Certeza:** Media-baja.

---

### ¿Cómo les compites?

Compites con:

1. **Más claridad de oferta.**
2. **Más implementación.**
3. **Más resultados medibles.**
4. **Mejor onboarding.**
5. **Plan anual visible.**
6. **Nicho más específico.**
7. **Menos cursos y más workflows terminados.**
8. **Comunidad más activa.**
9. **Casos con métricas.**
10. **Oferta premium de soporte.**

Tu ángulo ideal:

> “No vendas 12 cursos. Vende 3 procesos automatizados, plantillas, acompañamiento y resultados.”