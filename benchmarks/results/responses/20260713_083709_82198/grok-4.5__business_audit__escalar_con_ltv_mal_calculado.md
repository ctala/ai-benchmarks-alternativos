# Grok 4.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `x-ai/grok-4.5`
- success: True  | final: 7.33 | quality: 8.4
- latency_total: 17.742s | tokens_per_second: 77.0
- input_tokens: 394 | output_tokens: 1367

## Respuesta completa

**No. No le des. El plan muere en la aritmética.**

### Errores del fundador
1. **Lifetime incorrecto**: con churn mensual del 8 %, el lifetime medio no es ~24 meses.  
   Lifetime (meses) = 1 / churn = 1 / 0,08 = **12,5 meses**.

2. **LTV sin margen bruto**: el LTV relevante es el de contribución (gross margin), no el de revenue bruto.  
   Si no descontás el 30 % de costos variables (infra + pagos), estás contando dinero que no te quedás.

### Cálculo correcto de unit economics
- ARPU mensual = $35  
- Contribución mensual por cliente = 35 × 0,70 = **$24,50**  
- LTV = contribución mensual / churn = 24,50 / 0,08 = **$306,25**  
- CAC = **$290**  
- **LTV / CAC ≈ 1,06**

Eso está muy por debajo del umbral sano (normalmente se busca ≥ 3× en SaaS para absorber overhead, riesgo, capital y varianza). Con LTV/CAC ≈ 1 estás básicamente recuperando el CAC y poco más; no hay margen de error ni profit real unitario.

### Payback y riesgo adicional
- Meses de payback = CAC / contribución mensual = 290 / 24,50 ≈ **11,8 meses**.  
  Con 8 % de churn mensual, una fracción importante de los clientes se va **antes** de que recuperes el CAC. El valor esperado apenas cubre, pero la cola de churn y la varianza te comen.

Meter $10.000 este mes ≈ 34 clientes adquiridos. A $306 de LTV esperado vs $290 de CAC, el valor esperado neto es casi cero (o ligeramente positivo/negativo según redondeos y costes no capturados). No es “escalar fuerte”; es quemar cash para crecer un P&L que no genera unit economics atractivos.

### Qué tendrías que ver para aprobar
- LTV/CAC realista ≥ 3 (idealmente con margen de seguridad).  
- Payback ≤ 6-9 meses (o justificado con muy alto LTV y baja churn).  
- Validación de que el CAC de $290 se mantiene a escala y que el 70 % de margen bruto es real (sin costes de soporte, onboarding, etc. escondidos).  
- Mejoras previas: bajar churn (el 8 % mensual es alto para un LTV decente a $35), subir precio/ARPU, o bajar CAC drásticamente.

**Conclusión**: con estos números no apruebo el gasto de $10k en paid. Primero arreglá lifetime, margen o CAC. La aritmética no miente: LTV ≈ $306 vs CAC $290 no da para escalar. Recalculá y volvé.