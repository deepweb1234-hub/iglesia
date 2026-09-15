"""
Gunicorn configuration for production
"""

import os


# Render proporciona PORT automáticamente
port = os.environ.get("PORT", "8000")

bind = f"0.0.0.0:{port}"
backlog = 2048


# Redis permite utilizar múltiples workers
workers = 2

worker_class = "sync"
worker_connections = 1000

timeout = 30
keepalive = 2


# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"


# Process
proc_name = "iglesia_vida_nueva"

daemon = False
pidfile = None
umask = 0

user = None
group = None
tmp_upload_dir = None
