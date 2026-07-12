#!/bin/bash

# Iglesia Vida Nueva - Flask Application Startup Script

# Development mode
if [ "$1" = "dev" ]; then
    echo "Starting in development mode..."
    export FLASK_ENV=development
    export FLASK_DEBUG=1
    python app.py
fi

# Production mode with Gunicorn
if [ "$1" = "prod" ]; then
    echo "Starting in production mode with Gunicorn..."
    gunicorn -c gunicorn.conf.py app:app
fi

# Default: show usage
if [ -z "$1" ]; then
    echo "Usage:"
    echo "  ./run.sh dev   - Start in development mode"
    echo "  ./run.sh prod  - Start in production mode with Gunicorn"
fi
