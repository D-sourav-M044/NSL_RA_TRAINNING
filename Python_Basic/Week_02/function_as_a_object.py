def add_explanation(line):
    return line + '!'
variable = add_explanation
print(variable('hello'))
print(variable)

#function as argument

def beautify(text):
    return text + "!"
def show(func,text):
    return 'hello ' + func(text)

print(show(beautify, 'robber'))