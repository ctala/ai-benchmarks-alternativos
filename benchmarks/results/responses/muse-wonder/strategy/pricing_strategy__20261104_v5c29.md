# Muse Wonder — strategy/pricing_strategy

- model_id: `meta/muse-wonder`
- success: True  | final: 8.18 | quality: 10.0
- latency_total: 32.503s | tokens_per_second: 115.4
- input_tokens: 177 | output_tokens: 3750

## Entrada exacta (lo que recibió el modelo)

**user:**

Mi SaaS de gestion de inventario tiene estos datos:
- CAC actual: $120
- LTV promedio: $840 (14 meses * $60/mes)
- Churn mensual: 7%
- 200 clientes actuales
- Competidores cobran entre $29 y $149/mes
- Mi costo por usuario es ~$8/mes

Estoy considerando subir el precio de $60 a $89/mes.
Analiza:
1. Calcula el LTV/CAC ratio actual y como cambiaria
2. Estima el impacto en churn (usa benchmarks de la industria SaaS)
3. Modela 3 escenarios: optimista, realista, pesimista
4. Dame tu recomendacion con numeros concretos
5. Sugiere una estrategia de implementacion (grandfather, gradual, etc)


## Respuesta completa

Tu problema no es el precio, es el churn. Y eso cambia toda la decisión.

Un 7% mensual en un SaaS de inventario — que debería ser muy sticky — es una señal de alerta. Un aumento del 48% de golpe, de $60 a $89, probablemente te haga ganar más por cliente, pero puede destruir tu base.

Vamos a los números.

### 1. Tu situación actual

**MRR actual:** 200 x $60 = **$12,000/mes**
**Margen bruto:** ($60 - $8) / $60 = **86.7%**
**Vida útil:** 1 / 0.07 = **14.3 meses** (coincide con tus 14 meses)

**LTV (ingresos):** $840
**LTV (margen bruto):** ($60-$8) x 14.3 = **$743**
**LTV/CAC:** $840 / $120 = **7.0x**
**Payback CAC:** $120 / ($60-$8) = **2.3 meses**

Un ratio saludable es 3x-5x. Estás en 7x. Eso significa una de dos: estás infra-precio, o estás invirtiendo muy poco en crecimiento. En teoría, tienes margen para subir.

**Si subes a $89 y NADA cambiara:**
Nuevo LTV = $89 x 14.3 = **$1,271**
Nuevo LTV/CAC = **10.6x**

Pero el churn sí va a cambiar.

**El punto de equilibrio es clave:**
Para que el nuevo LTV sea mejor que $840, necesitas:
$89 / churn_nuevo > $840  ->  **churn_nuevo < 10.6%**

Si tu churn pasa del 10.6% mensual, la subida te *destruye* valor aunque cobres más.

### 2. Impacto estimado en churn

Benchmarks SaaS SMB (ChartMogul, ProfitWell/Paddle):
- Churn SMB saludable: 3% - 5% mensual. Tú estás en 7%, ya estás en zona de riesgo.
- Subidas del 5-10% anual: casi sin impacto.
- Subidas del 20-30%: +1 a 2 puntos de churn.
- Subidas >40% de golpe: 15% a 30% de baja inmediata en SMB precio-sensible, más caída del 20-40% en conversión de nuevos.

Tu elasticidad es mala porque tu churn ya indica baja percepción de valor / baja dependencia.

### 3. Modelación de 3 escenarios

Asumo baja inmediata al anunciar + nuevo churn permanente + aumento de CAC por menor conversión.

|  | Actual | Optimista | Realista | Pesimista |
| :--- | :--- | :--- | :--- | :--- |
| **Precio** | $60 | $89 | $89 | $89 |
| **Baja inmediata** | - | 5% (10 clientes) | 15% (30 clientes) | 30% (60 clientes) |
| **Churn mensual nuevo** | 7.0% | 7.8% | 9.5% | 13.0% |
| **Vida útil** | 14.3m | 12.8m | 10.5m | 7.7m |
| **LTV ingresos** | $840 | **$1,141** | **$937** | **$685** |
| **LTV margen** | $743 | $1,038 | $853 | $623 |
| **CAC estimado** | $120 | $132 (+10%) | $150 (+25%) | $180 (+50%) |
| **LTV/CAC** | 7.0x | 8.6x | 6.2x | 3.8x |
| **Payback** | 2.3m | 1.6m | 1.9m | 2.2m |

**Proyección solo con tu base actual, próximos 12 meses (sin clientes nuevos):**

- **Sin subir:** $99,768 de ingresos acumulados
- **Optimista:** 190 clientes x $89 = $16,910 MRR inicial -> **$135,060 (+35%)**
- **Realista:** 170 clientes x $89 = $15,130 MRR inicial -> **$111,160 (+11%)**
- **Pesimista:** 140 clientes x $89 = $12,460 MRR inicial -> **$77,825 (-22%)**

En el escenario realista ganas, pero mucho menos de lo que parece: +48% de precio = solo +11% de ingreso a 12 meses. En el pesimista, pierdes.

### 4. Mi recomendación concreta

**No subas de $60 a $89 de golpe a los 200 actuales. Sí sube a $89, pero solo para nuevos, y lleva a los actuales de forma gradual.**

Con tu churn, un aumento directo es una apuesta con ~40% de probabilidad de salir mal.

Haz esto en su lugar:

**Objetivo a 6 meses: $15,000 - $16,000 MRR con 175-185 clientes.**
Es mejor que $12,460 MRR con 140 clientes estresados.

Estrategia ganadora: Crear tiers, no solo subir.

1.  **Starter: $49/mes** - Inventario básico, 1 usuario, 500 SKUs. Captura a los que compiten en $29.
2.  **Pro: $89/mes** - Todo lo que tienes hoy, usuarios ilimitados. Este es tu nuevo precio ancla.
3.  **Business: $149/mes** - Multi-almacén, API, soporte prioritario. Igualas el techo del mercado.

Así, $89 deja de ser "una subida" y pasa a ser "el plan del medio".

### 5. Plan de implementación en 90 días

**Fase 1: Test en nuevos (Día 1-45)**
Sube el precio en la web a $89 solo para registros nuevos. No toques a los actuales.
Mide: Si tu conversión cae >35% o tu CAC supera $170 durante 2 semanas, el mercado no acepta $89. Baja a $79 para testear. $79 con churn 8.5% ya te da un LTV de $929, mejor que hoy.

**Fase 2: Grandfather temporal, NO permanente (Día 45)**
Grandfather para siempre te cuesta: 200 x $29 = **$5,800/mes perdidos para siempre**. No lo hagas.

Anuncia a actuales con 60 días de aviso:
> "Tu precio queda bloqueado en $69 durante los próximos 12 meses. Luego pasará a $89. Si pagas anual hoy, te lo dejo en $690/año por 2 años."

$69 es +15%, psicológicamente aceptable. Esperas perder 5-8% aquí, no 15%.

**Fase 3: Subida escalonada**
Mes 3: $60 -> $69
Mes 9: $69 -> $79
Mes 15: $79 -> $89

Tres subidas <15% tienen una tasa de aceptación 3x mayor que una del 48% según datos de ProfitWell.

**Antes de todo, ataca el churn 30 días:**
Entrevista a los últimos 20 que se fueron. Si bajas el churn de 7% a 5% con el precio actual, tu LTV pasa de $840 a $1,200. Es el mismo efecto que subir a $89, con cero riesgo.

Sube el precio, pero no uses a tus 200 clientes actuales como conejillos de indias.