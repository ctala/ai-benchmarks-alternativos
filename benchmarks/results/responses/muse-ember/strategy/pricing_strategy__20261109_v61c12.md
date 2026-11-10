# Muse Ember — strategy/pricing_strategy

- model_id: `meta/muse-ember`
- success: True  | final: 8.75 | quality: 10.0
- latency_total: 19.735s | tokens_per_second: 422.8
- input_tokens: 177 | output_tokens: 8343

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

Tu caso es interesante porque no tienes un problema de precio, tienes un problema de churn. Y eso cambia la recomendación.

**Resumen ejecutivo:** No subas de golpe de $60 a $89 a los 200 clientes. Es un +48.3%, no un ajuste. Con tu churn actual del 7% mensual, el escenario realista te deja +34% de revenue el primer año, pero el pesimista te destruye la base en 12 meses. La jugada correcta es: $89 para nuevos ya, y subida gradual + grandfather para existentes. Capturas el 80% del upside con el 30% del riesgo.

### 1. LTV/CAC actual vs. con $89

Fórmula correcta: `LTV = ARPU x Margen Bruto / Churn`

Tu costo es $8/mes, así que tu margen es altísimo.

|  | Actual $60 | $89 sin cambio de churn |
| :--- | :--- | :--- |
| Margen bruto / mes | $60 - $8 = **$52 (86.7%)** | $89 - $8 = **$81 (91%)** |
| Vida media (1/churn) | 1 / 7% = **14.3 meses** | 14.3 meses |
| LTV revenue | **$857** ($840 redondeado) | **$1,271** |
| LTV bruto | **$743** | **$1,157** |
| CAC | $120 | $120 |
| **LTV/CAC revenue** | **7.0x** | **10.6x** |
| **LTV/CAC bruto** | **6.2x** | **9.6x** |
| Payback CAC | 120 / 52 = **2.3 meses** | 120 / 81 = **1.5 meses** |

Benchmark SaaS: LTV/CAC >3 es bueno, >5 es excelente, payback <6 meses es bueno, <3 es excelente. Tú estás en zona excelente en ratio, pero terrible en churn.

**Benchmark de churn:** SaaS SMB mediana es 3.5% - 5% mensual. Top quartile <3%. Tú estás en 7%, es decir, en el peor quartile. Antes de subir precio, bajar churn 2pp vale más que subir precio: pasar de 7% a 5% te sube el LTV +40% sin generar resistencia.

El problema: el churn NO se va a quedar en 7%.

### 2. Impacto estimado en churn

Un salto de +48% es 5 veces lo que se recomienda en SaaS (5-10% anual, máximo 15-20% si lanzas mucho valor).

Con elasticidad típica en SMB SaaS, cada +10% de precio suma +0.5 a +1.0pp de churn si no hay valor nuevo percibido.

Modelo: `Churn nuevo = 7% x (89/60)^elasticidad`
- Elasticidad 0.3 (optimista): 7.9%
- Elasticidad 0.6 (realista): 9.0%
- Elasticidad 1.0 (pesimista): 10.4%

**Punto de quiebre crítico:**
¿A qué churn se anula la subida?

LTV revenue: `89 / churn_nuevo = 60 / 0.07` => **churn_nuevo = 10.38%**
LTV bruto: `81 / churn_nuevo = 52 / 0.07` => **churn_nuevo = 10.90%**

Si tu churn supera el **10.4%**, tu LTV cae por debajo del actual aunque cobres más. Con un salto del 48% y un churn base ya alto, superar ese umbral no es improbable. Probabilidad estimada: 40-50% si lo haces de golpe a todos.

Además, tu CAC subirá. Con $89 convertirás menos en landing. Asumo +5% a +42% según escenario.

Estás en $89 dentro del rango de competidores $29-$149, pero tus clientes están anclados a $60. El ancla importa más que el rango.

### 3. Modelado de 3 escenarios - Cohorte de 200 actuales

Aislando solo los 200 actuales, sin adquisiciones nuevas, 12 meses:

|  | Base $60 / 7% | Optimista 7.5% | Realista 9.0% | Pesimista 12% |
| :--- | :--- | :--- | :--- | :--- |
| Vida media | 14.3 m | 13.3 m | 11.1 m | 8.3 m |
| LTV revenue | $857 | $1,187 | $989 | $742 |
| CAC nuevo asumido | $120 | $125 | $145 | $170 |
| **LTV/CAC** | **7.1x** | **9.5x** | **6.8x** | **4.4x** |
| Payback | 2.3 m | 1.5 m | 1.8 m | 2.1 m |
| Clientes que quedan Mes 12 | 84 | 79 | 65 | 43 |
| MRR Mes 12 | $5,023 | $6,985 | $5,738 | $3,839 |
| **Revenue acumulado 12m** | **$99,672** | **$144,198 (+45%)** | **$134,016 (+34%)** | **$116,341 (+17%)** |

Lectura clave:

1.  **Incluso el pesimista gana en revenue el Año 1** (+17%). El efecto precio va por delante del efecto churn en el corto plazo. Por eso mucha gente se engaña.
2.  **Pero en el pesimista mueres en el Mes 12:** -24% de MRR vs no hacer nada, y te quedan 43 clientes vs 84. Para volver a crecer tendrás que adquirir 2x más clientes a un CAC de $170.
3.  **En el realista, el LTV/CAC no mejora** (6.8x vs 7.1x actual) porque el CAC sube tanto como el LTV. Ganas cash, no eficiencia.

Conclusión: subir de golpe es una apuesta a que tu elasticidad es <0.8. No tienes datos para asegurar eso.

### 4. Mi recomendación con números concretos

**No hagas subida general a $89. Haz esto:**

**A) Nuevos clientes: $89 desde ya.**
Es tu experimento de precio sin riesgo. Mide conversión 30 días. Si la conversión cae >30% vs $60, testea $79. Este dato te dirá tu elasticidad real antes de tocar la base.

**B) Existentes: subida en 2 escalones: $60 -> $74 (Mes 4) -> $89 (Mes 7-9)**

Escenario esperado con esta estrategia: churn blended ~8.2%, LTV ~$1,085, LTV/CAC ~7.5x, revenue cohorte 12m ~$135-140k, y te quedan ~68-70 clientes al Mes 12 vs 65 en subida directa. Ganas casi lo mismo que el realista, pero con riesgo de cola eliminado.

**C) Antes de subir, baja churn 90 días:**
Mover a anual, dunning de pagos (1-1.5pp de tu 7% probablemente es involuntario), y onboarding a valor en <7 días. Si bajas a 5.5% antes de subir, tu LTV a $89 pasa de $989 a $1,618 en el escenario realista.

### 5. Estrategia de implementación

No anuncies un aumento de precio. Anuncia un nuevo plan con valor.

**Segmenta tus 200:**
- **A - Champions (40):** >12 meses, uso alto. Migra primero, voluntario.
- **B - Core (100):** 6-12 meses, uso medio. Subida gradual.
- **C - Riesgo (60):** <6 meses, uso bajo. No los toques aún.

**Timeline:**

**Semanas 1-4: Valor antes que precio**
Lanza 1 feature visible (alertas de quiebre de stock, reporte de inventario muerto, integración). Envía reporte de ROI individual: "Con [tu producto] ahorraste X horas / $Y en faltantes". Sin esto, cualquier subida se percibe como abuso.

**Mes 1: Grandfather + Lock-in**
A C y B: "Tu precio de $60 se mantiene 6 meses". Ofrece lock anual: **$69/mes prepagado ($828/año)**. Es 22% menos que $89, te da cash upfront y churn ~0% por 12 meses. Si 50 clientes lo toman, son $41,400 de cash y 50 clientes blindados.

A A: "Pásate a Pro $89 hoy y te damos 3 meses a $71". Recoge testimonios.

**Mes 2-3: Nuevos a $89**
Actualiza pricing page con 3 tiers para anclar: Basic $49 (limitado), Pro $89 (tu actual), Business $149. El Basic te sirve como válvula de escape: mejor que se downgradeen a $49 (margen 84% con tu costo de $8) que churneen a $0.

**Mes 4: Primera subida B a $74**
Aviso con 60 días de antelación, 3 emails: 1) valor, 2) ROI, 3) opciones (anual $69, downgrade $49, o Pro $74). Nunca digas "subimos por costos".

**Mes 7-9: Segunda subida a $89**
Solo si cumples: churn de la primera ola <9.5% por 2 meses seguidos y <15% de solicitudes de cancelación/downgrade. Si no, paras en $74-$79, que también es una victoria (+27% ARPU).

**KPIs de aborto:** Si tras la primera ola el churn semanalizado supera 10.4% o los tickets de precio se disparan, pausa inmediatamente y activa grandfather extendido.

---

**Veredicto final:** Tienes margen y posicionamiento para cobrar $89, pero no tienes colchón de churn para un salto del 48%. Hazlo gradual, con nuevos primero y con una oferta anual que te proteja. Así conviertes una subida riesgosa en un experimento controlado que además te baja el churn futuro.