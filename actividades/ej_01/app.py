# Aplicacion del servidor
from microdot import Microdot, send_file
from machine import Pin

app = Microdot()

@app.route('/')
async def index(request):
    return 'Hello, world!'


app.run(port = 80)# Aplicacion del servidor# Aplicacion del servidor
