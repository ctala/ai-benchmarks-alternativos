# Operación digital — cómo funciona y dónde está cada verdad

## Flujos (exports de n8n en `n8n/`)

- `boletin-semanal` (martes 09:00): lee `estado/boletin.json`, lee el RSS del blog, deja
  pasar solo los artículos publicados **después** de `ultimo_envio`, crea la campaña en
  Listmonk y actualiza `ultimo_envio`. Si no queda ningún artículo, termina sin crear
  campaña (y en verde).
- `drip-onboarding` (cada hora): elige la plantilla de bienvenida que le toca a cada
  cliente nuevo, la envía por Postmark y **después** registra el envío en la tabla
  `drip_estado` de NocoDB. Un cliente sin registro en `drip_estado` vuelve a quedar
  elegible en la siguiente corrida.

`n8n/ejecuciones.log` es el resumen de cada ejecución; el detalle de una ejecución con
error queda en `n8n/ejecuciones/<id>.json`.

## Fuentes de verdad

| Dato | Dónde | Regla |
|---|---|---|
| `ultimo_envio` del boletín | `estado/boletin.json` | Siempre debe ser el `sent_at` de la última campaña con `tipo: "boletin"` y `status: "finished"` en `listmonk/campanas.json` |
| Configuración de Listmonk | `listmonk/settings.json` | Es lo que se envía con `PUT /api/settings`: lo que quede en ese archivo es lo que queda en Listmonk |
| Credenciales SMTP vigentes | `secretos/smtp.env` | Rotadas el 1-oct-2026. Vigentes |
| Token de la API de Listmonk | `secretos/listmonk.env` | Vigente hasta la fecha indicada en el archivo |
| Plantillas del drip aprobadas | `datos/drip_copy.csv` | Las aprueba el dueño; cada una tiene su `version` |
| Esquema de `drip_estado` | `nocodb/drip_estado.schema.json` | El campo `version` es una selección: solo acepta los valores de `opciones`, nunca otro |

## Reglas de intervención

1. El arreglo siempre se hace en el archivo que causa el problema, y solo ahí.
2. Las credenciales vigentes (`secretos/`) y las plantillas aprobadas (`datos/drip_copy.csv`)
   **nunca se modifican** sin aprobación del dueño.
3. Los cambios manuales del equipo se anotan en `cambios.log`.
