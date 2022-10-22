import os
class Password:
    def __init__(self, site=None, username=None, word=None):
        self.site = site
        self.username = username
        self.word = word

    def __eq__(self, other):
        return self.site == other.site and self.username == other.username

    def __repr__(self):
        return f'Site: {self.site}  Username: {self.username}  Password:  {self.word}'

class Stash:
    def __init__(self):
        self.passwords = []

    def safe(self, file):
        with open(file, 'w') as f:
            for i in self.passwords:
                f.writelines(str(i) + "\n")

    def read(self, file):
        self.passwords = []
        with open(file, 'r') as f:
            for i in  f.readlines():
                a = i.split(" ")
                self.add(*a)

    def add(self, *items):
          self.passwords.append(Password(*items))

if __name__ == '__main__':
    a = Stash()
    a.add("a", "c", "123")
    a.add("a", "b", "123")

    a.safe("text.txt")
    a.read("text.txt")
    print(a.passwords)