
from settings import env

data_user = {}

class user_servise():
    def get(self, hash):
        # Если нет пользователя то создаёт его
        if not hash in data_user:
            data_user[hash] = env.FORMAT_USER_DATA
            
        return data_user[hash]


def test():
    user_servise.get(None, '4144')
    user_servise.get(None, '4114')
    user_servise.get(None, '4122')
    print(data_user)