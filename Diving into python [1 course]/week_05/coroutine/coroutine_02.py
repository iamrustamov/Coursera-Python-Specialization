# Сопрограммы, вызов метода close()


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
g.send("golang is better?")
g.send("python is simple!")
g.close()
