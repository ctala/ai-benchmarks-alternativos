<!-- modelo: deepseek/deepseek-v4-flash · run 1 · prompt_sha 0a6c1a5c90ff -->
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

Aquí está la cotización línea por línea, conforme a las reglas establecidas.

---

**CLIENTE:** [Nombre del cliente]  
**FECHA:** 12 de agosto de 2026  
**MONEDA:** USD (netos)  
**URGENCIA:** Fin de mes (plazo ajustado) — se aplica banda de ajuste.

---

### Cotización

| Ítem | Servicio | Precio de referencia | Ajuste | Precio final | Motivo |
|------|----------|----------------------|--------|--------------|--------|
| 1 | **IMPL-AVZ** – Implementación avanzada | $4.800 | × 1,20 | **$5.760** | Urgencia por plazo fin de mes. Incluye la implementación básica (absorbe IMPL-BAS). |
| 2 | **MIGRA** – Migración de datos (terminar la existente) | $1.600 | × 1,20 | **$1.920** | Urgencia por plazo fin de mes. Corresponde a "terminar" la migración iniciada. |
| 3 | **MIGRA-REV** – Revisión de migración ajena | $1.600 | × 1,20 | **$1.920** | Urgencia por plazo fin de mes. Revisar lo que ya hizo el proveedor anterior (regla 4: cuesta lo mismo que hacer). |
| 4 | **INTEG** – Integración con sistema externo (ERP) | $2.100 | × 1,20 | **$2.520** | Urgencia por plazo fin de mes. |
| — | **DIAG** – Diagnóstico de procesos | — | — | **$0** | No se cotiza. El cliente ya tiene diagnóstico de otra consultora. |
| — | **CAPA** – Capacitación | — | — | **No incluido** | No solicitado explícitamente. Si lo desean, se cotiza aparte. |
| — | **SOP-3M** – Soporte 3 meses | — | — | **No incluido** | No solicitado explícitamente. Si lo desean, se cotiza aparte. |

---

### Totales

| Concepto | USD |
|----------|-----|
| Implementación avanzada (IMPL-AVZ) | 5.760 |
| Migración – terminar (MIGRA) | 1.920 |
| Revisión de migración ajena (MIGRA-REV) | 1.920 |
| Integración con ERP (INTEG) | 2.520 |
| **TOTAL** | **$12.120 USD** |

---

### Notas importantes

1. **Banda de ajuste:** Se aplicó un factor de **1,20** (20% de recargo) sobre el precio de referencia de cada ítem, debido a la urgencia del plazo (“para fin de mes”). Esto está dentro de la banda permitida (0,85 – 2,00).
2. **Absorción:** `IMPL-AVZ` ya incluye `IMPL-BAS`. No se cobran ambos.
3. **Revisión = hacer:** `MIGRA-REV` se cotiza al mismo precio que `MIGRA` (regla 4). Se cotizan ambos porque el cliente pide revisar lo existente *y* terminarlo.
4. **No cotizado:** Diagnóstico (ya tienen), capacitación y soporte (no pedidos). Si se requieren, se emite una cotización complementaria.

Quedamos a disposición para ajustar o aclarar cualquier punto.
