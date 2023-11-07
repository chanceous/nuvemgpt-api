import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/home/ubuntu/api")  # Ruta al directorio principal de tu aplicación

from main import api as application  # Importa la instancia de Flask de main.py

# Esta línea es importante para que mod_wsgi pueda encontrar la aplicación
application = application