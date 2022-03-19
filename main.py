# Genetic Algorithm : be or not to be
# Matis CAFFIAUX 

from operator import ge
from random import randrange , random


class Person() :

    genotype : str = ""

    def __init__(self, genotypeLength : int, genotype="") -> None:
        if genotype == "":
            for _ in range(genotypeLength):
                self.genotype +=  (lambda : chr(ord("a") +randrange(25)))()
        else:
            self.genotype = genotype

    def __str__(self) -> str:
        return self.genotype

    def __add__(self, other): # Multi-cross random points
        childGenotype = ""
        
        for index in range(len(self.genotype)):
            
            if randrange(2) == 0:   # Left Parent
                childGenotype += self.genotype[index]
            else:                   # Right Parent
                childGenotype += other.genotype[index]
    
        return Person(len(self.genotype),childGenotype)

    def replace(self , toRemove:int) -> None:
        temp = ""
        for index, elem in enumerate(self.genotype):
            if index != toRemove:
                temp += elem
            else:
                temp += (lambda : chr(ord("a") +randrange(25)))()
        self.genotype = temp

    def mutate(self):
        mutation = randrange(len(self.genotype))
        for mutation in range(mutation):
            self.replace(randrange(len(self.genotype)))

    
    def evaluate(self, genotypeGoal : str) -> float:
        temp : float = 0.0

        for index , elem in enumerate(self.genotype):
            if elem == genotypeGoal[index] : 
                temp += 1

        return temp/(index+1)


class Population():
    pop: list = []

    probGrowth : float
    probMutation : float

    genotypeGoal :str 

    def __init__ (self , sizeOfPop : int ,genotypeLength : int, genotypeGoal: str , probGrowth : float = 0.50, probMutation : float = 0.30) -> None :
        self.probGrowth = probGrowth
        self.probMutation = probMutation
        self.genotypeGoal = genotypeGoal
        
        for _ in range(sizeOfPop):
            self.pop.append(Person(genotypeLength))
        
    def __str__(self) -> str:
        temp = ""
        for index, elem in enumerate(self.pop):
            temp+= f"Person {index}: "+elem.__str__() +" "+str(elem.evaluate(self.genotypeGoal))+"\n"
        return temp

    def sort(self) -> None:
        self.pop = sorted(self.pop, key=lambda x: x.evaluate(self.genotypeGoal), reverse=True)
    

    def newGen(self) -> None:
        self.sort()

        reproducers = self.pop[0:len(self.pop)//6]
        childs = []

        i,j = 0,1
        while(len(childs)< int(len(self.pop)*self.probGrowth)):
            if(i == len(reproducers)):
                i, j = 0 , j+1

            child = reproducers[i]+reproducers[j]

            if(random()<=self.probMutation): # Mutation
                child.mutate()

            childs.append(child)

        self.pop[len(self.pop)-1 - int(len(self.pop)*self.probGrowth):-1] = childs # Replacement of worst parents

    
    def iterate(self, nIter : int) -> None:
        for _ in range(nIter):
            if(_%((nIter//10)+1) == 0):

                print(f"Iteration n°:{_} \r")
            self.newGen()

            if(self.pop[0].evaluate(self.genotypeGoal) ==1.0):
                print(f"Goal has been found in {_} Iterations \n")
                return None
    
    def until(self):
        nInter = 1
        while True:
            if(nInter%100 == 0):
                print(f"Iteration n°:{nInter} \r", )

            self.newGen()
            nInter+=1

            if(self.pop[0].evaluate(self.genotypeGoal) == 1.0):
                print(f"Goal has been found in {nInter} Iterations \n")
                return None

            

if __name__ == '__main__':

    pop = Population(2000, 11, "beornottobe")
    pop.until()
    print(pop.pop[0], pop.pop[0].evaluate("beornottobe"))
    
