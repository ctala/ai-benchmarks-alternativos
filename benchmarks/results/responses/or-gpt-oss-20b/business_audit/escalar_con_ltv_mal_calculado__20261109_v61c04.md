# GPT-OSS 20B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.3 | quality: 10.0
- latency_total: 12.475s | tokens_per_second: 132.6
- input_tokens: 250 | output_tokens: 1654

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de unit economics. Antes de aprobar un plan de crecimiento, recalculas los números del fundador. Muchos planes mueren en la aritmética.

**user:**

Ya soy rentable y quiero escalar fuerte con publicidad pagada. Mis números:

- Precio: $35/mes por cliente.
- Churn mensual: 8%.
- Margen bruto: 70% (después de infraestructura y procesador de pagos).
- Mi costo de adquirir un cliente con publicidad (CAC): $290.

Mi cálculo: como un cliente se queda unos 2 años, el LTV es 35 × 24 = $840. Contra un CAC de $290, eso me da LTV/CAC = 2,9, que está por encima de 3 más o menos. Así que voy a meter $10.000 en publicidad este mes.

¿Le doy?


## Respuesta completa

## 1️⃣ La aritmética del “cliente de 2 años” está mal

- **Churn mensual = 8 %** → el cliente promedio se queda **1 / 0.08 ≈ 12.5 meses** (1 año y 3 meses), no 24 meses.  
  - Si quieres usar 24 meses, necesitas un churn de ~4 % mensual, lo cual no es tu caso.

## 2️⃣ ¿Cómo calcular el LTV real?

```
LTV = (Precio mensual × Margen bruto) × Duración media
```

- Precio mensual: **$35**  
- Margen bruto: **70 %** → Pago mensual neto = 35 × 0.70 = **$24.50**  
- Duración media (por churn 8 %): **12.5 meses**

```
LTV = 24.50 × 12.5 = $306.25
```

> **Tu LTV es ≈ $300, no $840.**

## 3️⃣ ¿Qué dice el ratio LTV/CAC?

- **LTV/CAC = $306.25 / $290 ≈ 1.06**  

Con un margen bruto del 70 %, el *break‑even* ratio es:

```
Break‑even ratio = 1 / (1 – margen bruto)
                 = 1 / (1 – 0.70)
                 = 3.33
```

Para que el negocio sea rentable, necesitas LTV/CAC ≥ 3.33.  
Con tu CAC de $290, el LTV debe ser al menos:

```
LTV ≥ 3.33 × 290 ≈ $966
```

Pero tu LTV real es $306.25 → **no alcanzas el objetivo**.

## 4️⃣ Otras métricas que te alertan

- **Payback period (tiempo de recuperación de CAC)**  
  ```
  Payback = CAC / (Margen mensual)
          = 290 / 24.50 ≈ 11.8 meses
  ```
  El CAC se recupera en 12 meses, justo cuando el cliente está a punto de irse (12.5 meses). No hay margen de seguridad.

- **Retención**: con 8 % de churn, perderás casi la mitad de tus clientes cada año.  
- **Escalabilidad**: cada dólar invertido en publicidad te queda con apenas 1 $ de margen neto.

## 5️⃣ ¿Qué debes hacer antes de gastar $10 000?

| Objetivo | Acciones concretas |
|----------|--------------------|
| **Reducir CAC** | 1. Optimiza el funnel de ventas (landing pages, copy, retargeting). <br>2. Usa canales con mejor ROAS (ej. email, SEO, partners). <br>3. Prueba A/B de creatividades y audiencias. |
| **Aumentar margen** | 1. Negocia tarifas de procesamiento de pagos. <br>2. Ofrece un plan premium con precios más altos. |
| **Disminuir churn** | 1. Implementa un programa de onboarding y soporte. <br>2. Crea contenido de valor que mantenga a los usuarios activos. <br>3. Analiza la razón de abandono y actúa. |
| **Revisar el pricing** | 1. Si el margen es bajo, evalúa un incremento de precio de $35 a $45‑$50. |
| **Cálculo real de LTV** | Usa cohortes reales (mes a mes) para medir LTV en lugar de suposiciones. |

> **Escala solo cuando**:  
> 1. LTV ≥ 3.33 × CAC (o LTV/CAC ≥ 3.33).  
> 2. Payback period ≤ 70 % de la duración media (idealmente < 6 meses).  
> 3. Margen neto mensual > $30 (para cubrir costos fijos y amortizar inversiones).

## 6️⃣ Resumen rápido

| Métrica | Valor actual | Necesario |
|---------|--------------|-----------|
| LTV | $306 | ≥ $966 |
| CAC | $290 | ≤ $92 |
| LTV/CAC | 1.06 | ≥ 3.33 |
| Payback | 11.8 meses | ≤ 8 meses |

### Decisión

**No** – Con los números actuales, gastar $10 000 en publicidad sería una inversión que casi se vuelve un gasto. Necesitas reducir CAC a menos de $92 o + un margen bruto más alto/menos churn antes de escalar.  

---

**Próximo paso**: revisa tu funnel y cohortes, reduce CAC, y recalcula LTV con los datos nuevos. Cuando el ratio LTV/CAC alcance 3.33+ y el payback sea razonable, entonces sí puedes considerar la inversión de $10 000.