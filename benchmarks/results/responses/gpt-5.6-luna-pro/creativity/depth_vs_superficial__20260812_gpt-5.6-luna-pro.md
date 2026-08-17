# GPT-5.6 Luna Pro — creativity/depth_vs_superficial

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 7.96 | quality: 9.0
- latency_total: 39.597s | tokens_per_second: 225.0
- input_tokens: 10515 | output_tokens: 8908

## Entrada exacta (lo que recibió el modelo)

**user:**

Un emprendedor te dice: "Estoy pensando en usar IA para mi startup de delivery de comida en Santiago. Que deberia hacer?"

Da una respuesta que demuestre PROFUNDIDAD real, no consejos genericos.
Incluye:
- Al menos 2 ideas especificas que NO sean obvias (no digas "usa IA para optimizar rutas", eso lo sabe cualquiera)
- Numeros o estimaciones concretas cuando sea posible
- Un riesgo no obvio que otros no mencionarian
- Una opinion contrarian o controversia sobre el tema

No me des una lista generica de "5 formas de usar IA". Quiero pensamiento original.


## Respuesta completa

Yo no empezaría con un chatbot ni con “IA para optimizar rutas”. En delivery, el problema principal no es encontrar el camino más corto: es que la promesa comercial se vuelve falsa por una combinación de cocina lenta, direcciones ambiguas, conserjería, ascensores, stock incompleto y tráfico.

Mi tesis sería: **usar IA para reducir la incertidumbre operativa antes de aceptar el pedido**, aunque eso implique rechazar o retrasar algunos pedidos.

### 1. Construiría un modelo de “probabilidad de pedido problemático”

No modelaría solamente el tiempo de viaje. Separaría el pedido en cuatro tiempos:

1. preparación real del restaurante;
2. espera del repartidor en el local;
3. traslado;
4. entrega dentro del edificio o condominio.

El cuarto componente es bastante ignorado. Entregar en una casa de Ñuñoa, en una torre con conserjería en Santiago Centro y en un condominio de Lo Barnechea son problemas diferentes aunque la distancia sea la misma.

El modelo podría estimar, por ejemplo:

- probabilidad de estar más de 15 minutos atrasado;
- probabilidad de que el repartidor tenga que llamar;
- probabilidad de cancelación;
- costo esperado del pedido en soporte, devolución y compensación.

Las variables útiles no son sólo GPS:

- restaurante, hora y día;
- combinación de productos —una hamburguesa sola no tiene el mismo tiempo que cinco platos distintos—;
- tiempo histórico entre “pedido recibido” y “pedido listo”;
- edificio, número de torre, presencia de conserjería;
- tasa histórica de llamadas del repartidor;
- lluvia, eventos, partidos y horarios de salida de oficinas;
- si el restaurante está simultáneamente recibiendo pedidos de otras plataformas.

La decisión no sería simplemente “asignar el repartidor más cercano”. Podría ser:

- no mostrar delivery de un restaurante durante 30 minutos si su cocina está saturada;
- ofrecer una ventana de 45 minutos en vez de prometer 25;
- enviar el repartidor más tarde para evitar que espere 15 minutos afuera;
- permitir el pedido sólo si el margen soporta la probabilidad de compensación.

Esto es importante porque un ETA agresivo puede ser **auto-destructivo**: si prometes 25 minutos y generas muchos pedidos, saturas la cocina, el ETA se vuelve todavía peor y el algoritmo aprende de datos contaminados.

Una estimación ilustrativa:

- 1.000 pedidos diarios;
- ticket promedio de $14.000;
- comisión del 25%: $3.500 por pedido;
- costo de repartidor: $2.200;
- pagos, soporte y devoluciones: $600;
- contribución aproximada: $700 por pedido antes de adquisición.

Si un pedido atrasado genera en promedio $1.200 entre cupón, soporte y pérdida de recompra, bajar los pedidos problemáticos de 12% a 9% ahorraría aproximadamente:

`1.000 × 3 puntos porcentuales × $1.200 = $36.000 diarios`

Eso parece modesto, pero son más de $10 millones al año, sin contar la retención. Y el beneficio principal probablemente no sea el ahorro directo, sino aumentar la recompra.

La métrica no debería ser “ETA promedio”. Usaría **P90 de atraso**, tasa de compensación y recompra a 30 días.

---

### 2. Resolvería la dirección como un problema de “últimos 100 metros”

En Santiago, una dirección escrita correctamente puede seguir siendo insuficiente. “Av. Apoquindo 4501” no dice necesariamente torre, acceso, estacionamiento, conserjería o si el repartidor debe entrar por otra calle. En edificios y condominios, el costo no está en llegar al pin: está en encontrar la entrada correcta y completar la entrega.

Crearía un sistema que convierta la dirección en un objeto operativo:

- coordenada de la entrada real, no sólo del centro del predio;
- nombre de torre o condominio;
- acceso recomendado;
- existencia de conserjería;
- instrucciones que históricamente funcionaron;
- probabilidad de que el cliente responda el teléfono;
- tiempo promedio desde llegada al edificio hasta entrega.

El componente de lenguaje puede interpretar texto libre —“dejar en recepción de la torre que está frente al Unimarc”—, pero no confiaría ciegamente en un LLM para geocodificar. Usaría reglas, mapas, GPS del repartidor y confirmación explícita del cliente.

En el checkout haría una pregunta de alto valor predictivo, no diez campos obligatorios:

> “¿Es casa, edificio o condominio?”  
> Si es edificio: “¿Tiene conserjería?” y “¿Qué torre/departamento?”

Para los lugares con muchos pedidos, se puede aprender un “perfil de acceso” con datos agregados. Por ejemplo, si 70% de los repartidores que llegan a un condominio terminan entrando por una calle distinta de la que devuelve el geocodificador, eso se convierte en una instrucción de despacho.

Supongamos que hoy 6% de los pedidos requieren una llamada adicional y que cada incidente cuesta $800 entre tiempo, soporte y atraso. Si esta capa reduce esos incidentes a 4% en 1.000 pedidos diarios:

`20 incidentes evitados × $800 = $16.000 diarios`

Además, se recupera capacidad del repartidor. En una operación densa, ahorrar tres minutos por entrega puede ser más valioso que ahorrar 300 metros de ruta.

---

### 3. Usaría IA para intervenir el menú, no para generar descripciones bonitas

Otro punto poco obvio: el menú es una fuente enorme de fallas. Los productos se agotan, tienen modificadores ambiguos, generan tiempos de preparación muy distintos o son rentables sólo cuando se compran en combinación.

Construiría un sistema que aprenda, por restaurante y franja horaria:

- qué productos tienen alta probabilidad de quiebre de stock;
- qué combinaciones producen reclamos;
- qué modificadores son operativamente imposibles;
- qué platos agregan mucho tiempo pero poco margen;
- qué sustituciones son aceptables para ese cliente.

Ejemplo: si los martes entre 13:00 y 14:00 un restaurante se queda sin papas grandes en 18% de los pedidos, la plataforma puede desactivar temporalmente esa opción o mostrar una sustitución antes del pago. Eso es mejor que llamar al cliente después de 25 minutos.

Pero pondría una restricción fuerte: **la IA nunca debe inventar equivalencias alimentarias**. No permitiría que el sistema sugiera automáticamente que un ingrediente es “sin gluten”, “sin lactosa” o seguro para una alergia. Esa información debe venir del restaurante y tener una política de trazabilidad. Una recomendación aparentemente útil podría causar una reacción alérgica y convertir un problema de UX en responsabilidad legal y reputacional.

---

### El experimento inicial que haría

No intentaría cubrir todo Santiago. Empezaría con dos o tres zonas de alta densidad y patrones distintos, por ejemplo una zona de oficinas, una residencial de edificios y una zona con condominios.

Durante seis semanas:

**Semanas 1–2:** instrumentar eventos:

- hora de recepción del pedido;
- hora real en que empieza la preparación;
- hora en que está listo;
- llegada y salida del repartidor;
- llamadas;
- ubicación exacta de entrega;
- compensaciones;
- cancelaciones.

**Semanas 3–4:** lanzar un modelo simple de riesgo, aunque sea gradient boosting o reglas bien calibradas. No hace falta un modelo sofisticado si los timestamps son malos.

**Semanas 5–6:** probar tres políticas:

- ETA conservador para pedidos de alto riesgo;
- throttling de restaurantes saturados;
- captura estructurada de acceso en edificios.

Compararía contra un grupo de control. Las métricas serían:

- P90 de tiempo total;
- porcentaje entregado dentro de la promesa;
- cancelaciones;
- compensaciones;
- minutos improductivos del repartidor;
- recompra a 30 días;
- contribución por pedido, no sólo número de pedidos.

---

### Riesgo no obvio

El riesgo más peligroso es que el modelo aprenda que ciertas comunas, edificios o tipos de clientes son “malos” y empiece a degradarles el servicio: ETAs más largos, menos restaurantes disponibles o precios mayores.

Eso puede ocurrir aunque nadie programe discriminación explícita. Si los edificios periféricos tienen más direcciones incompletas, el modelo puede concluir que conviene no servirlos. Luego reciben menos servicio, generan menos datos positivos y el modelo confirma su propia conclusión: un círculo vicioso de exclusión geográfica.

También hay un riesgo laboral: usar el modelo para medir qué repartidor “pierde tiempo” puede penalizar a personas que atienden zonas con ascensores lentos, controles de acceso o mayor inseguridad. El sistema debe distinguir entre ineficiencia del repartidor y fricción estructural del lugar.

Por eso revisaría métricas por comuna, tipo de edificio y horario, y pondría límites a decisiones automatizadas de cobertura.

---

### Mi opinión contrarian

**No intentaría maximizar pedidos al comienzo. Intentaría maximizar pedidos que merezca la pena cumplir.**

Un pedido adicional puede destruir margen si requiere esperar 20 minutos en un restaurante, subir 15 pisos, llamar tres veces y entregar un cupón por atraso. Las startups suelen celebrar volumen bruto mientras subsidian complejidad.

También sería contrario a construir un modelo propio de IA demasiado pronto. El verdadero activo no será el algoritmo: será el conjunto de datos operativos que nadie más tiene —tiempo real de preparación, entrada efectiva a edificios, confiabilidad por producto y costo de cada falla—. Al principio usaría modelos existentes y concentraría el esfuerzo en **capturar eventos correctos y convertirlos en decisiones operativas**.

Si después de 1.000–2.000 pedidos diarios en una zona no puedes demostrar una mejora de al menos 10–15% en atraso, compensaciones o minutos improductivos, probablemente no necesitas una IA más sofisticada. Necesitas arreglar el proceso, el contrato con los restaurantes o la promesa comercial.