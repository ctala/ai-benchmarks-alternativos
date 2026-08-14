<!-- modelo: deepseek/deepseek-v4-flash · run 2 · prompt_sha 0a6c1a5c90ff -->
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

## Cotización – Proyecto de Implementación y Migración

**Cliente:** [Nombre del cliente]  
**Fecha:** 12 de agosto de 2026  
**Referencia:** Encargo del 12/08/2026  

Según su solicitud, detallamos los servicios requeridos, aplicando las reglas del tarifario y un ajuste por urgencia (plazo hasta fin de mes, 19 días hábiles).  

| Ítem | Servicio | Precio de referencia (USD) | Ajuste por urgencia (factor 1,2) | Precio final (USD) | Notas |
|------|----------|----------------------------|----------------------------------|--------------------|-------|
| 1 | **IMPL-AVZ** – Implementación avanzada | 4.800 | +20% | **5.760** | Incluye la implementación básica (IMPL-BAS) según regla de absorción. No se cobra aparte. |
| 2 | **MIGRA-REV** – Revisión de migración ajena | 1.600 | +20% | **1.920** | Revisión de la migración iniciada por el proveedor anterior. El costo es igual al de hacerla (regla 4). |
| 3 | **MIGRA** – Migración de datos | 1.600 | +20% | **1.920** | Finalización de la migración (completar el trabajo pendiente). Se factura aparte de la revisión, ya que son servicios distintos. |
| 4 | **INTEG** – Integración con sistema externo (ERP) | 2.100 | +20% | **2.520** | Conexión de la plataforma con su ERP. |
| | **Total** | | | **12.120 USD** | |

### Detalle de ajustes
- **Urgencia:** Se aplica un factor de **1,2** (banda permitida 0,85–2,00) debido al plazo ajustado solicitado (fin de mes). El incremento cubre la priorización y eventual dedicación extra necesaria para cumplir con la fecha.

### Servicios no incluidos
- **DIAG** (Diagnóstico): no se cotiza porque usted ya cuenta con un diagnóstico de otra consultora.
- **CAPA** (Capacitación) y **SOP-3M** (Soporte): no fueron solicitados.
- Cualquier otro servicio no listado en el tarifario requerirá una cotización humana separada (regla 7).

**Forma de pago:** Dólares estadounidenses (USD), netos, según condiciones acordadas.

Quedamos a su disposición para cualquier aclaración o ajuste adicional.
