# Qwen 3.7 Flash — business_audit/churn_mezcla_free_y_pago

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 9.06 | quality: 10.0
- latency_total: 31.041s | tokens_per_second: 96.2
- input_tokens: 189 | output_tokens: 2985

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

Como analista de retención, mi primera regla es siempre esta: **nunca actúes sobre una métrica sin verificar primero qué población está midiendo y cómo se calculó**. En tu caso, el pánico es comprensible, pero los números te están jugando una mala pasada. Vamos paso a paso.

### 🔍 1. Verificación de población y cálculo
La fórmula que usó tu panel es:
`Churn = Usuarios dados de baja / Usuarios al inicio del mes × 100`  
`62 / 200 = 31%` ✅ Matemáticamente correcta.

**Pero el error está en la población:** mezclar usuarios gratuitos y de pago en un mismo churn diluye la realidad del negocio. En modelos freemium, el churn gratuito suele ser alto y natural; el churn que impacta sostenibilidad, LTV y previsibilidad es el **Paid Churn**.

Desglosemos por segmento:
| Segmento | Inicio de mes | Bajas | Churn real |
|----------|---------------|-------|------------|
| Gratuito | 178           | 60    | **33.7%**  |
| Pago     | 22            | 2     | **9.1%**   |

### 📊 2. ¿Qué tan grave es?
- **Churn general (31%):** No es alarmante cuando se ve con lupa. Es típico en plataformas freemium donde la barrera de entrada es baja y muchos usuarios prueban sin intención de quedarse.
- **Churn de pago (9.1%):** Es la métrica que sí importa. Un 9% mensual en B2C o SaaS pequeño es **elevado**, pero con solo 22 usuarios activos, la varianza estadística es alta. Perder 2 clientes en un mes puede ser ruido, pero si se repite 2-3 meses seguidos, indica fuga estructural.
- **Conclusión:** No estás en crisis. Tienes una señal de alerta en el segmento que paga, pero el pánico viene de una métrica mal segmentada.

---

### 🛠️ 3. Plan de acción inmediato

#### ✅ Fase 1: Validación y limpieza (Día 1-3)
1. **Revisa la definición de "baja" en tu BD:** ¿Incluye trial expirados? ¿Cuentas duplicadas por re-registro? ¿Usuarios desactivados temporalmente marcados como `cancelled`? Filtra solo bajas confirmadas (razón explícita o transacción fallida recurrente).
2. **Contacta a los 2 usuarios de pago perdidos:** Llama o envía un mensaje personal. Pregunta: ¿problema técnico?, ¿precio?, ¿falta de valor percibido?, ¿competencia? Anota patrones. Con n=2, cada respuesta vale oro.
3. **Exporta cohortes:** No mires solo el snapshot mensual. Calcula churn por cohorte de registro (ej: usuarios que llegaron en marzo vs abril). Esto revela si el churn viene de malas adquisiciones o de degradación post-onboarding.

#### 📈 Fase 2: Ajuste de métricas y dashboards (Semana 1)
1. **Separa KPIs obligatoriamente:**
   - `Free Churn` → métrica de volumen/top-of-funnel
   - `Paid Churn` → métrica de salud de negocio
   - `Net Revenue Churn` (si aplican upgrades/downgrades) → métrica financiera
2. **Elimina el "churn global" del dashboard principal.** Si alguien pregunta, explica: *"Lo medimos separado porque las dinámicas de retención son distintas por plan"*.
3. **Añade margen de confianza o advertencia de muestra:** Con <50 usuarios pagados, marca visualmente que los cambios mensuales pueden tener alta varianza.

#### 🔄 Fase 3: Estrategia de retención (Semanas 2-4)
| Segmento | Acción clave | Ejemplo concreto |
|----------|--------------|------------------|
| **Pago** | Proactive Success + Exit Flow | - Email de check-in a día 14 y 30<br>- Al hacer clic en "Cancelar": ofrecer pausa, cambio de plan, o encuesta de 1 pregunta<br>- Asignar responsable de cuenta o success manager rotativo |
| **Gratuito** | Trigger de valor + Upgrade path | - Identificar hitos de uso (ej: 3ª sesión, primer feature key)<br>- Enviar tutorial contextual justo después<br>- Ofrecer prueba extendida o descuento de lanzamiento al pasar a pago |

#### 📉 Fase 4: Monitoreo continuo
- **Tracker semanal de Paid Churn** (no solo mensual)
- **Ratio de Reactivación:** ¿Cuántos de los 60 gratuitos volvieron en 30 días? Si es >15%, tu producto tiene demanda latente.
- **Umbral de alerta:** Si Paid Churn supera consistentemente **5-7% mensual durante 2 meses**, activa protocolo de retención intensiva (auditoría de onboarding, revisión de pricing, intervención manual de cuentas de alto LTV).

---

### 💡 Regla práctica para el futuro
> *"Si el churn sube, primero pregunta: ¿qué población entró en la ecuación?"*  
Un churn del 30% en free users no es fuego. Un churn del 9% en paid users es humo que hay que rastrear. Tu plataforma no está fallando; tu panel te estaba ocultando dónde está el riesgo real.

Si quieres, puedo ayudarte a:
- Configurar la fórmula exacta de Paid Churn en tu SQL/BI
- Diseñar un flujo de exit survey de 1 pregunta
- Crear un tracker semanal de retención por cohorte

Solo dime en qué stack trabajas (Mixpanel, Amplitude, Looker, custom DB, etc.) y te doy el código o estructura lista para copiar.