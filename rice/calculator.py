import simplegui

store = 0
operand = 0

def output():
    print "Store = ", store
    print "Operand = ", operand
    print ""
    
def swap():
    global store, operand
    store, operand = operand, store
    output()
    
def add():
    global store, operand
    store = store + operand
    output()
    
def sub():
    global store, operand
    store = store - operand
    output()
    
def mult():
    global store, operand
    store = store * operand
    output()
    
def div():
    global store, operand
    store = store / operand
    output()
    
def enter(inp):
    global operand
    operand = float(inp)
    output()
    
frame = simplegui.create_frame("Calculator", 300, 300)
frame.add_button("Print", output, 100)
frame.add_button("Swap", swap, 100)
frame.add_button("Add", add, 100)
frame.add_button("Sub", sub, 100)
frame.add_button("Mult", mult, 100)
frame.add_button("Div", div, 100)
frame.add_input("Enter operand", enter, 100)


frame.start()
