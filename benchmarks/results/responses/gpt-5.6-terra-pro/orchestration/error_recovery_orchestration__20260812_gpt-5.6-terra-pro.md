# GPT-5.6 Terra Pro — orchestration/error_recovery_orchestration

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 6.75 | quality: 7.5
- latency_total: 11.74s | tokens_per_second: 139.2
- input_tokens: 4528 | output_tokens: 1634

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

La consulta falló porque la base `production` está en mantenimiento y no acepta conexiones; el proveedor estima recuperación en unas 2 horas.

Para cumplir antes de las 5 pm, ajustaría el plan así:

1. **No esperar únicamente a la base principal.** Buscar una fuente alternativa:
   - réplica de solo lectura / *data warehouse*;
   - panel de BI con datos ya actualizados;
   - exportación programada (CSV/Excel) del cierre mensual;
   - sistema de facturación o pagos, si es la fuente operativa de ventas.

2. **Preparar el resumen en paralelo** con la última exportación disponible, identificándolo como “preliminar” y señalando su fecha/hora de corte.

3. **Validar y reenviar una versión final** cuando vuelva la base, si hubiera diferencias.

4. **Avisar al equipo ahora** de la contingencia y de la hora prevista de entrega, para que no esperen cifras definitivas sin contexto.

¿Dónde están normalmente los reportes o dashboards de ventas —por ejemplo, Power BI, Looker, un bucket de archivos, una réplica de la base o un sistema de facturación—? Con esa ubicación puedo obtener los datos alternativos y preparar el correo.