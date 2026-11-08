# Gemini 3.8 Flash — orchestration/error_recovery_orchestration

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.64 | quality: 10.0
- latency_total: 11.949s | tokens_per_second: 66.6
- input_tokens: 498 | output_tokens: 796

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

### 1. Diagnóstico del fallo
* **Causa:** La base de datos principal (`production`) está bajo mantenimiento programado y rechaza conexiones (`Connection refused`).
* **Impacto temporal:** La ventana estimada de recuperación es de 2 horas. Si la hora actual deja poco margen respecto a las 5:00 PM, no podemos depender únicamente de esperar a que termine el mantenimiento.

---

### 2. Alternativas propuestas
1. **Buscar réplicas o almacenes alternativos (Data Warehouse / Réplica de lectura):** Comprobar si existen bases de datos de solo lectura (`analytics`, `reporting`, `replica`) o APIs internas (BI / ERP) que sigan operativas.
2. **Consultar respaldos o exportaciones locales:** Verificar si existen volcados recientes, archivos `.csv`, `.json` o reportes diarios/mensuales ya exportados en el servidor de archivos.
3. **Plan de contingencia temporal:** Si no hay fuentes secundarias y la ventana de 2 horas finaliza antes de las 5:00 PM, dejar listo el script de extracción, procesamiento y plantilla de correo para ejecutarlo automáticamente en cuanto la base de datos vuelva a estar en línea.

---

### 3. Ajuste del plan general
* **Fase 1 (Inmediata):** Explorar fuentes secundarias disponibles (archivos locales y réplicas de datos).
* **Fase 2:** Si encontramos los datos, procesar el resumen de ventas. Si no, preparar la plantilla y el script de consolidación.
* **Fase 3:** Enviar el resumen por correo al equipo antes de las 5:00 PM.

---

Voy a comenzar verificando si disponemos de archivos de respaldo o exportaciones recientes de ventas en el sistema: