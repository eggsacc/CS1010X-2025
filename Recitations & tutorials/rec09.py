class Food(object):
    def __init__(self, name, nutrition, good_until):
        self.name = name
        self.nutrition = nutrition
        self.good_until = good_until
        self.age = 0
    
    def sit_there(self, time):
        self.age += time
    
    def eat(self):
        if(self.age <= self.good_until):
            return self.nutrition
        
        else:
            return 0
    
class AgedFood(Food):
    def __init__(self, name, nutrition, good_until, good_after):
        super().__init__(name, nutrition, good_until)
        self.good_after = good_after

    def sniff(self):
        return self.age >= self.good_after
    
    def eat(self):
        if(self.sniff()):
            return super().eat
        else:
            return 0
        
class VendingMachine(Food):
    def __init__(self, name, nutrition, good_until):
        super().__init__(name, nutrition, good_until)
    
    def sit_there(self, time):
        self.age += time / 2
    
    def sell_food(self):
        food = Food(self.name, self.nutrition, self.good_until)
        food.age = self.age
        return food

def mapn(fn, args):

    # Check for empty input params
    if(not args):
        return None
    
    output = []
    # Convert params to lists
    args = [list(arg) for arg in args]

    while len(args[0]):
        terms = []

        # Return partial solution if input param lengths are different
        for arg in args:
            if(not len(arg)):
                return output
            else:
                terms.append(arg[0])
                
        terms = [arg[0] for arg in args]
        args = [arg[1:] for arg in args]
        output.append(fn(*terms))

    return tuple(output)