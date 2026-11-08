# Qwen 3.8 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.47 | quality: 10.0
- latency_total: 238.685s | tokens_per_second: 69.6
- input_tokens: 255 | output_tokens: 16608

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

No. **No le doy al plan de $10.000 en publicidad con estos números como plan de escalamiento fuerte.**  
Tu aritmética actual no muestra un negocio listo para escalar; muestra un negocio **apenas rentable por cliente**, con riesgo alto de volverse negativo si CAC, churn, soporte, reembolsos o impuestos se desvían un poco.

---

## 1. Tu cálculo tiene dos errores grandes

Tú calculaste:

> LTV = $35 × 24 meses = $840  
> LTV/CAC = $840 / $290 = 2,9

Problema 1: **$840 es LTV de ingresos, no LTV bruto.**  
Para comparar contra CAC, necesitas usar margen bruto, no facturación bruta.

Problema 2: **con 8% de churn mensual, un cliente promedio no dura 24 meses.**  
Dura alrededor de:

> Vida esperada = 1 / churn mensual = 1 / 0,08 = **12,5 meses**

Para que un cliente promedio dure 24 meses, el churn mensual debería ser aproximadamente:

> 1 / 24 = **4,2% mensual**

Además, con 8% de churn mensual, solo quedan:

- Mes 12: 0,92¹² ≈ **36,8%** de clientes
- Mes 24: 0,92²⁴ ≈ **13,5%** de clientes

---

## 2. Recálculo correcto

### Margen bruto mensual por cliente

> $35 × 70% = **$24,50 de margen bruto mensual**

### LTV bruto con churn 8% mensual

> LTV bruto = $24,50 / 0,08 = **$306,25**

### LTV/CAC correcto

> LTV/CAC = $306,25 / $290 = **1,06**

No es 2,9. Es **1,06**.

Y 1,06 está muy lejos del benchmark saludable de **3× o más** para escalar con publicidad pagada.

### Aporte neto por cliente

> $306,25 - $290 = **$16,25 por cliente**

Eso significa que, después de pagar el CAC, cada cliente promedio te deja **apenas $16,25 de margen bruto lifetime**.

Con ese margen tan fino, cualquier desvío te mata:

- CAC sube 10% → pierdes dinero.
- Churn sube a 9% → pierdes dinero.
- Soporte, reembolsos, ventas, herramientas, impuestos o fallas de pago entran en la cuenta → pierdes dinero.

---

## 3. Qué pasa si metes $10.000 este mes

Con CAC de $290:

> Clientes esperados = $10.000 / $290 ≈ **34,5 clientes**

### Ingresos del nuevo cohort en el primer mes

> 34,5 × $35 = **$1.207,50 de ingreso mensual**

### Margen bruto del nuevo cohort en el primer mes

> 34,5 × $24,50 = **$845,25 de margen bruto mensual**

Es decir: gastas $10.000 hoy y ese cohort te devuelve **$845 de margen bruto en el primer mes**.

### Lifetime bruto esperado del cohort

> 34,5 × $306,25 ≈ **$10.560 de margen bruto lifetime**

Neto lifetime:

> $10.560 - $10.000 = **+$560**

ROI lifetime sobre ad spend:

> $560 / $10.000 = **5,6%**

Eso es casi break-even. No es un motor de crecimiento.

### Si miras solo 24 meses

Con churn 8%, el margen bruto lifetime a 24 meses no es $306,25 por cliente, sino:

> $24,50 × (1 - 0,92²⁴) / 0,08 ≈ **$264,84 por cliente**

Para el cohort de $10.000:

> 34,5 × $264,84 ≈ **$9.130 de margen bruto a 24 meses**

Neto a 24 meses:

> $9.130 - $10.000 = **-$870**

Si tu horizonte de evaluación es 24 meses, **el plan es negativo**.

---

## 4. Payback: parece bueno, pero no es tan bueno

Si ignoras churn:

> Payback = CAC / margen bruto mensual = $290 / $24,50 = **11,8 meses**

Parece razonable.

Pero con churn 8%, la vida esperada del cliente es **12,5 meses**. Es decir:

> El payback consume casi toda la vida esperada del cliente.

Además, un cliente que cancela antes de 12 meses no recupera el CAC:

- 11 meses × $24,50 = $269,50 → no cubre $290
- 12 meses × $24,50 = $294,00 → apenas cubre $290

Con churn 8% mensual, solo alrededor del **37% de los clientes llega a 12 meses**.

---

## 5. Sensibilidad: el plan es frágil

Con tus números actuales:

| Escenario | LTV bruto | LTV/CAC | Lectura |
|---|---:|---:|---|
| Actual: CAC $290, churn 8%, precio $35, margen 70% | $306,25 | **1,06** | No escalable |
| CAC sube a $320 | $306,25 | **0,96** | Pierdes dinero |
| Churn sube a 9% | $272,22 | **0,94** | Pierdes dinero |
| CAC baja a $200 | $306,25 | **1,53** | Débil |
| CAC baja a $150 | $306,25 | **2,04** | Aceptable, pero no fuerte |
| CAC baja a $100 | $306,25 | **3,06** | Escalable |
| Churn baja a 5% | $490,00 | **1,69** | Débil |
| Churn baja a 3% | $816,67 | **2,82** | Casi saludable |
| Churn baja a 2% | $1.225,00 | **4,22** | Muy bueno |
| Precio sube a $75 | $656,25 | **2,26** | Aceptable |
| Precio sube a $100 | $875,00 | **3,02** | Escalable |

---

## 6. Qué necesitas para decir “sí”

Para que el plan sea fuerte, necesitas uno de estos ajustes, o una combinación:

### Si mantienes churn 8% y margen 70%

| Objetivo | CAC necesario | Churn necesario | Precio necesario |
|---|---:|---:|---:|
| LTV/CAC = 2× | ≤ $153 | ≤ 4,2% | ≥ $66 |
| LTV/CAC = 3× | ≤ $102 | ≤ 2,8% | ≥ $99 |

Es decir: con tus números actuales, para llegar a un LTV/CAC de 3× necesitas:

- Bajar CAC de $290 a alrededor de **$100**, o
- Bajar churn de 8% a alrededor de **2,8%**, o
- Subir precio de $35 a alrededor de **$99** con el mismo margen.

---

## 7. Veredicto

**No le doy al plan de $10.000 como crecimiento fuerte.**

Tu LTV/CAC real, con margen bruto y churn, es:

> **1,06**

Eso no es un negocio escalable con paid ads. Es un negocio que apenas sobrevive a la adquisición pagada.

Sí podrías darle luz verde a un **test controlado**, por ejemplo $1.000–$2.000, para validar cohortes reales, CAC estable, churn por mes, reembolsos, soporte y conversión. Pero no como plan de escalamiento.

Para escalar fuerte, primero necesitas:

1. **Bajar CAC real**, incluyendo marketing, ventas, onboarding, soporte, reembolsos y fallas de pago.
2. **Bajar churn** o vender planes anuales/compromisos más largos.
3. **Subir precio**, margen o añadir expansión de ingresos.
4. **Confirmar que el LTV bruto / CAC sea ≥ 2,5–3×** con datos de cohortes, no con promedio simple.
5. **Payback ≤ 12 meses**, idealmente menor, con margen de error.

Con los números actuales, el plan no muere por falta de ambición. Muere por esta línea:

> **$306,25 de LTV bruto contra $290 de CAC = $16,25 de margen por cliente.**

Eso no es crecimiento. Es una apuesta frágil.