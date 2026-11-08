# Tencent Hy4 — business_strategy/plan_monetizar_medio_con_restricciones

- model_id: `tencent/hy4`
- success: True  | final: 6.9 | quality: 8.0
- latency_total: 168.628s | tokens_per_second: 90.3
- input_tokens: 408 | output_tokens: 15229

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un estratega de negocio que trabaja con fundadores solos y sin capital. Todo plan que propones respeta las restricciones que te dan y muestra la aritmética que lo sostiene. Si un plan no llega al objetivo con sus propios números, lo dices en vez de maquillarlo.

**user:**

Tengo un medio digital de nicho (noticias de tecnología) y necesito hacerlo rentable. Quiero un plan para llegar a **$5.000 USD/mes** en 90 días.

LO QUE TENGO:
- 300.000 visitas/mes de tráfico orgánico (SEO), creciendo.
- El contenido lo genero de forma automatizada, así que publicar más no me cuesta tiempo.
- Audiencia: profesionales y curiosos de tecnología, mayormente LATAM.
- Autoridad de dominio decente, los artículos rankean.

LO QUE NO TENGO:
- **No tengo lista de correo.** Cero suscriptores hoy.
- **No tengo presupuesto para publicidad pagada.** Cero.
- Soy una sola persona y le puedo dedicar ~4 horas al día.

RESTRICCIONES DURAS (si las rompes, el plan no me sirve):
- **NO quiero publicidad display ni programática** (AdSense y similares). Ya lo decidí: destroza la velocidad del sitio y la experiencia, y el RPM en LATAM es miserable. No insistas con esto.
- No puedo contratar a nadie en 90 días.

Dame el plan. Y muéstrame la aritmética: cómo llegan los $5.000/mes con los números que tú mismo propongas.


## Respuesta completa

## Veredicto

**Sí llega a $5.000 USD/mes en el mes 3, pero no por el tráfico ni por publicar más.** Llega por convertir tu autoridad de dominio en **3 contratos prepagos** + **un MRR pequeño propio** + **afiliación de texto**. Con mis propios números, el mes 3 deja **$5.745 netos**.

Y te digo ya el caso en el que **no** llega: si cierras 2 sponsors en vez de 3, quedas en **$4.605**. Faltan $395. No lo voy a disfrazar con el crecimiento del tráfico ni con un cobro anual en el día 89.

**Display/programática queda fuera desde la línea 1.** No la propongo, no la menciono como "aunque sea poco", y la convierto en argumento comercial: tu sitio sigue rápido *por eso* el patrocinio vale $1.200 y no $200.

---

## 1. El modelo: 3 líneas, cero `<script>` de terceros

| Línea | Formato | Precio | Por qué no rompe tu restricción |
|---|---|---|---|
| **A. Patrocinio editorial B2B** | 1 mención de texto en la newsletter + 1 artículo marcado "Patrocinado" + enlace de texto en 3 artículos ya rankeados. Máx. 3 slots/mes. | **$1.200/mes, prepago** | Ni banner, ni iframe, ni píxel del anunciante. Mides clics con un `302` tuyo en `/go/<slug>`. Si el sponsor pide píxel, la respuesta es no. |
| **B. "Radar Tech LATAM"** | Suscripción mensual: comparativa de precios/lanzamientos actualizada + CSV/Notion + alertas. Se entrega por correo. | **$25/mes** | Link de pago externo, sin widget embebido. Cero JS en el sitio. |
| **C. Afiliación editorial** | Enlaces de texto `rel="sponsored nofollow"` **solo** en artículos de comparativa / precio / "alternativas a X". 1 por artículo. | Comisión media **$6** | No es display ni subasta ni programática: es un enlace que ya forma parte del contenido. No carga nada. |

> **Nota de honestidad sobre la regla:** si tú consideras que la línea C también viola tu "no publicidad", el plan cae a **$4.845** y **no llega**. En ese caso necesito 80 pagos en vez de 60, o un 4º slot. Te lo digo ahora, no en el día 80. Lo dejo como plan principal porque un enlace de afiliado no es AdSense ni similar en términos de velocidad, pero la decisión es tuya.

**Coste de herramientas: $0/mes.** Substack gratis para la lista (cobro el producto **por fuera**, así Substack no se queda su 10%), payment link de PayPal/Wise/Stripe sin mensualidad, lead magnet en Notion/Drive, `/go/` en tu propio servidor, Search Console. Solo hay fees por transacción, y ya están descontados abajo.

---

## 2. Supuestos míos (todos declarados, ninguno escondido)

1. **Congelo el tráfico en 300.000 visitas/mes durante los 3 meses.** Dijiste que crece; **no lo cuento**. Si crece, es upside, no parte del cálculo.
2. De esas 300k, **80.000/mes (26,7%) son intención comercial** ("mejor X", "X vs Y", "precio de X"). *Se valida el día 3 con Search Console.* Si son menos, ajusto la línea C y lo digo.
3. Captura de correo: **0,8% de visitas = 2.400/mes**. Uso enlace HTML propio a la página de suscripción, **sin iframe ni embed de Substack** dentro del artículo (eso sí cargaría terceros). Asumo fricción extra, por eso no pongo 1,5%.
4. Bajas de lista: **5%**.
5. Conversión a pago: **0,88%** de activos (60 de 6.800). Conservador para B2B/profesionales.
6. Fee de cobro: **5%** sobre sponsors y producto (PayPal/Wise LATAM). Los afiliados los paga el programa, sin fee tuyo.
7. **Cero anualidades.** Todo es mensual. El mes 3 es MRR real, no un cobro grande disfrazado de "$5.000/mes".
8. **Cero pagos a 30/60 días.** Prepago o no hay plan (ver §7).

---

## 3. Aritmética del mes 3 (días 61–90)

**Primero, de dónde sale la lista**

| Concepto | Cálculo | Resultado |
|---|---|---|
| Visitas 90 días | 300.000 × 3 | 900.000 |
| Suscriptores brutos | 900.000 × 0,8% | 7.200 |
| Bajas 5% | 7.200 × 0,95 | 6.840 → **uso 6.800** (redondeo a la baja) |

**De dónde salen los $900 de afiliación**

| Concepto | Cálculo | Resultado |
|---|---|---|
| Visitas intención comercial | supuesto validado día 3 | 80.000 |
| Clics a ofertas | 80.000 × 10% | 8.000 |
| Conversiones | 8.000 × 1,9% ≈ 152 → **150** (redondeo a la baja) | 150 |
| Ingreso | 150 × $6 | **$900** |

**Cierre del mes 3**

| Línea | Bruto | Fee 5% | Neto |
|---|---:|---:|---:|
| A. 3 sponsors × $1.200 | 3.600 | 180 | **3.420** |
| B. 60 pagos × $25 | 1.500 | 75 | **1.425** |
| C. Afiliación (sin fee nuestro) | 900 | 0 | **900** |
| **TOTAL** | **6.000** | **255** | **$5.745** ✅ |

**Colchón: $745 (14,9%) por encima del objetivo.** No viene de subir conversiones raras: viene de que $1.200 por 300k visitas orgánicas + una lista de ~7k es un precio B2B cerrable, no inflado.

---

## 4. De dónde salen los 3 sponsors (esto no puede aparecer por arte de magia)

Embudo de outreach, hecho por ti, 15 emails/día bien personalizados:

| Paso | Tasa | Número |
|---|---|---|
| Emails (días 11–55, 40 días × 15) | — | **600** |
| Respuestas | 10% | 60 |
| Reuniones cortas | 25% de respuestas | 15 |
| Contratos firmados | 27% de reuniones | **4** |

Facturas **3** (los slots disponibles) y dejas **1 en lista de espera** como reemplazo si alguien no renueva. Prospectos: devtools, hosting/cloud, VPN, bootcamps, APIs fintech con venta en LATAM. El media kit es **una página**: 300k visitas orgánicas, autoridad, y la frase "sin banners ni scripts de terceros: tu marca no compite con 4 redes de anuncios".

En el mes 3 los 3 activos son **2 renovaciones + 1 que entra de la espera**.

---

## 5. Curva de 90 días (rampa, no salto en el día 89)

| | Mes 1 (días 1–30) | Mes 2 (31–60) | Mes 3 (61–90) |
|---|---:|---:|---:|
| Suscriptores activos | 2.400 | ~4.600 | **6.800** |
| Sponsors facturando | 0 | 2 | **3** |
| Pagos Radar | 0 (lanza día 45) | 25 | **60** |
| Afiliación | 600 (ramp-up días 10–30) | 900 | **900** |
| **Bruto** | 600 | 3.925 | **6.000** |
| **Neto en cuenta** | **$600** | **$3.774** | **$5.745** ✅ |

**Hitos duros**
- **Día 1:** regla `cero <script> de terceros`. Creas `/go/<slug>` (302 propio) para medir clics sin píxeles.
- **Día 3:** Search Console confirma las visitas de intención comercial. Si son <60k, reajusto la línea C en ese momento.
- **Día 5:** lead magnet + bloque HTML de captura insertado por plantilla en los ~200 artículos con más tráfico (coste único; tu contenido automatizado hace el resto).
- **Día 7:** `/patrocinio` publicado con precio, 3 slots, y la lista explícita de lo que **no** se vende (banners, píxeles, programática).
- **Día 10:** 60 prospectos + plantilla listos → arranca el outreach.
- **Día 45:** Radar a $25, ofrecido solo a quien ya recibió 2+ correos.
- **Semana 8 (día ~56):** condición de éxito = **3 cobros prepagos confirmados**, no "3 firmas". Sin esto, el plan no llega.

---

## 6. Cabe en tus 4 h/día (360 h en 90 días)

| Bloque | Horas |
|---|---:|
| Infra (captura, `/patrocinio`, media kit, `/go/`, plantillas) | 30 |
| Outreach: 600 emails a 8 min | 80 |
| Follow-ups, reuniones, propuestas | 34 |
| Armar Radar + landing + payment link + welcome | 16 |
| Entregar menciones, reportes a sponsors, soporte | 23 |
| Métricas y operación (contenido = 0 h, es automatizado) | 23 |
| **Planificado** | **~206 h (2,3 h/día)** |
| **Buffer para rechazos, renegociaciones y soporte imprevisto** | **~154 h** |

No asumo eficiencia perfecta. El buffer es parte del plan, no un sobrante optimista. **Cero contrataciones, cero publicidad pagada.**

---

## 7. Prueba de estrés: cuándo NO llega (dicho explícitamente)

| Escenario | Neto mes 3 | ¿Llega? |
|---|---:|---|
| **Plan base** | **5.745** | ✅ |
| Cierras **2** sponsors, no 3 | **4.605** | ❌ **Faltan $395. No lo maquillo.** |
| Decidas que los afiliados también violan tu regla | **4.845** | ❌ Faltan $155 → necesito 80 pagos o 4º slot |
| Captura cae a 0,4% (lista 3.400 → 30 pagos) | **5.033** | ✅ pero **sin colchón**: cualquier otro fallo lo rompe |
| Afiliación cae a la mitad | **5.295** | ✅ |
| **Aceptas cobro a 30 días en vez de prepago** | 3.600 se cobran en el mes 4 | ❌ **No llega en 90 días** aunque el run-rate sea correcto |

**Condiciones no negociables, en orden:**
1. **Prepago mensual.** Es la que más fácilmente te hace fallar sin que los números parezcan malos.
2. **3 cobros confirmados en semana 8**, no 3 conversaciones.
3. **Sin píxel del anunciante**, aunque lo pida. Se mide con `/go/`.
4. **Máximo 3 slots y 1 enlace sponsored por artículo**, con `rel="sponsored nofollow"`, para no tocar el SEO que ya te da 300k visitas.
5. **No contar el crecimiento del tráfico ni anualidades** en el cálculo. Si aparecen, se anotan como upside.

---

## Día 91

El objetivo se cumple en el mes 3 con **$5.745 netos y MRR real**. Pero lo que te quedas no es el pico: es una lista de ~6.800 profesionales, 60 pagos recurrentes y 3 contratos que se renuevan. Si el día 91 un sponsor se cae, ya tienes el 4º en espera y una línea propia que no depende de venderle a nadie. Eso es lo que hace que el mes 4 no vuelva a empezar de cero.