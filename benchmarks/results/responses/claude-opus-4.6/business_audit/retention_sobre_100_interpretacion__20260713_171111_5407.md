# Claude Opus 4.6 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-opus-4-6`
- success: True  | final: 8.07 | quality: 10.0
- latency_total: 28.107s | tokens_per_second: 39.0
- input_tokens: 170 | output_tokens: 1095
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una interpretación completa y práctica de las métricas de retención de ingresos y clientes.

## Respuesta completa

# No. Tu lectura es incorrecta en un punto crítico.

Tienes que separar dos métricas que tu panel está mezclando en tu cabeza:

---

## Lo que dice el 114%: Retención de Ingresos Neta (NRR)

Esto mide **dinero**, no clientes. Significa que los clientes que ya tenías el mes pasado **hoy generan un 14% más de ingresos** gracias a expansiones (upgrades, upsells, etc.).

Pero ese 114% es un **número neto**: las expansiones están **enmascarando** las pérdidas por churn.

### Ejemplo con tus números

Supongamos que el mes pasado facturabas $10,000 entre 40 clientes:

| Concepto | Impacto |
|---|---|
| Ingresos iniciales (40 clientes) | $10,000 |
| Perdidos por los 4 clientes que se fueron | −$1,000 |
| Ganados por upgrades de los que se quedaron | +$2,400 |
| **Ingresos de la cohorte original** | **$11,400** |
| **NRR** | **114%** |

El 114% es real, pero **esconde una pérdida real dentro**.

---

## Lo que NO dice el 114%: Retención de Clientes (Logo Retention)

Esta es la métrica que estás ignorando:

$$\frac{36}{40} = 90\%$$

**Perdiste el 10% de tus clientes en un solo mes.**

Si eso se anualiza:

$$1 - (0.90)^{12} ≈ 72\%\ \text{de churn anual}$$

Eso es **alarmante**. Significa que a lo largo de un año, al ritmo actual, perderías casi 3 de cada 4 clientes.

---

## Por qué tu conclusión es peligrosa

Tu razonamiento de "dejo de preocuparme por el churn y meto todo en adquisición" tiene tres problemas graves:

**1. Dependencia frágil de pocos clientes**
Hoy tu ingreso crece porque unos pocos clientes suben de plan. Si uno o dos de esos "expansores" se van el mes que viene, tu NRR se desploma y **no tienes colchón** porque la base se ha reducido.

**2. El churn compone igual que el crecimiento**
Perder 4 clientes de 40 no parece grave. Perder 4 de 36 el mes siguiente ya es un 11%. La base se encoge y cada baja pesa más. Es una espiral.

**3. Adquirir sobre una base con fugas es llenar un balde roto**
Si tu CAC es, digamos, $500 por cliente y pierdes 10% mensual, necesitas adquirir constantemente solo para mantenerte. Cada euro en adquisición rinde menos.

---

## Lo que deberías hacer

```
NO:  "NRR > 100% → el churn no importa → todo a adquisición"

SÍ:  Tratar ambas métricas como complementarias:
     ┌─────────────────────────────────────┐
     │  NRR 114%  →  Buena señal: sabes    │
     │               monetizar tu base      │
     │                                      │
     │  Logo Retention 90%/mes → Alarma:    │
     │               tu base se encoge      │
     └─────────────────────────────────────┘
```

**Prioridad inmediata:** Entender por qué se fueron esos 4 clientes. ¿Perfil equivocado? ¿Onboarding débil? ¿Falta de valor en el plan base?

**Prioridad paralela:** Sí, sigue captando, pero sabiendo que la adquisición no compensa un problema de retención de logos; solo lo aplaza.

---

### En una frase

> Un NRR del 114% con una retención de logos del 90% mensual significa que **eres muy bueno extrayendo valor de quien se queda, pero muy malo reteniendo a quien llega**. Si no corriges lo segundo, lo primero dejará de salvarte.