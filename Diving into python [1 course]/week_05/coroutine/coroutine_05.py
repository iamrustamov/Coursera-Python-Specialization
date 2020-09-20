# Сопрограммы, yield from PEP 0380


def grep(pattern):
    print("Start grep")
    while True:
        line = yield
        if pattern in line:
            print(line)


def grep_python_coroutine():
    g = grep("python")
    yield from g


g = grep_python_coroutine()  # is a coroutine?
g
g.send(None)
g.send("python wow!")
