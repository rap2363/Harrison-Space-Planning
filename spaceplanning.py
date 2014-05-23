## Space planning code for the Harrison Space
import spaceplandata
import random


employees,desks = spaceplandata.data()
numEmployees = len(employees)
numDesks = len(desks)

def run():
    solution = randomSolution()
    print evaluateSolution(solution)



# Generates a Random solution
def randomSolution():
    return dict(zip(range(numEmployees),random.sample(range(numDesks), numEmployees)))

# Evaluates a solution
def evaluateSolution(solution):
    scores = []
    for indID,deskID in solution.items():
        scores.append(evaluateIndividual(indID, deskID))
    print scores
    return sum(scores)/numEmployees

# Evaluates an individual solution
def evaluateIndividual(indID, deskID):
    prefs = employees[indID]['preferences']
    deskScore = [desks[deskID]['individualScore'], desks[deskID]['lightScore'], desks[deskID]['loudnessScore']]
    return sum([nu*score for nu,score in zip(prefs, deskScore)])

## Algorithms to Solve #############################################################################

def simulatedAnnealing():
    s = randomSolution()
    e = evaluateSolution(s)
    sbest = s
    ebest = e
    k = 0
    kmax = 1000
    while k < kmax:
        T = calculateTemperature(k/kmax)
        snew = getNeighbor(solution)
        enew = evaluateSolution(snew)
        if()

## Calculates the temperature parameter for SA
def calculateTemperature(nu):
    Tmax = .3
    return Tmax*(1-nu)

## Calculates a neighbor by swapping two people's locations and moving someone to a random, empty location
def getNeighbor(solution):


####################################################################################################

if __name__ == '__main__':
    run()