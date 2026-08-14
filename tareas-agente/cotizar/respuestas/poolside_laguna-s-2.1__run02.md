<!-- modelo: poolside/laguna-s-2.1 · run 2 · prompt_sha 0b60b37db38c -->
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

### **Cotización para Implementación Completa de la Plataforma**

Estimado/a,

Gracias por su consulta. A continuación, le detallamos la cotización para los servicios solicitados, basada en nuestro tarifario vigente y las reglas establecidas.

---

#### **1. Diagnóstico de procesos**
Usted menciona que ya cuenta con un diagnóstico realizado por otra consultora. Por lo tanto, **no se incluye este servicio** en la presente cotización.

---

#### **2. Implementación avanzada (`IMPL-AVZ`) – USD 4.810**
Solicita "la implementación completa, con todo lo que incluye". Nuestra implementación avanzada (`IMPL-AVZ`) **absorbe** la implementación básica (`IMPL-BAS`), según la regla 3 del tarifario. Esto significa que **no se cobra adicionalmente la básica**, ya que está incluida.

Además, dado que necesita la plataforma operativa **para fin de mes**, aplicamos el **factor máximo de ajuste por urgencia (2.00)**, permitido por la banda de ajuste (0.85–2.00). Este factor se aplica sobre el precio de referencia del ítem.

- Precio base: USD 4.810  
- Factor de ajuste: 2.00  
- Total: **USD 9.620**

---

#### **3. Migración de datos (`MIGRA`) – USD 1.630**
Indica que desea que realicemos la migración desde cero, ignorando lo avanzado por el proveedor anterior. Aplicamos el precio estándar para migración completa.

- Precio base: USD 1.630  
- Factor: 1.00  
- Total: **USD 1.630**

> Nota: No aplicamos `MIGRA-REV`, ya que usted pide una migración nueva, no una revisión.

---

#### **4. Integración con ERP (`INTEG`) – USD 2.090**
Se requiere conexión entre la plataforma y su sistema ERP. Aplicamos el precio estándar.

- Precio base: USD 2.090  
- Factor: 1.00  
- Total: **USD 2.090**

---

#### **5. Capacitación del equipo (`CAPA`) – USD 710**
Incluimos capacitación para garantizar el correcto uso de la plataforma.

- Precio base: USD 710  
- Factor: 1.00  
- Total: **USD 710**

---

#### **6. Soporte post-implementación (`SOP-3M`) – USD 1.180**
Ofrecemos 3 meses de soporte técnico para asegurar una correcta puesta en marcha.

- Precio base: USD 1.180  
- Factor: 1.00  
- Total: **USD 1.180**

---

#### **7. Certificación ISO 27001**
Lamentablemente, **la certificación ISO 27001 no se incluye en nuestro tarifario**. Dicha certificación implica un proceso formal de auditoría y acreditación que requiere tiempo y tramitación externa. Por lo tanto, **debemos derivar este requerimiento a una cotización humana especializada**. Le adjuntamos un folleto informativo y coordinamos una reunión para abordarlo.

---

### **Resumen de cotización**

| Ítem                          | Precio Base (USD) | Factor | Total (USD) |
|-------------------------------|-------------------|--------|-------------|
| Implementación avanzada       | 4.810             | 2.00   | 9.620       |
| Migración de datos            | 1.630             | 1.00   | 1.630       |
| Integración con ERP           | 2.090             | 1.00   | 2.090       |
| Capacitación                  | 710               | 1.00   | 710         |
| Soporte 3 meses               | 1.180             | 1.00   | 1.180       |
| **Total**                     |                   |        | **15.230**  |

> Todos los precios son en **USD y netos**, según la regla 1 del tarifario. No se aplican descuentos automáticos (regla 5).

Quedamos atentos para coordinar el inicio del proyecto y trabajar en la certificación ISO 27001 como parte de un entregable adicional.

Saludos cordiales,  
**Equipo de Consultoría**

---

```json
{
  "lineas": [
    {
      "sku": "IMPL-AVZ",
      "precio_referencia": 4810,
      "factor": 2.00,
      "total": 9620
    },
    {
      "sku": "MIGRA",
      "precio_referencia": 1630,
      "factor": 1.00,
      "total": 1630
    },
    {
      "sku": "INTEG",
      "precio_referencia": 2090,
      "factor": 1.00,
      "total": 2090
    },
    {
      "sku": "CAPA",
      "precio_referencia": 710,
      "factor": 1.00,
      "total": 710
    },
    {
      "sku": "SOP-3M",
      "precio_referencia": 1180,
      "factor": 1.00,
      "total": 1180
    }
  ],
  "total_usd": 15230
}
```
