from app import *

from service import JWT, data_base, theards, user_server_data

from settings import env
tokin_service = JWT.tokinService()



@app.route('/')
def index():
    # asd
    # jwts = tokin_service.generateTokins({"dq":'qwe'})
    # print()
    user_server_data.test()
    q = {
        'q':123
    }
    user_server_data.data_user['4122']['jwt'] = JWT.tokinService.generateTokins('', q)
    print(JWT.tokinService.decodeTokins(None, type_sc='ACCESS' , JWT_text=user_server_data.data_user['4122']['jwt']['accessTokin']),'\n',
    JWT.tokinService.decodeTokins(None, type_sc='REFRESH' , JWT_text=user_server_data.data_user['4122']['jwt']['refreshTokin']))
    return user_server_data.data_user