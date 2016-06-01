class Hello:
    global MSG
    def __init__(self):
        print("instanciando...")
        self.set_msg("Hola GIT!")

    def get_msg(self):
        return self.MSG

    def set_msg(self, m):
        self.MSG = m

if __name__ == '__main__':
    a = Hello()
    print(a.get_msg())
