"""
Gunicorn configuration file for production deployment
"""

import os


# ============================================================
# SERVER SOCKET
# ============================================================

# Render proporciona automáticamente la variable PORT.
# Si ejecutas localmente y PORT no existe, utilizará 8000.
port = os.environ.get("PORT", "8000")

bind = f"0.0.0.0:{port}"

backlog = 2048


# ============================================================
# WORKERS
# ============================================================

# IMPORTANTE:
# El contador de espectadores utiliza memoria del proceso Flask.
# Por eso usamos un solo worker para que todos los espectadores
# compartan el mismo contador.
workers = 1

worker_class = "sync"
worker_connections = 1000

timeout = 30
keepalive = 2


# ============================================================
# LOGGING
# ============================================================

accesslog = "-"
errorlog = "-"
loglevel = "info"


# ============================================================
# PROCESS NAMING
# ============================================================

proc_name = "iglesia_vida_nueva"


# ============================================================
# SERVER MECHANICS
# ============================================================

daemon = False
pidfile = None
umask = 0

# No necesitamos cambiar usuario/grupo en Render.
user = None
group = None

tmp_upload_dir = None
