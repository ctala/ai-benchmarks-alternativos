# Claude Opus 5 (suscripción) — business_audit/teardown_competidor_sin_inventar

- model_id: `claude-opus-5`
- success: True  | final: 2.28 | quality: 2.0
- latency_total: 115.6s | tokens_per_second: 56.5
- input_tokens: 2 | output_tokens: 6536

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

# Teardown: comunidad de automatización, $39/mes

Antes de nada: con lo que tienes **no se puede responder "cuánto factura"** con un rango útil. La brecha entre los escenarios plausibles es de 20-30x. Lo que sí puedo hacer es mostrarte dónde está la bifurcación, cuál es mi apuesta y qué 3 observaciones baratas la cierran.

---

## 1. Qué es dato y qué no

| Observación | Estatus |
|---|---|
| Precio listado $39/mes | **DATO** (aunque "precio listado" ≠ precio promedio pagado: puede haber cupones, legacy, founding members) |
| 2.400 miembros en portada | **DATO del contador**, no de pagadores. Es la variable que rompe todo el análisis |
| 3 posts/semana en feed público | **DATO de bajísimo valor.** En estas plataformas el feed público muestra una fracción mínima; la actividad real es privada. No sirve para juzgar salud |
| 60.000 seguidores del fundador | **DATO**, pero sin tasa de crecimiento ni engagement es casi decorativo |
| 12 cursos listados | **DATO de oferta**, no de demanda ni de calidad |

Nada de lo que ves es una métrica de negocio. Son cinco métricas de vitrina, y cuatro están diseñadas para verse bien.

---

## 2. Cuánto factura

Todo depende de una sola pregunta que aún no respondiste: **¿el contador de 2.400 incluye gente gratis?**

| Escenario | Supuesto | Pagadores | MRR bruto |
|---|---|---|---|
| **A — Todo de pago** | Muro duro, 2.400 = pagadores activos | 2.400 | **~$93.600** (~$1,1M ARR) |
| **B — Freemium** | 2.400 total, conversión free→paid 2-5% | 48-120 | **~$1.900-4.700** |
| **C — Pago con inflado** | Muro duro, pero el contador arrastra lapsados/lifetime/staff | 1.400-1.700 | **~$55.000-66.000** |

**Mi apuesta: escenario B o C, no A. Confianza ~60-65%. [INFERENCIA MEDIA]**

El razonamiento es un cruce entre los dos únicos números que se restringen entre sí. Una audiencia social convierte típicamente **0,5-2% de seguidores a cliente pagador** de un producto de $39/mes, a lo largo de toda la vida del funnel. Con 60.000 seguidores eso da **300 a 1.200 pagadores**. Para sostener 2.400 pagadores tendrían que convertir al 4% de su audiencia — el doble del techo habitual — o tener canales grandes que no estás viendo (YouTube, newsletter, ads, partnerships).

En cambio, 2.400 miembros *totales* desde 60.000 seguidores es un 4% audiencia→miembro gratis: perfectamente normal, casi aburrido.

Traducción: **el número más probable es que estés mirando una comunidad de $2.000-5.000/mes disfrazada de una de $90.000/mes**, o una intermedia. Y si es A de verdad, es un negocio top-tier absoluto y competirle de frente es otra conversación.

---

## 3. Qué tan sano es

Tres cosas que sí puedo decir con la información disponible.

**a) La ausencia de plan anual es la señal más fuerte que me diste. [INFERENCIA ALTA, si se confirma]**

Si de verdad no hay anual, es un negocio 100% expuesto a la fuga mensual y sin caja adelantada. Con churn típico de comunidades pagas a este precio (**8-15% mensual**), un escenario A pierde **190-360 miembros cada mes** solo por desgaste — eso es reponer $7.500-14.000 de MRR mensual únicamente para quedar plano. Desde 60.000 seguidores, sostener ese ritmo exige ads o lanzamientos constantes. Es un negocio que corre para quedarse quieto.

Y ojo: si el anual existe pero está escondido tras el checkout, tu observación es un falso negativo. Verifícalo antes de construir estrategia sobre esto.

**b) 12 cursos es una señal ambigua que se inclina a negativa. [INFERENCIA MEDIA]**

En comunidades de este tipo, el catálogo grande suele ser síntoma de *content treadmill*: producir más contenido para justificar la cuota mensual, porque la comunidad por sí sola no retiene. Que no se vea cuáles están terminados refuerza la lectura. Un catálogo con cursos incompletos es deuda visible: cada uno es una promesa que el miembro nuevo descubre rota en la semana 2. Ese es exactamente el momento donde se decide el churn.

**c) Concentración de riesgo en una sola persona y un solo canal.**

60.000 seguidores del fundador = la adquisición depende de que él siga publicando. Sin equipo visible ni segundo canal, un mes malo del fundador es un mes malo de MRR. [INFERENCIA MEDIA]

**Lo que NO puedo evaluar y es lo que más importa:** retención, engagement real, y si los miembros consiguen resultados. Todo eso vive detrás del muro.

---

## 4. Cómo les compites

**No compitas en precio.** $35 vs $39 es invisible para el comprador. Bajar a $29 te quita 25% de margen y no te da un solo cliente que no ibas a tener igual.

Cuatro cuñas ordenadas por qué tan difícil les es responder:

1. **Anual con descuento agresivo.** Si ellos son mensual puro, tú capturas 12 meses de caja por adelantado y matas 11 oportunidades de churn. Ellos no pueden copiarlo rápido sin destruir su MRR reportado del trimestre. Si operas CAR, ya tienes esto ($249/año, 41% off) — es tu ventaja estructural más grande contra este perfil de competidor y probablemente no la estás usando como argumento comercial.

2. **Estrecha el nicho.** "Automatización" es una categoría, no una promesa. Un competidor de 2.400 miembros no puede especializarse sin canibalizar a su base actual. Tú sí. Gana quien diga a quién NO sirve.

3. **Compite en implementación, no en catálogo.** Ellos tienen 12 cursos; tú no ganas con 15. Ganas con sesiones en vivo, revisión de trabajo, y miembros que muestran lo que construyeron. El catálogo es respaldo, no producto.

4. **Haz visible lo que ellos esconden.** Publica resultados de miembros con nombre y cifra. Es la métrica que su vitrina no muestra — y no la muestra por algo.

---

## 5. Las 6 mediciones que cierran la incertidumbre

Ordenadas por valor sobre esfuerzo. Las primeras tres cambian el análisis entero y toman menos de una hora.

1. **¿Puedes entrar sin pagar?** Intenta unirte. Responde solo el 70% del teardown. Costo: 2 minutos.

2. **Wayback Machine sobre su página pública.** Busca capturas de hace 3, 6 y 12 meses y anota el contador de miembros en cada una. Esto te da la **curva de crecimiento hoy**, sin esperar un mes. Es la medición de mejor retorno de toda la lista: distingue "2.400 y subiendo 150/mes" de "2.400 estancado desde marzo" — dos negocios completamente distintos con el mismo número en portada.

3. **Screenshot del contador cada lunes, 4 semanas.** Crecimiento neto. Cruzado con el punto 2, te da tendencia real.

4. **Meta Ads Library + búsqueda de su marca.** ¿Compran tráfico? ¿Desde cuándo? Volumen y antigüedad de creativos. Si pautan fuerte, el escenario A se vuelve más creíble y su costo real de adquisición es alto. Si no pautan nada, el crecimiento depende solo del fundador.

5. **Fechas de actualización de los 12 cursos.** Cursos sin tocar en 12+ meses = catálogo muerto, no catálogo grande.

6. **Quién comenta en el feed público.** Cuenta personas únicas en los últimos 10 posts. Si son las mismas 4-5, la comunidad es delgada por muy alto que esté el contador.

---

**Resumen honesto:** hoy sabes su precio y poco más. La bifurcación free/paid vale 20-30x en la estimación de facturación, y se resuelve en dos minutos intentando entrar. Hazlo antes de tomar cualquier decisión estratégica basada en este teardown.