<!-- modelo: tencent/hy3 · run 1 · prompt_sha 0b60b37db38c -->
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

Hola equipo,

Les dejo la cotización del encargo del cliente, redactada para enviar y con su bloque JSON para carga en sistema.

---

### Cotización — Plataforma y servicios asociados

Estimados,

Gracias por su mensaje. Con base en nuestro tarifario y reglas de cotización, armamos el presupuesto de los servicios que sí podemos tarifar a la fecha. Les detallamos línea por línea:

1. **Diagnóstico (DIAG):** *Excluido.* Indican que ya cuentan con un diagnóstico de otra consultora, así que no cobramos este ítem.
2. **Implementación completa (IMPL-AVZ):** **USD 4.810** (precio de referencia). Corresponde a la Implementación avanzada, la cual absorbe la Implementación básica (IMPL-BAS) según nuestras reglas. Por lo tanto, no se cobran ambas por separado.
3. **Migración de datos (MIGRA):** **USD 1.630** (precio de referencia). Se cotiza la ejecución desde cero, descartando el trabajo previo del proveedor anterior, según lo pedido.
4. **Integración con ERP (INTEG):** **USD 2.090** (precio de referencia). Conectamos la plataforma con su sistema externo.

**Ajuste por urgencia:** Solicitan tener todo operativo para fin de mes, lo que implica un cronograma muy comprimido. Aplicamos un factor de **1,5** (recargo del 50%) sobre el precio de referencia de cada ítem, dentro de nuestra banda de ajuste permitida (0,85 a 2,00). 
- IMPL-AVZ: 4.810 × 1,5 = 7.215 USD
- MIGRA: 1.630 × 1,5 = 2.445 USD
- INTEG: 2.090 × 1,5 = 3.135 USD

**Certificación ISO 27001:** Este requerimiento **no está en nuestro tarifario**. Por política de la consultora, lo que no figura en la lista va a cotización humana (no se estima por analogía). Lo derivaremos a nuestro equipo para presupuestar aparte y les enviaremos el valor confirmado antes de la firma.

**Total estimado (servicios tarifados):** 12.795 USD (netos, en dólares).

Quedamos a la espera de sus comentarios y del avance de la cotización humana para la certificación.

Saludos,

*Asistente de la consultora*

---

```json
{
  "lineas": [
    {
      "sku": "IMPL-AVZ",
      "precio_referencia": 4810,
      "factor": 1.5,
      "total": 7215,
      "detalle": "Implementación avanzada (absorbe IMPL-BAS, no se cobra aparte)"
    },
    {
      "sku": "MIGRA",
      "precio_referencia": 1630,
      "factor": 1.5,
      "total": 2445,
      "detalle": "Migración de datos desde cero"
    },
    {
      "sku": "INTEG",
      "precio_referencia": 2090,
      "factor": 1.5,
      "total": 3135,
      "detalle": "Integración con sistema externo (ERP)"
    }
  ],
  "total_usd": 12795,
  "exclusiones": [
    "DIAG: solicitado explícitamente por el cliente (ya lo poseen)"
  ],
  "cotizacion_humana": [
    "ISO 27001: no figura en tarifario, requiere evaluación humana"
  ]
}
```
