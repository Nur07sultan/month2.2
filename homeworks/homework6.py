from blessed import Terminal

term = Terminal()

fruits = [
    (term.red, " Apple"),
    (term.yellow, " Banana"),
    (term.magenta, " Grapes"),
    (term.green, " Mango"),
    (term.cyan, " Orange"),
    (term.blue, " Strawberry"),
    (term.white, " Pineapple")
]

for color, fruit in fruits:
    print(color(fruit))