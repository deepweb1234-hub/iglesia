"""
Iglesia Vida Nueva - Flask Application
Production-ready with Gunicorn support
"""
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')

# Data for the application
SERMONS = [
    {
        "id": 1,
        "title": "El Poder de la Fe",
        "speaker": "Pastor Juan García",
        "date": "19 Enero 2026",
        "duration": "45 min",
        "description": "Descubre cómo la fe puede mover montañas y transformar tu vida completamente.",
        "category": "Fe",
        "featured": True,
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8EFwjM3x0QFMNk6CjXWJbmt6hivb5D8tgXw&s",
        "video_url": "https://app.videonest.co/embed/single/1598771"

        
    },
    {
        "id": 2,
        "title": "Caminando en Obediencia",
        "speaker": "Pastor Juan García",
        "date": "12 Enero 2026",
        "duration": "52 min",
        "description": "La obediencia a Dios es la clave para desbloquear sus bendiciones en nuestra vida.",
        "category": "Obediencia",
        "featured": False,
    },
    {
        "id": 3,
        "title": "La Gracia Transformadora",
        "speaker": "Pastora María López",
        "date": "5 Enero 2026",
        "duration": "48 min",
        "description": "La gracia de Dios no solo nos perdona, sino que nos transforma desde adentro.",
        "category": "Gracia",
        "featured": False,
    },
    {
        "id": 4,
        "title": "Viviendo con Propósito",
        "speaker": "Pastor Juan García",
        "date": "29 Diciembre 2025",
        "duration": "55 min",
        "description": "Dios tiene un propósito único para cada uno de nosotros. Aprende a descubrirlo.",
        "category": "Propósito",
        "featured": False,
    },
    {
        "id": 5,
        "title": "El Amor que Restaura",
        "speaker": "Pastora María López",
        "date": "22 Diciembre 2025",
        "duration": "42 min",
        "description": "El amor de Dios tiene el poder de restaurar corazones rotos y relaciones dañadas.",
        "category": "Amor",
        "featured": False,
    },
    {
        "id": 6,
        "title": "Fortaleza en la Prueba",
        "speaker": "Pastor Juan García",
        "date": "15 Diciembre 2025",
        "duration": "50 min",
        "description": "Las pruebas no vienen para destruirnos, sino para fortalecernos y acercarnos a Dios.",
        "category": "Fe",
        "featured": False,
    },
]

SERVICES = [
    {
        "icon": "calendar",
        "title": "Servicio Familiar",
        "day": "Domingo",
        "time": "8:00 AM",
        "description": "Un servicio diseñado para toda la familia, con actividades especiales para niños.",
        "features": ["Escuela Dominical", "Guardería disponible", "Café de bienvenida"],
    },
    {
        "icon": "calendar",
        "title": "Servicio General",
        "day": "Domingo",
        "time": "10:30 AM",
        "description": "Nuestro servicio principal con adoración, predicación y tiempo de comunión.",
        "features": ["Adoración en vivo", "Mensaje pastoral", "Oración de fe"],
    },
    {
        "icon": "book",
        "title": "Estudio Bíblico",
        "day": "Miércoles",
        "time": "7:00 PM",
        "description": "Profundiza en la Palabra de Dios con enseñanzas prácticas y relevantes.",
        "features": ["Estudio versículo por versículo", "Discusión grupal", "Material de apoyo"],
    },
]

MINISTRIES = [
    {
        "icon": "baby",
        "title": "Ministerio Infantil",
        "description": "Clases y actividades diseñadas especialmente para los más pequeños.",
        "schedule": "Domingos durante los servicios",
    },
    {
        "icon": "users",
        "title": "Jóvenes",
        "description": "Un espacio para que los jóvenes crezcan en su fe y compartan con otros.",
        "schedule": "Sábados 5:00 PM",
    },
    {
        "icon": "heart",
        "title": "Matrimonios",
        "description": "Fortalece tu relación matrimonial con enseñanzas y actividades en pareja.",
        "schedule": "Primer sábado del mes",
    },
    {
        "icon": "music",
        "title": "Adoración",
        "description": "Si tienes talento musical, únete a nuestro equipo de alabanza.",
        "schedule": "Ensayos: Jueves 7:00 PM",
    },
]


# Routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/adoracion')
def adoracion():
    return render_template('adoracion.html')


@app.route('/servicios')
def servicios():
    return render_template('servicios.html', services=SERVICES, ministries=MINISTRIES)


@app.route('/predicas')
def predicas():
    categories = ["Todas", "Fe", "Gracia", "Amor", "Propósito", "Obediencia"]
    featured = next((s for s in SERMONS if s["featured"]), None)
    return render_template('predicas.html', sermons=SERMONS, categories=categories, featured=featured)


@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)


# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
