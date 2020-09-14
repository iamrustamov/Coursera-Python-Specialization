import os
import tempfile
import uuid


class File:
    def __init__(self, filename):
        self.dir = filename
        self.line = 0
        if not os.path.exists(filename):
            open(self.dir, 'w').close()

    def write(self, text):
        with open(self.dir, 'w') as f:
            return f.write(text)

    def read(self):
        with open(self.dir, 'r') as f:
            return f.read()

    def __add__(self, other):
        file = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()))
        cls = File(file)
        cls.write(self.read() + other.read())
        return cls

    def __str__(self):
        return self.dir

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.dir, 'r') as f:
            try:
                txt = f.readlines()[self.line]
                self.line += 1
                return txt
            except IndexError:
                self.line = 0
                raise StopIteration
