# Сопрограммы (корутины)


def grep(pattern):
    print("Start grep")
    while True:
        line = yield
        if pattern in line:
            print(line)


g = grep("python")
next(g)  # g.send('None')
g.send("golang is better?")
g.send("python is simple!")
