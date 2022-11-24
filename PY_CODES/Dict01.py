print("*******This is to translate input from user in English to Frenchls in a dictionaries data type******\n")
Garden_avail = {
    "prune": "dried_plum",
    "banana": "banane",
    "pineapple": "ananas",
    "apple": "pomme",
    "guava" :"goyave",
}
User = (input('insert your favorite fruits inside the garden\n'))
word = Garden_avail.get(User)
if User in Garden_avail:
    print(word)
else:
    print("not in the garden")    