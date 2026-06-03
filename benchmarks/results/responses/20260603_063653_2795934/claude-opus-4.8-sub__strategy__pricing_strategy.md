# Claude Opus 4.8 (suscripción) — strategy/pricing_strategy

- model_id: `claude-opus-4-8`
- success: True  | final: 7.09 | quality: 10.0
- latency_total: 60.106s | tokens_per_second: 70.5
- input_tokens: 2026 | output_tokens: 4239
- judge_score: 5.0 | justificación: 

## Respuesta completa

# Análisis: subir de $60 a $89/mes

Antes de los números, una aclaración importante que cambia el análisis: tu LTV de $840 está calculado sobre **ingreso**, no sobre **margen**. Con costo de $8/usuario, tu margen es $52/mes, así que tu LTV real (gross margin) es ~$742. Te doy ambos porque el de margen es el que importa para decisiones.

## 1. LTV/CAC actual vs proyectado

**Vida promedio del cliente** = 1 / churn = 1 / 0.07 = **14.3 meses** ✓ (cuadra con tu cálculo)

| Métrica | Actual ($60) | Nuevo ($89) |
|---|---|---|
| LTV (ingreso) | $840 | $89/churn |
| LTV (margen, costo $8) | $742 | $81/churn |
| CAC | $120 | $120 |
| **LTV/CAC (ingreso)** | **7.0** | ver abajo |
| **LTV/CAC (margen)** | **6.2** | ver abajo |

LTV/CAC nuevo según dónde quede el churn:

| Churn nuevo | LTV ingreso | LTV/CAC | LTV margen | LTV/CAC margen |
|---|---|---|---|---|
| 7% (sin cambio) | $1,271 | 10.6 | $1,157 | 9.6 |
| 9% | $989 | 8.2 | $900 | 7.5 |
| 12% | $742 | 6.2 | $675 | 5.6 |

**Insight #1:** Un 7:1 actual es señal de que estás **sub-cobrando**. El benchmark sano de SaaS es 3:1. Estás dejando dinero en la mesa y/o sub-invirtiendo en crecimiento. **Incluso en el peor escenario de churn (12%), tu ratio sigue en 6.2** — el doble de lo saludable. Esto solo ya justifica la subida.

## 2. Impacto en churn (benchmarks SaaS)

Una subida de $60→$89 es **+48%**, no trivial. Lo que dice la industria:

- Subidas de precio bien comunicadas a la base existente generan un **spike temporal** de churn (1-3 meses), no un nuevo nivel permanente.
- Regla práctica (Price Intelligently / ProfitWell): por cada +10% de precio se espera ~+0.5-1pp de churn temporal si está bien gestionado; mal gestionado (sin aviso, sin grandfather) puede ser 3-4x peor.
- Para +48% sin mitigación, un spike de **5-15% one-time** de la base es el rango realista; con grandfather, mucho menos.
- Clientes B2B de inventario tienen **switching cost alto** (datos, integraciones, capacitación) → son más resistentes al churn por precio que un SaaS B2C.

**Insight #2:** Tu rango de competidores ($29-$149) ubica a $89 cómodamente en la mitad. No te estás saliendo del mercado; estás dejando de ser el más barato.

## 3. Tres escenarios

Base actual: 200 clientes × $60 = **$12,000 MRR**; margen = 200 × $52 = **$10,400/mes**.
A $89: margen/usuario = $81.

| Escenario | Churn one-time | Clientes | MRR nuevo | Δ MRR | Margen nuevo | Δ Margen |
|---|---|---|---|---|---|---|
| **Optimista** | 5% (190) | 190 | $16,910 | **+41%** | $15,390 | **+48%** |
| **Realista** | 12% (176) | 176 | $15,664 | **+30%** | $14,256 | **+37%** |
| **Pesimista** | 25% (150) | 150 | $13,350 | **+11%** | $12,150 | **+17%** |

**El número que cierra la decisión — breakeven:**
- Para igualar tu MRR actual necesitarías caer a **135 clientes** → puedes perder **32%** de la base.
- Para igualar tu **margen** actual: caer a **128 clientes** → perder **36%**.

**Insight #3:** Tendrías que perder ~1 de cada 3 clientes solo por el precio para quedar igual. Eso es catastróficamente improbable en B2B con switching cost. **El riesgo está fuertemente sesgado a tu favor.**

## 4. Recomendación concreta

**Sube el precio. Sí.** Pero no a $89 plano para todos de golpe.

- **Nuevos clientes:** $89 **desde ya**. Riesgo cero sobre tu base, y empiezas a capturar valor inmediatamente. Vigila que la conversión no caiga >15% (eso subiría tu CAC efectivo).
- **Base existente:** migra con grandfather (ver punto 5).
- **Número objetivo:** apunta al escenario realista (~176 clientes, +30% MRR, +37% margen ≈ **+$3,850/mes de margen, ~$46k/año**) sin gastar $1 más en adquisición.
- **Considera $79 en vez de $89** si quieres minimizar fricción: sigues capturando +32% de precio con un salto psicológicamente más digerible (debajo del umbral de $80). Pero $89 está bien soportado por tus números.

Reinvierte parte del margen extra en crecimiento: con LTV/CAC de 8-10 puedes permitirte un CAC más alto para acelerar.

## 5. Estrategia de implementación

Recomiendo **grandfather con migración gradual** (el mejor balance riesgo/captura):

1. **Nuevos = $89 hoy.** Sin anuncio, sin drama.
2. **Grandfather a la base actual** por 3-6 meses al precio viejo. Esto compra goodwill y evita el spike.
3. **Migración con aviso de 60-90 días.** Email personal del fundador explicando el *por qué* (nuevas features, soporte, inversión en el producto), no "subimos precios".
4. **Ancla con valor:** lanza/empaqueta una mejora visible junto con la subida para que se perciba como upgrade, no como castigo.
5. **Oferta de retención para leales:** quien pase a plan **anual** mantiene un precio intermedio (ej. $75/mes facturado anual). Esto reduce churn (lock-in 12 meses) y mejora cash flow.
6. **Segmenta:** si tienes clientes grandes/heavy users, considera un tier superior ($129-149) — tienes margen hacia el techo de $149 del mercado.

**Lo que NO haría:** subida plana retroactiva a todos sin aviso. Es lo único que podría empujarte al escenario pesimista.

---

**Bottom line:** Tus unit economics gritan que estás barato (7:1 cuando 3:1 es sano). El breakeven exige perder 32% de clientes — improbabilísimo en B2B. Sube, grandfather a la base, $89 a nuevos ya. Upside esperado ~+$46k/año de margen con riesgo controlado.

¿Quieres que arme esto como un modelo en una hoja de cálculo con sliders (churn, % grandfather, conversión) para que juegues los escenarios?