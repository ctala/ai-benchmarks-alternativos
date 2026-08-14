<!-- modelo: openai/gpt-5.6-luna · run 7 · prompt_sha 0a6c1a5c90ff -->
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

## Cotización preliminar

**Moneda:** USD netos  
**Ajuste aplicado:** factor **1,25** por urgencia de entrega para fin de mes. Se aplica sobre el precio de referencia de cada ítem, no sobre precios de lista alternativos.

| Ítem | Precio de referencia | Ajuste | Precio cotizado | Motivo |
|---|---:|---:|---:|---|
| **IMPL-AVZ — Implementación avanzada** | USD 4.800 | × 1,25 | **USD 6.000** | Corresponde a la implementación completa. Incluye la implementación básica, por lo que **no se cobra IMPL-BAS aparte**. |
| **MIGRA-REV — Revisión de migración ajena** | USD 1.600 | × 1,25 | **USD 2.000** | La migración fue iniciada por otro proveedor. Revisar cuesta lo mismo que hacerla; no se aplica descuento por tratarse de una revisión. |
| **INTEG — Integración con sistema externo** | USD 2.100 | × 1,25 | **USD 2.625** | Conexión con el ERP externo. |

### Total cotizado hasta el alcance definido

**USD 10.625 netos**

### Alcance pendiente de cotización humana

La solicitud también incluye **terminar la migración parcialmente realizada**. El tarifario contempla la migración de datos completa y la revisión de una migración ajena, pero no define un precio específico para completar una migración inconclusa.

Por lo tanto, **no se agrega automáticamente el precio de MIGRA ni se estima por analogía**. La finalización deberá relevarse y cotizarse por separado.
