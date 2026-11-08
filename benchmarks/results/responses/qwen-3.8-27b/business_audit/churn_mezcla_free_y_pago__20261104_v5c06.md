# Qwen 3.8 27B — business_audit/churn_mezcla_free_y_pago

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 8.04 | quality: 10.0
- latency_total: 336.54s | tokens_per_second: 37.8
- input_tokens: 227 | output_tokens: 12728

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



Primer: **no entres en pánico**. El 31% es una alarma, pero casi seguro no es “31% de churn de clientes de pago”. Está midiendo una población diferente a la que normalmente te preocupa.

## 1. Qué está midiendo realmente tu panel

Tu panel calcula:

> **62 bajas / 200 usuarios a inicio de mes = 31% de churn total de cuentas.**

Pero esa población de 200 no es homogénea:

| Segmento | Usuarios a inicio | Bajas | Churn del segmento |
|---|---:|---:|---:|
| Gratis | 178 | 60 | **33.7%** |
| Pago | 22 | 2 | **9.1%** |
| Total | 200 | 62 | **31.0%** |

Dato clave:

- Las **60 bajas gratuitas** aportan **30 puntos porcentuales** al churn total.
- Las **2 bajas de pago** aportan **1 punto porcentual** al churn total.

Es decir, tu 31% está compuesto mayoritariamente por churn gratuito:

> **31% = 30 pp de churn gratuito + 1 pp de churn de pago.**

Si tu negocio depende de los 22 clientes de pago, el número más importante no es 31%, sino:

> **Churn de base de pago = 2 / 22 = 9.1%.**

Y, si los planes tienen el mismo precio, ese 9.1% también sería aproximadamente tu **churn de MRR**. Si los planes tienen precios diferentes, deberías calcular:

> **Churn de ingresos = MRR perdido por cancelaciones / MRR a inicio de mes.**

---

# 2. ¿Qué tan grave es?

## Como churn total de cuentas: alto, pero no necesariamente crítico

Un churn total del 31% parece enorme, pero tu base está compuesta por un 89% de usuarios gratuitos. En un modelo freemium, es completamente posible que el churn de cuentas gratuitas sea alto.

La pregunta no es solo:

> “¿Cuántos usuarios se fueron?”

Sino:

> “¿Esos usuarios gratuitos deberían haberse activado, probado, convertido o seguido usando el producto?”

Si los 60 usuarios gratuitos simplemente se registraron y nunca completaron el onboarding, tu problema no es “retención de clientes”, sino **activación de usuarios nuevos** o **calidad del tráfico**.

## Como churn de clientes de pago: moderado, pero no despreciable

Perdiste 2 clientes de pago sobre 22. Eso es **9.1% de tu base de pago mensual**.

Con una base pequeña, eso importa mucho:

- 1 cliente de pago = **4.5%** de tu base.
- 2 clientes de pago = **9.1%**.
- 3 clientes de pago = **13.6%**.

Por lo tanto, aunque sean solo 2 cuentas, **no debes ignorarlo**. En una base de 22, cada cliente mueve mucho el número.

No es una catástrofe inmediata, pero sí una señal de que hay que investigar con urgencia.

También hay que tener cuidado: con solo 22 clientes de pago, un mes de 9.1% puede ser ruido, pero también puede ser una tendencia. Con 22 clientes, no puedes extraer una tendencia fuerte de un solo mes.

Mi lectura:

> **No estás en un churn de 31% de clientes de pago. Estás en un churn total de cuentas de 31%, impulsado por churn gratuito, con un churn de pago de 9.1% que debe investigarse.**

---

# 3. La pregunta del 5%

Tú pensabas que estabas en 5%. Ahí hay una trampa importante: **¿5% de qué?**

### Caso A: Si el 5% era churn de clientes de pago

Entonces estás por encima:

> Churn de pago real: **9.1%**  
> Meta o expectativa: **5%**

Eso es relevante. Hay que investigar las 2 cancelaciones de pago.

### Caso B: Si el 5% era churn total de cuentas

Entonces tu expectativa probablemente no era realista si tienes 178 usuarios gratuitos y 22 de pago.

Un churn total del 5% con esa mezcla implicaría aproximadamente:

> 5% de 200 = 10 bajas.

Pero tienes 62. El exceso viene sobre todo del segmento gratuito.

### Caso C: Si el 5% venía de meses anteriores

Entonces hay que revisar si hubo un cambio:

- Nueva campaña de tráfico.
- Cambios en el free tier.
- Falla técnica.
- Error de datos.
- Usuarios de prueba.
- Usuarios importados.
- Usuarios inactivos que se limpiaron.
- Fallas de pago.
- Lanzamiento de una versión nueva.
- Cambio de precio.
- Competidor.

---

# 4. Plan de acción

## Fase 0: Congela el mensaje interno

No dejes que el número “31% de churn” se corra como si fuera churn de clientes de pago.

Mensaje recomendado:

> “El churn total de cuentas es 31%, pero la base está compuesta por 89% de usuarios gratuitos y 11% de pago. El churn de base de pago es 9.1%, correspondiente a 2 de 22 clientes. El problema principal visible está en las cuentas gratuitas: 60 bajas de 178 usuarios free. Vamos a separar churn total, churn de pago y churn gratuito, y a investigar las 2 cancelaciones de pago y la activación gratuita.”

---

## Fase 1: Validar la métrica en las próximas 48 horas

Antes de culpar al producto, verifica que el número sea real.

Revisa:

1. **¿Qué significa “baja” en tu panel?**
   - ¿Cancelación manual?
   - ¿Cuenta eliminada?
   - ¿Usuario inactivo 30 días?
   - ¿Pago fallido?
   - ¿Cuenta de prueba?
   - ¿Cuenta creada y nunca activada?

2. **¿Los 200 usuarios iniciales eran realmente activos?**
   - ¿Incluyen cuentas creadas pero nunca usadas?
   - ¿Incluyen usuarios invitados?
   - ¿Incluyen cuentas de prueba?
   - ¿Incluyen bots o registros duplicados?
   - ¿Incluyen usuarios importados?

3. **¿Las 62 bajas fueron dentro del mismo mes?**
   - Verifica fechas exactas.
   - Busca picos.
   - Identifica si hubo un evento: outage, cambio de plan, precio, bug, campaña, etc.

4. **¿El churn de pago es voluntario o involuntario?**
   - Falló la tarjeta?
   - Hubo disputa de pago?
   - El cliente pidió cancelar?
   - Se fue por precio?
   - Se fue por falta de uso?
   - Se fue por un bug?

5. **Calcula churn de MRR real.**

Si los planes valen distinto:

> Churn de MRR = MRR perdido / MRR inicial.

Ejemplo:

- MRR inicial: $1,000.
- Se van 2 clientes: uno de $50 y otro de $100.
- MRR perdido: $150.
- Churn de MRR: 15%.

Eso puede ser distinto al churn por cuentas.

---

## Fase 2: Investigar las 2 cancelaciones de pago

Esto es urgente porque son ingresos directos.

Haz lo siguiente:

1. Contacta a los 2 clientes que se fueron.
2. Pregunta por qué se fueron.
3. Revisa su uso del producto.
4. Revisa tickets de soporte.
5. Revisa si hubo fallas de pago.
6. Revisa si cambiaste precios, features, límites o términos.
7. Revisa si se fue por competencia.
8. Revisa si había un bug o problema de onboarding.

Clasifica cada cancelación:

| Tipo | Ejemplo | Acción |
|---|---|---|
| Involuntaria | Tarjeta vencida, pago rechazado, problema con pasarela | Recuperar con dunning, retry, actualizar método de pago |
| Voluntaria por precio | “Está caro” | Ajustar packaging, tiers, trial, valor |
| Voluntaria por uso | “No lo uso” | Mejorar activación, casos de uso, reminder |
| Voluntaria por problema | Bug, soporte, data loss | Fix urgente |
| Voluntaria por competencia | Encontró mejor alternativa | Mejorar diferenciación |
| Voluntaria por falta de valor | No entendió para qué sirve | Reforzar onboarding y valor inicial |
| No aplicable | Cliente fantasma, prueba, error | Limpiar base |

Con solo 2 clientes, la investigación manual es más valiosa que cualquier dashboard.

---

## Fase 3: Diagnosticar el churn gratuito

Aquí está el mayor volumen: 60 bajas de 178.

Necesitas saber si esas 60 personas eran “usuarios” o simplemente registros inactivos.

Preguntas clave:

1. **¿Qué porcentaje de los 178 gratuitos completó el onboarding?**
2. **¿Qué porcentaje logró la primera acción de valor?**
   - Creó un proyecto.
   - Conectó una herramienta.
   - Invitó a un equipo.
   - Importó datos.
   - Realizó la acción central del producto.
3. **¿Cuánto tardaron en llegar a la primera acción de valor?**
4. **¿Desde qué fuente llegaron?**
   - Orgánico.
   - Ads.
   - Red social.
   - Referido.
   - App store.
   - Campaña específica.
5. **¿Usaron móvil, desktop o ambos?**
6. **¿Se fueron el mismo día, al día siguiente o después de varios días?**
7. **¿Alguno de esos usuarios gratuitos mostró intención de pago?**
   - Visitó pricing.
   - Comenzó trial.
   - Intentó actualizar.
   - Descargó reportes.
   - Creó contenido.

### Escenarios posibles

#### Escenario A: Los 60 free nunca se activaron

Entonces tu problema no es churn de clientes, sino **activación**.

Acciones:

- Mejorar onboarding.
- Reducir pasos hasta el primer valor.
- Enviar emails de activación.
- Mostrar in-app prompts.
- Pedir menos información al inicio.
- Dar un caso de uso claro.
- Detectar usuarios bloqueados.
- Ofrecer plantilla o demo.
- Limitar el free tier si atrae usuarios sin intención.

#### Escenario B: Los 60 free sí se activaron pero no convirtieron

Entonces hay un problema de **valor, pricing, fit o conversión**.

Acciones:

- Mejorar la propuesta de valor.
- Hacer más visible el upgrade.
- Crear trial.
- Ofrecer límite claro.
- Segmentar usuarios con intención.
- Hacer follow-up manual a usuarios que usan mucho el free.
- Ajustar el free tier para que el pago tenga sentido.

#### Escenario C: Los 60 free vinieron de una mala fuente

Entonces el problema es **calidad de tráfico**.

Acciones:

- Revisar campaña.
- Ajustar mensaje de adquisición.
- Ajustar promesa.
- Filtrar audiencias.
- Medir conversión por canal, no solo registro.

#### Escenario D: Hubo un evento técnico o de producto

Revisa:

- Deploys recientes.
- Fallas.
- Errores.
- Lentitud.
- Data loss.
- Cambios de UI.
- Cambios en límites.
- Cambios en pricing.

---

# 5. Dashboard que debes construir esta semana

Deja de usar un solo número de churn. Crea estas métricas:

## Para negocio / ingresos

| Métrica | Fórmula |
|---|---|
| Churn de clientes de pago por cuenta | Bajas de pago / Clientes de pago a inicio |
| Churn de MRR | MRR perdido / MRR a inicio |
| Churn por ingresos | Ingresos perdidos / Ingresos a inicio |
| NRR | (MRR inicial + expansión - contracción - churn) / MRR inicial |
| Clientes de pago activos | Base de pago al cierre |
| MRR | Suma de suscripciones activas |

## Para producto / free tier

| Métrica | Fórmula |
|---|---|
| Churn gratuito | Bajas free / Free a inicio |
| Activación free | % de usuarios free que completó acción clave |
| Tiempo a primer valor | Días desde registro hasta primera acción de valor |
| Conversión free a pago | Pagados nuevos / Free activos o trial |
| Cohortes semanales de free | Activación por semana de registro |

## Para retención de pago

| Métrica | Fórmula |
|---|---|
| Retención mensual de pago | 1 - churn de pago |
| Cohortes de pago | Retención por mes desde pago inicial |
| Tasa de renovación | Renovaciones / pagos que debían renovar |
| Motivo de cancelación | Clasificación de bajas |

---

# 6. Qué no hacer ahora

No tomes decisiones grandes por un solo mes.

Evita:

- Matar el free tier de inmediato.
- Subir precios sin más datos.
- Culpar al producto sin ver las 2 cancelaciones de pago.
- Asumir que el 31% es churn de clientes.
- Comparar 31% contra 5% sin definir si el 5% era churn total, churn de pago o churn de MRR.
- Creer que el problema es solo el churn, cuando probablemente es activación gratuita + retención de pago.

---

# 7. Plan concreto por días

## Hoy / mañana

1. Exportar datos brutos.
2. Calcular churn por segmento.
3. Calcular churn de MRR.
4. Validar definición de “baja”.
5. Identificar los 2 clientes de pago que se fueron.
6. Revisar si hubo pago fallido.
7. Contactar a los 2 clientes.
8. Aclarar internamente: el churn total es 31%, pero el churn de pago es 9.1%.

## Esta semana

1. Crear dashboard con:
   - Churn total.
   - Churn gratuito.
   - Churn de pago.
   - Churn de MRR.
   - Activación de free.
   - Cohortes semanales.
2. Segmentar los 60 usuarios gratuitos que se fueron.
3. Revisar onboarding.
4. Revisar fuentes de tráfico.
5. Clasificar motivos de cancelación de pago.
6. Identificar quick wins.

## Próximas 2 semanas

1. Lanzar mejoras de onboarding si hay users no activados.
2. Implementar secuencia de emails para usuarios free inactivos.
3. Crear aviso in-app para usuarios que no completan activación.
4. Mejorar flujo de pago / dunning si hubo churn involuntario.
5. Agregar pregunta de cancelación:
   - Precio.
   - No lo uso.
   - Problema técnico.
   - Competidor.
   - Falta una feature.
   - Otro.
6. Medir si el churn de pago baja o si la activación free mejora.

## Próximos 30 días

1. Revisar 3-4 cohortes semanales, no solo un mes.
2. Definir metas separadas:
   - Churn de pago objetivo.
   - Churn de MRR objetivo.
   - Activación free objetivo.
   - Conversión free a pago objetivo.
3. Decidir si el free tier está atrayendo a usuarios correctos.
4. Ajustar experimentos.
5. Reportar con tres números, no uno:
   - Churn total de cuentas.
   - Churn de pago.
   - Churn de MRR.

---

# 8. Cómo comunicar el estado

Puedes decir esto:

> “Revisamos el reporte de churn. El 31% corresponde al churn total de cuentas, no al churn de clientes de pago. De 200 usuarios a inicio de mes, 178 eran gratuitos y 22 de pago. Hubo 62 bajas: 60 gratuitas y 2 de pago.  
>   
> El churn gratuito fue 33.7%, y es el que está inflando el número total. El churn de base de pago fue 9.1%, es decir, 2 de 22. Si todos los planes valen igual, eso representa aproximadamente 9.1% de churn de MRR; si los planes valen distinto, calcularemos churn por MRR.  
>   
> La prioridad inmediata es investigar las 2 cancelaciones de pago y entender por qué 60 usuarios gratuitos no se mantuvieron. No tomaremos decisiones sobre free tier o pricing solo con un mes de datos.”

---

# 9. Diagnóstico rápido

Con los datos que me diste:

## Lo más probable

- Tu problema principal no es que tus clientes de pago estén masivamente huyendo.
- Tu problema principal es que tienes una base grande de usuarios gratuitos con churn alto.
- Pero también tienes una alerta importante en pago: 9.1% mensual con solo 22 clientes.

## Lo más serio

- Si las 2 cancelaciones de pago fueron voluntarias y por problema del producto, eso es prioridad alta.
- Si fueron por pago fallido, es un problema operativo recuperable.
- Si el 33.7% de free nunca se activó, tu embudo está perdiendo valor antes de llegar a monetización.

## Lo menos alarmante

- Que el churn total de cuentas sea 31% si tu modelo es freemium y la mayoría de cuentas son gratuitas.

---

# 10. Resumen final

> **No estás en un churn de 31% de clientes de pago.**  
> **Estás en un churn total de cuentas de 31%, donde 97% de las bajas son gratuitas.**  
> **Tu churn de base de pago es 9.1%: 2 de 22.**  
> **Eso no es una muerte inmediata, pero sí merece investigación urgente por el tamaño pequeño de tu base de pago.**  
> **Tu mayor fuga está en free: 60 de 178. Eso sugiere un problema de activación, cualificación o calidad de tráfico.**

Tu prioridad debe ser:

1. **Validar la métrica.**
2. **Separar churn total, gratuito y de pago.**
3. **Investigar las 2 cancelaciones de pago.**
4. **Diagnosticar por qué 60 free no se activaron o no se quedaron.**
5. **Construir cohortes semanales.**
6. **Definir metas separadas para free activation y paid retention.**