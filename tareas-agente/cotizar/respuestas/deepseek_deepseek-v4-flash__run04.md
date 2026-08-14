<!-- modelo: deepseek/deepseek-v4-flash · run 4 · prompt_sha 0a6c1a5c90ff -->
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

Acá va la cotización línea por línea, según las reglas del tarifario y lo que pide el cliente.

---

## Cotización (USD) — Proyecto plataforma

**Cliente:** [Sin identificar]  
**Fecha:** 12 de agosto de 2026  
**Plazo solicitado:** Fin de agosto (urgencia)

---

### 1. Diagnóstico de procesos (DIAG)
**No se cotiza.**  
El cliente declara que ya tiene un diagnóstico hecho por otra consultora. Aunque no se especifica si es completo o válido, por regla 7 (lo que no está en el tarifario o no aplica no se estima) se omite. Si el cliente pidiera revisar ese diagnóstico, eso no está en el tarifario y requeriría cotización humana.

---

### 2. Implementación avanzada (IMPL-AVZ)
**Precio de referencia:** USD 4.800  
**Absorbe a:** IMPL-BAS (no se cobra aparte)  
**Motivo:** El cliente pide "la implementación completa, con todo lo que incluye". Según el tarifario, IMPL-AVZ ya incluye la básica.

**Ajuste por urgencia:**  
Plazo muy ajustado (fin de mes, 19 días desde hoy). Se aplica el extremo superior de la banda de ajuste: **2,00**.  
→ Precio final: 4.800 × 2,00 = **USD 9.600**

---

### 3. Migración de datos (MIGRA) + Revisión de migración ajena (MIGRA-REV)
**Contexto:** El cliente tiene una migración empezada por otro proveedor, quedó a medias. Pide que alguien la **revise y la termine**.  
Esto implica dos servicios diferentes:

- **Revisar** lo hecho hasta ahora → MIGRA-REV (USD 1.600, según regla 4: cuesta lo mismo que hacer).
- **Terminar** la migración → MIGRA (USD 1.600).

Ambos se cotizan por separado porque son etapas distintas y el tarifario los distingue. No hay absorción entre ellos.

**Ajuste por urgencia (aplica a ambos):**  
Se aplica la misma banda 2,00 por el plazo único.

- MIGRA-REV: 1.600 × 2,00 = **USD 3.200**
- MIGRA: 1.600 × 2,00 = **USD 3.200**

---

### 4. Integración con sistema externo (INTEG)
**Precio de referencia:** USD 2.100  
**Motivo:** El cliente pide conectar la plataforma con su ERP.

**Ajuste por urgencia:**  
Ídem, banda 2,00.  
→ Precio final: 2.100 × 2,00 = **USD 4.200**

---

### 5. Capacitación de equipo (CAPA) y Soporte 3 meses (SOP-3M)
**No se cotizan automáticamente.**  
El cliente no los menciona. Si se consideraran necesarios, deberían pedirse explícitamente o cotizarse como recomendación aparte. Por regla 7, no se agregan sin pedido.

---

## Resumen de la cotización

| Ítem | Precio final (USD) |
|------|-------------------|
| IMPL-AVZ (incluye IMPL-BAS) | 9.600 |
| MIGRA-REV (revisión) | 3.200 |
| MIGRA (terminar) | 3.200 |
| INTEG (ERP) | 4.200 |
| **Total** | **20.200 USD** |

---

**Nota:**  
- Todos los precios son netos en USD, no convertidos a moneda local.  
- El ajuste por urgencia (×2,00) se aplicó sobre el precio de referencia de cada ítem, según regla 2.  
- Cualquier servicio no listado (como revisar el diagnóstico ajeno o capacitación) deberá cotizarse por separado con intervención humana.
