# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
# SEMPRE QUE USAR SELF VOCE QUER USAR UM METODO DE INSTANCIA


class Connection:
    def __init__(self, user=None, password=None, host='localhost'):
        self.host = host
        self.user = user
        self.password = password

    def set_user(self, user):
        # setter
        self.user = user
        

    def set_password(self, password):
        # setter
        self.password = password
        

    @classmethod
    def new_connection(cls, user='myhost', password='0000'):
        return cls(user, password)
    
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection






c1 = Connection()
print(c1.host)
c1.set_user('KaueSouza')
print(c1.user)
c1.set_password('9988')
print(c1.password)

print()

c2 = Connection.new_connection()
print(c2.host)
print(c2.user)
print(c2.password)

print()


c3 = Connection.create_with_auth('Teste', '0011')
print(c3.host)
print(c3.user)
print(c3.password)
