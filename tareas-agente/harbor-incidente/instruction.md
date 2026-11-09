Eres quien atiende la operación digital de Ferretería El Roble SpA. En `/app/tickets.md` hay
tres incidentes abiertos (INC-1, INC-2, INC-3). En `/app` tienes los exports de n8n y su
log, la configuración de Listmonk, el estado de los flujos, los secretos, el esquema de
NocoDB, las plantillas del drip, el registro de cambios y `README-operacion.md`, que
explica cómo funciona todo y las reglas de intervención (se cumplen).

Para cada incidente:

1. Encuentra la causa real y clasifícala con **uno** de estos ids:

   | id | significa |
   |---|---|
   | `credencial_expirada` | una credencial o token venció o dejó de ser válido |
   | `password_enmascarado` | un secreto quedó guardado con su valor enmascarado (`••••`) en vez del real |
   | `estado_con_fecha_futura` | un estado guardado tiene una fecha posterior a la real y el flujo descarta todo |
   | `opcion_select_faltante` | un campo de selección no acepta un valor que los datos sí usan |
   | `rate_limit_proveedor` | el proveedor rechaza por exceso de solicitudes |
   | `workflow_duplicado` | dos flujos con el mismo propósito se pisan |
   | `nodo_desactivado` | un nodo del flujo está desactivado |
   | `zona_horaria` | una hora se interpreta en la zona horaria equivocada |

2. Aplica el arreglo en el archivo que causa el problema, dentro de `/app`.

Escribe `/app/diagnostico.json`:

```json
{
  "incidentes": [
    {"ticket": "INC-1", "causa": "<id>", "archivo": "ruta/relativa/a/app", "arreglo": "qué cambiaste"}
  ]
}
```

Una entrada por ticket. Lo que se revisa es la causa elegida y el estado final de los
archivos de `/app`.
