# Nemotron 3 Ultra 550B — business_audit/retention_sobre_100_interpretacion

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 4.94 | quality: 4.8
- latency_total: 22.783s | tokens_per_second: 40.4
- input_tokens: 147 | output_tokens: 921

## Respuesta completa

**Incorrecto en ambos supuestos.** Y la decisión de «dejar de preocuparte por el churn» basada en ese 114 % es peligrosa.

---

### Qué te dice realmente ese 114 %

| Métrica | Fórmula (simplificada) | Tu caso |
|---------|------------------------|---------|
| **Net Revenue Retention (NRR)** | `(MRR inicio − downgrades − churn + expansion) / MRR inicio` | **114 %** → el *cohort* de clientes que tenías al inicio del mes vale ahora un 14 % más en MRR. |
| **Gross Revenue Retention (GRR)** | `(MRR inicio − downgrades − churn) / MRR inicio` | **< 100 %** (seguro), porque perdiste 4 logos y sus planes base. |
| **Logo / Customer Retention** | `Clientes fin de mes / Clientes inicio de mes` | **36 / 40 = 90 %** → **10 % de logo churn mensual**. |

**Tu NRR 114 % nace de que la *expansión* (upsells) supera al *churn + downgrades* en euros, no de que no se vaya nadie.**

---

### Por qué no puedes ignorar el churn

1. **Fuga de logos = 10 %/mes → ~70 % anual.**  
   Aunque los que se quedan paguen más, estás rellenando un balde con un agujero grande. Cada cliente nuevo cuesta CAC; perder 4 al mes te obliga a adquirir > 4 solo para mantener la base.

2. **Concentración de riesgo.**  
   El crecimiento depende de que *los mismos* clientes sigan subiendo de plan. Si se saturan o cambia el mercado, el NRR colapsa y no tienes base de clientes para amortiguar.

3. **Señal de producto/mercado.**  
   10 % de logo churn mensual en B2B SaaS suele indicar: onboarding débil, expectativas mal alineadas, falta de *stickiness* o competencia agresiva. Es un síntoma, no un ruido.

4. **Unit economics.**  
   LTV se calcula con *gross* churn, no net. Si modelas LTV con NRR 114 % inflarás el valor del cliente y podrás permitirte CAC insostenibles.

---

### Qué deberías hacer **ya**

| Acción | Por qué |
|--------|---------|
| **Separa NRR y GRR en el dashboard** | Verás el 114 % (bonito) y el ~85-90 % GRR (realidad de fuga de ingresos base). |
| **Trackea Logo Churn y su cohorte** | ¿Se van los nuevos? ¿Los antiguos? ¿Por plan? |
| **Entrevista a los 4 que se fueron** | Razones reales > especulaciones. |
| **Fija un objetivo de GRR ≥ 90 % mensual (≈ 70 % anual)** | Antes de escalar adquisición, tapa la fuga. |
| **Modela CAC Payback con GRR, no NRR** | Evita sobrestimar cuánto puedes pagar por cliente. |

---

### En una frase
**NRR 114 % significa que *exprimir* a los que quedan compensa *perder* a los que se van; no significa que no se vaya nadie.**  
Si dejas de arreglar el 10 % de logo churn, tu crecimiento será una carrera en cinta: corres más (adquisición) para quedarte en el mismo sitio.