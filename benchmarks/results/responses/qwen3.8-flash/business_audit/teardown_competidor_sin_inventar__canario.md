# Qwen 3.8 Flash — business_audit/teardown_competidor_sin_inventar

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 4.3 | quality: 4.0
- latency_total: 161.204s | tokens_per_second: 91.3
- input_tokens: 231 | output_tokens: 14714

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

# Teardown competitivo — basado solo en señal pública

**Importante:** esto es un análisis con *muy poca evidencia*, así que separo claramente:

- **[Hecho]**: lo que sí se puede afirmar desde lo público.
- **[Inferencia]**: lo que probablemente sea, pero no está confirmado.
- **[Desconocido]**: lo que no puedo saber.
- **Certeza**: Alta / Media / Baja.

Asumo que el símbolo `$` es USD. Si no, cambia la escala.

---

## 1. Resumen rápido

Lo que parece ser:

- Una **comunidad de pago** sobre automatización.
- Un modelo de **membresía recurrente**.
- Un negocio **founder-led**, con tracción aparente.
- Probablemente **rentable o con buen margen**, pero con salud real incierta.
- Un competidor vulnerable si no tiene retención, engagement privado y una propuesta clara de resultado.

Mi lectura:

> **No veo una máquina imbatible. Veo un negocio de membresía con escala aparente, probablemente mid-six figures ARR, pero muy dependiente del fundador y con señales insuficientes sobre churn, actividad real y valor entregado.**

---

## 2. Lo que sé, lo que infiero y lo que no sé

| Señal pública | Hecho | Inferencia probable | Certeza | Implicación competitiva |
|---|---|---|---|---|
| Comunidad de pago sobre automatización en plataforma tipo membresía | **[Hecho]** El modelo es recurring revenue | **[Inferencia]** Probablemente el negocio vive de suscripciones mensuales, no de ventas puntuales | Alta | Debes competir con retención y valor continuo, no solo con tráfico |
| Muestra “2.400 miembros” | **[Hecho]** Hay un número visible de miembros | **[Inferencia]** Puede ser miembros actuales, históricos, free + paid, o miembros que alguna vez pagaron | Baja | Ese número es social proof, pero no prueba facturación ni salud |
| Precio visible: $39/mes | **[Hecho]** El precio público es $39/mes | **[Inferencia]** Si no se ve plan anual, puede que prioricen mensual o que la página de precios esté incompleta | Media | Puedes atacar con anual, premium o implementación |
| 3 posts por semana en feed público | **[Hecho]** Hay contenido público consistente | **[Inferencia]** Puede ser contenido de captación, no necesariamente actividad real de comunidad privada | Baja | Debes verificar engagement privado antes de asumir que es sano |
| Fundador con 60.000 seguidores en una red social | **[Hecho]** Existe audiencia pública relevante | **[Inferencia]** El crecimiento probablemente depende mucho del fundador y su distribución | Alta | Su moat es audiencia, pero también su riesgo |
| 12 cursos listados | **[Hecho]** Hay un catálogo visible | **[Inferencia]** Puede ser un activo grande, o contenido incompleto/desactualizado | Baja | Puedes atacar con cursos terminados, actualizados y con implementación |

---

## 3. Estimación de facturación

### 3.1 Cálculo bruto si todo fuera literal

Si:

- 2.400 miembros = suscriptores activos de pago
- Todos pagan $39/mes
- No hay descuentos, gratuitos, bajas ni planes anuales

Entonces:

```text
MRR = 2.400 × $39 = $93.600
ARR = $93.600 × 12 = $1.123.200
```

Eso es:

> **~$1.12M ARR si los 2.400 miembros son todos pagantes activos a precio completo.**

Pero eso es una hipótesis fuerte y probablemente optimista.

---

### 3.2 Por qué no puedo usar ese número como “facturación real”

No sé:

- Si “2.400 miembros” incluye:
  - miembros actuales
  - miembros históricos
  - trials
  - gratuitos
  - bajas
  - miembros con descuento
- Si hay plan anual oculto.
- Si el precio efectivo promedio es menor.
- Si hay reembolsos.
- Si la plataforma cobra fees.
- Si los impuestos están incluidos.
- Si hay afiliados o descuentos.

Por eso, el número visible es **indicador de escala aparente**, no prueba de facturación.

---

### 3.3 Escenarios de facturación

| Escenario | Supuestos | MRR estimado | ARR estimado | Probabilidad subjetiva |
|---|---:|---:|---:|---:|
| Optimista / literal | 2.400 miembros activos pagando $39 | $93.600 | $1.123.200 | 15% |
| Base | ~1.700–1.900 miembros activos pagando ARPU efectivo $34–$36 | $58k–$68k | $700k–$820k | 45% |
| Conservador | ~1.100–1.300 miembros activos pagando ARPU efectivo $30–$33 | $33k–$43k | $400k–$520k | 25% |
| Pesimista | ~500–800 miembros activos pagando ARPU efectivo $28–$32 | $14k–$26k | $170k–$310k | 15% |

**Mi mejor estimación responsable:**

> **ARR probable entre $500k y $900k**, con posibilidad de llegar a ~$1.1M si los 2.400 miembros son realmente activos y pagantes.

Certeza: **Media-Baja**.

---

## 4. ¿Cuánto margen probable tienen?

No tengo datos de costos, pero por modelo de negocio puedo inferir.

### 4.1 Señales de margen alto

Un negocio de membresía suele tener:

- costos variables bajos
- plataforma tipo Circle, Mighty Networks, Kajabi, etc.
- fees de procesamiento ~2.5%–3.5%
- contenido que se puede reutilizar
- comunidad que puede escalar con poca plantilla
- fundador como principal activo de adquisición

**Certeza: Media.**

### 4.2 Costos probables

| Concepto | Estimación posible |
|---|---:|
| Plataforma de membresía | $50–$500/mes |
| Fees de pagos | ~3%–4% de MRR |
| Email marketing | $50–$300/mes |
| Herramientas de automatización | $100–$500/mes |
| Editor / VA / community manager | $500–$3.000/mes |
| Publicidad / afiliados | $0–$50.000+/mes |
| Sueldos | $0–$20.000+/mes |

Si son solo fundador + 1–2 personas, el margen operativo puede ser alto.

### 4.3 Estimación de caja probable

Con ARR base de $700k:

```text
Ingreso mensual promedio: ~$58k
Fees pagos: ~$1.7k
Plataforma + herramientas: ~$1k–$2k
Equipo pequeño: ~$3k–$10k
Marketing: variable
```

En un escenario founder-led con bajo equipo:

> **Margen operativo probable: 50%–80%**, si no invierten fuerte en ads.

Certeza: **Media-Baja**.

---

## 5. ¿Qué tan sano es el negocio?

Aquí es donde hay más incertidumbre.

### 5.1 Señales verdes

| Señal | Por qué es positiva | Certeza |
|---|---|---|
| Modelo de membresía recurrente | Mejor que vender cursos sueltos | Alta |
| Precio visible | Reduce fricción de compra | Alta |
| 2.400 miembros mostrados | Social proof fuerte | Media |
| 3 posts/semana en público | Consistencia de contenido | Media |
| Fundador con 60k seguidores | Distribución orgánica | Alta |
| 12 cursos listados | Profundidad aparente de oferta | Media |

---

### 5.2 Señales de riesgo

| Riesgo | Por qué importa | Certeza |
|---|---|---|
| “2.400 miembros” puede no ser miembros activos | Infla la percepción de tracción | Alta |
| No se ve plan anual | Puede perder caja o tener pricing incompleto | Media |
| No se sabe churn | Una membresía puede morir en silencio | Alta |
| No se sabe actividad privada | Comunidad puede estar muerta aunque el feed público sea bonito | Alta |
| Dependencia del fundador | Si cambia algoritmo o se quema, el negocio sufre | Alta |
| 12 cursos sin saber completitud | Puede ser catálogo, no producto terminado | Media |
| Automatización es categoría amplia | Competidores pueden nichar más fuerte | Alta |

---

### 5.3 La variable que decide todo: churn

Para una comunidad de pago, el churn mensual es crítico.

| Churn mensual | Vida media aproximada | Miembros nuevos necesarios para mantener 2.400 |
|---:|---:|---:|
| 2% | ~50 meses | ~48/mes |
| 3% | ~33 meses | ~72/mes |
| 5% | ~20 meses | ~120/mes |
| 8% | ~12.5 meses | ~192/mes |
| 12% | ~8.3 meses | ~288/mes |

Con 60.000 seguidores del fundador:

- Si churn es 5%, necesitan ~120 nuevos miembros/mes.
- Eso equivale a ~0.2% de la audiencia cada mes.
- Es plausible con contenido constante y confianza.
- Si churn es 8%–12%, el negocio se vuelve más frágil.

**Mi lectura:**

> Si el churn está por debajo de 5% mensual, el negocio es razonablemente sano.  
> Si está por encima de 8%, puede estar comprando crecimiento y perdiendo dinero a largo plazo.

Certeza: **Baja**, porque no tengo datos de retención.

---

### 5.4 Scorecard de salud competitivo

| Dimensión | Nota | Comentario |
|---|---:|---|
| Modelo de negocio | 9/10 | Membresía recurrente es excelente |
| Tracción aparente | 8/10 | 2.400 miembros y $39/mes se ven fuertes, pero no confirmados |
| Distribución | 7/10 | 60k seguidores es activo, pero depende de fundador |
| Contenido | 6/10 | 12 cursos es mucho, pero no sabemos calidad/actualización |
| Comunidad real | 4/10 | No veo actividad privada ni testimonios de engagement |
| Retención | 3/10 | Churn desconocido; es la mayor incógnita |
| Defensibilidad | 4/10 | Cursos y comunidad pueden replicarse si no hay nicho fuerte |
| Riesgo fundador | 7/10 | Alto: el negocio parece depender mucho de una persona |
| Oportunidad de competir | 7/10 | Hay hueco en nicho, implementación y acompañamiento |

**Veredicto de salud:**

> **Negocio probable: viable y con caja. Salud real: incierta. Riesgo principal: churn + dependencia del fundador.**

Certeza global: **Media**.

---

## 6. Cómo te posicionas contra ellos

No intentes competir por “más cursos”. Eso suele ser una guerra de contenido y no siempre gana quien tiene más.

Compites mejor por:

1. **Nicho**
2. **Resultado**
3. **Velocidad de implementación**
4. **Acompañamiento**
5. **Prueba social específica**
6. **Calidad de comunidad**
7. **Precio/valor más claro**

---

## 7. Posicionamientos ganadores

### 7.1 Ataque por nicho

Ellos parecen generalistas: “automatización”.

Tú puedes ser específico:

- Automatización para agencias.
- Automatización para e-commerce.
- Automatización para SaaS.
- Automatización para coaches.
- Automatización para operaciones.
- Automatización para equipos de soporte.
- Automatización para pequeños negocios locales.
- Automatización para creadores.
- Automatización con n8n para freelancers.
- Automatización con Make/Zapier para marketing.

**Posicionamiento:**

> “No es una comunidad general de automatización. Es una comunidad para [nicho] que quiere automatizar [proceso] en [tiempo].”

Ejemplo:

> “Automatización para agencias: reduce 10 horas/semana en reporting, onboarding y seguimiento de clientes.”

Certeza de oportunidad: **Alta**.

---

### 7.2 Ataque por resultado

Vender “automatización” es abstracto.

Vender resultados es más fuerte:

- Ahorrar 10 horas/semana.
- Reducir soporte en 30%.
- Automatizar facturación.
- Eliminar tareas manuales de reporting.
- Hacer onboarding de clientes en 1 día.
- Responder leads en menos de 1 minuto.
- Reducir errores humanos.
- Escalar operaciones sin contratar.

**Posicionamiento:**

> “No vengo a enseñarte automatización. Vengo a ayudarte a automatizar tu operación en 30 días.”

Certeza de oportunidad: **Alta**.

---

### 7.3 Ataque por implementación

Muchas comunidades enseñan conceptos.

Tú puedes vender ejecución:

- Plantillas listas.
- Workflows descargables.
- Sesiones de implementación.
- Office hours.
- Revisión de automatizaciones.
- Retos semanales.
- Accountability groups.
- Casos reales.
- Integraciones paso a paso.

**Posicionamiento:**

> “Menos biblioteca de cursos. Más automatizaciones funcionando.”

Certeza de oportunidad: **Alta**.

---

### 7.4 Ataque por velocidad

Si ellos tienen 12 cursos, puede haber fricción: “por dónde empiezo”.

Tú puedes simplificar:

- Onboarding en 5 minutos.
- Ruta recomendada por perfil.
- Primer resultado en 7 días.
- Plantilla inicial lista.
- Checklist de implementación.
- Soporte rápido.

**Posicionamiento:**

> “Tu primera automatización funcionando en 7 días o te ayudamos gratis.”

Certeza de oportunidad: **Media-Alta**.

---

### 7.5 Ataque por frescura de contenido

12 cursos listados pueden ser un activo o una deuda.

Puedes atacar si:

- Los cursos están incompletos.
- No se actualizan.
- No reflejan cambios de herramientas.
- No tienen ejemplos recientes.

Tu propuesta:

- Contenido actualizado mensualmente.
- Changelog público.
- Nuevas automatizaciones cada mes.
- Casos con herramientas actuales.
- Integraciones con IA.

**Posicionamiento:**

> “Una comunidad que se actualiza cada mes, no un repositorio de cursos congelados.”

Certeza: **Media**, porque no sé si están desactualizados.

---

### 7.6 Ataque por comunidad real

Si su feed público tiene 3 posts/semana, no sé si la comunidad privada es activa.

Tú puedes construir comunidad con rituales:

- Office hours semanales.
- AMA mensual.
- Reto de 14 días.
- accountability por roles.
- presentación de casos.
- revisión de workflows.
- canales por herramienta.
- eventos en vivo.
- normas claras de participación.

**Posicionamiento:**

> “No solo contenido. Una comunidad que te ayuda a implementar.”

Certeza de oportunidad: **Alta**.

---

## 8. Estrategia de pricing

Ellos tienen $39/mes visible.

### Opción A: Igualar precio

Puede funcionar si:

- Tienes mejor nicho.
- Tienes mejor onboarding.
- Tienes más prueba social.
- Tienes distribución propia.

Pero competir solo por precio es débil.

**Recomendación:** no lo hagas salvo que tengas una ventaja clara de distribución.

---

### Opción B: Subir precio con más valor

Puedes cobrar:

- $59–$79/mes: comunidad + plantillas + office hours.
- $99–$149/mes: comunidad + implementación guiada + grupos pequeños.
- $299–$499/trimestre: programa corto + comunidad.
- $997–$1.997: cohort o bootcamp de automatización.
- $2.500+: done-for-you o consultoría.

**Mi recomendación:**

> Ve premium si puedes demostrar implementación.  
> $39/mes es fácil de comparar. $99/mes con resultado claro es más defendible.

Certeza: **Media-Alta**.

---

### Opción C: Bajar precio y escalar

$19–$29/mes con:

- biblioteca de plantillas
- acceso self-service
- sin soporte humano
- comunidad pasiva

Puede funcionar si tienes tráfico masivo.

Pero si no tienes distribución, es difícil.

**Recomendación:** evitar a menos que tengas una ventaja de acquisition muy fuerte.

---

## 9. Oferta recomendada para competir

Una oferta simple y defendible:

### Núcleo

**Nombre posible:**

- “Automatización Aplicada”
- “Ops Automática”
- “Automatiza Tu Negocio”
- “Comunidad de Automatización para [nicho]”

### Precio sugerido

- $79/mes
- o $199/trimestre
- o $699/año con bonus

### Incluye

1. Comunidad privada.
2. Plantillas de automatización.
3. Office hours semanales.
4. Reto de implementación mensual.
5. Casos reales.
6. Acceso a biblioteca actualizada.
7. Onboarding por perfil.
8. Soporte por preguntas.

### Promesa

> “Implementa tu primera automatización útil en 14 días.”

### Garantía

- 14 días.
- O “si no automatizas un proceso real en 30 días, te ayudamos gratis”.

---

## 10. Cómo explotar sus posibles debilidades

### Debilidad 1: Número de miembros poco transparente

Ataque:

- Muestra miembros activos reales.
- Publica testimonios recientes.
- Muestra actividad semanal.
- Usa “miembros activos esta semana” en lugar de “2.400 miembros totales”.

---

### Debilidad 2: No se ve plan anual

Ataque:

- Crea plan anual atractivo.
- Ofrece 2 meses gratis.
- Incluye bonus de onboarding.
- Usa anual para mejorar caja y retención.

Ejemplo:

```text
Mensual: $79
Anual: $690 (~$57.50/mes)
Bonus: biblioteca de plantillas + sesión de implementación
```

---

### Debilidad 3: 12 cursos, pero completitud desconocida

Ataque:

- Ofrece rutas cortas.
- “Empieza aquí si eres agencia”.
- “Empieza aquí si eres e-commerce”.
- “Empieza aquí si eres SaaS”.
- Cursos de 10–15 minutos.
- Checklist final.
- Plantilla descargable.

---

### Debilidad 4: Fundador como centro del negocio

Ataque:

- Construye equipo visible.
- Mentores por nicho.
- Community managers.
- Casos de otros expertos.
- Marca propia, no solo persona.

---

### Debilidad 5: Automatización generalista

Ataque:

- Nicho específico.
- Stack específico.
- Resultado específico.
- Caso específico.
- Comparación honesta: “si quieres general, ve con X; si quieres automatizar [nicho], ve con Y”.

---

## 11. Canales para competir sin tener 60k seguidores

El fundador tiene audiencia. Tú puedes no tenerla.

No necesitas igualar eso al inicio.

### Canales recomendados

| Canal | Uso |
|---|---|
| SEO | Páginas tipo “automatización para [nicho]” |
| YouTube | Tutoriales de implementación |
| LinkedIn | Casos, workflows, errores comunes |
| X/Twitter | Mini-hilos con automatizaciones |
| Lead magnet | Plantillas, calculadora, checklist |
| Comparativas | “Alternativa a [competidor]” |
| Alianzas | Agencias, herramientas, influencers micro |
| Paid ads | Solo si tienes CAC controlado |
| Email | Secuencia de onboarding y retención |

### Lead magnets potentes

- “10 automatizaciones para [nicho]”.
- “Calculadora de horas ahorradas”.
- “Plantilla de workflow para [proceso]”.
- “Checklist de automatización sin romper tu operación”.
- “Errores comunes al automatizar con Make/Zapier/n8n”.

---

## 12. Métricas que debes vigilar

No te obsesiones con “miembros totales”.

Mira:

### Adquisición

- Visitantes → leads.
- Leads → pruebas.
- Pruebas → pagos.
- CAC.
- Conversión por canal.

### Activación

- % que completa onboarding.
- % que instala su primera plantilla.
- % que automatiza algo real en 14 días.
- % que asiste a primera sesión.

### Retención

- Churn mensual.
- Net revenue retention.
- % activo semanal.
- % que renueva.
- Refund rate.

### Comunidad

- Posts por miembro activo.
- Comentarios por post.
- Asistencia a eventos.
- Top 10% de miembros.
- Sentimiento.

### Valor

- Casos publicados.
- Horas ahorradas.
- Resultados reportados.
- Testimonios con métricas.

---

## 13. Benchmarks aproximados

Estos son rangos útiles, no verdades absolutas.

| Métrica | Nivel aceptable | Nivel bueno | Nivel excelente |
|---|---:|---:|---:|
| Churn mensual | <8% | <5% | <3% |
| Activación | >30% | >50% | >65% |
| Actividad semanal | >20% | >30% | >40% |
| NRR | >80% | >90% | >100% |
| LTV/CAC | >2 | >3 | >5 |
| Payback CAC | <6 meses | <3 meses | <1 mes |
| Refund rate | <5% | <3% | <1% |

Certeza: **Media**.

---

## 14. Plan competitivo de 30 días

### Semana 1: Validar el terreno

- Comprar o auditar su comunidad si es posible.
- Revisar testimonios recientes.
- Ver actividad privada.
- Revisar si los cursos están completos.
- Verificar pricing, anual, reembolsos y soporte.
- Identificar 10 quejas o gaps visibles.

### Semana 2: Elegir tu wedge

Define una sola posición:

> “Para [nicho] que quiere [resultado] usando [herramienta] en [tiempo].”

Ejemplo:

> “Para agencias que quieren automatizar reporting y onboarding de clientes en 30 días.”

### Semana 3: Construir oferta mínima

Crea:

- Landing page.
- 3 casos o promesas claras.
- 5 plantillas.
- 1 sesión semanal.
- Onboarding simple.
- Precio de prueba o founding members.

### Semana 4: Conseguir primeros 10–20 miembros

Canales:

- 50 mensajes directos a personas del nicho.
- 3 posts con caso real.
- 1 lead magnet.
- 1 webinar corto.
- 1 oferta founding member.

Meta:

> No necesitas 2.400 miembros. Necesitas 20 personas que implementen y te den prueba social.

---

## 15. Qué datos faltan para mejorar el análisis

Para pasar de “estimación” a “casi seguro”, necesitaría:

1. **Definición de “2.400 miembros”**
   - ¿Activos? ¿Históricos? ¿Free + paid?

2. **Pricing page completa**
   - ¿Hay anual?
   - ¿Hay descuento?
   - ¿Hay taxes?
   - ¿Hay trial?

3. **Churn estimado**
   - ¿Cuántos renuevan?
   - ¿Cuántos cancelan?

4. **Actividad privada**
   - Posts/día.
   - Comentarios.
   - Eventos.
   - Asistencia.

5. **Calidad de cursos**
   - ¿Están terminados?
   - ¿Actualizados?
   - ¿Con plantillas?
   - ¿Con casos?

6. **Fuente de crecimiento**
   - ¿Orgánico?
   - ¿Ads?
   - ¿Afiliados?
   - ¿SEO?
   - ¿YouTube?

7. **Equipo**
   - ¿Solo fundador?
   - ¿Community manager?
   - ¿Soporte?

8. **Testimonios**
   - ¿Recientes?
   - ¿Con resultados medibles?
   - ¿De distintos segmentos?

9. **Refund policy**
   - ¿Generosa?
   - ¿Restringida?
   - ¿Puede indicar churn alto?

10. **Stack tecnológico**
   - ¿Zapier?
   - ¿Make?
   - ¿n82?
   - ¿IA?
   - ¿Integraciones?

---

## 16. Mi veredicto final

### ¿Cuánto facturan?

Mi estimación:

> **Probablemente entre $500k y $900k ARR.**  
> Podrían llegar a ~$1.1M ARR si los 2.400 miembros son activos y pagantes.  
> Pero también podrían estar más cerca de $300k–$500k si el número incluye históricos, gratuitos o bajas.

Certeza: **Media-Baja**.

---

### ¿Qué tan sano es el negocio?

Es un negocio con estructura sólida:

- recurring revenue
- social proof
- audiencia del fundador
- catálogo de contenido
- precio claro

Pero la salud real depende de datos que no se ven:

- churn
- actividad privada
- completitud de cursos
- renovación
- dependencia del fundador
- calidad de implementación

Mi lectura:

> **Probablemente es un negocio rentable y escalable, pero no necesariamente robusto. Su mayor riesgo no es la competencia directa; es la retención y la dependencia del fundador.**

Certeza: **Media**.

---

### ¿Cómo les compites?

No los compitas con “más contenido”.

Compite con:

1. **Nicho claro**
   - No “automatización”, sino “automatización para [nicho]”.

2. **Resultado medible**
   - No “aprende automatización”, sino “ahorra 10 horas/semana”.

3. **Implementación acompañada**
   - Office hours, plantillas, retos, revisiones.

4. **Onboarding rápido**
   - Primer resultado en 7–14 días.

5. **Comunidad viva**
   - Eventos, accountability, casos reales.

6. **Pricing más inteligente**
   - Sube a $79–$149/mes si aportas implementación.
   - Ofrece anual si ellos no lo muestran.

7. **Prueba social específica**
   - Casos por vertical, no testimonios genéricos.

---

## 17. Recomendación accionable

Si yo tuviera que atacar a este competidor, haría esto:

### Posicionamiento

> “Comunidad de automatización aplicada para [nicho], donde implementas tu primer workflow en 14 días.”

### Precio

- $79/mes
- o $199/trimestre
- o $690/año con bonus

### Oferta

Incluye:

- biblioteca de plantillas
- onboarding por perfil
- office hours semanal
- reto mensual
- casos reales
- revisión de automatizaciones
- acceso a comunidad privada activa

### Diferenciador

> “No es una biblioteca de 12 cursos. Es un sistema para automatizar tu operación.”

### Primer movimiento

1. Elige un nicho.
2. Crea una landing con promesa clara.
3. Publica 3 casos o mini-casos.
4. Ofrece 10 founding spots.
5. Mide activación y retención.
6. Si 30%–50% logran automatizar algo real en 14 días, tienes un negocio.

---

## 18. TL;DR

- **Facturación visible bruta:** ~$1.12M ARR si los 2.400 miembros son todos pagantes activos.
- **Facturación probable:** entre **$500k y $900k ARR**.
- **Certeza:** media-baja.
- **Salud:** negocio probable rentable, pero con riesgo alto por churn desconocido y dependencia del fundador.
- **Mayor debilidad:** no se sabe si los miembros están activos, si los cursos están completos y si la comunidad privada funciona.
- **Mejor forma de competir:** nicho + resultado + implementación + comunidad viva.
- **No compitas con más cursos.** Compite con: “aquí automatizas algo real en 14 días”.