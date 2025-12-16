COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
def color_code(color):
    i= 0
    for i in range(len(COLORS)):
        if COLORS[i] == color:
                 return i 

def colors():
    return COLORS