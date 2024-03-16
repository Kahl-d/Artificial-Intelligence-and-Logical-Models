from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(

    # Basic puzzle conditions to seperate valid models
    # A is either a knight or a knave
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # If A is telling the lie, he is a Knave
    # As what A says is universally false for our models
    # So if A says something flase, A is Knave
    Biconditional(Not(And(AKnight, AKnave)), AKnave)


)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Basic puzzle conditions to seperate valid models
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    # If what A says is not true, A is a Knave
    # Also the other way, when we decide that a is a Knave
    # then what A says, both AKnave and BKnave cannot be true
    Biconditional(Not(And(AKnave, BKnave)), AKnave)



)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Basic puzzle conditions to seperate valid models
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    # Biconditional for A
    # If what a says is false, A is a Knave and
    # If A is a Knave, then what A says is false
    Biconditional(Not(Or(And(AKnight, BKnight), And(AKnave, BKnave))), AKnave),


    # If what B says is not true, B is a Knave, and vice versa
    # If B is a Knave, what he says is not true
    Biconditional(Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))), BKnave)


)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Basic puzzle conditions to seperate valid models
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    # A's simple statement
    # if A is a knight, then he is telling the truth, he must be a Knight
    Implication(Or(AKnight, AKnave), AKnight),

    # If B says exacly what A said, then B is a knight, else B is a knave
    # Other conditions are sufficient, so we dont need to add for this case


    # If C is telligh the truth about A he is a knight
    # And vice versa
    Biconditional(AKnight, CKnight),

    # If B is telling the truth then C is a knave, B is a Knight
    # And vice versa
    Biconditional(CKnave, BKnight)


)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
