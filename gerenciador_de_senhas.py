class PasswordManager:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash_function(self, key):
        return hash(key) % self.size
    
    def add_password(self, website, username, password):
        hashed_key = self._hash_function(website)
        for item in self.table[hashed_key]:
            if item[0] == website:
                item[1] = username
                item[2] = password
                return
        self.table[hashed_key].append([website, username, password])
    
    def remove_password(self, website):
        hashed_key = self._hash_function(website)
        for i, item in enumerate(self.table[hashed_key]):
            if item[0] == website:
                del self.table[hashed_key][i]
                return
    
    def get_password(self, website):
        hashed_key = self._hash_function(website)
        for item in self.table[hashed_key]:
            if item[0] == website:
                return item[2]
        return None
    
    def get_username(self, website):
        hashed_key = self._hash_function(website)
        for item in self.table[hashed_key]:
            if item[0] == website:
                return item[1]
        return None

'''
if __name__ == '__main__':
    # Cria um novo gerenciador de senhas
    pm = PasswordManager()

    # Adiciona uma senha para o site example.com
    pm.add_password("example.com", "alice", "1234")

    # Adiciona outra senha para o mesmo site
    pm.add_password("test.com", "bob", "5678")

    # Obtém a senha para o site example.com
    print(pm.get_password("example.com")) # Output: 5678

    # Remove a senha para o site example.com
    pm.remove_password("example.com")

    # Tenta obter a senha para o site example.com novamente
    print(pm.get_password("example.com")) # Output: None
'''

'''
if __name__ == '__main__':
    pm = PasswordManager()
    pm.add_password("example.com", "bob", "5678")
    pm.add_password("test.com", "alice", "1234")
    pm.add_password("carol.com", "carol", "9012")
    pm.add_password("douglas.com", "douglas", "3456")
    pm.add_password("eve.com", "eve", "7890")
    pm.add_password("frank.com", "frank", "1357")
    pm.add_password("grace.com", "grace", "2468")
    pm.add_password("helen.com", "helen", "3579")
    pm.add_password("isaac.com", "isaac", "4680")
    pm.add_password("judy.com", "judy", "5791")
    pm.add_password("kate.com", "kate", "6802")

    print(pm.get_username("test.com")) # Output: alice
    print(pm.get_password("test.com")) # Output: 1234
    print(pm.get_password("kate.com")) # Output: 6802
    print(pm.table)
'''