# Tencent Hy4 preview — business_audit/auditoria_pnl_error_plantado

- model_id: `tencent/hy4-preview`
- success: True  | final: 1.46 | quality: 0.0
- latency_total: 29.24s | tokens_per_second: 49.5
- input_tokens: 224 | output_tokens: 1446

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

Como controller financiero, mi respuesta corta es: **No, los números no te dan con seguridad.**

Aunque tu margen del 40% es excelente, estás cometiendo un error común: confundir **Rentabilidad** con **Liquidez**.

Aquí tienes el análisis de por qué los números no cierran como esperas:

### 1. El desglose real de tu dinero
Vamos a ver dónde está ese 40% de margen (Utilidad Operativa):

*   **Ingresos Totales:** $12.400
*   **Costos Totales:** $7.400
*   **Utilidad Operativa (EBITDA):** **$5.000** (Efectivamente, es el 40% de tus ingresos).

### 2. El impacto de la contratación
Si contratas a alguien por $2.500, ese gasto entra directamente a tu estado de resultados:

*   **Utilidad actual:** $5.000
*   **Nuevo costo fijo (Salario):** -$2.500
*   **Nueva Utilidad Operativa:** **$2.500**
*   **Nuevo Margen:** **20%**

### 3. El problema del "Margen de Seguridad"
Aquí es donde los números **no me cuadran para una decisión responsable**:

1.  **Costos Ocultos:** Un empleado o contractor rara vez cuesta solo el salario. Dependiendo de tu país, debes sumar impuestos, seguridad social o prestaciones (calcula al menos un 20-30% extra). Si son $2.500 + impuestos, tu utilidad real podría caer a **$1.750 o menos**.
2.  **Riesgo Operativo:** Tu negocio depende de la publicidad ($3.900). Si el próximo mes el costo de la publicidad sube o las conversiones bajan un 20%, tus ingresos caerían a $9.920. 
    *   Con $9.920 de ingresos y tus costos actuales, tu ganancia sería de apenas $2.520. 
    *   Al pagar los $2.500 del sueldo, **te quedarías con $20 para ti.**
3.  **Liquidez vs. Crecimiento:** Estás a punto de convertir el 50% de tu ganancia neta en un costo fijo. Si el mes viene malo, no puedes "despedir" a alguien de un día para otro sin costos de liquidación o sin dañar la moral del equipo.

### Mi recomendación como Controller:

**No contrates a alguien por $2.500 todavía.** Tu estructura de costos es muy sensible a la publicidad.

**¿Qué opciones tienes?**

*   **Opción A (Conservadora):** Contratar a alguien **part-time** o por **proyecto** por $1.000 - $1.200. Esto protege tu margen y te da aire para seguir invirtiendo en Ads.
*   **Opción B (Estratégica):** Si esa persona va a encargarse de generar más ventas (ventas activas o gestión de tráfico), debes exigirle un KPI claro: *"Para pagarte $2.500, necesito que mis suscripciones pasen de $9.800 a $12.000 en los próximos 60 días"*.
*   **Opción C (Financiera):** No aceptes la contratación hasta que tengas un **Fondo de Reserva** en el banco que cubra al menos 3 meses del salario de esa persona ($7.500). 

**Veredicto:** Los números "cierran" en el papel hoy, pero **no son sostenibles** ante cualquier variación del mercado. Tu margen de error es demasiado estrecho.