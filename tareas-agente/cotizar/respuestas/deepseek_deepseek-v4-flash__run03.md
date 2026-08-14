<!-- modelo: deepseek/deepseek-v4-flash · run 3 · prompt_sha 0a6c1a5c90ff -->
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

Aquí tienes la cotización detallada, línea por línea, según las reglas establecidas.

---

**Cotización – Proyecto de Implementación, Migración e Integración**  
**Fecha:** 12 de agosto de 2026  
**Cliente:** [Nombre del Cliente]  
**Moneda:** USD (netos, no convertidos)

---

### 1. Diagnóstico de procesos (DIAG)
| Ítem | Precio de lista | Ajuste | Precio final | Motivo |
|------|----------------|--------|--------------|--------|
| DIAG | $900 | No aplica | **$0** | El cliente ya tiene un diagnóstico hecho por otra consultora. No se cotiza. |

---

### 2. Implementación avanzada (IMPL-AVZ)
| Ítem | Precio de lista | Ajuste | Precio final | Motivo |
|------|----------------|--------|--------------|--------|
| IMPL-AVZ | $4.800 | Banda 2,00 (urgencia: "para fin de mes") | **$9.600** | Incluye la implementación básica (IMPL-BAS) según tarifario; no se cobran ambas. Se aplica banda 2,00 por plazo extremadamente ajustado. |

*Nota: IMPL-BAS queda absorbido por IMPL-AVZ y no se factura.*

---

### 3. Migración de datos – Revisión y finalización
El cliente necesita:
- Revisar una migración ajena que quedó a medias.
- Terminarla.

Según regla 4: *"Revisar cuesta lo mismo que hacer"*, por lo que no hay descuento.

Además, se requiere:
- Revisar = MIGRA-REV ($1.600)
- Terminar = MIGRA ($1.600)

Ambos se cotizan por separado, pues son trabajos distintos sobre la misma migración (revisar lo existente + completar lo pendiente).

| Ítem | Precio de lista | Ajuste | Precio final | Motivo |
|------|----------------|--------|--------------|--------|
| MIGRA-REV | $1.600 | Banda 2,00 (urgencia) | **$3.200** | Revisión completa de migración iniciada por otro proveedor. Plazo ajustado. |
| MIGRA | $1.600 | Banda 2,00 (urgencia) | **$3.200** | Finalización de la migración. Plazo ajustado. |

---

### 4. Integración con sistema externo (INTEG)
| Ítem | Precio de lista | Ajuste | Precio final | Motivo |
|------|----------------|--------|--------------|--------|
| INTEG | $2.100 | Banda 2,00 (urgencia) | **$4.200** | Conexión con ERP del cliente. Plazo ajustado. |

---

### 5. Capacitación y soporte
El cliente no los menciona explícitamente, pero solicita "todo lo que incluye". Según tarifario:
- CAPA (capacitación): no está mencionada en el encargo ni es parte obligatoria de la implementación. No se incluye automáticamente.
- SOP-3M (soporte): no fue solicitado. No se incluye.

Ambos quedan fuera de esta cotización. Si el cliente los requiere, debemos pedir confirmación por escrito.

---

### Resumen final

| Concepto | Monto (USD) |
|----------|-------------|
| Diagnóstico (DIAG) – No aplica | $0 |
| Implementación avanzada (IMPL-AVZ) | $9.600 |
| Revisión de migración ajena (MIGRA-REV) | $3.200 |
| Finalización de migración (MIGRA) | $3.200 |
| Integración con ERP (INTEG) | $4.200 |
| **Total estimado** | **$20.200** |

**Nota:** Todos los precios incluyen el factor de urgencia (banda 2,00) por la fecha límite de fin de mes. Si el plazo se flexibiliza, los precios pueden reducirse.

---

*¿Aprobamos esta cotización para enviar al cliente?*
