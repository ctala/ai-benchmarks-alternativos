# Claude Opus 5 Fast — strategy/pricing_strategy

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 4.35 | quality: 5.0
- latency_total: 36.448s | tokens_per_second: 224.8
- input_tokens: 288 | output_tokens: 8192

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

# Análisis de pricing: $60 → $89

## 0. Primero, una corrección metodológica

Tu LTV está calculado sobre **ingreso**, no sobre **margen bruto**. Es el error más común y distorsiona todas las decisiones río abajo.

| Métrica | Tu cálculo | Cálculo correcto |
|---|---|---|
| Vida promedio | 14 meses (1/0.07 = 14.3) ✓ | 14.3 meses |
| LTV | $840 (ingreso) | **$743** (margen: $52 × 14.3) |
| LTV/CAC | 7.0x | **6.2x** |
| CAC payback | — | **2.3 meses** |

---

## 1. LTV/CAC actual vs. proyectado

**Situación actual: 6.2x con payback de 2.3 meses.**

Esto no es "buena salud", es una **señal de alarma de subprecio**. El benchmark sano es 3:1 con payback de 6–12 meses. Un 6.2x significa una de dos cosas (normalmente ambas):

1. Estás dejando dinero sobre la mesa en precio
2. Estás subinvirtiendo en adquisición

**Proyección a $89** (clientes nuevos, churn constante 7%):

| | Hoy ($60) | A $89 |
|---|---|---|
| Margen bruto/mes | $52 (86.7%) | $81 (91.0%) |
| LTV (margen) | $743 | **$1,157** |
| CAC (asumiendo +25% por menor conversión) | $120 | $150 |
| **LTV/CAC** | 6.2x | **7.7x** |
| CAC payback | 2.3 meses | 1.9 meses |

**El dato que decide el debate:** tu CAC podría subir hasta **$386** y aún tendrías un ratio 3:1 sano. Tienes un colchón de 3.2x. El riesgo de precio aquí es estructuralmente bajo.

---

## 2. Impacto esperado en churn

Benchmarks relevantes (ProfitWell/Paddle, Price Intelligently, OpenView SaaS Benchmarks):

| Magnitud del aumento | Churn incremental típico |
|---|---|
| <10% | Prácticamente nulo (0–1pp) |
| 10–25% | 1–3pp, transitorio |
| **25–50%** | **8–15% de cancelación única + 0.5–1.5pp sostenido** |
| >50% | Alto riesgo, requiere reposicionamiento |

Tu aumento es de **+48.3%**: estás en el límite superior de la banda "manejable".

**Tres matices importantes:**

- **Churn adelantado ≠ churn incremental.** Con 7% mensual, ~14% de tu base se iría en los próximos 2 meses de todas formas. Una parte de las cancelaciones post-aumento son personas que ya estaban de salida. El daño real es menor que el titular.
- **Cohortes nuevas suelen mejorar.** Precio más alto filtra compradores por precio y atrae clientes con más presupuesto y más intención. No es raro ver churn 1–2pp *mejor* en cohortes post-aumento.
- **Tu 7% es el verdadero problema.** 7% mensual = **58% de churn anual**. El benchmark SMB es 3–5% mensual. Volveré a esto en la recomendación.

---

## 3. Tres escenarios (base existente de 200 clientes, 12 meses)

**Baseline sin cambios:** $12,000 MRR → 84 clientes en mes 12 → **$92,692 ingreso acumulado / $80,332 margen bruto**

| | **Optimista** | **Realista** | **Pesimista** |
|---|---|---|---|
| Cancelación inmediata | 5% (10 clientes) | 12% (24) | 20% (40) |
| Base restante | 190 | 176 | 160 |
| Churn sostenido | 7% | 8% | 9.5% |
| **MRR día 1** | $16,910 (+41%) | $15,664 (+31%) | $14,240 (+19%) |
| Clientes mes 12 | 80 | 65 | 48 |
| Ingreso 12m | $130,616 | $113,911 | $94,712 |
| Margen bruto 12m | $118,876 | $103,672 | $86,200 |
| **vs. baseline (MB)** | **+48%** | **+29%** | **+7%** |
| Probabilidad estimada | 25% | 50% | 25% |

**Valor esperado ponderado: $113,288 de ingreso (+22% vs. baseline).**

### El número que realmente importa

$60 / $89 = **0.674**

Puedes perder **32.6% de tu base el día uno** y seguir con el mismo MRR. En margen bruto ($52/$81), el punto de equilibrio es **35.8%**.

Ni siquiera tu escenario pesimista (20%) se acerca al breakeven. **La asimetría está brutalmente a tu favor.** El escenario realista de "esto sale mal" sigue siendo positivo.

---

## 4. Recomendación

**Sube el precio. Pero no de la forma que estás planteando.**

### 4.1 No hagas un precio único plano — pasa a tres tiers

Con competidores entre $29 y $149, un solo punto de precio te deja capturar mal el valor en ambos extremos. Estructura sugerida:

| Tier | Precio | Función |
|---|---|---|
| **Starter** | $39/mes | Defensa contra el competidor de $29. Destino de downgrade (retención en vez de cancelación) |
| **Pro** | $89/mes | Tier ancla. Aquí va el 60–70% |
| **Business** | $169/mes | Multi-almacén, API, usuarios ilimitados, soporte prioritario. Captura tu 15% superior |

Un tier alto suele añadir 8–15% de ingreso solo por autoselección — de clientes que ya habrían pagado más. Y el Starter convierte cancelaciones en downgrades, que es la diferencia entre $0 y $39.

### 4.2 Clientes nuevos: inmediato, y prueba $99

Cambio de precio hoy en el sitio. El costo de probar $99 vs. $89 durante 6 semanas es cero — divide el tráfico y mide conversión trial→pago. Con payback de 1.9 meses, sobre-optimizar a la baja es más caro que equivocarse hacia arriba.

**Métrica única a vigilar:** conversión trial→pago. Es tu indicador adelantado de si el mercado acepta $89.

### 4.3 Base existente: migración con tarifa de lealtad

Mi recomendación es **no** llevar la base existente a $89 directo. Lleva a **$79 con framing de "tarifa de lealtad permanente"** (11% off del precio público).

Modelado del híbrido:

| | Híbrido ($79 lealtad) | Migración completa ($89) |
|---|---|---|
| Cancelación inmediata | ~7% | ~12% |
| MRR día 1 | $14,694 (+22%) | $15,664 (+31%) |
| Ingreso 12m | $110,118 | $113,911 |
| Margen bruto 12m | $98,967 | $103,672 |
| Varianza / riesgo | Baja | Media |

Capturas **97% del valor con la mitad del riesgo** y una fracción de la carga de soporte. Además el descuento te da una razón concreta para pedir algo a cambio: el plan anual.

### 4.4 Empuja el plan anual con fuerza

Anual a **$890/año** (2 meses gratis). Con 7% de churn mensual, cada conversión a anual:
- Bloquea 12 meses de ingreso que estadísticamente no tendrías (vida esperada: 14 meses, pero con alta varianza)
- Adelanta caja para financiar adquisición
- Saca a ese cliente de la ecuación de churn mensual

Si el 30% de la base convierte, son ~$50K de caja adelantada.

### 4.5 El elefante en la sala: tu churn

Con $89 y 7% de churn, tu LTV es $1,157. Con $89 y **5%** de churn: **$1,620** (+40%).

El aumento de precio te da +29% de margen bruto. Bajar el churn de 7% a 5% te da +40% — y es acumulativo con el precio. **Después de ejecutar el pricing, el churn es tu prioridad #1 absoluta.** 58% de churn anual significa que reconstruyes tu base entera cada 17 meses solo para quedarte en el mismo sitio.

---

## 5. Plan de implementación

**Semanas 1–2 — Preparación**
- Segmenta los 200 clientes por uso real (logins, SKUs gestionados, transacciones). Vas a encontrar tres grupos: power users que pagarían $150, usuarios medios, y ~15–20% de zombies casi inactivos que se van a ir con cualquier excusa. No pelees por los zombies.
- 10–15 llamadas de 20 minutos con clientes activos. No preguntes "¿pagarías $89?" — pregunta qué alternativa evaluaron, qué les costaría el proceso manual, cuánto tiempo ahorran.
- Define tu criterio de aborto **por escrito y antes de lanzar**.

**Semanas 3–4 — Entrega de valor**
Envía 1–2 mejoras visibles antes o junto al anuncio. Nunca subas precio sobre un producto estático — es la diferencia entre "invirtieron en el producto" y "se pusieron codiciosos".

**Semana 5 — Anuncio (aviso de 60–90 días)**
- Email del fundador, no de "el equipo". Directo, sin disculpas, sin párrafos de relleno.
- Estructura: qué hemos construido → nuevo precio $89 → **tu tarifa de lealtad es $79, permanente** → fecha efectiva → opción anual a $790 (aplicando tu tarifa) → responde a este correo si tienes dudas.
- Ten listas las ofertas de retención antes de enviar: downgrade a Starter, anual con descuento, 3 meses de extensión para cuentas en riesgo.

**Semanas 6–13 — Ejecución**
- Todos los emails de cancelación responde tú personalmente los primeros 30 días. Es la mejor investigación de mercado que vas a hacer.
- Dashboard diario: solicitudes de cancelación, downgrades, conversiones a anual, trial→pago.

**Mes 4+ — Reinversión**
Con payback de 1.9 meses