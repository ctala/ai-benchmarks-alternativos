# KAT Coder Air v2.5 — business_audit/churn_mezcla_free_y_pago

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 9.1 | quality: 10.0
- latency_total: 8.415s | tokens_per_second: 193.9
- input_tokens: 189 | output_tokens: 1632

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de retención. Antes de interpretar una métrica, verificas qué población está midiendo realmente.

**user:**

Estoy en pánico. Mi plataforma reporta un churn del 31% este mes y pensé que estaba en 5%. ¿Qué hago?

Datos que me da el panel:
- Usuarios totales que se dieron de baja este mes: 62
- Usuarios totales a inicio de mes: 200
- Churn reportado: 31%

Detalle que encontré exportando la tabla:
- De los 200 usuarios, 178 están en el plan gratuito y 22 son de pago.
- De las 62 bajas, 60 eran del plan gratuito y 2 eran de pago.

¿Qué tan grave es? Dame un plan.


## Respuesta completa



# Análisis de Retención: Churn del 31%

## 🔍 Diagnóstico Rápido

**El churn del 31% es engañoso.** No estás en crisis, pero tienes un problema de segmentación que tu panel no muestra.

| Métrica | Valor | Interpretación |
|---------|-------|----------------|
| Churn general | 31% | **Distorsionado** por plan gratuito |
| Churn gratuito | 60/178 = **33.7%** | Alto, pero esperado en freemium |
| Churn de pago | 2/22 = **9.1%** | **Este es el número real a vigilar** |

## 🚨 Qué tan grave es

**No es una emergencia de ingresos**, pero sí una alerta de estructura:

1. **El churn de pago (9.1%) es preocupante** si tu benchmark de industria es <5%. En SaaS B2B es alto; en B2C puede ser normal.
2. **El churn gratuito (33.7%) es ruido estadístico** si tu modelo es freemium. Usuarios que no pagan y no usan son normales que se vayan.
3. **El riesgo real**: Si el churn de pago sigue así, pierdes ingresos recurrentes. 2 usuarios de pago menos = 2/22 = 9.1% de tu base pagante desaparecida.

## 📋 Plan de Acción Inmediato

### Semana 1: Entender las causas
- [ ] **Entrevistar a los 2 usuarios de pago que se fueron**. ¿Precio? ¿Falta de valor? ¿Soporte?
- [ ] **Revisar señales de churn** en los 20 usuarios de pago restantes: ¿uso decreciente? ¿tickets de soporte?
- [ ] **Verificar cálculo del panel**: ¿El churn se calcula sobre usuarios *activos* o sobre *todos los registrados*? Si es sobre todos, el 31% está inflado por cuentas inactivas/fantasma.

### Semana 2: Segmentar mejor
- [ ] **Calcular churn por cohorte** (cuándo se registraron). ¿Los nuevos gratuitos se van rápido? ¿Los antiguos también?
- [ ] **Analizar conversión gratuito→pago**: ¿Cuántos gratuitos se convirtieron este mes? Si la conversión es baja, el churn gratuito es menos crítico.
- [ ] **Comparar con benchmarks de tu industria**. ¿9.1% churn de pago es alto para tu sector?

### Semana 3: Actuar
- [ ] **Campaña win-back** para usuarios de pago que mostraron señales de churn (uso bajo, quejas).
- [ ] **Revisar onboarding de gratuitos**: ¿El 33.7% se va porque no vieron valor? Mejorar el "aha moment".
- [ ] **Considerar métrica alternativa**: Churn de ingresos (NRR) en lugar de churn de usuarios.

## 🎯 Recomendación Clave

**Deja de mirar el 31%.** Tu north star debe ser:
- **Churn de pago mensual** (<5% si es posible)
- **Net Revenue Retention** (>100% es ideal)

El churn gratuito alto no mata tu negocio si tu modelo es freemium. El churn de pago sí. Enfoca recursos en retener a los que pagan, no en retener a los que no pagan.

---

**¿Quieres que profundice en algún aspecto? Por ejemplo, cómo calcular el NRR o cómo diseñar una campaña win-back efectiva.**