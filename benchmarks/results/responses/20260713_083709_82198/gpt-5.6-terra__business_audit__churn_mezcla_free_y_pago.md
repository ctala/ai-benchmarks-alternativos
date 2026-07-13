# GPT-5.6 Terra — business_audit/churn_mezcla_free_y_pago

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 7.11 | quality: 8.4
- latency_total: 18.361s | tokens_per_second: 99.1
- input_tokens: 165 | output_tokens: 1819

## Respuesta completa

Respira: el **31% no parece ser churn de clientes de pago**, sino churn de toda tu base, incluyendo el plan gratuito.

### Qué está midiendo realmente el panel

| Segmento | Usuarios al inicio | Bajas | Churn mensual |
|---|---:|---:|---:|
| Total | 200 | 62 | **31.0%** |
| Gratuito | 178 | 60 | **33.7%** |
| De pago | 22 | 2 | **9.1%** |

Cálculos:

- Churn total: `62 / 200 = 31%`
- Churn free: `60 / 178 = 33.7%`
- Churn paid: `2 / 22 = 9.1%`

Por tanto, si lo que te preocupaba era la retención de ingresos o clientes de pago, la cifra relevante ahora es **9,1% mensual**, no 31%.

## ¿Qué tan grave es?

Depende de qué tipo de negocio y de tu definición de “baja”, pero hay dos lecturas distintas:

1. **El 31% de churn free no es necesariamente una emergencia.**  
   En productos freemium, mucha gente prueba el producto, no encuentra valor rápido o deja de usarlo. Puede ser normal, aunque también puede indicar problemas de activación, onboarding o calidad de adquisición.

2. **El 9,1% de churn paid sí merece atención.**  
   No es comparable con 31%, pero tampoco es trivial. Con solo 22 clientes de pago, perder 2 altera mucho el porcentaje:
   - 1 baja sería 4,5%.
   - 2 bajas son 9,1%.
   - 3 bajas serían 13,6%.

   Es una base pequeña: una o dos cuentas cambian mucho la métrica. No concluyas todavía que hay una tendencia estructural con un único mes.

Además, tu estimación inicial de 5% no estaba muy lejos en términos absolutos: estás hablando de **un cliente adicional** sobre una base de 22. Aun así, conviene investigar los dos casos.

## Prioridad inmediata: verificar la definición

Antes de actuar, confirma estas cuatro cosas en el panel:

- ¿“Baja” significa que cancelaron, o que su suscripción ya terminó efectivamente?
- ¿Incluye usuarios gratuitos que eliminaron su cuenta, quedaron inactivos o simplemente desinstalaron?
- ¿El denominador son usuarios activos al inicio del mes, o todos los usuarios registrados?
- ¿Los 2 clientes de pago eran clientes que ya estaban activos al inicio del mes?  
  Para churn mensual, normalmente deben contarse solo clientes existentes al inicio, no altas y bajas dentro del mismo mes.

Si las respuestas son correctas, reporta estas métricas separadas:

- **Churn de clientes de pago (logo churn): 9,1%**
- **Churn de usuarios gratuitos: 33,7%**
- **Churn total de cuentas: 31,0%**
- **Revenue churn / MRR churn:** pendiente de calcular con los ingresos perdidos, no solo número de cuentas.

La última es especialmente importante: perder dos clientes pequeños no tiene el mismo impacto que perder dos cuentas grandes.

## Plan de acción

### Hoy–próximas 48 horas: entender las 2 bajas de pago

Haz una ficha para cada una:

- Plan y MRR que pagaban.
- Antigüedad como cliente.
- Fecha de alta, fecha de cancelación y motivo declarado.
- Uso en los 30, 60 y 90 días previos: frecuencia, funcionalidades usadas, usuarios activos, eventos clave.
- Tickets de soporte, fallos, problemas de facturación o cambios de precio.
- Segmento: industria, tamaño, canal de adquisición, caso de uso.
- ¿Habían reducido uso antes de cancelar?

Contacta a ambas personas con un mensaje corto y no defensivo. Por ejemplo:

> “Vimos que cancelaste [producto]. Estamos intentando mejorar y agradeceríamos 10 minutos para entender qué no funcionó: ¿faltaba alguna función, el precio no encajaba, no hubo suficiente uso o resolviste el problema de otra forma?”

No intentes venderles de inmediato. Primero clasifica la causa.

### Esta semana: segmentar la base de pago

Con 22 clientes, puedes revisar prácticamente todos de forma individual. Crea un semáforo:

- **Verde:** uso frecuente y evento de valor reciente.
- **Amarillo:** uso cayendo, poca adopción de funciones clave, ningún login reciente, renovación próxima.
- **Rojo:** sin actividad relevante, soporte negativo, pago fallido, cancelación programada.

Para los amarillos y rojos:

- Contacto proactivo de éxito de cliente.
- Revisión de onboarding o configuración.
- Ayuda para alcanzar un primer resultado concreto.
- Recordatorios de valor o casos de uso relevantes.
- Resolver fricción de facturación, permisos, integraciones o soporte.

El objetivo no es “mandar emails de retención” a todos; es detectar si los clientes están logrando valor antes de que dejen de usar el producto.

### Esta semana: investigar el 33,7% de churn gratuito

No lo mezcles con el problema de pago, pero tampoco lo ignores. Revisa:

- Canal de adquisición de quienes abandonan.
- Si completaron onboarding.
- Si llegaron al “momento de valor” del producto.
- Tiempo hasta abandonar.
- Diferencias entre quienes abandonan y quienes se mantienen o convierten a pago.

Preguntas útiles:

- ¿El tráfico gratuito está mal cualificado?
- ¿La propuesta de valor y el onboarding prometen algo que el producto no entrega rápido?
- ¿Hay una limitación del plan free que hace imposible experimentar valor?
- ¿Son cuentas basura, duplicadas o pruebas de muy baja intención?

Un churn free alto puede ser aceptable si los usuarios que permanecen convierten bien. Si casi nadie activa o convierte, es un problema de adquisición y activación, no necesariamente de retención de pago.

## Cambia el dashboard desde ya

No uses una única métrica de “churn”. Separa al menos:

1. **Paid logo churn**  
   `clientes de pago perdidos / clientes de pago al inicio del período`

2. **Free user churn**  
   `usuarios free perdidos / usuarios free al inicio del período`

3. **Gross Revenue Churn**  
   `MRR perdido por downgrades y cancelaciones / MRR inicial`

4. **Net Revenue Retention (NRR)**  
   Considera ingresos perdidos, expansiones y upgrades. Es la medida más útil para salud de ingresos recurrentes.

5. **Retención por cohorte**  
   Clientes agrupados por mes de alta, plan, canal y segmento. Esto te dirá si el problema viene de clientes nuevos, de un canal específico o de una cohorte concreta.

## Cómo comunicarlo internamente

No digas: “Tenemos 31% de churn de clientes”.

Di algo como:

> “El panel estaba agregando cuentas gratuitas y de pago. El churn total de cuentas fue 31%, impulsado por 60 bajas free. El churn de clientes de pago fue 2 de 22, o 9,1%. Estamos validando la definición de baja, calculando churn de MRR y revisando las causas de las dos cancelaciones.”

Eso es preciso, evita pánico innecesario y deja claro que hay trabajo que hacer.

## Conclusión

No estás ante un 31% de churn de pago. Estás ante:

- **33,7% de churn en free**, que requiere analizar activación y calidad de adquisición.
- **9,1% de churn de pago**, que requiere investigar dos casos concretos y vigilar la tendencia.
- Una base de pago pequeña, donde cada cliente perdido mueve mucho el porcentaje.

La acción más importante es dejar de mirar el churn agregado como indicador principal y empezar a seguir, por separado, **retención free, churn de logos pagados y churn de ingresos**.