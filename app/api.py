from service import JWT, data_base, theards, user_server_data
from app import *

from settings import env
# tokin_service = JWT.tokinService(env)


# resp.set_cookie('sessionID', '', expires=0)   #Сбросить куки
tokinService = JWT.tokinService()

@app.route('/')
def index():
    print('s')
    return render_template('index.html')