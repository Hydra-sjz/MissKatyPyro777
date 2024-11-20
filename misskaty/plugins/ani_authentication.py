from pymongo import MongoClient as MC
from misskaty import app, BOT_USERNAME
from misskaty.vars import SUDO as AUTH_USERS
D = "DATABASE_URI"

c = MC(D)['anibot']

AUTH_USERS = c.get_collection('AUTH_USERS')

app.url_map.strict_slashes = False


@app.route('/gjanilist')
def adddd_auth():
    k = AUTH_USERS.insert_one({'code': request.args['code'], 'id': 'pending'})
    return redirect(f'https://telegram.me/{BOT_USERNAME}?start=code_{str(k.inserted_id)}', code=302)
  
