# Kimi K3.1 Pro — business_audit/retention_sobre_100_interpretacion

- model_id: `moonshotai/kimi-k3.1-pro`
- success: True  | final: 7.81 | quality: 10.0
- latency_total: 189.835s | tokens_per_second: 26.3
- input_tokens: 245 | output_tokens: 4998

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

**No. Estás mezclando retención de ingresos con retención de clientes**, y tus cifras muestran que pueden moverse en direcciones opuestas.

### Qué significa realmente el 114 %

Si el panel usa la definición habitual, se trata de **retención neta de ingresos (NRR)**:

\[
NRR=\frac{MRR\ inicial - MRR\ perdido\ por\ bajas - MRR\ perdido\ por\ downgrades + MRR\ de\ expansión}{MRR\ inicial}
\]

Normalmente **excluye los ingresos de clientes nuevos**. Un 114 % significa que la cohorte de clientes que ya tenías genera un **14 % más de ingresos netos** al final del periodo, gracias a que las subidas de plan superan las pérdidas.

Puede coexistir con bastante churn. Por ejemplo, por cada 100 € de MRR inicial:

- Pierdes 20 € por bajas.
- Ganas 34 € por ampliaciones.
- Terminas con 114 €: **NRR del 114 %**, aunque la retención bruta de ingresos sea solo del 80 %.

### Qué dicen tus clientes: de 40 a 36

- **Si no hubo altas nuevas:** perdiste 4 clientes. Tu retención de clientes fue del **90 %** y tu churn de clientes, del **10 %**.
- **Si hubo altas nuevas:** los saldos no bastan para calcular el churn exacto, pero al menos 4 de los 40 clientes iniciales ya no están al cierre. Por tanto, la retención de esa cohorte es **como máximo del 90 %**, y podría ser menor.

Las subidas de plan explican perfectamente que los ingresos crezcan mientras disminuye el número de clientes.

### ¿Deberías centrarte solo en captación?

**No.** El 114 % es una señal positiva sobre la expansión neta, pero no demuestra que el churn sea bajo ni que el crecimiento sea sostenible. La expansión podría depender de unos pocos clientes o de subidas de plan que no se repitan.

Antes de reasignar todo el esfuerzo, revisa por separado:

1. **Churn y retención de clientes** de la cohorte inicial.
2. **Retención bruta de ingresos (GRR)**, sin contar expansiones.
3. Churn de MRR, downgrades y upgrades por separado.
4. Concentración de la expansión: cuánto del 114 % depende de tus mayores cuentas.

**Lectura correcta:** estás aumentando los ingresos de tu base existente gracias a la expansión, pero tu base de clientes se está contrayendo. Puedes tener un buen NRR y, simultáneamente, un problema de churn que no conviene ignorar.