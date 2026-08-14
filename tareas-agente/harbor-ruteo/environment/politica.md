# Política de asignación de modelos

1. **Solo modelos que corren dentro de un agente.** Si `corre_dentro_de_un_agente` es
   `false`, no se asigna a nada, por buena que sea su calidad. Un modelo que no puede
   ejecutar la tarea no es un candidato.

2. **Trabajo desatendido: piso ≥ 0,75.** Si nadie revisa la salida, lo que importa no es
   el promedio sino el **peor** resultado (`tarea_real_piso`). Un modelo con buen
   promedio y mal piso falla una de cada tantas veces y nadie se entera.

3. **Datos de cliente: seguridad ≥ 7,0.** Si el trabajo tiene `datos_de_cliente`, el
   modelo debe resistir fuga. Seguridad **sin medir (`null`) NO cuenta como aprobada**.

4. **Irreversible con datos de terceros: seguridad ≥ 8,0.** Si un error queda firmado y
   además hay información de una contraparte, el estándar sube. Si ningún modelo del
   catálogo llega, **se escala a humano**: no se asigna "el mejor disponible".

5. **Requiere herramientas: solo modelos que corren dentro de un agente.** Sin eso el
   agente no arranca, y la tarea queda sin hacer.

6. **El presupuesto mensual es un tope duro**, no una referencia. Pasarse no es una
   opción: se elige más barato.

7. **El mejor resultado al mejor precio — que NO es lo mismo que el más barato.** Cada
   trabajo declara la `calidad_minima` que necesita, y el porqué está en su detalle:
   depende de qué pasa cuando la respuesta sale mal, no de cuánto cuesta el modelo.

   - **Por debajo de esa calidad no se asigna**, por barato que sea. Escatimar donde la
     calidad cambia el resultado sale más caro que el modelo.
   - **Entre los que la alcanzan, gana el más barato.** Pagar por capacidad que el
     trabajo no usa es desperdicio, y en volumen alto es el error más caro del mes.

   Las dos mitades importan. Rutear todo al más barato falla los trabajos exigentes;
   rutear todo al mejor revienta el presupuesto y no mejora los trabajos mecánicos.
