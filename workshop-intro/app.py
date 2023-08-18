from chalice import Chalice

app = Chalice(app_name='workshop-intro')


@app.route('/')
def index():
    return {'hello': 'world'}
