# GPT-5.6 Sol — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 6.38 | quality: 8.14
- latency_total: 115.207s | tokens_per_second: 12.5
- input_tokens: 186 | output_tokens: 1442

## Respuesta completa

No le daría todavía los $10.000. La aritmética del canal pagado está prácticamente en break-even.

### Recálculo

Con churn mensual constante de 8%:

- **Vida media esperada:** \(1 / 0,08 = 12,5\) meses, no 24.
- **Ingreso LTV:** \(35 / 0,08 = \$437,50\)
- **LTV de margen bruto:** \(437,50 \times 70\% = \$306,25\)
- **LTV/CAC correcto:** \(306,25 / 290 = 1,06\)

Además, incluso usando tus 24 meses:

- LTV de ingresos: $840
- LTV con margen bruto: \(840 \times 70\% = \$588\)
- LTV/CAC: \(588 / 290 = 2,03\), no 2,9  
- Y \(840/290=2,90\) sigue estando por debajo de 3.

### Qué producirían $10.000

A CAC constante de $290:

- Clientes adquiridos: aproximadamente **34,5**
- Margen bruto esperado de toda su vida: aproximadamente **$10.560**
- Excedente antes de salarios, soporte, herramientas, impuestos y costo de capital: apenas **$560**

Eso es solo un **5,6% nominal** a lo largo de varios años. Con la erosión del churn, la cohorte recuperaría el CAC aproximadamente en el **mes 36**, no en 11,8 meses. A los 24 meses aún no lo habría recuperado.

Y al escalar suelen empeorar el CAC o la calidad de los clientes.

### Umbrales para que tenga sentido

Para llegar a **LTV/CAC = 3**, necesitas alguna de estas condiciones:

- **CAC máximo:** aproximadamente **$102**, manteniendo todo lo demás.
- **Churn máximo:** aproximadamente **2,8% mensual**, manteniendo CAC de $290.
- O una mejora equivalente en precio y margen.

**Conclusión:** no escales fuerte todavía. Haz pruebas pequeñas y mide por cohorte el CAC marginal, churn de clientes pagados y margen real. Ser rentable hoy no implica que cada nuevo dólar de publicidad sea rentable; con estos números, el canal pagado está demasiado cerca del punto de equilibrio.