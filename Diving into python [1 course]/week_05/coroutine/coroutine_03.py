# Сопрограммы, генерация исключений


def grep(pattern):
    print("Start grep")
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("stop grep")


g = grep("python")
next(g)  # g.send('None')
g.send("python is simple!")
g.throw(RuntimeError, "something wrong")
