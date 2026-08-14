<!-- modelo: tencent/hy3 · run 1 · prompt_sha 0a6c1a5c90ff -->
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

**Cotización — Encargo del 12 de agosto de 2026**

*Nota: Precios en dólares estadounidenses (USD), netos, sin conversión a moneda local (Regla 1).*

A continuación, el desglose línea por línea del encargo según el tarifario y las reglas de la consultora:

---

### 1. Implementación avanzada (IMPL-AVZ)
- **Precio de referencia:** 4.800 USD  
- **Detalle:** El cliente solicita "la implementación completa, con todo lo que incluye". El tarifario indica que `IMPL-AVZ` absorbe a `IMPL-BAS` (Regla 3), por lo que la implementación básica no se cobra por separado.  
- **Ajuste:** Se aplica un factor de **1.5x** por urgencia (plazo a fin de mes). Este valor está dentro de la banda de ajuste permitida de 0,85 a 2,00 sobre el precio de referencia (Regla 2).  
- **Precio final:** 4.800 × 1.5 = **7.200 USD**

### 2. Revisión de migración ajena (MIGRA-REV)
- **Precio de referencia:** 1.600 USD  
- **Detalle:** El cliente tiene una migración a medias de un proveedor anterior y pide que se revise. Por Regla 4, revisar una migración ajena cuesta igual que hacerla; no hay descuento por "solo revisar".  
- **Ajuste:** Se aplica factor de **1.5x** por urgencia (mismo plazo ajustado, Regla 2).  
- **Precio final:** 1.600 × 1.5 = **2.400 USD**

### 3. Integración con sistema externo (INTEG)
- **Precio de referencia:** 2.100 USD  
- **Detalle:** El cliente requiere conectar la plataforma con su ERP.  
- **Ajuste:** Se aplica factor de **1.5x** por urgencia (Regla 2).  
- **Precio final:** 2.100 × 1.5 = **3.150 USD**

---

### Ítems excluidos o pendientes de cotización humana

- **Diagnóstico (DIAG):** El cliente aclara que ya cuenta con un diagnóstico de otra consultora, por lo que no se incluye en el encargo.
- **Finalización de la migración (completar lo a medias):** El cliente pide "revisar y terminar" la migración. El tarifario contempla hacer la migración completa (`MIGRA`) o revisarla (`MIGRA-REV`), pero no existe un ítem específico para completar una migración parcial de un tercero. Por Regla 7, lo que no está en el tarifario va a cotización humana y no se estima por analogía. Este costo **no está incluido** en los números anteriores.
- **Capacitación (CAPA) y Soporte (SOP-3M):** No fueron mencionados en el correo, por lo que no se cotizan.

---

### Resumen
- IMPL-AVZ: 7.200 USD  
- MIGRA-REV: 2.400 USD  
- INTEG: 3.150 USD  
- **Total cotizable en esta instancia:** **12.750 USD**  
- **Pendiente:** Cotización humana para la finalización de la migración a medias.  

*(Sin descuentos automáticos aplicados, según Regla 5).*
