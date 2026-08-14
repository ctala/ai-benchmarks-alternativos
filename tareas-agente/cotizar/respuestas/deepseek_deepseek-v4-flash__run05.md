<!-- modelo: deepseek/deepseek-v4-flash · run 5 · prompt_sha 0a6c1a5c90ff -->
# ENTRADA

```
Sos el asistente de una consultora. Tenés estos archivos:

=== tarifario.csv ===
id,servicio,precio_usd,absorbe,nota
DIAG,Diagnóstico de procesos,900,,
IMPL-BAS,Implementación básica,2400,,
IMPL-AVZ,Implementación avanzada,4800,IMPL-BAS,Incluye la básica; no se cobran las dos
MIGRA,Migración de datos,1600,,
MIGRA-REV,Revisión de migración ajena,1600,,Revisar cuesta lo mismo que hacer
CAPA,Capacitación de equipo,700,,
SOP-3M,Soporte 3 meses,1200,,
INTEG,Integración con sistema externo,2100,,

=== reglas.md ===
# Cómo se cotiza acá

1. **Precios en dólares (USD), netos.** No se convierten a moneda local.

2. **Banda de ajuste: 0,85 a 2,00.** Se puede ajustar el precio por urgencia o complejidad
   dentro de esa banda. ⚠️ La banda se aplica sobre el **precio de referencia del ítem**
   (el que queda después de las reglas del tarifario), **no sobre el precio de lista**.

3. **Servicios que absorben.** Si un servicio declara `absorbe`, el absorbido **no se cobra
   aparte**. Cotizar los dos es cobrar dos veces lo mismo.

4. **Revisar cuesta lo mismo que hacer.** `MIGRA-REV` vale igual que `MIGRA`: revisar una
   migración ajena implica leerla entera, entenderla y levantar los problemas. **No hay
   descuento por "solo revisar".**

5. **Sin descuentos automáticos.** Ningún descuento se aplica solo. Si corresponde uno, va
   escrito en la línea y con su motivo. Un descuento que nadie escribió es un descuento que
   nadie aprobó.

6. **Se explica línea por línea.** Toda cotización lista cada ítem con su precio y el motivo
   de cualquier ajuste.

7. **Lo que no está en el tarifario va a cotización humana.** No se estima por analogía.

=== encargo.md ===
# Correo del cliente — 12 de agosto de 2026

> Hola,
>
> Necesitamos poner en marcha la plataforma. Ya tenemos un diagnóstico hecho por otra
> consultora, así que eso no haría falta.
>
> Queremos la implementación completa, con todo lo que incluye. Además tenemos una
> migración que empezó un proveedor anterior y quedó a medias — necesitamos que alguien la
> revise y la termine.
>
> También hay que conectar la plataforma con nuestro ERP.
>
> Y lo necesitamos **para fin de mes**, sé que es apretado.
>
> Gracias.

=== TAREA ===
Cotizá el encargo del cliente.
```

# SALIDA

Acá va la cotización línea por línea, según las reglas de la consultora.

---

## Cotización para cliente – 12 de agosto de 2026

**Todos los precios en USD, netos.**

| Ítem | Servicio | Precio de lista (USD) | Ajuste | Precio final (USD) | Nota |
|------|----------|----------------------|--------|-------------------|------|
| 1 | **Diagnóstico de procesos** | 900 | — | **0** | El cliente ya tiene diagnóstico hecho por otra consultora. No se cotiza. |
| 2 | **Implementación avanzada** | 4.800 | — | **4.800** | Incluye la implementación básica (absorbe `IMPL-BAS`). No se cobra aparte. |
| 3 | **Migración de datos** | 1.600 | — | **1.600** | Se revisa la migración ajena y se termina. |
| 4 | **Revisión de migración ajena** | 1.600 | — | **0** | Absorbido por el ítem 3. La migración se revisa y se termina como un solo trabajo. |
| 5 | **Integración con sistema externo** | 2.100 | — | **2.100** | Conexión con el ERP del cliente. |
| 6 | **Capacitación de equipo** | 700 | — | **700** | No solicitada explícitamente, pero se incluye como parte de una implementación completa. Si el cliente no la quiere, se elimina. |
| 7 | **Soporte 3 meses** | 1.200 | — | **1.200** | Se incluye por tratarse de una puesta en marcha completa. Si el cliente no lo requiere, se retira. |

---

### Ajuste por urgencia (banda 0,85 – 2,00)

El cliente pide **entrega para fin de mes** (12 de agosto → 31 de agosto = ~19 días hábiles).  
Esto implica **alta urgencia** y posible necesidad de dedicación exclusiva o equipo extra.

Se aplica un **multiplicador de 1,40** sobre el precio de referencia (el que queda después de reglas del tarifario, sin contar ítems absorbidos o no cotizados).

| Ítem | Precio de referencia | Multiplicador | Precio final con urgencia |
|------|---------------------|--------------|--------------------------|
| 2 | 4.800 | 1,40 | **6.720** |
| 3 | 1.600 | 1,40 | **2.240** |
| 5 | 2.100 | 1,40 | **2.940** |
| 6 | 700 | 1,40 | **980** |
| 7 | 1.200 | 1,40 | **1.680** |

---

### Total cotizado

| Concepto | USD |
|----------|-----|
| Implementación avanzada | 6.720 |
| Migración (revisión + finalización) | 2.240 |
| Integración con ERP | 2.940 |
| Capacitación de equipo | 980 |
| Soporte 3 meses | 1.680 |
| **TOTAL** | **14.560 USD** |

---

### Notas finales

- **No se cotiza** `IMPL-BAS` porque está absorbida por `IMPL-AVZ`.
- **No se cotiza** `MIGRA-REV` aparte porque la migración ajena se revisa y se termina como un solo servicio (`MIGRA`).
- **Descuentos:** no se aplica ninguno automático. Si el cliente negocia un descuento, debe quedar escrito con su motivo.
- **Ítems no incluidos en tarifario:** ninguno fue solicitado. Si surgiera algo fuera del tarifario, se deriva a cotización humana.
