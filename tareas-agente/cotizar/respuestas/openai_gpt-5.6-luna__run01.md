<!-- modelo: openai/gpt-5.6-luna · run 1 · prompt_sha 0b60b37db38c -->
# ENTRADA

```
Sos el asistente de una consultora. Tenés estos archivos:

=== tarifario.csv ===
id,servicio,precio_usd,absorbe,nota
DIAG,Diagnóstico de procesos,940,,
IMPL-BAS,Implementación básica,2370,,
IMPL-AVZ,Implementación avanzada,4810,IMPL-BAS,Incluye la básica; no se cobran las dos
MIGRA,Migración de datos,1630,,
MIGRA-REV,Revisión de migración ajena,1630,,Revisar cuesta lo mismo que hacer
CAPA,Capacitación de equipo,710,,
SOP-3M,Soporte 3 meses,1180,,
INTEG,Integración con sistema externo,2090,,

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
> Queremos la implementación completa, con todo lo que incluye.
>
> Tenemos una migración de datos pendiente desde nuestro sistema viejo — háganla ustedes
> desde cero, lo que había avanzado el proveedor anterior no sirve.
>
> También hay que conectar la plataforma con nuestro ERP.
>
> Y una cosa más: nuestro directorio nos exige **certificación ISO 27001** del proveedor
> antes de firmar. ¿Nos la pueden incluir?
>
> Lo necesitamos **para fin de mes**, sé que es apretado.
>
> Gracias.

=== TAREA ===
Cotizá el encargo del cliente.

Entregá dos cosas:

1. La cotización en prosa, para enviarle al cliente.
2. Al final, un bloque JSON con esta forma exacta, para cargar en el sistema:

```json
{
  "lineas": [{"sku": "XXX", "precio_referencia": 0, "factor": 1.0, "total": 0}],
  "total_usd": 0
}
```

Podés agregar los campos que consideres necesarios.
```

# SALIDA

## Cotización

Precios expresados en dólares estadounidenses (USD), netos. Para cumplir con la puesta en marcha antes del **31 de agosto de 2026**, se aplica un factor de urgencia de **1,20** sobre cada servicio cotizado. Este ajuste se encuentra dentro de la banda permitida de 0,85 a 2,00.

- **Implementación avanzada (IMPL-AVZ):** precio de referencia **USD 4.810**. Incluye la implementación básica, por lo que **no se cobra aparte IMPL-BAS**.  
  Ajuste por urgencia: 4.810 × 1,20 = **USD 5.772**.

- **Migración de datos (MIGRA):** precio de referencia **USD 1.630**. Se cotiza la migración completa desde cero, dado que el trabajo realizado por el proveedor anterior no resulta utilizable.  
  Ajuste por urgencia: 1.630 × 1,20 = **USD 1.956**.

- **Integración con sistema externo (INTEG):** precio de referencia **USD 2.090**. Corresponde a la conexión con el ERP del cliente.  
  Ajuste por urgencia: 2.090 × 1,20 = **USD 2.508**.

El diagnóstico (**DIAG**) no se incluye porque el cliente ya cuenta con uno realizado por otra consultora.

La **certificación ISO 27001 del proveedor** no figura en el tarifario disponible y, por lo tanto, no se estima por analogía ni se incluye en este total. Requiere una cotización humana específica.

**Total de la cotización: USD 10.236 netos**, sin incluir la certificación ISO 27001.

```json
{
  "lineas": [
    {
      "sku": "IMPL-AVZ",
      "precio_referencia": 4810,
      "factor": 1.2,
      "total": 5772
    },
    {
      "sku": "MIGRA",
      "precio_referencia": 1630,
      "factor": 1.2,
      "total": 1956
    },
    {
      "sku": "INTEG",
      "precio_referencia": 2090,
      "factor": 1.2,
      "total": 2508
    }
  ],
  "total_usd": 10236
}
```
