
class Usuario_loged:
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
            cls._instance.Nickname = None
            cls._instance.Saldo = None
            cls._instance.Rol = None
            cls._instance.Ventas = None
        return cls._instance
    def guardarUsuario(self,Nick,Saldo,Rol):
        self.Nickname = Nick
        self.Saldo = Saldo
        self.Rol = Rol
    def guardarCreador(self,Nick,Saldo,Rol,Ventas):
        self.Nickname = Nick
        self.Saldo = Saldo
        self.Rol = Rol
        self.Ventas = Ventas