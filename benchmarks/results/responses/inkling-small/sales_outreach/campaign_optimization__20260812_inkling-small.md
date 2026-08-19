# Inkling Small — sales_outreach/campaign_optimization

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.73 | quality: 10.0
- latency_total: 34.22s | tokens_per_second: 109.9
- input_tokens: 270 | output_tokens: 3760

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

Primero, un detalle importante: **estás gastando $7,100** ($2,100 + $1,800 + $3,200) con un presupuesto de $5,000/mes. Eso implica que o hay un error de cuentas o estás sobrepasando el presupuesto diario. Corrige eso inmediatamente con límites de gasto diarios.

---

### 1. Métricas calculadas

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---|---|---|---|
| **CTR** | 3.0% (1,500/50k) | 4.0% (4,800/120k) | **6.0%** (900/15k) |
| **CPC** | **$1.40** | **$0.38** | $3.56 |
| **Conv. Rate** | **3.0%** | 0.5% | 4.0% |
| **CPA** | **$46.67** | $75.00 | $88.89 |
| **Signups / $** | 1 por cada $46.7 | 1 por cada $75 | 1 por cada $88.9 |

**Interpretación rápida:**
- **A** es tu máquina de conversión más eficiente: CPA más bajo y buena tasa de conversión.
- **B** trae mucho tráfico barato (CTR 4%, CPC $0.38), pero casi nadie convierte (0.5%). Es tráfico frío/educativo.
- **C** tiene la mayor intención (CTR 6%, CVR 4%), pero es muy caro por signup ($88.89).

---

### 2. ¿Escalar o pausar?

| Campaña | Veredicto | Justificación con números |
|---|---|---|
| **A** | **ESCALAR** | Es tu mejor ROI. CPA $46.67 vs $75 y $88.89. Por cada $1,000 gastados obtienes ~21 signups, vs 13 en B y 11 en C. |
| **B** | **PAUSAR o reducir a mínimo** | CPA $75 (60% más caro que A) y CVR 0.5%. Estás pagando $1,800 por solo 24 signups. Mejor usar ese presupuesto para A o para remarketing. |
| **C** | **MANTENER con presupuesto limitado / optimizar** | Alto CPA ($88.89), pero captura usuarios de alta intención (buscan "alternativa a X"). No la pauses del todo si tu LTV justifica el costo, pero no la escales hasta bajar el CPA. |

**Regla de oro:** Con $5,000, tu objetivo es maximizar signups. Si pones todo en A (hipotéticamente), tu CPA promedio bajaría. B está "quemando" presupuesto en tráfico que no convierte.

---

### 3. Cómo redistribuir los $5,000/mes

Te propongo una distribución basada en eficiencia y riesgo:

| Campaña | Presupuesto | % | Justificación |
|---|---|---|---|
| **A (Landing)** | **$3,000** | 60% | Escalar lo que funciona. Puedes subir presupuesto 40-50% si mantienes CPA cerca de $50. |
| **C (Competidor)** | **$1,200** | 24% | Mantener para capturar intención de cambio, pero con límite estricto. Si sube el CPC, baja el presupuesto. |
| **B (Blog)** | **$500** | 10% | No pausar 100% si sirve para remarketing o audiencia de lookalike, pero **cambiar el objetivo**: no busques signups directos, usa un **lead magnet** (ej. "Guía PDF de inventario"). Si sigues sin resultados, pausar. |
| **Buffer / Tests** | **$300** | 6% | Para nuevos A/B tests (landing de C, audiencia remarketing). |

**Alternativa más agresiva (si tu prioridad es solo signups):**
- A: $3,500
- C: $1,500
- B: $0 (pausada)

Esto podría darte ~75-85 signups con $5,000 vs los 105 actuales que te cuestan $7,100. Es decir: **más eficiente, menos gasto, mejor control**.

---

### 4. A/B Tests para el próximo mes

Divídelos por campaña para no mezclar variables.

#### Campaña A (Landing principal) — Objetivo: bajar CPA de $46.67
- **Landing:** Formulario en 1 paso vs. 2 pasos (email primero, luego datos).
- **Headline:** "Software de inventario para pymes" vs. "Reduce pérdidas de inventario en 30 días".
- **Social proof:** Testimonios con foto y nombre vs. logos de clientes.
- **CTA:** "Prueba gratis 14 días" vs. "Empieza hoy sin tarjeta".
- **Video:** Añadir un video de 30s de la interfaz vs. imagen estática.

#### Campaña B (Blog / Contenido) — Objetivo: subir CVR de 0.5% a 2%+
- **No busques signup directo**; usa un **lead magnet**: "Descarga la plantilla de control de inventario" vs. artículo sin captura.
- **Landing de captura:** Pop-up al 50% de scroll vs. banner fijo al final.
- **CTA:** "Leer artículo" vs. "Descargar guía gratis".
- **Audiencia:** Solo remarketing (visitantes A y C) vs. tráfico frío.

#### Campaña C (Competidor) — Objetivo: bajar CPA de $88.89
- **Landing específica:** Página de comparación "Nosotros vs [Competidor]" vs. landing principal.
- **Mensaje:** "Migración gratuita y sin complicaciones" vs. "Mejor precio / más funciones".
- **Oferta:** Trial de 30 días vs. descuento del primer mes.
- **Keywords negativas:** Añadir términos de "trabajo", "empleo", "gratis" si no aplican, para reducir clicks irrelevantes.

#### Tests generales de cuenta
- **Audiencias:** Remarketing 7 días vs. 30 días para A y C.
- **Dispositivos:** Si el 70% de signups viene de desktop, reduce bids en mobile para B.
- **Horario:** Si B convierte solo en horarios laborales, restringe sus anuncios.
- **Extensiones:** Prueba extensiones de precio o de llamada en A vs. solo sitelinks.

---

### Resumen de acción inmediata

1. **Corrige el presupuesto**: Pon un límite diario de ~$167 ($5,000/30) para no excederte.
2. **Sube A a $3,000** y monitorea que el CPA no suba de $55.
3. **Baja C a $1,200** y crea una landing de comparación específica.
4. **Pausa o reduce B a $500**; si se mantiene, cambia la oferta a un lead magnet.
5. **Corre el CPA promedio**: De $67.62 ($7,100/105 signups) a un objetivo de ~$55 ($5,000/90 signups).

¿Tienes el valor de vida del cliente (LTV) o el precio de tu producto? Con ese dato puedo calcular exactamente cuánto puedes pagar por signup y confirmar si C merece mantenerse o debe pausarse totalmente.