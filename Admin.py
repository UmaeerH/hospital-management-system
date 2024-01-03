import itertools

class Admin:
    newaid = itertools.count()
    def __init__(self, uName, password, address="None provided"):
        self.__userName = uName
        self.__pass = password
        self.__address = address
    
    def get_userName(self):
        return self.__userName
    def set_userName(self, newUser):
        self.__userName = newUser

    def get_pass(self):
        return self.__pass
    def set_pass(self, newPass):
        self.__pass = newPass
    
    def get_address(self):
        return self.__address
    def set_address(self, newAddress):
        self.__address = newAddress

    def __str__(self):
        return f'User: {self.__userName}\tPass: {self.__pass}'
    
#testing
def main():
    add1 = Admin("Umi", "Git")
    add2 = Admin("Keller", "Grenada")
    print(add1)
    print(add2)

if __name__ == "__main__":
    main()