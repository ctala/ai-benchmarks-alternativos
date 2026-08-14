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

7. **A igualdad de condiciones, gana el más barato.** Pagar de más por capacidad que el
   trabajo no necesita es el error más caro y el más fácil de cometer.
