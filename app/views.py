from app import *

from service import JWT, data_base, theards, user_server_data

from settings import env

@app.route('/inc/<qq>')
def index(qq):
    # print('as',user_server_data.data_user)
    # asd
    # jwts = tokin_service.generateTokins({"dq":'qwe'})
    # print()
    
    q = {
        'q':qq
    }
    ret = user_server_data.user_servise.get(None, qq)
    print('\n', ret, '\n')
    # qwers = (JWT.tokinService.generateTokins(None, q))
    # print(qwers)
    ret['jwt'] = JWT.tokinService.generateTokins(None, q)
    # user_server_data.data_user['4114']['jwt'] = 'qwe'
    # print(JWT.tokinService.decodeTokins(None, type_sc='ACCESS' , JWT_text=user_server_data.data_user['4122']['jwt']['accessTokin']),'\n',
    # JWT.tokinService.decodeTokins(None, type_sc='REFRESH' , JWT_text=user_server_data.data_user['4122']['jwt']['refreshTokin']))
    # return ret
    # print(user_server_data.data_user)
    return user_server_data.data_user