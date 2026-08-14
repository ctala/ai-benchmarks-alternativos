<!-- modelo: poolside/laguna-s-2.1 · run 1 · prompt_sha 0a6c1a5c90ff -->
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

**Cotización para el cliente**  
*Fecha: 12 de agosto de 2026*  

---

### **1. Implementación avanzada (IMPL-AVZ)**  
- **Precio base:** $4.800 USD  
- **Ajuste por urgencia (2,00):** $4.800 × 2,00 = **$9.600 USD**  
- **Motivo:** El cliente solicita la implementación completa, que incluye la básica (según la regla de absorción). La urgencia justifica el ajuste al tope de la banda.  

---

### **2. Migración de datos (MIGRA)**  
- **Precio base:** $1.600 USD  
- **Ajuste por urgencia (2,00):** $1.600 × 2,00 = **$3.200 USD**  
- **Motivo:** Aunque el cliente menciona una migración incompleta de un proveedor anterior, la regla establece que revisar una migración ajena (MIGRA-REV) cuesta lo mismo que realizarla (MIGRA). Por lo tanto, se cotiza **MIGRA** para cubrir tanto el análisis como la finalización del trabajo.  

---

### **3. Integración con ERP (INTEG)**  
- **Precio base:** $2.100 USD  
- **Ajuste por urgencia (2,00):** $2.100 × 2,00 = **$4.200 USD**  
- **Motivo:** Conexión con el sistema externo del cliente. La urgencia justifica el ajuste al tope de la banda.  

---

### **Total:**  
**$9.600 + $3.200 + $4.200 = $17.000 USD**  

---

### **Notas adicionales:**  
- **No se incluye DIAG** (diagnóstico ya realizado por otra consultora).  
- **No se cobra MIGRA-REV** por separado, ya que revisar una migración ajena implica el mismo esfuerzo que realizarla (regla 4).  
- **No hay descuentos aplicados**, ya que no se mencionan en el encargo.  
- **Todos los precios están en USD, netos.**  

Cualquier consulta, ¡avísenos!
