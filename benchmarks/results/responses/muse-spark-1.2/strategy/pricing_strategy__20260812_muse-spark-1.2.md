# Muse Spark 1.2 — strategy/pricing_strategy

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 8.5 | quality: 10.0
- latency_total: 23.192s | tokens_per_second: 146.5
- input_tokens: 176 | output_tokens: 3397

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

Tu subida de $60 a $89 es un +48.3% de golpe. Con tu churn actual es una jugada de alto riesgo. Aquí va el análisis frío con números:

### 1. LTV/CAC Ratio Actual vs Nuevo

Tu cálculo de LTV es de Ingresos. El que importa para inversores es el LTV de Margen Bruto.

*   Costo por usuario: $8
*   Margen Bruto Actual: $60 - $8 = $52 -> 86.6%
*   Margen Bruto Nuevo: $89 - $8 = $81 -> 91%

| Métrica | Actual $60 | Nuevo $89 |
| :--- | :--- | :--- |
| **LTV Ingresos** | $840 | Depende del churn |
| **LTV Margen Bruto** | $742 | Depende del churn |
| **LTV/CAC Ingresos** | **7.0x** | Ver escenarios |
| **LTV/CAC Margen Bruto** | **6.18x** | Ver escenarios |
| **Payback CAC** | 2.3 meses | 1.48 meses |

**Lectura:** Tienes un ratio de 7x. El benchmark saludable en SaaS es 3x - 4x. Un ratio >5x indica que estás **infra-cobrando** y dejando dinero en la mesa. Tienes margen para subir precio, pero tu churn te está matando.

> **Dato clave: Tu churn de 7% mensual es ALARMANTE.** En SaaS SMB B2B el benchmark es 3% a 5% mensual. 7% mensual = 58% de churn anual. Pierdes más de la mitad de tus clientes cada año. Subir precio sin arreglar retención es echar gasolina a un balde con agujeros.

### 2. Impacto Estimado en Churn

Según ProfitWell / Price Intelligently y ChartMogul: Cada 10% de subida de precio genera entre 2% y 4% de aumento en churn y un 10-15% de churn inmediato por shock.

Tu subida es de 48.3%. No es lineal. El mercado la percibe como "casi 50% más caro".

**Punto de Equilibrio:** ¿Cuánto churn puedes tolerar antes de perder plata?
`Churn Break-even = $89 * 7% / $60 = 10.38%`
**Si tu churn mensual sube por encima de 10.38% después de la subida, tu LTV será PEOR que ahora, aunque cobres más.**

### 3. Modelo de 3 Escenarios

Asumo un churn inmediato por el anuncio + churn mensual recurrente nuevo. Base: 200 clientes, MRR actual $12,000.

| Escenario | Churn Inmediato | Clientes que quedan | Churn Mensual Nuevo | Nuevo LTV Ingresos | Nuevo LTV/CAC | MRR Día 1 Post-Subida | MRR en 12 meses sin adquirir nuevos* |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **OPTIMISTA** 15% prob. | 10% pierdes 20 | 180 | 8.0% | $1,112 | **9.27x** | **$16,020 +33.5%** | $5,874 |
| **REALISTA** 60% prob. | 20% pierdes 40 | 160 | 10.0% | $890 | **7.41x** | **$14,240 +18.6%** | $4,005 |
| **PESIMISTA** 25% prob. | 35% pierdes 70 | 130 | 12.5% | $712 | **5.93x** | **$11,570 -3.6%** | $2,491 |

*Proyección solo de tu base actual, sin contar nuevos clientes. Demuestra cómo el churn compuesto te come vivo. Con tu churn actual de 7%, en 12 meses igual caerías a $5,016 MRR si no adquieres a nadie.

**Conclusión del modelo:**
*   Solo en el escenario optimista ganas claramente.
*   En el realista ganas MRR a corto plazo pero tu LTV casi no mejora y en 12 meses estarás PEOR que si no hubieras tocado nada.
*   En el pesimista pierdes MRR desde el día 1 y destruyes valor.

Y falta lo peor: **A $89 tu conversión de nuevos clientes caerá 20-30% y tu CAC subirá de $120 a $150-$180.** No lo modelé y empeora todos los escenarios.

### 4. Mi Recomendación con Números

**NO subas de $60 a $89 de golpe a tu base actual. Es un riesgo injustificado.**

Tu mejor jugada es una subida de **$60 a $69-$79** con estrategia de Grandfathering.

**Opción Recomendada: Precio a $79 para nuevos y migración controlada**

Si subes a $79 +31.6%:
*   Break-even de churn sube a 9.21% -> Tienes mucho más margen de error.
*   Escenario realista churn 9%: LTV = $877 -> Ratio 7.31x. MRR día 1 con 15% churn inmediato: 170 * $79 = $13,430 (+11.9%) sin el shock brutal de $89.

**¿Quieres llegar a $89? Hazlo en 2 escalones:** $60 -> $79 ahora -> $89 en 9 meses, solo si tu churn baja de 5%.

### 5. Estrategia de Implementación: Grandfather + Nuevos Planes

No hagas un aumento plano. Haz re-empaquetado de valor.

**Fase 1 - Próximos 30 días: Validación sin riesgo**
1.  Crea 3 planes: **Starter $49, Pro $89, Business $149.** Tu plan actual de $60 se convierte en el Pro de $89 pero con más límites/features.
2.  Pon el precio de **$89 SOLO para clientes nuevos** durante 60 días. Mide conversión y CAC real. Si tu conversión cae >30%, $89 no es sostenible.

**Fase 2 - Migración de base actual - Día 60:**
1.  **Grandfather por 6 meses:** Avisa con 60 días de anticipación: *"Mantienes $60 por 6 meses más como agradecimiento. Luego migrarás a $79 como precio de fundador, nunca pagarás $89."* Creas urgencia y lealtad.
2.  **Ancla de valor:** No digas "subimos precio". Di: *"Lanzamos nueva versión con X feature que pediste. Tu plan ahora vale $89, pero tu precio de lealtad será $79."*
3.  **Opción de pago anual con descuento:** Ofrece $790/año -> equivale a $65/mes. Mejoras tu cash flow y reduces churn anual del 58% al ~35%. El 20-30% de tu base lo tomará.

**Fase 3 - Comunicación:**
Email 1 a 60 días: Anuncio de valor + roadmap
Email 2 a 30 días: Recordatorio + oferta anual
Email 3 a 7 días: Última oportunidad para lock anual

**KPIs que debes monitorear semanalmente:**
*   Churn inmediato <15%
*   Churn mensual nuevo <9%
*   % de clientes que toman oferta anual >20%
*   NPS no debe caer más de 10 puntos

Si no puedes crear nuevos planes, entonces haz **Aumento Gradual:** $60 -> $69 en 3 meses -> $79 en 6 meses. Nunca más de 20% de golpe.

> **Prioridad #1 antes de subir precio:** Baja ese churn de 7% a 4.5%. Con 7% estás perdiendo 14 clientes al mes. Cada punto de churn que bajes vale más que subir $20 el precio. Implementa onboarding, health scores y dunning management primero.

¿Quieres que te modele la proyección a 12 meses incluyendo adquisición de 15 clientes nuevos/mes a $79 vs $89 para ver el ARR real?