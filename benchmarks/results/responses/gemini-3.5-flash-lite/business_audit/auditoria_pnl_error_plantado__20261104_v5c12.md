# Gemini 3.5 Flash Lite — business_audit/auditoria_pnl_error_plantado

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 5.65 | quality: 5.0
- latency_total: 4.202s | tokens_per_second: 152.3
- input_tokens: 207 | output_tokens: 640

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

**Los números no cierran. Tu margen real no es del 40%, es del 40.32% antes de impuestos, pero estás ignorando un costo operativo crítico.**

Antes de evaluar la contratación, vamos a revisar la P&L (Cuenta de Resultados) real de tu negocio con tus datos:

*   **Ingresos Totales:** $12.400
*   **Costos Totales (Operativos):** $7.400
*   **Beneficio Bruto / EBITDA Operativo:** $5.000 ($12.400 - $7.400)
*   **Tu margen real:** 40.32% ($5.000 / $12.400). *Hasta aquí, el cálculo matemático de tu margen es correcto, pero incompleto.*

### Dónde falla el número:
En ningún lado de tu estructura de costos veo tu propio sueldo (costo de fundador), ni provisiones para impuestos, ni imprevistos. 

Si asumimos que esos $5.000 son la caja libre que deja el negocio hoy:
1.  **Caja actual:** $5.000
2.  **Costo del nuevo empleado:** -$2.500
3.  **Caja restante:** $2.500

Si contratas a alguien por $2.500, **te estás comiendo exactamente el 50% de la ganancia neta actual del negocio** de un solo golpe. 

### Mi opinión como Controller Financiero:
**No te da el número para una contratación fija de $2.500 con este nivel de ingresos.** 

Una regla financiera sana (especialmente en negocios digitales, que son volátiles) es que un nuevo costo fijo de personal no debería comprometer más del 20% al 25% de tu beneficio operativo, a menos que esa contratación genere un retorno de inversión (ROI) medible y directo a corto plazo (por ejemplo, un closer de ventas o un trafficker con retainer por objetivos).

**¿Qué hacer en su lugar?**
*   **Opción A (Riesgo alto):** Si contratas a esa persona, tu margen de maniobra ante un mes malo de publicidad ($3.900) o una caída en suscripciones es prácticamente cero. Quedarás con caja negativa muy rápido.
*   **Opción B (Financieramente seguro):** Busca un modelo híbrido (freelance por horas, o un salario base menor + comisiones por resultados) hasta que tus ingresos fijos (suscripciones de $9.800) cubran holgadamente toda la estructura de costos incluyendo al nuevo empleado.

¿Esa contratación va a generar ingresos directos inmediatos que eleven tu facturación por encima de los $15.000 el próximo mes? Si la respuesta es "no lo sé", la respuesta a tu contratación es **no**.