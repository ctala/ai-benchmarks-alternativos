# Muse Spark 1.3 — business_audit/teardown_competidor_sin_inventar

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 5.67 | quality: 6.0
- latency_total: 28.866s | tokens_per_second: 134.4
- input_tokens: 190 | output_tokens: 3879

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

Te hago el teardown, pero con honestidad radical desde el inicio:

Con solo 6 datos públicos **no puedo saber** cuánto facturan ni qué tan sanos están. Solo puedo estimar rangos. Aquí te separo todo.

**Leyenda de certeza que usaré en todo el análisis:**
* **[DATO]** = Lo que tú viste. Certeza **Alta** de que lo observaste, **Media** de que sea verdad (no lo verifiqué yo).
* **[INFERENCIA - Alta/Media/Baja]** = Lo que yo deduzco. No es un hecho.

---

### 1. Punto de partida: lo que SÍ sabemos vs. lo que NO sabemos

**[DATO] Lo que sabemos (porque tú lo viste):**
1. Es comunidad de pago sobre automatización en plataforma de membresía.
2. Portada dice "2.400 miembros".
3. Precio visible: $39/mes.
4. Publican 3 posts/semana en feed público.
5. Fundador tiene 60.000 seguidores en una red.
6. Listan 12 cursos, estado de finalización desconocido.

**[DATO] Lo que NO sabemos - y es crítico:**
No sabemos si "2.400 miembros" = pagando activos, acumulados históricos, o incluye free trials / cancelados. **[INFERENCIA - Media]**: En este tipo de plataformas, el número de portada suele ser total acumulado, no MRR activo. Certeza Media, basado en patrón de mercado.
No sabemos si hay plan anual, lifetime, cupones, afiliados.
No sabemos churn, crecimiento, engagement real (comentarios, vistas), ni costes.

> Sin eso, cualquier cifra de facturación es una **hipótesis, no un hecho.**

### 2. ¿Cuánto factura? Mi estimación por escenarios

**Cálculo matemático máximo, sin ajustes:**
2.400 x $39 = $93.600 MRR = $1.123.200 ARR
**[DATO + Cálculo]** Certeza Alta en la matemática, **Certeza Baja** en que sea real.

Nadie cobra el 100% al precio full. Te doy 3 escenarios **[INFERENCIA - Certeza Baja en todos]**:

**Escenario A - Optimista (creen todo lo que muestran):**
2.400 activos x $39 = **$93.6k MRR / ~$1.12M ARR bruto**
Menos comisiones Stripe (~2.9% + $0.30) + plataforma (~3-5%) = Neto ~$85k-87k MRR.
Probabilidad: Baja. Asume 0% churn, 0% descuentos, 0% inactivos.

**Escenario B - Base (mi apuesta más razonable):**
Asumo: solo 70-75% son pagadores activos, y el ARPU real es ~$33-35 por anuales con descuento (2 meses gratis es estándar).
1.800 activos x $34 = **~$61.200 MRR / ~$734k ARR bruto.** Neto ~$56k MRR.
**[INFERENCIA - Certeza Media-Baja]**. Es lo más típico en comunidades de este tamaño.

**Escenario C - Conservador (número inflado):**
Asumo: 50% son activos reales, ARPU $30.
1.200 x $30 = **$36.000 MRR / ~$432k ARR bruto.** Neto ~$33k MRR.
**[INFERENCIA - Certeza Baja]**, pero posible si el "2.400" incluye toda la historia.

**Mi conclusión:** **[INFERENCIA - Certeza Media]** Facturan probablemente entre **$36k y $61k MRR neto**. No tomes los $93k como verdad.

### 3. ¿Qué tan sano es el negocio?

Lo analizo por pilares:

**1. Adquisición: Parece sana, pero frágil.**
**[DATO]** 60k seguidores -> 2.400 miembros = 4% conversión total.
**[INFERENCIA - Certeza Media]**: Eso es una conversión muy buena, lo que indica que el motor es 100% marca personal orgánica. CAC probablemente casi $0.
**[INFERENCIA - Certeza Media]**: Riesgo alto: dependencia total del fundador. Si él para, se para el crecimiento. No sabemos si crecen o están estancados.

Para mantener 2.400 miembros con un churn normal de membresías ($30-50/mes = 5-8% mensual) **[INFERENCIA mercado - Certeza Media]**, necesitan captar 120-190 nuevos/mes solo para no caer. Con 60k seguidores, es factible, pero es una treadmill constante.

**2. Retención / Producto: Señal amarilla.**
**[DATO]** 3 posts/semana + 12 cursos listados.
**[INFERENCIA - Certeza Baja]**: 3 posts/semana es consistencia saludable, no excelente. No sabemos si hay comentarios, ni si la gente termina los cursos.
**[INFERENCIA - Certeza Baja]**: 12 cursos "sin saber si están terminados" suele ser mala señal en estos negocios: mucho contenido ancho y poco profundo para vender. Eso genera churn por "ya vi todo" o "está incompleto".

**3. Monetización: Dejan dinero sobre la mesa.**
**[DATO]** Solo se ve $39/mes.
**[INFERENCIA - Certeza Media]**: Si no tienen anual, están perdiendo cashflow por adelantado y aumentando churn. Si sí lo tienen y no lo muestran, es un error de pricing page. En ambos casos, es un punto débil. Su LTV estimado (si churn 7%): $39 / 0.07 = ~$557 **[INFERENCIA - Certeza Baja]**.

**Salud general:** **[INFERENCIA - Certeza Baja]** Negocio probablemente rentable y lifestyle (fundador + 1-2 soporte), no una máquina escalable. Nota: 6.5/10 con alta incertidumbre.

### 4. Cómo les compites (atacando lo que inferimos)

No compitas frontal por $39. Ataca sus 3 debilidades probables:

**1. Posicionamiento: Sé lo opuesto a "12 cursos genéricos".**
Ellos venden amplitud. Tú vende finalización.
Idea: "No 12 cursos. 1 sistema para automatizar X en 30 días con plantillas listas." Cobra $79/mes premium o $19/mes nicho. Ganas por claridad.

**2. Distribución: No pelees en su red.**
**[INFERENCIA - Certeza Media]** Él domina una red con 60k. Tú no le vas a ganar ahí.
Juega en otro campo: SEO en YouTube ("cómo automatizar [herramienta] + [industria]"), o partnerships con agencias. Su dependencia del fundador es tu oportunidad.

**3. Oferta de retención: Comunidad + Resultado, no solo contenido.**
Su punto débil probable es churn por contenido incompleto. Ofrece lo que retiene: auditorías en vivo 1 vez/mes, bolsa de jobs/freelance, directorio de plantillas descargables, certificación. Eso justifica quedarte 12 meses.

### Qué mirar después para afinar esto (si quieres, te ayudo)

Para pasar de **[INFERENCIA - Baja]** a **[Alta]**, necesitaría que me traigas:
1. Captura del checkout (¿hay anual? ¿trial?)
2. Link a sus posts públicos (quiero ver likes/comentarios por post)
3. Archive.org de su portada hace 6 meses (¿decía 1.800 o 2.400? = velocidad de crecimiento)

¿Quieres que te modele el escenario B con tus costes para ver a qué precio tendrías que entrar para quitarles 200 miembros en 90 días?