# KAT Coder Pro v2.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `kwaipilot/kat-coder-pro-v2.5`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 21.167s | tokens_per_second: 96.8
- input_tokens: 217 | output_tokens: 2048

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



**No le des luz verde.** Tu cálculo del LTV tiene un error crítico que infla el ratio LTV/CAC de 1,06 a 2,9. Escalar con esos números quemaría caja rápidamente.

### 🔍 Dónde está el error

Calculaste el LTV como `$35 × 24 meses = $840`, asumiendo que todos los clientes se quedan exactamente 2 años. Pero con un **churn del 8% mensual**, la vida media de un cliente es de solo **12,5 meses** (1 / 0,08), y al cabo de 24 meses solo queda el ~13% de los clientes originales.

La fórmula correcta para LTV (con margen bruto) es:

**LTV = (ARPU × Margen Bruto) / Churn mensual**  
= ($35 × 0,70) / 0,08  
= $24,50 / 0,08  
= **$306,25**

### 📊 Los números reales

| Métrica | Tu cálculo | Cálculo correcto |
|---------|------------|------------------|
| LTV (con margen) | $840 | **$306** |
| LTV/CAC | 2,9 | **1,06** |
| Payback period | ~12 meses | **11,8 meses** |
| Vida media del cliente | 24 meses | **12,5 meses** |

Con un **LTV/CAC de 1,06**, cada cliente apenas recupera su costo de adquisición, sin dejar margen para cubrir costos fijos (equipo, oficinas, etc.). Estarías creciendo por crecer, no por rentabilidad.

### ⚠️ Banderas rojas adicionales

1. **Churn del 8% mensual** es muy alto para un producto de $35/mes (equivale a ~63% anual). Sugiere problemas de retención o de ajuste producto-mercado.
2. **CAC de $290** es excesivo para un ticket mensual de $35. Lo habitual en SaaS B2C/B2B pequeño es que el CAC se recupere en ≤12 meses; aquí estás en el límite, pero con un LTV tan bajo, el riesgo es alto.
3. **Payback de ~12 meses**: tardas un año en recuperar la inversión de adquisición. Si escalas con $10.000/mes, necesitarás un colchón de caja importante para aguantar hasta que los clientes paguen su CAC.

### 🛑 Recomendación

**No inviertas los $10.000 en publicidad pagada todavía.** Primero mejora los unit economics:

- **Reduce el churn**: Investiga por qué se van los clientes. Un churn del 5% mensual ya subiría el LTV a $490 (LTV/CAC = 1,7). Con un 3%, el LTV sería $817 (LTV/CAC = 2,8).
- **Baja el CAC**: Prueba canales más baratos (content, referidos, partnerships) antes de pagar $290 por cliente.
- **Sube el precio o el margen**: Un aumento del 20% en el precio ($42/mes) mejoraría significativamente el LTV.
- **Valida el churn real**: Asegúrate de que el 8% sea correcto; a veces los fundadores subestiman el churn neto (bajas + downgrades).

### ✅ Cuándo sí escalar

Cuando logres un **LTV/CAC ≥ 3** y un **payback ≤ 6 meses**, la publicidad pagada será un motor de crecimiento sostenible. Hasta entonces, enfócate en retención y eficiencia de adquisición.