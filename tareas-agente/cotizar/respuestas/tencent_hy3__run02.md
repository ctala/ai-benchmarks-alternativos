<!-- modelo: tencent/hy3 · run 2 · prompt_sha 0b60b37db38c -->
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

**Cotización preliminar — 12 de agosto de 2026**

Estimados,

A continuación les detallamos la cotización de los servicios que podemos facturar directamente según nuestro tarifario, más una nota sobre el ítem que requiere evaluación humana por no estar contemplado en lista.

**1. Implementación avanzada (IMPL-AVZ)**
- Precio de referencia: USD 4.810
- Este servicio absorbe la implementación básica (IMPL-BAS), por lo que no se cobra por separado (regla de tarifario).
- Al requerir todo el proyecto para fin de mes (plazo ajustado), aplicamos un factor de urgencia de 1,8 sobre el precio de referencia del ítem (dentro de la banda permitida de 0,85 a 2,00).
- **Subtotal: USD 8.658**

**2. Migración de datos desde cero (MIGRA)**
- Precio de referencia: USD 1.630
- Corresponde la migración completa porque el avance previo no sirve; no es revisión de terceros (no aplica descuento alguno por "solo revisar", regla 4).
- Factor de urgencia 1,8 por el mismo plazo de entrega.
- **Subtotal: USD 2.934**

**3. Integración con ERP (INTEG)**
- Precio de referencia: USD 2.090
- Conexión de la plataforma con su sistema externo (ERP).
- Factor de urgencia 1,8 por plazo de fin de mes.
- **Subtotal: USD 3.762**

**No se incluyen en esta cotización:**
- *Diagnóstico de procesos (DIAG)*: tal como indican, ya cuentan con uno de otra consultora; no se cobra.
- *Capacitación (CAPA)* y *Soporte 3 meses (SOP-3M)*: no fueron solicitados; pueden agregarse si los requieren.

**Pendiente de cotización humana:**
- *Certificación ISO 27001*: este requisito de su directorio no está en nuestro tarifario estándar. Por regla 7, no se estima por analogía y va a cotización humana. Les enviaremos un número dedicado a la brevedad.

**Total cotizable según tarifario (sin ISO 27001): USD 15.354**

Quedamos a su disposición para ajustar alcance o adelantar la cotización humana de la certificación.

---

```json
{
  "lineas": [
    {
      "sku": "IMPL-AVZ",
      "precio_referencia": 4810,
      "factor": 1.8,
      "total": 8658,
      "nota": "Incluye IMPL-BAS (absorbe); no se cobra aparte. Factor 1.8 por urgencia (fin de mes)."
    },
    {
      "sku": "MIGRA",
      "precio_referencia": 1630,
      "factor": 1.8,
      "total": 2934,
      "nota": "Migración desde cero. Factor 1.8 por urgencia."
    },
    {
      "sku": "INTEG",
      "precio_referencia": 2090,
      "factor": 1.8,
      "total": 3762,
      "nota": "Integración con ERP. Factor 1.8 por urgencia."
    }
  ],
  "total_usd": 15354,
  "cotizacion_humana": [
    {
      "sku": "ISO-27001",
      "motivo": "No está en el tarifario. Certificación requerida por el directorio. Requiere cotización humana (regla 7)."
    }
  ],
  "excluidos": [
    {
      "sku": "DIAG",
      "motivo": "Cliente ya tiene diagnóstico de otra consultora; no se cobra."
    },
    {
      "sku": "IMPL-BAS",
      "motivo": "Absorbido por IMPL-AVZ."
    },
    {
      "sku": "MIGRA-REV",
      "motivo": "No aplica; se hace migración desde cero (MIGRA)."
    },
    {
      "sku": "CAPA",
      "motivo": "No solicitado."
    },
    {
      "sku": "SOP-3M",
      "motivo": "No solicitado."
    }
  ]
}
```
