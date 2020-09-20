def value(colors):
    return int(''.join(map(str, [color_code(color) for color in colors[:2]])))

def color_code(color):
    return colors().index(color)

def colors():
    return ["black", "brown", "red", "orange",
            "yellow", "green", "blue", "violet",
            "grey", "white"]
