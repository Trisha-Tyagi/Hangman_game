import hangman_stages
import random

word=["apple","banana", "elephant", "giraffe", "computer",
    "python", "bicycle", "airplane", "kangaroo", "waterfall",
    "strawberry", "pineapple", "chocolate", "sunshine", "notebook",
    "hamburger", "mountain", "telescope", "basketball", "submarine",
    "architecture", "bicycle", "courage", "dolphin", "exploration",
    "fireplace", "glacier", "horizon", "imagination", "jellyfish",
    "knowledge", "labyrinth", "meteor", "nebula", "oasis",
    "penguin", "quicksilver", "radiance", "symphony", "tornado",
    "universe", "volcano", "whirlpool", "xylophone", "yacht", "zebra"]
p=random.choice(word)
print(p)
chances=6
space=[]
for i in p:
    space.append("_")
while (chances>=0):
    print("Guess a no:")
    letter=input()
    isletter=False
    for i in range(len(p)):
        
        if (letter==p[i] and space[i]=="_"):
            space[i]=letter
            print('your left chances:',chances)
            print(space)
            isletter=True
            break
    if ("_" not in space and chances>=0):
        print("you won")
        break
    if (isletter==False):
        chances-=1
        print('your left chances:',chances)
        print(hangman_stages.stages[chances])
        print(space)
        if(chances<0):
            print("you lose")
print("game over")
        
        
