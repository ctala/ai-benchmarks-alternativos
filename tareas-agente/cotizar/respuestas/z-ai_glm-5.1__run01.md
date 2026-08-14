<!-- modelo: z-ai/glm-5.1 · run 1 · prompt_sha 0a6c1a5c90ff -->
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

¡Hola! Acá va la cotización basada en el tarifario y las reglas de la consultora, respondiendo al correo del cliente.

***

**Cotización — Puesta en marcha de plataforma**
**Fecha:** 12 de agosto de 2026
**Validez:** Precios en USD, netos.

Ítems cotizados:

**1. IMPL-AVZ — Implementación avanzada**
*   Precio de referencia: USD 4.800
*   Ajuste: x1,50 (Urgencia: plazo hasta fin de mes)
*   **Precio final: USD 7.200**
*   *Nota:* El cliente solicita la "implementación completa". De acuerdo con las reglas, este servicio absorbe la implementación básica (IMPL-BAS), por lo que no se cotiza ni cobra la básica por separado.

**2. MIGRA-REV — Revisión de migración ajena**
*   Precio de referencia: USD 1.600
*   Ajuste: x1,50 (Urgencia: plazo hasta fin de mes)
*   **Precio final: USD 2.400**
*   *Nota:* El cliente pide que se revise la migración a medias. De acuerdo con las reglas, revisar cuesta lo mismo que hacer; no hay descuento por "solo revisar".

**3. MIGRA — Migración de datos**
*   Precio de referencia: USD 1.600
*   Ajuste: x1,50 (Urgencia: plazo hasta fin de mes)
*   **Precio final: USD 2.400**
*   *Nota:* El cliente pide que, además de revisar, se "termine" la migración. Como no existe una tarifa para "medio trabajo" y no se estima por analogía, se cotiza el servicio completo de migración para completar la tarea.

**4. INTEG — Integración con sistema externo (ERP)**
*   Precio de referencia: USD 2.100
*   Ajuste: x1,50 (Urgencia: plazo hasta fin de mes)
*   **Precio final: USD 3.150**

---

**Ítems excluidos (a solicitud del cliente):**
*   **DIAG (Diagnóstico de procesos):** No se cotiza ya que el cliente indica que ya lo tienen hecho por otra consultora.

---

**Resumen de la cotización:**

| Ítem | Servicio | Precio Ref. (USD) | Ajuste | Precio Final (USD) |
| :--- | :--- | :--- | :--- | :--- |
| IMPL-AVZ | Implementación avanzada | 4.800 | x1,50 | 7.200 |
| MIGRA-REV | Revisión de migración ajena | 1.600 | x1,50 | 2.400 |
| MIGRA | Migración de datos | 1.600 | x1,50 | 2.400 |
| INTEG | Integración con sistema externo | 2.100 | x1,50 | 3.150 |
| **TOTAL** | | **10.100** | | **15.150** |

*El ajuste del 50% (x1,50) sobre el precio de referencia de cada ítem se debe a la urgencia del plazo requerido (fin de mes), el cual se encuentra dentro de la banda de ajuste permitida (0,85 a 2,00).*
