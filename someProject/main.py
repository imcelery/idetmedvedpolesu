
class Password:
    def __init__(self, site=None, username=None, word=None):
        self.site = site
        self.username = username
        self.word = word

    def __eq__(self, other):
        return self.site == other.site and self.username == other.username

    def __repr__(self):
        return str({"site": self.site, "username": self.username, "word": self.word})


class Stash:
    def __init__(self):
        self.passwords = []

    def encode(self, input):
        return " ".join(eval(str(input)).values())

    def decode(self, input):
        return input

    def safe(self, file):
        with open(file, 'w') as f:
            for i in self.passwords:
                f.writelines(self.encode(i) + "\n")

    def read(self, file):
        self.passwords = []
        with open(file, 'r') as f:
            for i in f.readlines():
                self.add(Password(*i[:-1].split(" ")))

    def add(self, item):
        self.passwords.append(item)

if __name__ == '__main__':
    a = Stash()
    a.add(Password("a", "c", "232"))
    a.add(Password("a", "b", "123"))

    a.safe("text.txt")
    a.read("text.txt")
    print(a.passwords)