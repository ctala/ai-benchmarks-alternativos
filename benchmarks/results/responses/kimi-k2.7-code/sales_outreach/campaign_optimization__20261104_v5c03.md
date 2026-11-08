# Kimi K2.7 Code — sales_outreach/campaign_optimization

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 7.01 | quality: 8.0
- latency_total: 49.865s | tokens_per_second: 61.6
- input_tokens: 283 | output_tokens: 3070

## Entrada exacta (lo que recibió el modelo)

**user:**

Tengo estos resultados de mi campana de Google Ads del ultimo mes:

Campana A (Landing principal):
- Impresiones: 50,000 | Clicks: 1,500 | Signups: 45 | Costo: $2,100
- Keywords: "software gestion inventario", "inventario pymes"

Campana B (Blog content):
- Impresiones: 120,000 | Clicks: 4,800 | Signups: 24 | Costo: $1,800
- Keywords: "como gestionar inventario", "problemas inventario restaurante"

Campana C (Competidor):
- Impresiones: 15,000 | Clicks: 900 | Signups: 36 | Costo: $3,200
- Keywords: "alternativa a [competidor]", "[competidor] vs"

Mi presupuesto total es $5,000/mes.

1. Calcula CTR, CPC, CPA, y conversion rate de cada campana
2. Cual campana debo escalar y cual pausar? Justifica con numeros
3. Como redistribuiria el presupuesto de $5,000?
4. Que A/B tests sugeririas para el proximo mes?


## Respuesta completa

Aquí tienes el análisis con los KPIs y recomendaciones basadas en los números.

## 1. KPIs por campaña

| Campaña | CTR | CPC | Conversion Rate | CPA (costo por signup) |
|---|---:|---:|---:|---:|
| **A – Landing principal** | 3.00% | **$1.40** | **3.00%** | **$46.67** |
| **B – Blog content** | 4.00% | **$0.38** | 0.50% | **$75.00** |
| **C – Competidor** | **6.00%** | **$3.56** | 4.00% | **$88.89** |

**Cómo se calculan:**
- **CTR** = Clicks ÷ Impresiones
- **CPC** = Costo ÷ Clicks
- **Conversion Rate** = Signups ÷ Clicks
- **CPA** = Costo ÷ Signups

> **Dato clave:** Estás gastando **$7,100/mes** y tu presupuesto es de **$5,000/mes**, así que necesitas recortar al menos **$2,100**.

---

## 2. ¿Cuál escalar y cuál pausar?

### ✅ Escala la Campaña A
- **Mejor CPA:** $46.67 (casi la mitad que C).
- Generó **45 signups**, la mayor cantidad.
- Aunque su CTR no es el más alto, **convierte muy bien** (3% de conversion rate).
- Es la campaña más eficiente para captar usuarios.

### ⚠️ Mantén/Optimiza la Campaña B (pero no la escales todavía)
- Tiene el **CPC más bajo ($0.38)** y buen tráfico, pero una **conversion rate muy baja (0.5%)**.
- Las keywords son informativas (“cómo gestionar inventario”), así que la intención de compra es menor.
- Es útil para **generar awareness**, pero no para escalar signups directamente sin mejorar el embudo.

### 🛑 Pausa (o reduce drásticamente) la Campaña C
- **CPA más alto:** $88.89.
- Aunque tiene buen CTR (6%) y buen CVR (4%), el **CPC es carísimo ($3.56)** y consume mucho presupuesto.
- Con keywords de competidor pagas mucho por clics que no siempre se convierten.
- Aportó 36 signups a $3,200: si pausas C, liberas presupuesto para A, que aportaría más signups por el mismo dinero.

---

## 3. Redistribución del presupuesto de $5,000

Como estás sobre presupuesto, una opción simple y basada en datos es **pausar C y mover la mayor parte del dinero a A**.

| Campaña | Presupuesto mensual | Razón |
|---|---:|---|
| **A – Landing principal** | **$3,200** | Escalar lo que mejor convierte |
| **B – Blog content** | **$1,800** | Mantener tráfico top funnel, pero optimizar conversiones |
| **C – Competidor** | **$0** | Pausar por CPA muy alto |
| **Total** | **$5,000** | ✅ Dentro del presupuesto |

**Proyección simple:** si la Campaña A mantiene su CPA de $46.67 con $3,200, podría generar alrededor de **68 signups** (vs. los 45 actuales).

> Alternativa conservadora: si no quieres pausar C por completo, redúcela a **$500** como test y ajusta A a **$2,900** y B a **$1,600**.

---

## 4. A/B tests recomendados para el próximo mes

### Campaña A (Landing principal)
- **Headline del hero:** hablar de “ahorra tiempo” vs “reduce pérdidas de stock”.
- **CTA:** “Prueba gratis” vs “Agenda una demo” vs “Empieza ahora”.
- **Formulario:** probar versión corta (email + contraseña) vs versión con más campos.
- **Prueba social:** incluir logos de clientes, testimonios o números de usuarios.
- **Video/demo:** landing con video explicativo vs landing solo con texto.

### Campaña B (Blog content)
- **CTA dentro del artículo:** “Descargar guía gratis” vs “Probar software gratis”.
- **Pop-up de salida:** ofrecer lead magnet relacionado al artículo.
- **Embudo:** enviar tráfico del blog a una landing dedicada en lugar de la homepage.
- **Retargeting:** crear audiencia de lectores del blog y mostrarles anuncios de la Campaña A.

### Campaña C (Competidor) — si decides mantenerla como test
- **Mensaje:** “alternativa a [competidor]” vs “[competidor] vs tu marca”.
- **Landing de comparación:** tabla de características con precios claros.
- **Oferta de migración:** “migramos tus datos gratis” para reducir fricción.
- **Negative keywords:** excluir términos como “login”, “soporte”, “opiniones” si no convierten.

### A nivel de anuncios
- Probar **Responsive Search Ads** con distintos mensajes (beneficio vs precio vs facilidad).
- Usar **extensiones de enlace** a páginas específicas (precios, funciones, demo).
- Revisar **palabras clave negativas**, especialmente en B y C.

---

### Resumen ejecutivo
- **Escala A:** mejor CPA y más signups.
- **Pausa C:** CPA muy alto y consume demasiado.
- **Optimiza B:** buen tráfico barato, pero necesita mejorar la conversión.
- **Redistribuye:** prioriza presupuesto para A, mantén B y elimina C.