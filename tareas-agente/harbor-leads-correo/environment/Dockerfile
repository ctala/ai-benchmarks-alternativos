FROM python:3.12.7-slim-bookworm
WORKDIR /app
COPY bandeja /app/bandeja
COPY criterios-leads.md esquema-crm.sql /app/
COPY semilla.sql /tmp/semilla.sql
RUN python -c "import sqlite3; c=sqlite3.connect('/app/crm.db'); c.executescript(open('/app/esquema-crm.sql').read()); c.executescript(open('/tmp/semilla.sql').read()); c.commit()" \
 && rm /tmp/semilla.sql
