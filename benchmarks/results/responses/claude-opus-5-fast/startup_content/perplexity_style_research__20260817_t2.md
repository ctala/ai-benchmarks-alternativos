# Claude Opus 5 Fast — startup_content/perplexity_style_research

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 7.09 | quality: 8.88
- latency_total: 35.695s | tokens_per_second: 200.7
- input_tokens: 297 | output_tokens: 7163
- judge_score: 4.2 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un asistente de investigacion. Tu rol es compilar informacion actual sobre un tema
para que un redactor pueda escribir un articulo. Proporciona datos estructurados, fuentes posibles,
y puntos clave. Formato similar a como Perplexity presenta resultados.

**user:**

Investiga: "Estado del venture capital en Latinoamerica Q1 2026"

Necesito:
1. Resumen ejecutivo (3 bullets)
2. Datos clave con numeros:
   - Inversion total estimada
   - Deals mas grandes
   - Paises lideres
   - Sectores hot
3. Tendencias principales (3-5)
4. Comparacion con Q1 2025
5. Quotes o perspectivas de actores relevantes
6. Fuentes sugeridas para profundizar

Formato estructurado, facil de escanear.


## Respuesta completa

# Investigación: Estado del VC en Latinoamérica — Q1 2026

## ⚠️ ADVERTENCIA CRÍTICA ANTES DE USAR ESTE MATERIAL

**No puedo entregarte datos reales de Q1 2026.** Dos razones concretas:

1. **No tengo acceso a internet ni herramientas de búsqueda en esta sesión.** Todo lo que sigue viene de mi entrenamiento, cuyo corte confiable es principios de 2025.
2. **Aunque lo tuviera, los reportes consolidados de Q1 2026 (LAVCA, Sling Hub, Crunchbase, KPMG) se publican entre la primera y la sexta semana posterior al cierre del trimestre** (es decir, abril 2026). Si estás escribiendo antes de eso, ni siquiera existen cifras oficiales todavía.

**Si invento números de inversión total, deals o valuaciones, tu redactor los publicará y serán falsos.** No voy a hacer eso.

Lo que sí te sirve, y te lo doy abajo:

- **A.** Línea base histórica verificable (2021–2024 + lo que sé de 2025) para que el redactor tenga contexto y punto de comparación
- **B.** Plantilla estructurada con los campos exactos a llenar, y de dónde sacar cada dato
- **C.** Lista de fuentes primarias con nombre, cadencia de publicación y qué métrica específica da cada una
- **D.** Lista de personas reales a las que pedir quotes, con su afiliación
- **E.** Hipótesis de tendencias a verificar (marcadas como hipótesis, no como hechos)

---

## A. LÍNEA BASE HISTÓRICA (para contexto y comparación)

### Inversión VC anual en LatAm

| Año | Monto aprox. | Nota |
|---|---|---|
| 2021 | ~US$15–16 mil M | Pico histórico (SoftBank, Tiger, tasas cero) |
| 2022 | ~US$7–8 mil M | Corrección |
| 2023 | ~US$3–4 mil M | Piso del ciclo |
| 2024 | ~US$4–4.5 mil M | Recuperación modesta |
| 2025 | **No confirmado** | Ver nota abajo |

> **Nivel de confianza:** medio-alto para 2021–2024. Las cifras varían entre fuentes (LAVCA, Crunchbase, Sling Hub y PitchBook usan metodologías distintas: algunas incluyen deuda, growth equity o rondas de empresas con HQ fuera de la región). **Verifica siempre con qué metodología trabaja la fuente que cites.**

> **2025:** mi información es fragmentaria y no la usaría sin verificar. No cito cifras.

### Distribución por país (patrón estructural 2022–2024)

- **Brasil:** ~50–60% del capital regional
- **México:** ~15–25%
- **Colombia, Chile, Argentina:** el resto, con volatilidad alta trimestre a trimestre
- Un solo mega-deal puede distorsionar completamente el ranking país en un trimestre dado. **Advierte esto en el artículo.**

### Concentración sectorial

- **Fintech:** históricamente 40–50% del capital regional. Es el dato estructural más estable de LatAm.
- Siguientes: proptech, logística/supply chain, healthtech, agtech, SaaS B2B.

### Deals grandes que sí puedo nombrar (pre-2025, para contexto histórico)

- **Ualá** (Argentina) — Serie E ~US$300M, liderada por Allianz X, ~nov 2024
- **QI Tech** (Brasil) — ~US$200M Serie B, General Atlantic, ~oct 2024
- **ASAAS** (Brasil) — Serie C, ~R$820M, 2024
- **Plata** (México) — ~US$160M, 2024

> Verifica montos exactos y fechas antes de publicar. Mi precisión en cifras específicas de rondas individuales es limitada.

---

## B. PLANTILLA A LLENAR (los datos que necesitas)

### 1. Resumen ejecutivo — 3 bullets
- [ ] Bullet 1: cifra total Q1 2026 + variación % vs Q1 2025 (fuente: LAVCA o Sling Hub)
- [ ] Bullet 2: el dato contraintuitivo del trimestre (¿cayó el número de deals pero subió el monto? ¿un país desplazó a otro?)
- [ ] Bullet 3: la tendencia estructural que el trimestre confirma o rompe

### 2. Datos clave
| Campo | Dónde conseguirlo |
|---|---|
| Inversión total Q1 2026 | LAVCA quarterly / Sling Hub / Crunchbase News |
| Nº de rondas | Mismas fuentes — **pide ambas métricas**, monto sin conteo engaña |
| Ticket promedio y mediana | Sling Hub, Distrito. La **mediana** es más honesta |
| Top 5 deals | LatamList, Contxto, Bloomberg Línea, comunicados de las empresas |
| Ranking por país | LAVCA; cruzar con ABVCAP (BR), AMEXCAP (MX) |
| Split por etapa (pre-seed→growth) | LAVCA, PitchBook |
| Sectores | Sling Hub, Distrito, CB Insights |
| Nuevos unicornios | Crunchbase Unicorn Board, LatamList |
| Salidas / M&A / IPOs | TTR Data, ABVCAP-KPMG |
| Fundraising de fondos (LP→GP) | LAVCA — **métrica clave y subreportada**: indica salud del ciclo 2027–2029 |

### 3. Tendencias — verificar cada una
### 4. Comparación Q1 2025 vs Q1 2026
> Pide a la fuente la serie trimestral completa, no solo el YoY. Un trimestre aislado es ruido.

### 5. Quotes → ver sección D
### 6. Fuentes → ver sección C

---

## C. FUENTES PRIMARIAS

### Nivel 1 — Data providers (cifras citables)

| Fuente | Qué da | Cadencia |
|---|---|---|
| **LAVCA** (lavca.org) | El estándar regional. VC + PE, por país y etapa. También fundraising de fondos | Anual + updates trimestrales |
| **Sling Hub** | Data granular LatAm, muy fuerte en Brasil. Reportes mensuales | Mensual/trimestral |
| **Distrito** (BR) | "Inside Venture Capital Brasil" | Trimestral |
| **Crunchbase News** | Suele publicar corte regional en los primeros días post-trimestre | ~3–5 días post-cierre |
| **PitchBook** | Metodología rigurosa. De pago | Trimestral |
| **CB Insights** — State of Venture | Corte LatAm dentro del global | Trimestral |
| **KPMG Venture Pulse** | Sección Américas | Trimestral, gratuito |
| **TTR Data** | M&A y salidas, no solo VC | Mensual |

### Nivel 2 — Asociaciones nacionales
- **ABVCAP** (Brasil) — reporte conjunto con KPMG
- **AMEXCAP** (México)
- **ARCAP** (Argentina), **ColCapital** (Colombia), **ACVC** (Chile)

### Nivel 3 — Prensa especializada
- **LatamList** / Emerging Markets Report — newsletter, buena cobertura de deals
- **Bloomberg Línea** — cobertura regional en español/portugués
- **Brazil Journal**, **NeoFeed**, **Valor Econômico**, **Startups.com.br** (Brasil)
- **Contxto**, **Expansión**, **El Economista** (México)
- **Reuters / Bloomberg** para deals grandes

### Nivel 4 — Reportes anuales de contexto
- **Atlantico** — "Latin America Digital Transformation Report" (Julio Vasconcellos). Excelente para narrativa macro
- **Endeavor Insight**
- **BID Lab / BID Invest**

---

## D. PERSONAS PARA QUOTES

> Todos son actores reales del ecosistema. Verifica cargos actuales antes de citar — hay rotación.

**Fondos regionales**
- Hernán Kazah / Nicolás Szekasy — **Kaszek**
- Eric Acher — **monashees**
- Federico Antoni / Fernando Lelo de Larrea — **ALLVP** (MX)
- Shu Nyatta / Marco Camhaji — **Bicycle Capital**
- Mike Packer — **QED Investors**
- Nathan Lustig — **Magma Partners**
- Mónica Saggioro — **MAYA Capital**
- Anna Raptis — **Amplifica Capital** (MX)
- Brian Requarth — **Latitud**

**Fundadores con visión de ecosistema**
- David Vélez — Nubank
- Pierpaolo Barbieri — Ualá
- Sergio Furió — Creditas

**Institucionales**
- Equipo de research de **LAVCA**
- **BID Lab**
- Local partners de **SoftBank Latin America** / **Upload Ventures**

**Tip para el redactor:** el quote más valioso no es "estamos optimistas". Pregunta específico: *¿cuántas term sheets firmaste este trimestre vs. el año pasado?* *¿Bajaron las valuaciones de entrada?* *¿Tus LPs están comprometiendo capital nuevo o solo haciendo follow-on?*

---

## E. HIPÓTESIS DE TENDENCIAS (verificar, NO publicar como hecho)

Estas son vectores que estaban activos hasta mi corte de información. Trátalas como preguntas de investigación:

1. **Tasas de interés locales como freno.** La Selic brasileña estuvo en niveles muy altos durante 2025. Con renta fija local pagando doble dígito, los LPs domésticos brasileños tienen poco incentivo para asignar a VC. → *Verificar nivel de Selic en Q1 2026 y su efecto en fundraising local.*

2. **IA: ¿adopción o creación?** La pregunta real para LatAm no es si hay hype, sino si aparecen startups de IA con producto propio o solo wrappers/aplicación vertical. → *Verificar cuántos deals de Q1 2026 se etiquetaron "AI" y qué construyen realmente.*

3. **Ventana de salidas.** Sin IPOs ni M&A significativos, el ciclo no cierra. → *Verificar si hubo IPOs de tech latinoamericana o adquisiciones relevantes.*

4. **Argentina post-reformas.** Cambios regulatorios y de control de capitales podrían reactivar el ecosistema. → *Verificar flujo real de capital a startups argentinas.*

5. **Deuda y venture debt.** Crecimiento de estructuras no dilutivas, especialmente en fintech de crédito. → *Verificar si las fuentes incluyen deuda en sus totales — esto infla comparaciones.*

6. **Stablecoins y pagos transfronterizos.** Vector activo en remesas LatAm. → *Verificar deals concretos.*

7. **México y relación comercial con EE.UU.** Incertidumbre arancelaria/nearshoring afecta apetito de riesgo. → *Verificar sentimiento de fondos mexicanos.*

---

## RECOMENDACIÓN DE PROCESO

1. **Descarga primero el reporte de LAVCA o Sling Hub de Q1 2026.** Es la columna vertebral del artículo.
2. **Cruza con una segunda fuente** (Crunchbase o Distrito). Si difieren >20%, explica la discrepancia metodológica en el artículo — eso es contenido de valor, no un problema.
3. **Consigue 2–3 quotes frescos.** Los reportes dan números; los inversionistas dan interpretación.
4. **Verifica cada deal individual** contra el comunicado oficial de la empresa. La prensa suele repetir montos inflados.

---

Si me compartes el reporte de Q1 2026 (pegando el texto o los datos), puedo estructurarlo, calcular las variaciones vs. Q1 2025 y armar el borrador completo con la estructura que pediste. También puedo redactar las preguntas específicas para las entrevistas si me dices a quién van a contactar.