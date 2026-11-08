# Tencent Hy4 — business_audit/teardown_competidor_sin_inventar

- model_id: `tencent/hy4`
- success: True  | final: 5.73 | quality: 6.0
- latency_total: 49.14s | tokens_per_second: 93.7
- input_tokens: 213 | output_tokens: 4602

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

Como analista, arranco separando el expediente en dos cajones: **tu evidencia** y **mis hipótesis**. No voy a rellenar huecos con datos que no me diste sin etiquetarlos antes.

**Veredicto ejecutivo (adelanto):** Facturan en un rango estimado de **$78k–$94k MRR** `[INFERENCIA · Certeza Media 60%]`. Es un negocio de margen muy alto, pero con señales de **fragilidad por retención y dependencia del fundador** `[INFERENCIA · Certeza Media 55%]`. Tu mejor ataque no es el precio, es la **ambigüedad de su catálogo** `[DATO]`.

---

### BLOQUE 0 · Inventario de evidencia

| Etiqueta | Qué tengo | Certeza |
|---|---|---|
| `[DATO]` | Comunidad de pago / automatización / plataforma de membresía | 100% |
| `[DATO]` | Contador público: "2.400 miembros" | 100% |
| `[DATO]` | Precio de lista: $39/mes | 100% |
| `[DATO]` | 3 posts/semana en feed **público** | 100% |
| `[DATO]` | Fundador: 60.000 seguidores | 100% |
| `[DATO]` | 12 cursos listados | 100% |
| `[DATO FALTANTE]` | Existencia de plan anual / descuentos / cupones | 100% (sé que no lo sé) |
| `[DATO FALTANTE]` | % de cursos realmente terminados | 100% (sé que no lo sé) |
| `[DATO FALTANTE]` | Si esos 3 posts son *teaser* o son el feed de pago replicado | 100% (sé que no lo sé) |

> ⚠️ **Trampa evitada**: `$39` es **precio de lista** `[DATO]`, no es **ARPA** (ingreso medio por cuenta) `[INFERENCIA]`. Toda estimación parte de ahí.

---

### BLOQUE 1 · ¿Cuánto facturan?

**1. Cálculo naive**
`2.400 × $39 = $93.600 MRR` → `~$1,12M ARR`
`[INFERENCIA · Certeza Media 65%]` — Es el techo matemático si todos pagan mes a mes sin descuento.

**2. Ajuste por estructura de precios oculta**
`[INFERENCIA · Certeza Baja 30%]` — Aplico un heurístico de industria (no un dato tuyo): en comunidades de creador, suele haber plan anual con ~25% de descuento y ~40% de adopción. Si eso fuera cierto aquí:
- 60% × 2.400 × $39 = $56.160
- 40% × 2.400 × ~$24 = $23.040
- **≈ $79.200 MRR equivalentes**

**3. Ajuste por el contador de portada**
`[INFERENCIA · Certeza Media 70%]` — Los contadores de landing suelen ser redondeados hacia arriba, incluir trials, o no descontar bajas. El "2.400" probablemente no es "2.400 tarjetas activas hoy".

| Escenario | MRR estimado | Certeza |
|---|---|---|
| Techo (todo mensual, contador real) | **$93,6k** | Media (60%) |
| Base (con anual + algo de redondeo) | **$78k – $85k** | **Media (55%)** |
| Suelo (mucho descuento / churn alto) | **< $70k** | Baja (25%) |

📌 **Respuesta**: *Probablemente ~$80k/mes (~$1M/año)*. Certeza global: **Media (55–60%)**. No puedo subirla sin ver el checkout.

---

### BLOQUE 2 · ¿Qué tan sano es?

| Dimensión | Lectura | Certeza |
|---|---|---|
| **Margen bruto** | Plataforma tipo membresía = coste fijo bajo + % por transacción. Estimado **85–92% de margen**. En papel, es una máquina de cash. | `[INFERENCIA · Alta 85%]` |
| **Adquisición** | 2.400 / 60.000 = **4,0% de conversión** sobre la audiencia. Ratio sano. *Pero* implica que el embudo es **100% dependiente del fundador** (key-person risk). | `[INFERENCIA · Media 60%]` |
| **Audiencia residual** | O les quedan 57,6k por convertir (upside) **o** esos 57,6k ya dijeron "no" (techo). No distingo cuál. | `[INFERENCIA · Baja 35%]` |
| **Retención 🚩** | **"12 cursos listados sin estado"** `[DATO]` + **3 posts/semana en feed *público*** `[DATO]`. Hipótesis: están vendiendo *roadmap* como catálogo y/o compensando con contenido de arriba del embudo lo que falta dentro. Patrón típico de **churn en mes 2–3**. | `[INFERENCIA · Baja-Media 40%]` |
| **Ambigüedad crítica** | No sé si esos 3 posts son un *teaser* (sano: top-of-funnel) o el espejo de una comunidad interna vacía (insano). **Esto cambia el diagnóstico por completo.** | `[DATO FALTANTE · 100%]` |

**Diagnóstico**: **Rentable, pero frágil** `[INFERENCIA · Certeza Media 55%]`. Tienen caja y margen; su punto débil no es la adquisición, es *qué pasa después de que la tarjeta cobra*.

---

### BLOQUE 3 · Cómo les compito (Playbook ordenado por certeza)

**🥇 Ataque 1 · Transparencia radical** *(anclado en `[DATO]`, no en hipótesis)*
> Ellos: *"12 cursos"* (sin estado). Tú: *"3 cursos **terminados al 100%**, última actualización [fecha], con plantillas descargables y changelog público"*.
Atacas la duda exacta que su portada genera, sin inventar nada. **Certeza de impacto: Alta (75%)**. Es el movimiento más barato y más defendible.

**🥈 Ataque 2 · Haz visible lo que ellos ocultan** *(anclado en `[DATO FALTANTE]`)*
> Publica **plan anual en la portada** (ej. $290/año ≈ $24/mes) + garantía de 30 días.
No compites bajando el mensual; compites **quitando fricción de decisión**. Si ellos tienen anual escondido en el checkout, tú ya ganaste la comparación antes del clic. **Certeza: Media (60%)**.

**🥉 Ataque 3 · Des-founderizar la propuesta** *(anclado en `[INFERENCIA · Media 60%]`)*
> Posiciona tu comunidad como **"sistema + plantillas + peers"**, no como *"acceso al gurú"*.
Si su fundador baja el ritmo, su embudo se seca; el tuyo no. Es una apuesta estructural, no de copy. **Certeza estratégica: Media (50%)**.

**🧪 Ataque 4 · Invertir el regalo** *(anclado en `[INFERENCIA · Baja 40%]` → **validar antes de ejecutar**)*
> Ellos regalan *contenido* (3 posts/sem) para llevar a pago. Hipótesis: tú regalas la **herramienta funcional** (un workflow de automatización que corre) y cobras por la **implementación acompañada**.
⚠️ Depende de resolver el `[DATO FALTANTE]` del feed. **No lo lances sin antes confirmar si esos posts son teaser o contenido interno.**

---

### BLOQUE 4 · Qué necesito para subirte la certeza (próximos 7 días)

1. **Scraping del contador**: anota "2.400" hoy y vuelve en 30 días. ¿Sube, baja, se queda clavado? → Pasa el churn de `Baja 40%` a `Media/Alta`.
2. **Checkout fantasma**: llega hasta poner tarjeta (sin pagar). ¿Aparece el anual? → Cierra el rango de MRR de `55%` a `~85%`.
3. **Fechas de los 3 posts**: ¿llevan 3 años publicando o arrancaron hace 6 semanas? → Valida la hipótesis de "roadmap vendido como catálogo".
4. **Social listening**: busca *"me salí"*, *"esperaba más"*, *"cuando sale el curso X"* en respuestas al fundador → Es la única vía externa para medir su retención.

---

**Cierre de analista**: Con lo que me diste, **sé** que tienen un precio, un contador, un catálogo ambiguo y un fundador con audiencia. **Infiero** ~$1M/año, margen alto y grieta en retención. Cualquier cifra que veas más precisa que `$78k–$94k` en otro informe, está inventando datos que tú y yo no tenemos. ¿Quieres que modele el Ataque 1 con un copy de portada lado a lado?