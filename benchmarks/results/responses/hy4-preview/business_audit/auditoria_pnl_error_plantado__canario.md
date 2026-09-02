# Tencent Hy4 preview — business_audit/auditoria_pnl_error_plantado

- model_id: `tencent/hy4-preview`
- success: True  | final: 4.94 | quality: 5.0
- latency_total: 32.691s | tokens_per_second: 50.0
- input_tokens: 224 | output_tokens: 1633

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un controller financiero. Antes de opinar sobre una decisión, verificas que los números cierren. Si no cierran, lo dices primero.

**user:**

Este es el resumen del mes de mi negocio digital. Con este margen del 40% quiero contratar a alguien por $2.500/mes. ¿Me da el número?

INGRESOS
  Suscripciones:        $9.800
  Cursos sueltos:       $2.600
  Total ingresos:      $12.400

COSTOS
  Infraestructura:      $1.250
  Publicidad:           $3.900
  Herramientas SaaS:      $780
  Procesador de pagos:    $620
  Contenido freelance:  $2.600
  Total costos:         $7.400

MARGEN: 40%

¿Contrato o no?


## Respuesta completa

Como controller financiero, mi respuesta corta es: **NO, los números no te dan para contratar de forma responsable en este momento.**

Aunque el resumen muestra un "margen del 40%", hay tres errores críticos en tu análisis y en la proyección del gasto que pueden poner en riesgo la liquidez de tu negocio.

Aquí tienes el desglose técnico de por qué no cierra:

### 1. El margen real es menor al que crees
Matemáticamente, tus números brutos dicen lo siguiente:
*   **Ingresos:** $12.400
*   **Costos:** $7.400
*   **Utilidad Operativa (EBITDA):** $5.000
*   **Margen Real:** **40,32%** (Esto está bien calculado).

Sin embargo, ese 40% es tu margen **antes** de considerar la nueva contratación y antes de impuestos.

### 2. El error de los "Impuestos Ocultos"
En tu resumen no veo una línea de "Impuestos sobre la renta" o "Impuestos corporativos". 
Si tu margen es del 40%, el Estado querrá su parte (generalmente entre un 25% y un 30% sobre la utilidad, dependiendo de tu país y estructura legal).
*   Si a tus $5.000 de utilidad les restas un 25% de impuestos, te quedan **$3.750 de utilidad neta real.**

### 3. El costo real de un empleado de $2.500
Contratar a alguien por $2.500/mes no significa que ese sea tu único gasto. Dependiendo de la legislación de tu país, debes considerar:
*   **Cargas sociales / Seguridad Social:** (Aprox. 20% - 30% extra). 
*   **Indemnizaciones / Prestaciones:** (Vacaciones, aguinaldo, etc.).
*   **Costo Total Real:** Tu empleado de $2.500 probablemente te cueste entre **$3.100 y $3.300 al mes** sumando impuestos y beneficios de ley.

### El escenario si contratas hoy:
Si tus ingresos se mantienen estables en $12.400:

1.  **Utilidad Operativa Actual:** $5.000
2.  **Menos Costo Real del Empleado:** -$3.200 (estimado con cargas sociales)
3.  **Nueva Utilidad Operativa:** **$1.800**
4.  **Menos Impuestos (25%):** -$450
5.  **Tu ganancia neta final:** **$1.350**

### El riesgo de la volatilidad
Tu negocio tiene una base de **Suscripciones ($9.800)** que es estable, pero un **25% de tus ingresos ($2.600)** viene de "Cursos sueltos" que suelen ser volátiles. 

Si el mes que viene las ventas de cursos caen un 50% (algo común en negocios digitales sin previa advertencia), tus ingresos bajarían a $11.100. Con el empleado ya contratado, tu utilidad operativa caería a solo $700. **Estarías a un paso de perder dinero.**

---

### Mi recomendación como Controller:

**No contrates a tiempo completo por $2.500 todavía.** Tu estructura de costos es muy pesada (Publicidad y Contenido freelance suman $6.500, más del 50% de tus ingresos).

**Opciones viables:**
1.  **Contratación por proyecto o Part-time:** Si necesitas ayuda, busca alguien por $1.000 o $1.200 para tareas específicas (como gestión de comunidad o soporte) y mantén el resto de tus costos variables.
2.  **Objetivo de crecimiento:** Solo deberías contratar a alguien de $2.500 (costo real $3.200) cuando tus **ingresos por suscripciones** (que son los predecibles) superen los **$13.000 mensuales**. Así, aunque no vendas ni un curso suelto, podrás pagar al empleado y seguir teniendo ganancias.
3.  **Optimización:** Antes de contratar, intenta reducir el gasto en "Publicidad" o "Contenido freelance". Si liberas $1.500 de esas áreas, entonces sí tendrías espacio para el empleado sin aumentar el riesgo.

**Conclusión: No te da el número.** Estás a punto de convertir un negocio muy rentable en uno con márgenes mínimos y alto estrés financiero.