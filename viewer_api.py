from flask import Flask, jsonify, request
from threading import Lock
import time
import re

app = Flask(__name__)

# Memoria temporal: viewer_id -> ultima actividad (Unix timestamp)
viewers = {}
lock = Lock()

VIEWER_TTL = 60  # segundos sin heartbeat antes de dejar de contar
VIEWER_ID_RE = re.compile(r"^[A-Za-z0-9_-]{16,128}$")


def cleanup_expired():
    now = time.time()
    expired = [vid for vid, last_seen in viewers.items()
               if now - last_seen > VIEWER_TTL]
    for vid in expired:
        viewers.pop(vid, None)


def valid_viewer_id(viewer_id):
    return isinstance(viewer_id, str) and bool(VIEWER_ID_RE.fullmatch(viewer_id))


@app.post("/api/viewers/heartbeat")
def heartbeat():
    data = request.get_json(silent=True) or {}
    viewer_id = data.get("viewer_id")
    playing = data.get("playing") is True

    if not valid_viewer_id(viewer_id):
        return jsonify({"ok": False, "error": "viewer_id inválido"}), 400

    with lock:
        cleanup_expired()

        if playing:
            viewers[viewer_id] = time.time()
        else:
            viewers.pop(viewer_id, None)

        count = len(viewers)

    return jsonify({"ok": True, "viewers": count})


@app.post("/api/viewers/leave")
def leave():
    data = request.get_json(silent=True) or {}
    viewer_id = data.get("viewer_id")

    if valid_viewer_id(viewer_id):
        with lock:
            viewers.pop(viewer_id, None)
            cleanup_expired()
            count = len(viewers)
    else:
        count = 0

    return jsonify({"ok": True, "viewers": count})


@app.get("/api/viewers/count")
def count():
    with lock:
        cleanup_expired()
        current = len(viewers)

    return jsonify({
        "ok": True,
        "viewers": current,
        "updated_at": int(time.time())
    })


if __name__ == "__main__":
    # Para desarrollo local.
    # En producción usa un servidor WSGI como Waitress/Gunicorn.
    app.run(host="0.0.0.0", port=5000, debug=True)
