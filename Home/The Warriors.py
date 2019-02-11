#Answer to The Warriors - https://py.checkio.org/en/mission/the-warriors/

class Warrior: #Class Declaration
    health = 50 #Assigning health to 50
    attack = 5 #Assigning attack to 5
    is_alive = True #Assigning if that warrior is alive or not
    def update(self): #A function to update is_alive parameter
        self.is_alive = True if self.health > 0 else False #Assigning is_alive to False if he has 0 health

class Knight(Warrior): #Inheriting Warrior quality
    attack = 7 #But with better attack skills

def fight(unit_1, unit_2): #Function to check who wins
    while(True): #To run until one of them falls
        unit_2.health -= unit_1.attack #First attack from the 1st Person to the 2nd Person
        unit_2.update() #Updating is_alive
        if unit_2.is_alive == False: #If is_alive is False, then the second warrior is down
            return True #That means the First Warrior has won
        unit_1.health -= unit_2.attack #Attack from the 2nd Person to the 1st Person
        unit_1.update()
        if unit_1.is_alive == False:  #If is_alive is False, then the first warrior is down
            return False #That means the First Warrior has lost

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")