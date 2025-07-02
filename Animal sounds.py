def animal_sounds(animals):
    for animal in animals:
        if animal == "cat":
            print("cat-meow")
        elif animal == "dog":
            print("dog-bark")
        elif animal == "cow":
            print("cow-moo")
        elif animal == "duck":
            print("duck-quack")
        else: 
            print(f"{animal} - unknown sound")
my_animals = ["cat","dog","cow","duck","lion"]
animal_sounds(my_animals)
        
