class Chain(object):

    def __init__(self, path=''):
        self._path = path
    def users(self, user_name):
        return Chain('/users/:{}'.format(user_name))
    def __getattr__(self,path):
        return Chain('{}/{}'.format(self._path,path))
    def __str__(self):
        return self._path

    def __repr__(self):
        return __str__

Chain().users('mike').repos
# /users/:user/repos