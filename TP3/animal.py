'''Creating animals and their children'''
# encoding : utf8

class Animal():
    '''Creating class Animal'''
    def __init__(self, name, species, age, diet) -> None:
        '''Defining initial class parameters(name,species etc) and creating empty list
        of children and an empty variable mother'''
        self.name=name
        self.species = species
        self.age = age
        self.diet = diet
        self.children = []
        self.mother = None
        self.foot=None
        self.mother_name="Unknown"
        self.children_info=[]
    def set_species(self, species):
        '''Function allowing to define species'''
        self.species = species

    def set_foot_nb(self, foot) :
        '''Function allowing to define number of feet'''
        self.foot = foot
        return super().__str__ + "She has " + self.foot +" feet"

    def add_children(self,child_name,child_age) -> None:
        '''Function allowing to add children'''
        #Create a child that also is an Animal, taking a given name and age
        #The child will inherit mother's species and diet
        child = Animal(child_name,self.species,child_age,self.diet)
        #if the created child is not in children list already, add the child object to
        #the list, and add child's name to the name list
        if child_name not in self.children_info:
            self.children.append(child)
            self.children_info.append(str(child.name))
            #set self as a child's mother
            child.mother_name = self.name
            child.mother = self
            #in variable mum stock the mother of the current object(child's grandmother)
            mum= self.mother
            while mum: #while mum exists
                for baby in self.children: #for each child in list of children
                    #if the name of the child is not in mothers list of children, add it to the list
                    if str(baby.name) not in mum.children_info:
                        mum.children.append(baby)
                        mum.children_info.append(baby.name)
                #stock in the variable mum mother of the current mother(child's great grandmother)
                mum=mum.mother
        else:
            print("You already have a child named like that...")
        return child

    def remove_children(self,child_name) -> None:
        '''Function allowing to remove children'''
        #if given name is in the list-remove it
        if child_name in self.children_info:
            self.children_info.remove(child_name)
        #for each child in list of children, if the name of the
        #object equals the given name-remove it
        for child in self.children:
            if str(child.name)==str(child_name):
                self.children.remove(child)
        #in variable mum stock the mother of the current object(child's grandmother)
        mum= self.mother
        while mum:#while mum exists
            for baby in mum.children: #for each child in grandmother's list of children
                #if the name of the child equals the given name -remove it from the list
                if str(baby.name)==str(child_name):
                    mum.children.remove(baby)
                    mum.children_info.remove(str(baby.name))
            #stock in the variable mum mother of the current mother(child's great grandmother)
            mum=mum.mother


    def __str__(self) -> str:
        if self.children_info:
            return self.name +" is a " +self.species + " who is " + str(self.age) +\
                " years old \nShe is " + self.diet +\
                ". Her children are : " +\
                str(self.children_info) + " and her mother is: " + str(self.mother_name)
        return self.name + " is a " +self.species + " who is "+\
                str(self.age) + " years old \nShe is " +\
                self.diet + "\n" +\
                "She doesn't have children and her mother is " + str(self.mother_name)

    def __eq__(self, __o: object) -> bool:
        return (self.species == __o.species and self.age == __o.age and
         self.diet == __o.diet and self.foot == __o.foot)

class Human(Animal):
    '''Creating class Human'''
    def __init__(self, name, age) -> None:
        super().__init__(name, "Human", age, "Omnivore")

class Snake(Animal) :
    '''Creating class Snake'''
    def __init__(self, name, age) -> None:
        super().__init__(name, "Snake", age, "Carnivore")

if __name__ == "__main__":
    animal1 = Animal("Bella","Dog",10,"Carnivore")
    animal2 = animal1.add_children("Lucy",8)
    animal3 = animal1.add_children("Coco",7)
    animal4 = animal2.add_children("Ginger",5)
    animal5 = animal4.add_children("Boo",3)
    animal6=animal5.add_children("Charlie",1)
    animal7=animal5.add_children("Ms.Whoof",1)
    print(animal1)
    print(animal2)
    print(animal3)
    print(animal4)
    print(animal5)

    animal5.remove_children("Ms.Whoof")
    print(animal5)
    print(animal1)

    human1 = Human("Mary", 75)
    human2 = human1.add_children("Alice",50)
    human3 = human1.add_children("Nicole",49)
    human4 = human2.add_children("Kate", 25)
    human5 = human3.add_children("Samantha",20)
    print(human1)
    print(human2)

    snake1 = Snake("Snoopy", 56)
    snake2 = snake1.add_children("Storm", 20)
    snake3=snake2.add_children("Saturn",10)
    print(snake1)
