## Space planning code for the Harrison Space
import spaceplandata
import math
import random
import numpy as np


employees,desks = spaceplandata.data()
numEmployees = len(employees)
numDesks = len(desks)
runTests = True
Tmax = .6

def run():
    solution = randomSolution()
    print evaluateSolution(solution)

def runTests():
    scores = []
    for i in range(10):
        scores.append(simulatedAnnealing()[1])
    print max(scores), np.var(scores)


# Generates a Random solution
def randomSolution():
    return dict(zip(range(numEmployees),random.sample(range(numDesks), numEmployees)))

# Evaluates a solution
def evaluateSolution(solution):
    scores = []
    for indID,deskID in solution.items():
        scores.append(evaluateIndividual(indID, deskID))
    return sum(scores)/numEmployees

# Evaluates an individual solution
def evaluateIndividual(indID, deskID):
    prefs = employees[indID]['preferences']
    deskScore = [desks[deskID]['individualScore'], desks[deskID]['lightScore'], desks[deskID]['loudnessScore']]
    return sum([nu*score for nu,score in zip(prefs, deskScore)])

## Algorithms to Solve #############################################################################

def simulatedAnnealing():
    solution = randomSolution()
    e = evaluateSolution(solution)
    k = 0
    kmax = 10000
    while k < kmax:
        T = calculateTemperature(k/kmax)
        solutionNew = getNeighbor(solution)
        enew = evaluateSolution(solutionNew)
        delE = enew - e
        if(boltzmann(delE, T) > random.random()):
            solution, e = solutionNew, enew
        k += 1
    return solution, e

## Calculates the temperature parameter for SA
def calculateTemperature(nu):
    return Tmax*(1-nu)

## Calculates the Boltzmannn distribution probability
def boltzmann(x, T):
    return 1/(1+math.exp(-(x/T)));

## Calculates a neighbor by swapping two people's locations and moving someone to a random, empty location
def getNeighbor(solution):
    n1,n2 = random.sample(range(numEmployees), 2)
    solution[n1], solution[n2] = solution[n2], solution[n1]
    emptyPlaces = getEmptyDesks(solution.values())
    nmove = random.choice(range(numEmployees))
    solution[nmove] = random.choice(emptyPlaces)
    return solution

## Finds the desks that haven't been used yet in the solution
def getEmptyDesks(nonEmptyDesks):
    emptyDesks = []
    for i in range(numDesks):
        if(not(i in nonEmptyDesks)):
            emptyDesks.append(i)
    return emptyDesks

####################################################################################################

if __name__ == '__main__':
    if(runTests):
        runTests()
    else:
        run()
