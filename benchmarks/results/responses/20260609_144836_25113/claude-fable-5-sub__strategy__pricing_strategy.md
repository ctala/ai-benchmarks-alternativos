# Claude Fable 5 (suscripción) — strategy/pricing_strategy

- model_id: `claude-fable-5`
- success: True  | final: 6.32 | quality: 8.5
- latency_total: 39.576s | tokens_per_second: 68.0
- input_tokens: 2 | output_tokens: 2693

## Respuesta completa

# Análisis de subida de precio: $60 → $89/mes

## 1. LTV/CAC actual vs proyectado

**Hoy:**
- LTV bruto: $840 / CAC $120 = **ratio 7:1**
- LTV sobre margen (más honesto): ($60 − $8) × 14 meses = $728 → **ratio 6.1:1**
- CAC payback: $120 / $52 margen = **2.3 meses**

Tu ratio actual ya es excelente (benchmark sano: 3:1). Eso te dice dos cosas: tienes espacio para subir precio **y** probablemente estás sub-invirtiendo en adquisición.

**Con $89 (asumiendo churn constante):**
- LTV: $89 × 14.3 = $1,271 → **ratio 10.6:1**
- Margen: $81/mes → payback baja a **1.5 meses**

## 2. Impacto esperado en churn

Una subida de **48%** es agresiva. Benchmarks de la industria (ProfitWell/Paddle, OpenView):

- Subidas bien comunicadas con grandfathering: +0.5 a +1.5 puntos de churn en la cohorte afectada, más un churn inmediato (one-time) de 5-15% de la base.
- Subidas mal ejecutadas (sin aviso, sin grandfathering): one-time loss de 20-30%.
- Dato clave: tu churn de 7% mensual **ya es alto** para SaaS B2B SMB (sano: 3-5%). Eso sugiere que parte de tu base no percibe valor suficiente — esos se irán con cualquier excusa, precio incluido.

## 3. Tres escenarios (aplicando a los 200 clientes)

MRR actual: 200 × $60 = **$12,000**

| Escenario | One-time loss | Churn nuevo | Clientes | MRR | LTV | LTV/CAC |
|---|---|---|---|---|---|---|
| Optimista | 5% (10 clientes) | 7% | 190 | $16,910 (+41%) | $1,271 | 10.6 |
| Realista | 12% (24 clientes) | 8.5% | 176 | $15,664 (+31%) | $1,047 | 8.7 |
| Pesimista | 22% (44 clientes) | 10% | 156 | $13,884 (+16%) | $890 | 7.4 |

**El número que importa:** tu break-even está en perder 65 clientes (32.5% de la base). $12,000 / $89 = 135 clientes. Incluso el escenario pesimista te deja **arriba** del MRR actual con menos clientes que soportar.

## 4. Recomendación

**Sube el precio. Los números no dejan duda:**

1. Tu ratio 7:1 grita que estás cobrando barato. $89 te deja en el medio del rango competitivo ($29-$149) — no te sales del mercado.
2. Hasta en el peor escenario ganas +$1,884/mes de MRR con 44 clientes menos que atender (menos soporte, menos infra).
3. Margen por usuario sube de 87% a 91%.

**Pero atiende el churn primero o en paralelo.** Con 7% mensual pierdes la mitad de tu base cada 10 meses. Subir precio sin arreglar retención es llenar un balde roto con agua más cara. Entrevista a los próximos 10 que cancelen antes de tocar nada.

## 5. Estrategia de implementación

**Fase 1 (mes 1): nuevos clientes a $89.** Riesgo cero de churn — nadie pierde nada. Mide conversión del funnel 30 días. Si la conversión cae menos de 20%, validaste el precio (a $89 necesitas solo 67% de la conversión actual para igualar revenue).

**Fase 2 (mes 2-3): existentes con grandfathering parcial.** No los subas a $89 directo. Opciones en orden de preferencia:
- **Anual lock-in:** "Tu precio sube a $89 en 90 días, o asegura $60/mes pagando el año por adelantado ($720)." Conviertes churn risk en cash flow + retención de 12 meses garantizada.
- **Precio puente:** existentes a $75, nuevos a $89. Reduce el shock de 48% a 25%.
- **Grandfathering total** solo para tu top 10-20% de cuentas (las de mayor uso/antigüedad/referidos).

**Fase 3: comunica con 60-90 días de aviso**, justificando con valor entregado (features lanzadas, roadmap), no con "nuestros costos subieron". Email personal del founder, no un banner.

**Métrica de control:** si el one-time churn de existentes supera 25% en los primeros 60 días, frena la migración de los que quedan y mantenlos en $60 o $75. Ya capturaste el upside con los nuevos.