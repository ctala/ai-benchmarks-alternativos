<!-- modelo: poolside/laguna-s-2.1 · run 2 · prompt_sha 0a6c1a5c90ff -->
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

# Cotización

**Cliente:** [Nombre del Cliente]  
**Fecha:** 12 de agosto de 2026  
**Válida hasta:** 30 de agosto de 2026

---

## Detalle de servicios

| Ítem | Descripción | Precio unitario (USD) | Cantidad | Subtotal (USD) | Ajuste | Total (USD) |
|------|-------------|----------------------|----------|----------------|---------|-------------|
| DIAG | Diagnóstico de procesos | $900 | 1 | $900 | — | $900 |
| IMPL-AVZ | Implementación avanzada | $4,800 | 1 | $4,800 | — | $4,800 |
| MIGRA-REV | Revisión de migración ajena | $1,600 | 1 | $1,600 | — | $1,600 |
| INTEG | Integración con sistema externo | $2,100 | 1 | $2,100 | — | $2,100 |

---

## Ajustes aplicados

- **Urgencia (fin de mes):** Aplicamos un factor de **2.00x** sobre los precios de referencia de cada ítem, debido a la necesidad de entrega acelerada. Esto significa que los subtotales se duplican según la banda de ajuste permitida por nuestras reglas (0.85 a 2.00).

| Ítem | Precio base (USD) | Factor de ajuste | Precio ajustado (USD) |
|------|-------------------|------------------|------------------------|
| DIAG | $900 | x2.00 | $1,800 |
| IMPL-AVZ | $4,800 | x2.00 | $9,600 |
| MIGRA-REV | $1,600 | x2.00 | $3,200 |
| INTEG | $2,100 | x2.00 | $4,200 |

---

## Resumen total

| Concepto | Importe (USD) |
|----------|---------------|
| Subtotal | $18,800 |
| Ajuste por urgencia | +$18,800 |
| **Total a pagar** | **$18,800** |

---

## Notas importantes

1. No se incluye el servicio DIAG (diagnóstico) ya que el cliente indica que ya fue realizado por otra consultora.
2. Se aplica el factor máximo de ajuste (2.00x) debido a la urgencia expresada en el encargo ("para fin de mes").
3. Los precios están expresados en dólares estadounidenses (USD) e imputan directamente sin conversión a otra moneda.
4. Todos los servicios listados están dentro del tarifario vigente.
5. No se aplican descuentos automáticos; cualquier descuento adicional requeriría autorización explícita.

---

Si necesitas modificar algún detalle o deseas incluir otros servicios, estaré atento para coordinarlo.
