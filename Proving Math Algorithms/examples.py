from logic import *


# Sentence: "If it's rains, it's wet".
def rain_wet():
    Rain = Atom('Rain')  # whether it's raining
    Wet = Atom('Wet')  # whether it's wet
    return Implies(Rain, Wet)


# Sentence: "There is a light that shines."
def light_shines():
    def Light(x): return Atom('Light', x)  # whether x is lit

    def Shines(x): return Atom('Shines', x)  # whether x is shining

    return Exists('$x', And(Light('$x'), Shines('$x')))


# Defining Parent in terms of Child.
def parent_child():
    def Parent(x, y): return Atom('Parent', x, y)  # whether x has a parent y

    def Child(x, y): return Atom('Child', x, y)  # whether x has a child y

    return Forall('$x', Forall('$y', Equiv(Parent('$x', '$y'), Child('$y', '$x'))))
