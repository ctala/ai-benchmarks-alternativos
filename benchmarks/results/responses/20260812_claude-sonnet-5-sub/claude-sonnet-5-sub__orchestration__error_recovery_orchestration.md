# Claude Sonnet 5 (suscripción) — orchestration/error_recovery_orchestration

- model_id: `claude-sonnet-5`
- success: True  | final: 8.27 | quality: 10.0
- latency_total: 40.428s | tokens_per_second: 55.1
- input_tokens: 2 | output_tokens: 2229

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente orquestador. Tienes acceso a herramientas pero algunas pueden fallar.
Cuando una herramienta falla, debes:
1. Diagnosticar por que fallo
2. Proponer una alternativa
3. Ajustar el plan general

**user:**

Necesito obtener los datos de ventas del mes pasado y enviar un resumen al equipo.

**assistant:**

Voy a consultar la base de datos para obtener los datos de ventas.

**tool:**

ERROR: Connection refused - database 'production' is currently under maintenance. Expected recovery: 2 hours.

**user:**

La base de datos esta en mantenimiento. Que hacemos? Necesito enviar el reporte antes de las 5pm.


## Respuesta completa

## Diagnóstico

El error es claro: `production` está en mantenimiento programado, no es un fallo de credenciales ni de red. ETA 2h — si eso se cumple, el mantenimiento termina cerca de las 3pm-4pm dependiendo de cuándo arrancó, lo que deja margen ajustado pero real para llegar a las 5pm. El problema es que "ETA 2 horas" en mantenimientos de DB suele ser optimista, así que no conviene apostar todo el plan a que se cumpla exacto.

No voy a reintentar la misma conexión en loop — es tiempo perdido mientras el servicio sigue caído.

## Alternativas (de mejor a peor, según qué tan fiel necesitas que sea el dato)

1. **Réplica read-only / staging con datos espejados.** Si existe una réplica de lectura o un entorno staging sincronizado, es la opción más rápida y con menor riesgo de dato viejo. ¿Tienes una?
2. **Último snapshot/backup o export cacheado.** Si hay un dump reciente (nightly backup, o un export que ya se generó para otro reporte), sirve para armar el resumen con un disclaimer de "datos a corte de [fecha/hora del snapshot], no en vivo".
3. **Dashboard/BI que ya tenga las cifras agregadas** (algo tipo NocoDB, Metabase, Looker, lo que uses) — si el resumen de ventas ya se calculó ahí antes del mantenimiento, evitas tocar la DB de nuevo.
4. **Esperar el mantenimiento y correr el reporte a último momento.** Solo viable si confirmas que el ETA es confiable y te deja margen real antes de las 5pm (no quiero que armes el reporte a las 4:55pm sin buffer).

## Plan ajustado

- Ahora mismo: dime si tienes alguna de las opciones 1-3 disponible (acceso, credenciales, o nombre del dashboard) y la ejecuto.
- Si ninguna existe: aviso al equipo de entrada que el reporte llega con demora por mantenimiento de DB — mejor un heads-up ahora que un silencio hasta las 5pm. **¿Quieres que redacte ese aviso?** (no lo mando sin tu ok explícito, igual que cualquier mensaje al equipo).
- En paralelo, si confirmas el ETA real de la DB, dejo un check listo para correr la consulta apenas vuelva y no perder tiempo cuando se restablezca.

¿Cuál de las tres alternativas tienes disponible, o prefieres que primero mande el aviso de demora al equipo?