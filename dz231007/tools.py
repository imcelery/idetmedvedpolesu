import os
class File:
    def __init__(self, name):
        self.name = name
        self.to_delete = False

    def __str__(self):
        return self.name


class FileSystem:
    def list_dir(self):
        raise NotImplementedError()

    def is_dir(self, filename):
        raise NotImplementedError()

    def add_path(self, path, name):
        raise NotImplementedError()

    def get_name(self, filename):
        raise NotImplementedError()

    def get_file(self, filename):
        raise NotImplementedError()

    def to_dir(self, dirname):
        raise NotImplementedError()


class LocalFileSystem(FileSystem):
    def __init__(self, path):
        self.path = path

    def list_dir(self):
        return os.listdir(self.path)

    def is_dir(self, filename):
        return os.path.isdir(self.add_path(self.path, filename))

    def add_path(self, path, name):
        return os.path.join(path, name)

    def get_name(self, filename):
        return self.add_path(self.path, filename)

    def get_file(self, filename):
        p = self.add_path(self.path, filename)
        with open(p, "rb") as f:
            data = f.read()
        return data

    def to_dir(self, dirname):
        return LocalFileSystem(self.add_path(self.path, dirname))


class FakeFileSystem(FileSystem):
    def __init__(self, path):
        self.path = path

    def list_dir(self):
        return self.path

    def is_dir(self, filename):
        return isinstance(list(filename.values())[0], list)

    def add_path(self, path, name):
        return path + "/" + name

    def get_name(self, filename):
        return list(filename.keys())[0]

    def get_file(self, filename):
        return list(filename.values())[0]

    def to_dir(self, dirname):
        return FakeFileSystem(list(dirname.values())[0])


def get_hash(path:str) -> str:
    h = str(hash(path))
    return h


def get_list_names(file_system: FileSystem) -> list[tuple[str, str]]:
    res = []
    for path in file_system.list_dir():
        if file_system.is_dir(path):
            res.extend(get_list_names(file_system.to_dir(path)))
        else:
            res.append((file_system.get_name(path), get_hash(file_system.get_file(path))))
    return res


def get_ext(filename: str) -> str:
    if "." in filename:
        return filename.rsplit(".", maxsplit=1)[-1]
    return ""


class File:
    def __init__(self, name):
        self.name = name
        self.to_delete = False

    def to_del(self):
        self.to_delete = True

    def to_save(self):
        self.to_delete = False

def filter(list_names: list[tuple[str, str]], filters: list[str]) -> list[tuple[str, str]]:
    filtered_list = []
    for el in list_names:
        ext = get_ext(el[0])
        if ext in filters:
            filtered_list.append(el)
    return filtered_list


def search_duplicates(list_names: list[tuple[str, str]]) -> dict[str, list[str]]:
    d = {}
    for path, hash in list_names:
        if hash not in d:
            d[hash] = []
        d[hash].append(path)
    l = list(d.keys())
    for i in l:
        if len(d[i]) == 1:
            d.pop(i)
    return d

def to_file_objects(d: dict[str, list[str]]) -> list[list[File]]:
    res = []
    for list_names in d.values():
        res.append([File(path) for path in list_names])
    return res

def list_files_to_files_to_remove(list_files: list[list[File]]) -> list[str]:
    o = []
    for i in list_files:
        for j in i:
            if j.to_delete:
                o.append(j.name)
    return o

def remove_file(list_files: list[str]):
    for i in list_files:
        os.remove(i)
