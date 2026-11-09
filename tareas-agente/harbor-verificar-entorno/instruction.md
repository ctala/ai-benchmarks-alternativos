Eres el asistente técnico de Ferretería El Roble SpA. Su proyecto de scripts internos está
en `/app/proyecto`. Cada uno de los encargos de abajo se revisa contra lo que el propio
proyecto declara en sus archivos, no contra valores por defecto ni contra lo habitual en
otros proyectos.

1. En `/app/proyecto/config/deploy.toml`, completa `python` con la versión exacta de Python
   que fija el proyecto y `ruff` con la versión de ruff que usa el proyecto (solo el
   número, por ejemplo `"1.2.3"`).
2. `python /app/proyecto/scripts/sincronizar.py --simular` falla. Instala la dependencia que
   falta, sin modificar el script, y regístrala en `/app/proyecto/requirements.txt`
   siguiendo la convención del proyecto.
3. Genera el reporte de ventas de octubre 2026 con `/app/proyecto/scripts/exportar.py` y
   guárdalo donde el proyecto guarda sus reportes, con el mismo esquema de nombre.
4. Crea `/app/proyecto/config/app.toml`, con el mismo formato que
   `config/app.example.toml`, con el host, el puerto y el nombre de la base de datos que
   usa este entorno.
5. Agrega la migración SQL que crea la tabla `boletas` (columnas `id`, `folio`, `fecha` y
   `monto_clp`) donde el proyecto guarda sus migraciones, con su numeración y su forma de
   nombrar los archivos.
