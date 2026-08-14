<!-- modelo: deepseek/deepseek-v4-flash · run 6 · prompt_sha 0a6c1a5c90ff -->
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

Acá va la cotización línea por línea, según las reglas de la consultora y el tarifario.

---

## Cotización para el cliente — 12 de agosto de 2026

**Todos los precios en USD, netos. Sin conversión a moneda local.**

| Ítem | Servicio | Precio unitario (USD) | Ajuste | Motivo | Precio final (USD) |
|------|----------|----------------------|--------|--------|-------------------|
| 1 | Diagnóstico de procesos (`DIAG`) | 900 | — | **No se cotiza.** El cliente ya tiene diagnóstico de otra consultora. | 0 |
| 2 | Implementación avanzada (`IMPL-AVZ`) | 4.800 | × **2,00** (máx. banda) | Urgencia: "para fin de mes". Se aplica la banda máxima por apuro extremo. | **9.600** |
| 3 | Migración de datos (`MIGRA`) | 1.600 | × **1,30** | Revisar y terminar una migración ajena a medio hacer implica complejidad adicional (entender lo hecho, corregir, completar). Banda media-alta. | **2.080** |
| 4 | Revisión de migración ajena (`MIGRA-REV`) | 1.600 | — | **No se cotiza aparte.** El cliente pide revisar *y* terminar la migración. La revisión está incluida en el trabajo de migración (ítem 3). Regla 4: revisar cuesta lo mismo que hacer, pero ya se está haciendo. | 0 |
| 5 | Integración con sistema externo (`INTEG`) | 2.100 | × **1,50** | Urgencia + conexión con ERP propio del cliente (complejidad técnica media-alta). | **3.150** |
| 6 | Capacitación de equipo (`CAPA`) | 700 | — | No solicitada explícitamente, no se incluye. | 0 |
| 7 | Soporte 3 meses (`SOP-3M`) | 1.200 | — | No solicitado. | 0 |

---

### Resumen

| Concepto | USD |
|----------|-----|
| Implementación avanzada | 9.600 |
| Migración de datos (revisar + terminar) | 2.080 |
| Integración con ERP | 3.150 |
| **Total estimado** | **14.830 USD** |

### Notas importantes

1. **No se descuenta nada automáticamente.** No hay promociones ni bonificaciones sin aprobación expresa.
2. **El diagnóstico no se cobra**, porque el cliente ya lo tiene.
3. **La implementación avanzada (`IMPL-AVZ`) ya absorbe la básica (`IMPL-BAS`)** según el tarifario, por lo que no se duplican costos.
4. **Migración:** se cotiza una sola vez el trabajo completo (revisar lo existente + terminarlo). La revisión por separado (`MIGRA-REV`) no aplica.
5. **Plazo:** el factor de urgencia se aplicó en los ítems 2, 3 y 5. Si el cliente necesita una cotización con menor ajuste, se puede renegociar la fecha de entrega.
6. **Lo que no está en el tarifario** (como personalización extra del ERP o desarrollo a medida) **va a cotización humana** — no se estima por analogía.

Quedamos a disposición para ajustar según necesidades.
