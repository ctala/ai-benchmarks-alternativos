# Claude Opus 5 Fast — business_audit/teardown_competidor_sin_inventar

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 2.28 | quality: 2.0
- latency_total: 36.847s | tokens_per_second: 184.0
- input_tokens: 286 | output_tokens: 6780

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

# Teardown competitivo — Comunidad de automatización $39/mes

Antes de nada: **todo lo que me diste son 6 datos de una landing page.** Ninguno de ellos es un dato financiero. Voy a construir estimaciones, pero quiero que veas exactamente dónde termina la evidencia y dónde empieza mi razonamiento, porque la respuesta honesta a "cuánto facturan" tiene un rango de 6x y eso *en sí mismo* es el hallazgo más importante.

Etiquetas que uso:
- **[DATO]** — observable, verificable
- **[INF-A/M/B]** — inferencia con confianza alta / media / baja
- **[ESPEC]** — especulación plausible, sin base sólida

---

## 1. Qué sabemos realmente

| Observación | Estatus | Lo que NO nos dice |
|---|---|---|
| "2.400 miembros" en portada | **[DATO]** de lo que *muestran*, no de lo que *es* | Si son de pago, si son activos, si es acumulado histórico |
| $39/mes visible | **[DATO]** del precio de lista | El precio *efectivo* que cobran de media |
| 3 posts/semana en feed público | **[DATO]** | Actividad dentro del muro de pago |
| Fundador: 60.000 seguidores | **[DATO]** | Alcance real, calidad, si convierte |
| 12 cursos listados | **[DATO]** | Cuántos existen de verdad |
| No se ve plan anual | **[DATO negativo]** — ausencia de evidencia | Que no exista |

---

## 2. El cálculo obvio está mal (y por qué importa)

2.400 × $39 = **$93.600/mes ≈ $1,1M ARR**. Ese número es casi con certeza incorrecto **[INF-A]**. Cuatro fugas, en orden de impacto:

**a) El contador probablemente no cuenta solo a quien paga.** **[INF-M]**
Es el factor con más peso, con diferencia. Muchas de estas plataformas permiten un grupo gratuito junto al de pago, y muchos operadores muestran en la landing la cifra más favorable. También suelen incluirse moderadores, invitados, afiliados y cortesías. No puedo saber cuál es el caso sin verlo por dentro.

**b) El ARPU real está por debajo de $39.** **[INF-A]**
Plan anual con descuento (lo típico es 15-20% off → equivalente ~$32-33/mes), precios *legacy* de fundadores tempranos, cupones de lanzamiento, cortesías. Casi ningún negocio de suscripción cobra su precio de lista de media.

**c) Fallos de cobro (churn involuntario).** **[INF-A]** Tarjetas caducadas y rechazos suelen comerse un porcentaje del MRR facturado cada mes.

**d) Reembolsos y garantías.** **[INF-B]** — desconocido, pero rara vez es cero.

---

## 3. Modelo de ingresos: tres escenarios

Todo esto es **[INF-M]** salvo donde marco lo contrario. Los supuestos están explícitos para que puedas cambiarlos cuando consigas datos.

| | **Bajo** | **Central** | **Alto** |
|---|---|---|---|
| % del contador que paga | 15% | 55% | 90% |
| Miembros de pago | ~360 | ~1.320 | ~2.160 |
| ARPU efectivo | $32 | $33 | $35 |
| **MRR** | **~$11.500** | **~$43.500** | **~$75.600** |
| **ARR bruto** | **~$138k** | **~$522k** | **~$907k** |

**Rango: $138k – $907k ARR.** Esa dispersión no es pereza analítica: es el estado real de la información. **No tomes ninguna decisión que dependa de saber si facturan $150k o $800k**, porque hoy no lo puedes saber. Sí puedes tomar decisiones que funcionen en todo el rango (sección 6).

### Un cruce que inclina la balanza

Hagamos una comprobación independiente desde el embudo. Con 60.000 seguidores en una red social, la conversión acumulada de audiencia a comunidad de pago concurrente suele moverse en torno al 0,5-2% **[INF-B — es un rango de referencia del sector, no una ley]**. Eso da **300-1.200 miembros de pago simultáneos**.

Para sostener 2.400 de pago *concurrentes* con esa sola audiencia, necesitarían una conversión del 4%, muy por encima de lo habitual. Conclusiones posibles:

1. El contador incluye miembros gratuitos **[INF-M — mi hipótesis principal]**
2. Tienen canales que no viste: YouTube, newsletter, ads, afiliados, otras plataformas **[INF-M]**
3. Son excepcionalmente buenos convirtiendo **[INF-B]**

Lo más probable es una mezcla de 1 y 2. **Esto empuja mi estimación central hacia la mitad baja del rango: entre $250k y $500k ARR** **[INF-M]**. Pero nota que es una inferencia sobre una inferencia — trátala como hipótesis a falsar, no como conclusión.

---

## 4. Salud del negocio: qué señala cada pista

### Señales que no puedes leer como positivas

**"3 posts/semana" no mide salud de comunidad.** **[INF-A]**
Es el feed *público* — casi con seguridad marketing del fundador, no vida interna. La métrica que importa es posts y comentarios generados *por miembros* dentro. Una comunidad sana tiene conversación diaria entre miembros sin el fundador. Una comunidad zombi tiene al fundador publicando 3 veces por semana en un salón vacío. **Desde fuera, ambas se ven idénticas.** Esto es lo primero que verificaría.

**"12 cursos, no se sabe cuántos terminados" es una señal ambigua tirando a mala.** **[INF-M]**
Dos lecturas:
- *Benigna*: biblioteca profunda, buena percepción de valor en el checkout.
- *Preocupante*: listar cursos incompletos es un patrón clásico de "producir contenido para justificar el precio". Y estratégicamente, **las bibliotecas de contenido retienen mal**: el miembro consume, siente que "ya lo tiene" y cancela sobre el mes 3-4. El contenido es un argumento de *adquisición*; lo que retiene es la interacción, la responsabilidad y los resultados.

**El precio $39 está en la zona incómoda.** **[INF-M]**
Demasiado caro para una compra impulsiva sin fricción, demasiado barato para financiar atención personalizada. A ese precio el negocio *depende* del volumen, y el volumen depende de reponer churn constantemente.

### La matemática que probablemente les duele

Con churn mensual del 8-10% (rango habitual en comunidades de este precio) **[INF-B]**:
- Vida media del cliente ≈ 10-12 meses → **LTV ≈ $350-450**
- Para mantener 1.300 miembros planos hacen falta **~110-130 altas nuevas al mes**, todos los meses, para siempre
- Para *crecer*, bastantes más

Esto significa: **el negocio no es una comunidad, es una máquina de captación que casualmente entrega una comunidad** **[INF-M]**. Y esa máquina tiene un solo motor.

### El riesgo estructural: dependencia de una persona

Los 60.000 seguidores son del **fundador**, no de la marca **[DATO]**. Si el fundador se quema, cambia de tema, o la plataforma le recorta alcance, la reposición de churn se cae y el MRR se desangra al 8-10% mensual **[INF-A — es aritmética, no opinión]**. Es la vulnerabilidad más explotable que veo, y es estructural: no la pueden arreglar rápido.

---

## 5. Cómo conseguir datos reales (barato, ordenado por ROI)

**Nivel 1 — gratis, hazlo esta semana:**

1. **Busca si existe una comunidad gratuita de la misma marca.** Resuelve de un golpe la incógnita del 6x. Prioridad absoluta.
2. **Wayback Machine sobre la landing.** Te da la serie histórica de: precio (¿han subido?), contador de miembros (¿trayectoria de crecimiento?), número de cursos (¿12 desde hace un año = producción parada?). Esto convierte una foto en una película. Es la técnica de mayor valor por minuto invertido.
3. **Registra el contador cada semana durante 6-8 semanas.** Te da el crecimiento *neto*.
4. **Busca su página de afiliados.** La comisión revela cuánto CAC toleran, lo que a su vez implica su LTV interno.
5. **Ofertas y lenguaje del fundador.** Si empuja mucho "cierro puertas" o descuentos frecuentes, suele indicar presión de captación **[INF-M]**.

**Nivel 2 — $39, el mejor dinero que gastarás:**

Entra un mes como cliente. Es competencia legítima y estándar. Mira, en orden:
- **Posts y comentarios de miembros (no del fundador) por día.** La métrica de salud real.
- **Hilos de bienvenida**: cuántos entran por semana → **altas brutas**
- **Altas brutas – crecimiento neto = churn.** Aquí obtienes el número que nadie publica.
- Cuántos de los 12 cursos están completos de verdad
- Si en el checkout aparece plan anual y con qué descuento → corrige tu ARPU
- Qué ofrecen en el flujo de cancelación (pausa, descuento) → mide su desesperación por retener
- Quién responde a los miembros: ¿el fundador, un equipo, nadie?

**Línea que no cruzo:** nada de scraping de datos de miembros, entrar con identidad falsa, ni contactar a sus clientes usando información obtenida dentro. Además de ser dudoso, si sale a la luz el daño reputacional supera cualquier ventaja.

---

## 6. Cómo competir

Estas cuatro jugadas funcionan **en los tres escenarios de facturación**, así que puedes empezar sin esperar a los datos.

### 1. No pelees por la distribución. Pelea por la especificidad.
No vas a ganar una guerra de audiencia contra 60.000 seguidores a corto plazo **[INF-A]**. "Automatización" es una categoría enorme y difusa — eso es exactamente lo que la hace atacable por los flancos. Coge un vertical o un rol concreto (automatización para agencias, para ops de ecommerce, para despachos contables) y sé insustituible ahí. Ellos no pueden seguirte sin diluir su propuesta amplia.

### 2. Ataca la retención, no el precio.
Si mi lectura de "biblioteca de contenido" es correcta **[INF-M]**, su punto débil es el mes 3-4. Construye lo que una biblioteca no puede dar: cohortes con fecha, responsabilidad, revisión de trabajo real, resultados medibles. Tu mensaje no es "más barato", es "aquí terminas lo que empiezas".

### 3. Barbell de precio, nunca $39.
Igualar su precio es la peor posición: compites en su terreno sin su distribución. Elige un extremo:
- **Abajo ($9-15):** volumen, entrada sin fricción, monetiza después con algo caro
- **Arriba ($150-400):** grupo pequeño, alto contacto, mismo MRR con 10x menos miembros y mucho menos churn

El extremo alto es más defendible si empiezas sin audiencia **[INF-M]**: menos clientes que captar, mejor retención, y ellos no pueden bajar a competir sin canibalizar su modelo de volumen.

### 4. Prepárate para el momento de fragilidad.
Vigila señales de que el motor de captación tose: contador plano varias semanas, promociones más agresivas, el fundador publicando menos. Ese es el momento de subir la inversión en contenido comparativo y en captar a sus miembros descontentos — con contenido público que resuelva justo lo que a ellos les falta, no con outreach directo a su lista.

---

## 7. Resumen honesto

| Pregunta | Respuesta más sólida que puedo dar |
|---|---|
| ¿Cuánto facturan? | $138k–$907k ARR. Mi centro es **$250-500k [INF-M]**. Necesitas 2 datos para reducirlo 5x: ¿el contador incluye gratuitos? ¿existe plan anual? |
| ¿Es un negocio sano? | **No lo sé, y desde fuera es imposible saberlo.** Es un negocio *rentable* casi seguro (costes bajos). Que sea *sano* depende del churn y de la dependencia del fundador, y ninguna de las dos cosas es visible. |
| ¿Cuál es su punto débil? | Dependencia de un solo canal personal para reponer un churn que probablemente es alto. **[INF-M]** |
| ¿Cómo compito? | Nicho más estrecho + retención por resultados + precio en un extremo del barbell. |

**El sesgo del que te aviso:** todo lo que te he dado sale de una landing page, y las landing pages están diseñadas para producir exactamente la impresión que produjeron. El "2.400" está ahí porque suena grande. Mi trabajo aquí ha sido no dejar que ese número ancle el análisis — y el tuyo es no dejar que mi estimación central lo sustituya como si fuera un hecho.

Pásame lo que encuentres del Nivel 1 y recalculo con rangos mucho más estrechos.