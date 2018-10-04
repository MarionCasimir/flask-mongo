from api.main import app

@app.route('/stores')
def get_stores():
    pass

@app.route('/stores/<int:id>')
def get_store_by_id(id):
    pass
