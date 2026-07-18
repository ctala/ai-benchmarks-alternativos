# Kimi K3 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.89 | quality: 10.0
- latency_total: 148.214s | tokens_per_second: 31.7
- input_tokens: 315 | output_tokens: 4693
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y consejos prácticos para un emprendedor.

## Respuesta completa

**No le des.** El plan muere en la aritmética: tienes dos errores que se multiplican entre sí.

## Error 1: La vida del cliente no es 24 meses

Con churn mensual del 8%, la vida esperada es:

**1 / 0,08 = 12,5 meses** (no 24)

24 meses de vida implicaría un churn de ~4,2%. Tu intuición ("se queda unos 2 años") contradice tu propio dato de churn — uno de los dos está mal, y conviene revisar cuál antes de gastar un peso.

## Error 2: El LTV se calcula sobre margen, no sobre ingreso

El CAC se paga completo; lo que recuperas es el margen bruto. Entonces:

**LTV = $35 × 0,70 × 12,5 = $306**

Contra un CAC de $290:

**LTV/CAC real = 1,06** — no 2,9.

Tu 2,9 solo existe usando revenue en vez de margen *y* duplicando la vida del cliente. Incluso regalándote los 24 meses, el LTV corregido sería $840 × 0,70 = $588 → ratio 2,0. Nunca llega a 3.

## Qué tan fino es el margen de seguridad

| Escenario | Resultado |
|---|---|
| Churn sube de 8% a 8,5% | LTV $288 < CAC $290 → **pierdes dinero** |
| CAC sube 6% al escalar (típico) | CAC $307 > LTV $306 → **pierdes dinero** |
| Con costo de capital 12% anual | VAN del LTV ≈ $275 < $290 → **destruyes valor** |

Tu churn de break-even es **8,45%**. Estás a 0,45 puntos porcentuales de perder plata en cada cliente. Y ojo: el CAC de $290 medido a bajo volumen casi siempre se degrada al escalar — los primeros dólares capturan la audiencia más barata.

## Qué hacen los $10.000 en la práctica

- Compran ~34 clientes.
- Mes 1 recuperas ~$845 de margen, decayendo 8% mensual.
- **Payback: ~35 meses** — casi 3 años, cuando el cliente promedio vive 12,5.
- La mitad de esos clientes cancela antes del mes 9, habiendo aportado menos de $150 contra los $290 que pagaste por ellos.

Tu rentabilidad actual viene de clientes adquiridos sin CAC pagado. Estos cohorts pagados la diluyen durante años.

## Qué tiene que ser verdad para aprobar esto

Para un ratio de 3x con estos números necesitas **una** de estas:

- **Churn ≤ 2,8% mensual** → LTV $875 → ratio 3,0
- **CAC ≤ ~$100** → con tu LTV actual de $306

Las dos apuntan al mismo diagnóstico: **tu problema es retención, no adquisición**. Un 8% mensual significa reemplazar el 62% de tu base cada año. Estás intentando llenar más rápido un balde con un agujero grande.

**Mi recomendación:**
1. No escalar paid ahora. Los $10k van a retención (onboarding, éxito de cliente, producto).
2. Mientras tanto, test acotado de $1–2k con CAC *fully loaded* (incluye creativos, agencia, descuentos) y tracking por cohorte, con techo de CAC.
3. Evalúa plan anual prepago: cambia radicalmente la caja y corta el churn de facto.
4. Verifica que tu margen del 70% incluya soporte — si escala con clientes, tu margen real de contribución es menor y el ratio empeora.

Cuando el churn baje de 4%, vuelve con los números y reabrimos la conversación.