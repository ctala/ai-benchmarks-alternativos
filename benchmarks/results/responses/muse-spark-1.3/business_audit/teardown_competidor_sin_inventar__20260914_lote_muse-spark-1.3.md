# Muse Spark 1.3 — business_audit/teardown_competidor_sin_inventar

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 5.7 | quality: 6.0
- latency_total: 32.015s | tokens_per_second: 108.2
- input_tokens: 190 | output_tokens: 3465

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

Te hago el teardown, pero con una regla estricta: separo lo que **realmente sabemos** de lo que **estoy estimando**. Porque con solo datos públicos, la facturación es un rango, no un número.

### TL;DR

**🟢 SABEMOS (tú lo viste):** Dicen tener 2.400 miembros y cobran $39/mes.
**🟡 INFIERO - Certeza Media:** Su facturación real más probable está entre **$65k - $80k MRR**, no los $93.6k teóricos. Es un negocio sano en adquisición pero probablemente dependiente del fundador y vulnerable en retención.
**🔴 DESCONOCEMOS:** Churn, cuántos de esos 2.400 pagan, costes, y actividad real dentro.

---

### 1. Cuánto factura: del techo teórico al rango realista

**🟢 SABEMOS - Certeza 100% sobre lo observado:**
* En portada *afirman* 2.400 miembros. No sabemos si son activos, de pago, históricos acumulados o totales.
* Precio visible es $39/mes.

**Cálculo techo teórico (matemática simple, no realidad):**
2.400 x $39 = **$93.600 MRR / $1.123.200 ARR**

> Esto es el 100% pagando precio completo, sin fallos de pago, sin descuentos, sin cuentas gratis. Casi nunca ocurre. Lo pongo solo como techo.

**🟡 INFIERO - Mis 3 escenarios:**

**1. Pesimista - Certeza Baja (30% probabilidad para mí): $42k - $55k MRR**
Por qué lo planteo: [INFERENCIA - Certeza Media] Muchas comunidades inflan el número con ex-miembros, cuentas inactivas, o staff/cortesías. Si el 40-50% no paga mes a mes, caen aquí.

**2. Base / Más probable - Certeza Media (60% probabilidad para mí): $65k - $80k MRR**
Asumo: [INFERENCIA - Certeza Media-Alta basada en benchmarks de membresías]
* -10% por fallos de tarjeta + churn natural del mes
* -10-15% por planes anuales con descuento (aunque no lo veas, [INFERENCIA - Certeza Alta] el 90% de comunidades de $30-50 lo tienen, normalmente $390/año = 2 meses gratis)
* -5% por cortesías, equipo, afiliados
Eso deja un efectivo de ~$28-$33 por "miembro mostrado", no $39.

**3. Optimista - Certeza Baja (20% probabilidad): $85k - $93.6k MRR**
Solo si: tienen cero plan anual, cero cuentas gratis y crecimiento tan rápido que el churn no se nota. Poco probable.

**🟡 INFIERO sobre beneficio neto - Certeza Media:**
No sabemos sus costes. Pero por benchmark: plataforma de membresía (5-10%) + Stripe/PayPal (~3.5% + $0.30) + herramientas. Quédate con ~85-90% de margen bruto antes de sueldos/ads. O sea, en escenario base: **~$58k - $72k brutos/mes para operar.**

### 2. Qué tan sano es el negocio

Lo analizo en 4 pilares:

**A) Adquisición: Se ve FUERTE, pero frágil**
* 🟢 SABEMOS: Fundador con 60.000 seguidores.
* 🟡 INFIERO - Certeza Media: 2.400 / 60.000 = 4% de conversión acumulada de audiencia a miembro. Es un ratio sano y creíble para nicho. No huele a fake.
* 🟡 INFIERO - Certeza Media-Alta: Son casi seguro **founder-led**. Riesgo: si el fundador deja de publicar, se cae la captación. No vemos otra fuente (SEO, ads, afiliados).
* 🔴 DESCONOCEMOS: Engagement real de esos 60k, crecimiento mensual, de dónde viene el tráfico.

**B) Activación / Contenido: Se ve CONSTANTE, pero superficial**
* 🟢 SABEMOS: 3 posts/semana en feed público + 12 cursos listados.
* 🟡 INFIERO - Certeza Media: 3x/semana es buen ritmo para mantener SEO social y percepción de actividad. Pero es feed *público*. No sabemos nada del valor *privado* (que es por lo que se paga).
* 🟡 INFIERO - Certeza Baja: 12 cursos suena a mucho. Mi hipótesis es que varios son cortos, desactualizados o "en construcción" para anclar valor. Es una táctica típica para justificar $39. No sabemos tasa de finalización.
* 🔴 DESCONOCEMOS: Comentarios, likes, cuánta gente entra al día, soporte.

**C) Retención: AQUÍ ESTÁ EL RIESGO**
* 🔴 DESCONOCEMOS: Churn. Y esto lo es todo.
* 🟡 INFIERO - Certeza Media (por benchmark, no por sus datos): Una comunidad de automatización a $39 suele tener un churn mensual de 5-9%. Eso significa que para mantener 2.400 estables, necesitan captar **120 a 216 miembros nuevos CADA MES**.
* 🟡 INFIERO - Certeza Media: A $39, el LTV probable es corto: $39 / 7% churn = ~$557 de vida cliente (~14 meses). Si su churn es 10%+, viven en una cinta de correr.

Conclusión de salud: [OPINIÓN, no hecho] Parece un negocio en fase "cash cow de creador", no una máquina escalable. Sano en caja, débil en defensibilidad.

### 3. Cómo les compites (sin pelear en su terreno)

No compitas con "otra comunidad de automatización a $39". Pierdes.

Aquí 4 ángulos donde son atacables, todos marcados:

**1. Ataca el resultado, no la biblioteca**
* 🟡 INFIERO - Certeza Media: Con 12 cursos, venden volumen. Tú vende velocidad: "Automatiza X en 7 días" vs "12 cursos".
* Recomendación: Nicho vertical (ej: automatización solo para agencias, solo para e-commerce, solo con IA + No-code). Ellos son generalistas por lo que describes.

**2. Ataca la dependencia del fundador**
* 🟡 INFIERO - Certeza Media: Todo apunta a marca personal. Si él falla, la comunidad se enfría.
* Recomendación: Posiciónate como comunidad operada / con soporte real / con expertos múltiples + sesiones en vivo + accountability. Eso retiene mejor que videos grabados.

**3. Ataca el precio por arriba, no por abajo**
* No bajes a $29. Te matas a churn igual.
* Recomendación: $39/mes es incómodo para B2B. Prueba $79-99/mes pero con 1 caso de uso que ahorre >$500/mes, o prueba $390/año bien empaquetado + garantía de 14 días. Ganas en LTV aunque tengas menos miembros.

**4. Ataca su punto ciego público**
* Publican 3x/semana en público. Úsalo.
* Recomendación: Haz teardown de sus posts con más comentarios (últimos 90 días). Ahí tienes sus dolores validados gratis. Crea un lead magnet / curso gratuito mejor que su mejor post.

### 4. Qué necesitas para subir mi certeza de Media a Alta

🔴 Hoy DESCONOCEMOS y deberías investigar (todo público y legal):
1.  ¿El contador de 2.400 sube con Wayback Machine? Si lleva 6 meses clavado, es número de marketing.
2.  ¿Comentarios por post? Si 60k seguidores = <50 likes/post, la adquisición es débil.
3.  ¿Hay prueba gratis / garantía? Cambia el MRR real un 20%.
4.  ¿Reviews en Trustpilot, Reddit, YouTube "review + [nombre]"? Ahí sale el churn y quejas de cursos incompletos.
5.  ¿Ofertas de Black Friday / anual oculto en checkout? Prueba llegar hasta el pago sin pagar.

Si me traes esos 5 datos, te recalculo el MRR con Certeza Alta y te digo exactamente qué curso lanzar para robarles miembros.

¿Quieres que te arme la tabla de seguimiento para espiar esos 5 puntos semana a semana?