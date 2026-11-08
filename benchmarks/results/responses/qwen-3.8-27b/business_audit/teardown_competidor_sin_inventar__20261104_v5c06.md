# Qwen 3.8 27B — business_audit/teardown_competidor_sin_inventar

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 5.32 | quality: 6.0
- latency_total: 276.289s | tokens_per_second: 31.7
- input_tokens: 231 | output_tokens: 8746

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



Voy a hacer el teardown **solo con lo que me diste**, sin inventar datos internos. Como analista competitivo, voy a separar siempre:

- **Dato visible**: lo que me confirmas de la página pública.
- **Inferencia**: mi interpretación razonada.
- **Supuesto**: lo que estoy asumiendo para poder calcular.
- **Certeza**: alta / media / baja.

Mi conclusión corta: **puede estar facturando desde ~110k hasta ~1.1M USD/año dependiendo de cuántos de esos 2.400 “miembros” son suscriptores activos reales**. Lo más probable, con solo señales públicas, es un escenario intermedio: **entre ~225k y ~560k USD/año**, pero con certeza baja porque la métrica “2.400 miembros” puede ser un número de vanidad o histórico.

---

## 1. Lo que sé y lo que infiero

| Señal | Lo que sé | Lo que infiero | Certeza |
|---|---|---|---|
| Comunidad de pago sobre automatización | Es un negocio de membresía/pago recurrente. | Es un modelo de MRR, no de venta puntual. | Alta |
| Muestra “2.400 miembros” en portada | Esa cifra está visible públicamente. | Puede representar: suscriptores actuales, estudiantes históricos, inscritos gratuitos, miembros inactivos o usuarios que compraron alguna vez. No necesariamente 2.400 personas pagando hoy. | Baja a media |
| Precio visible: $39/mes | Ticket mensual visible. | No sé si hay plan anual, descuento, trial, precio antiguo o oferta limitada. | Alta sobre el precio visible; baja sobre el modelo total |
| 3 posts por semana en feed público | Hay publicación pública constante. | Tienen operación mínima de contenido, pero no necesariamente producto profundo. 3 posts/semana es sostenibilidad moderada, no necesariamente alta retención. | Media |
| Fundador tiene 60.000 seguidores | El fundador tiene audiencia propia. | Probablemente una parte importante de su captación viene de su audiencia personal. Riesgo de dependencia del fundador. | Alta sobre la audiencia; media sobre conversión |
| 12 cursos listados, no se ve cuántos están terminados | Tienen un catálogo amplio de cursos. | Puede ser señal de amplitud, pero también de producto incompleto, backlog o “promesa sin entrega”. | Media |

---

## 2. Estimación de facturación

### Fórmula base

Si **todos** los 2.400 miembros fueran suscriptores activos pagando $39/mes:

\[
2.400 \times 39 = 93.600 \text{ USD/mes}
\]

\[
93.600 \times 12 = 1.123.200 \text{ USD/año}
\]

Ese es el **tope teórico máximo** si los 2.400 son miembros actuales pagando.

Pero en la realidad, “2.400 miembros” en una portada suele incluir:

- miembros activos;
- miembros inactivos;
- miembros que cancelaron;
- estudiantes que compraron un curso;
- inscritos en lista gratuita;
- miembros de versiones antiguas;
- o una combinación de todo.

Por eso hay que modelar por porcentajes.

---

## 3. Escenarios de facturación

### Supuesto

- Precio: **$39/mes**.
- Cifra pública: **2.400 miembros**.
- No sabemos cuántos están activos.
- No contamos impuestos, reembolsos, descuentos, plan anual ni costos.
- “Ingreso neto de plataforma” aproximado: **85–92% del MRR** después de procesadores, plataforma y costes técnicos menores, antes de marketing, contenido, soporte y impuestos.

| Escenario | % de miembros activos pagando | MRR estimado | Facturación anual estimada | Ingreso neto bruto aproximado/año* |
|---|---:|---:|---:|---:|
| Pesimista | 5% | $4.680 | $56.160 | $47k–$52k |
| Bajo | 10% | $9.360 | $112.320 | $95k–$103k |
| Medio-bajo | 20% | $18.720 | $224.640 | $190k–$206k |
| Medio | 25% | $23.400 | $280.800 | $238k–$258k |
| Medio-alto | 40% | $37.440 | $449.280 | $381k–$413k |
| Alto | 50% | $46.800 | $561.600 | $477k–$516k |
| Muy alto | 80% | $74.880 | $898.560 | $763k–$826k |
| Tope teórico | 100% | $93.600 | $1.123.200 | $954k–$1.033M |

\* Aproximación después de plataforma/pagos, antes de marketing, soporte, contenido e impuestos.

### Mi lectura

Con solo señales públicas, el escenario más probable para mí sería:

> **Entre 20% y 50% de esos 2.400 siendo miembros activos pagando.**

Eso implicaría:

> **Facturación anual estimada: ~225k a ~560k USD.**

Y un ingreso neto bruto aproximado de:

> **~190k a ~516k USD/año**, antes de costos de captación, contenido, soporte e impuestos.

Pero repito: **certeza baja**, porque el dato crítico —cuántos están pagando hoy— no es visible.

---

## 4. Estimación de LTV y churn

Como es una membresía, la salud real depende mucho del **churn mensual**.

### Fórmula básica

\[
LTV = \frac{\text{ARPU mensual}}{\text{churn mensual}}
\]

ARPU visible: $39/mes.

| Churn mensual | LTV bruto aproximado |
|---:|---:|
| 3% | $1.300 |
| 5% | $780 |
| 8% | $487 |
| 12% | $325 |

En comunidades de pago, un churn mensual típico puede moverse entre **3% y 15%**, dependiendo de:

- calidad del contenido;
- comunidad activa;
- soporte;
- onboarding;
- si hay eventos en vivo;
- si hay resultados tangibles;
- si el usuario ve valor cada mes.

### Lectura

Si su churn es:

- **3–5% mensual**: el negocio puede ser bastante sano.
- **5–8% mensual**: viable, pero requiere captación constante.
- **8–12% mensual**: negocio frágil; necesita vender mucho para mantenerse estable.
- **>12% mensual**: probablemente un “churn machine”, a menos que el CAC sea muy bajo.

---

## 5. Qué tan sano es el negocio

### Señales positivas

#### 1. Tiene precio recurrente

**Dato:** $39/mes visible.  
**Lectura:** No es una venta puntual; busca flujo recurrente.  
**Certeza:** alta sobre el modelo; media sobre su rentabilidad real.

#### 2. Tiene una base de miembros mostrada

**Dato:** 2.400 miembros visibles.  
**Lectura:** Al menos tiene prueba social mínima. Puede ser histórico, pero aun así ayuda a convertir.  
**Certeza:** alta sobre la existencia del número; baja sobre si son activos.

#### 3. Publica 3 posts por semana

**Dato:** feed público con 3 posts/semana.  
**Lectura:** Tienen consistencia mínima de contenido. No parece un proyecto abandonado.  
**Certeza:** alta sobre la publicación; media sobre la calidad y la retención.

#### 4. Fundador con 60.000 seguidores

**Dato:** fundador con 60k seguidores.  
**Lectura:** Probablemente tiene ventaja de distribución orgánica. Puede captar clientes con menos dependencia de pauta.  
**Certeza:** alta sobre la audiencia; media sobre conversión.

---

### Señales de riesgo

#### 1. “2.400 miembros” puede ser métrica inflada

Muchas comunidades muestran:

- miembros totales históricos;
- inscritos;
- estudiantes;
- usuarios que alguna vez entraron;
- miembros inactivos;
- o una mezcla.

Si solo 10% pagan hoy, la facturación baja de ~1.1M a ~112k/año.

**Certeza:** baja sobre el número real.

#### 2. 12 cursos, pero no se ve completitud

**Dato:** 12 cursos listados.  
**Lectura:** Puede ser catálogo amplio, pero también puede indicar:

- cursos sin terminar;
- contenido incompleto;
- promesa de actualización constante;
- o productos que no generan suficiente valor.

Si el miembro entra y ve cursos incompletos, eso genera fricción y churn.

**Certeza:** alta sobre que no se ve completitud; inferencia media sobre calidad.

#### 3. 3 posts por semana puede ser poco para justificar $39/mes

Para una membresía de pago, el miembro espera:

- contenido nuevo;
- plantillas;
- soportes;
- actualizaciones;
- dudas respondidas;
- casos;
- retos;
- eventos;
- implementación.

Tres posts públicos por semana son una señal de actividad, pero no garantizan retención.

**Certeza:** media.

#### 4. No se ve plan anual

**Dato:** no se ve plan anual ni descuentos.  
**Lectura:** Puede significar varias cosas:

- oferta simple;
- poca optimización de retención;
- falta de estrategia de cash flow;
- o simplemente que la página pública no muestra todo.

Un plan anual suele ser bueno para predecibilidad. Si no existe, el modelo depende más de renovaciones mensuales.

**Certeza:** baja.

#### 5. Posible dependencia del fundador

Si el fundador tiene 60k seguidores y la comunidad se apoya en su autoridad, hay riesgo de **key person**.

Riesgos:

- si se cansa, el negocio sufre;
- si hace pivot, la comunidad puede marcharse;
- si no escala sistema, depende de su tiempo;
- si no hay comunidad orgánica entre miembros, el valor recae en él.

**Certeza:** media.

---

## 6. Veredicto de salud

Con lo que tienes, yo clasificaría el negocio así:

> **Probablemente viable, pero frágil. No sé si es un negocio sólido o un negocio de alta rotación.**

Mi puntuación subjetiva:

### Si 2.400 son en gran parte miembros activos pagando

- Salud: **7–8/10**
- Facturación: potencialmente > $500k/año.
- Riesgo: dependencia de retención y del fundador.

### Si solo una parte está activa

- Salud: **5–6/10**
- Facturación: probablemente $150k–$400k/año.
- Riesgo: churn, producto incompleto y dependencia de captación constante.

### Si “2.400” es sobre todo histórico o gratuito

- Salud: **3–4/10**
- Facturación: quizás <$150k/año.
- Riesgo: número de vanidad, retención débil.

---

## 7. Cómo les puedes competir

No te recomiendo competir solo por precio. $39/mes no es tan alto ni tan bajo; es un precio defensivo pero fácil de atacar si tú ofreces **más claridad, más resultado y más implementación**.

Tu ventaja no debería ser “soy más barato”. Debería ser:

> “Te entrego un sistema de automatización más claro, más completo y con más resultado que un curso.”

---

## 8. Tu posición competitiva recomendada

### Opción 1: Nicho más específico

Si ellos hacen “automatización” en general, tú puedes atacar un nicho concreto:

- automatización para agencias;
- automatización para e-commerce;
- automatización para inmobiliarios;
- automatización para SaaS;
- automatización para creadores;
- automatización para clínicas;
- automatización para equipos de operaciones.

Ejemplo de posicionamiento:

> “Automatización para agencias que quieren vender flujos a sus clientes.”

Eso convierte una promesa genérica en una promesa comercial.

**Certeza:** alta, porque es una estrategia, no un dato.

---

### Opción 2: Vender resultado, no curso

Ellos listan cursos. Tú puedes vender:

- flujos listos para usar;
- plantillas;
- integraciones;
- plantillas de correo;
- dashboards;
- automatizaciones de ventas;
- automatizaciones de onboarding;
- automatizaciones de soporte;
- automatizaciones de recuperación.

Tu mensaje:

> “No te enseño teoría. Te doy sistemas de automatización que puedes instalar y usar.”

Eso ataca directamente el riesgo de “12 cursos sin ver si están terminados”.

---

### Opción 3: Comunidad + implementación

Si ellos tienen feed público con 3 posts/semana, tú puedes ofrecer:

- 1 sesión en vivo semanal;
- 1 reto mensual;
- revisión de flujos;
- soporte en comunidad;
- plantillas descargables;
- actualizaciones mensuales;
- office hours.

Eso justifica mejor el pago recurrente.

---

## 9. Estrategia de precio

No bajarías necesariamente a $19 o $29. En automatización, $39 puede ser visto como barato si no hay profundidad.

Te propongo una estructura:

### Plan de entrada

- **$29/mes por 3 meses** o trial de 7 días.
- Objetivo: reducir fricción.
- No lo hagas permanente si no quieres devaluar.

### Plan estándar

- **$49/mes**
- Incluye:
  - acceso a flujos;
  - plantillas;
  - comunidad;
  - 1 sesión mensual;
  - actualizaciones.

### Plan premium

- **$99–$149/mes**
- Incluye:
  - sesión grupal;
  - revisión de flujo;
  - acceso anticipado;
  - soporte prioritario;
  - flujos avanzados.

### Plan anual

- **$399/año** en vez de $468.
- Beneficio:
  - cash flow anticipado;
  - churn menor;
  - compromiso mayor.

Eso te da una oferta más fuerte que “$39/mes sin plan anual visible”.

---

## 10. Cómo captar clientes si tu audiencia es menor que 60k

Si el fundador tiene 60k seguidores, no pelees solo en alcance. Pule en **conversión, nicho y prueba**.

### Tácticas

#### 1. Challenge de 5 o 7 días

Ejemplo:

> “En 7 días automatiza tu seguimiento a leads.”

Entregas:

- día 1: diagnóstico;
- día 2: embudo;
- día 3: automatización de correo;
- día 4: integración;
- día 5: métricas;
- día 6: caso;
- día 7: oferta.

Esto genera demanda y prueba social.

#### 2. Contenido demostrativo

No hagas solo “5 tips de automatización”. Haz:

- antes/después;
- flujos completos;
- capturas reales;
- resultados;
- errores comunes;
- comparativas de herramientas;
- casos por industria.

#### 3. Lead magnet muy específico

Ejemplos:

- “10 automatizaciones para agencias”;
- “Flujo de recuperación de carrito para e-commerce”;
- “Sistema de seguimiento B2B con IA”;
- “Onboarding automatizado para clientes de agencia”.

#### 4. Alianzas

Busca:

- consultores de marketing;
- expertos en IA;
- creadores de contenido;
- agencias;
- expertos en e-commerce;
- coaches de ventas.

No necesitas más audiencia que ellos si conviertes mejor.

#### 5. SEO y YouTube

Automatización es un tema con búsqueda. Puedes crear contenido como:

- “cómo automatizar ventas con n8n/Make/Zapier”;
- “automatización para inmobiliarios”;
- “cómo usar IA para seguimiento de leads”;
- “mejores automatizaciones para agencias”.

YouTube puede ser tu principal canal a 6–12 meses.

---

## 11. Cómo ganar en retención

En membresías, la retención es más importante que el lanzamiento.

Tu miembro debería sentir que cada mes:

- ve contenido nuevo;
- recibe plantillas;
- participa en comunidad;
- aprende algo aplicable;
- tiene soporte;
- ve progreso.

### Checklist de retención

- Onboarding claro: qué debe hacer en la primera hora.
- Calendario mensual de contenido.
- 1 reto mensual.
- 1 sesión en vivo mensual.
- Biblioteca de plantillas.
- Updates mensuales de herramientas.
- Comunidad activa.
- Soporte visible.
- Testimonios nuevos.
- Ofertas de referidos.

---

## 12. Cómo monitorizar al competidor

Para afinar la estimación, yo haría esto:

### 1. Comprar la membresía o usar trial

Si tienen trial o acceso gratuito, entras y mides:

- cuántos cursos están completos;
- calidad del contenido;
- actividad de comunidad;
- frecuencia real de entregas;
- soporte;
- tono del fundador;
- nivel de los miembros;
- si hay eventos en vivo.

### 2. Observar cambios de precio

Comprueba cada 1–3 meses:

- precio;
- plan anual;
- trial;
- descuentos;
- bonos;
- cambios de nombre;
- cambios de promesa.

### 3. Buscar pruebas externas

Revisa:

- redes sociales;
- reseñas;
- comentarios;
- menciones;
- ex alumnos;
- casos de uso;
- quejas públicas;
- testimonios;
- cambios en el feed.

### 4. Medir su consistencia

Crea una hoja con:

- posts por semana;
- temas recurrentes;
- calidad;
- si suben plantillas;
- si hacen eventos;
- si actualizan cursos;
- si el fundador sigue activo.

### 5. Estimar churn por señales indirectas

Señales de churn alto:

- pocos comentarios;
- membresía silenciosa;
- cursos viejos;
- falta de novedades;
- fundador ausente;
- cambio de precio;
- descuentos agresivos;
- mensajes desesperados;
- poca prueba social nueva.

Señales de churn bajo:

- casos nuevos;
- comunidad activa;
- eventos constantes;
- miembros compartiendo resultados;
- contenido actualizado;
- precio estable;
- plan anual;
- testimonios recientes.

---

## 13. Plan de ataque en 60 días

### Día 1–7: investigación

- Compras o pruebas públicas.
- Mapeas cursos, comunidad, feed y precio.
- Buscas quejas y testimonios.
- Identificas nicho débil.

### Día 8–14: posicionamiento

Eliges un nicho y una promesa.

Ejemplo:

> “Automatización para agencias que quieren vender flujos a sus clientes.”

O:

> “Automatización para e-commerce que quiere recuperar ventas sin enviar más publicidad.”

### Día 15–28: oferta

- Creas lead magnet.
- Creas challenge.
- Preparas landing.
- Defines precio.
- Prepara contenido demo.

### Día 29–45: distribución

- Publicas 3–4 piezas/semana.
- Haces challenge.
- Lanzas oferta a lista.
- Contactas alianzas.
- Publicas demos.

### Día 46–60: conversión y retención

- Abres comunidad.
- Haces primera sesión en vivo.
- Recoges testimonios.
- Ajustas onboarding.
- Mides CAC, churn, activación y conversión.

---

## 14. Tus KPIs clave

No midas solo ventas. Mide:

### Adquisición

- CAC;
- coste por lead;
- conversión landing;
- coste por suscriptor.

### Activación

- % de miembros que hacen el onboarding;
- tiempo hasta primera acción;
- % que usa una plantilla o flujo.

### Retención

- churn mensual;
- churn a 30/60/90 días;
- % de sesiones activas;
- % de miembros que participan en comunidad.

### Ingresos

- MRR;
- ARR;
- LTV;
- LTV/CAC;
- payback del CAC.

### Prueba social

- testimonios;
- casos;
- capturas de resultados;
- referidos.

---

## 15. Resumen ejecutivo

### ¿Cuánto factura?

No se puede saber con certeza solo desde fuera.

- **Tope teórico:** ~$1.12M/año si los 2.400 son suscriptores activos.
- **Escenario probable medio:** ~$225k–$560k/año si entre 20% y 50% están activos.
- **Escenario conservador:** <$150k/año si solo una fracción paga.

Mi estimación más razonable con las señales actuales:

> **~$225k–$560k USD/año, con certeza baja/media.**

### ¿Qué tan sano es?

> **Probablemente viable, pero con riesgos importantes.**

Puntos fuertes:

- precio recurrente;
- base mostrada;
- contenido público consistente;
- fundador con audiencia.

Puntos débiles:

- posible métrica inflada;
- cursos sin completitud visible;
- posible falta de plan anual;
- posible dependencia del fundador;
- comunidad puede tener churn alto.

### ¿Cómo les compites?

No ataques solo precio. Ataca con:

1. **Nicho más específico.**
2. **Promesa de resultado.**
3. **Flujos listos para usar, no solo cursos.**
4. **Comunidad con implementación.**
5. **Precio con trial, anual y premium.**
6. **Distribución por contenido demostrativo, challenge y alianzas.**
7. **Retención por onboarding, retos, soporte y actualizaciones.**

Tu mejor ángulo:

> “Yo no vendo otro curso de automatización. Vendo sistemas de automatización, plantillas y comunidad para conseguir un resultado concreto.”