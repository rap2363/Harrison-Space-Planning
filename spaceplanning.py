## Space planning code for the Harrison Space
import spaceplandata
import math
import random
import numpy as np
import pylab as plt


employees,desks, teams = spaceplandata.data()
numEmployees = len(employees)
numDesks = len(desks)
testing = False
Tmax = 6
numOffspring = 2 ## Number of offspring to produce per couple
pmut = .6 #Probability of mutation
pop_size = 100 #Population size
MAX_DIST_SQUARED = 1.1296

def run():
    random.seed(0)
    ITERS = 10000
    pop, maxScores, minScores, avgScores = geneticAlgorithm(ITERS, pmut)
    best = pop[pop_size-1]
    #best[1][13] = 16
    print 'Score:' +str(best[0])
    for indID,deskID in best[1].items():
        print employees[indID]['name']+': '+str(deskID)
    plt.plot(range(ITERS), avgScores, range(ITERS), maxScores, range(ITERS), minScores)
    plt.show()
    plt.figure()
    for i in range(numEmployees):
        loc = desks[best[1][i]]['location']
        x,y = loc[0],loc[1]
        plt.text(x, y, employees[i]['name'], fontsize=8)
    plt.xlim(0,.7)
    plt.ylim(0,1)
    plt.show()

def runTests():
    ITERS = 10000
    bestScores = []
    for pmut in np.arange(0,1,.05):
        print pmut
        pop, maxScores, minScores, avgScores = geneticAlgorithm(ITERS, pmut)
        bestScores.append(maxScores[ITERS-1])
    plt.plot(np.arange(0,1,.05), bestScores)
    plt.show()

## Generates a Random solution
def randomSolution():
    return dict(zip(range(numEmployees),random.sample(range(numDesks), numEmployees)))

## Evaluates a solution
def evaluateSolution(solution):
    scores = []
    teamScores = []
    for indID,deskID in solution.items():
        scores.append(evaluateIndividual(indID, deskID))
        teamScores.append(evaluateTeamScore(indID, deskID, solution))
    return (sum(scores)+sum(teamScores))/numEmployees
    #return min(scores)+min(teamScores)

## Evaluates an individual solution
def evaluateIndividual(indID, deskID):
    prefs = employees[indID]['preferences']
    deskprefs = [prefs[0], prefs[2], prefs[3]]
    deskScore = [desks[deskID]['individualScore'], desks[deskID]['lightScore'], desks[deskID]['loudnessScore']]
    return sum([nu*score for nu,score in zip(deskprefs, deskScore)])

## Evaluates the individual's team score
def evaluateTeamScore(indID, deskID, solution):
    indTeams = [team for team in teams if (indID in team)]
    totdist = 0
    for indTeam in indTeams:
        dist = 0
        for otherInd in indTeam:
            dist += squareDistance(desks[deskID]['location'], desks[solution[otherInd]]['location'])
        totdist += dist/(len(indTeams)*len(indTeam))
    return employees[indID]['preferences'][1]*(1-2*totdist)

## Algorithms to Solve #############################################################################

## Finds the optimal through a genetic algorithm
def geneticAlgorithm(ITERS, prob_mutation):
    pop = generatePopulation()
    minScores,maxScores,avgScores=[],[],[]
    for k in range(ITERS):
        reproducers = pickReproducingPopulation(pop)
        offspring = produceOffspring(reproducers, prob_mutation)
        pop.extend(offspring)
        pop = eugenics(pop, len(pop)-pop_size)
        scores = [p[0] for p in pop]
        maxScores.append(np.max(scores))
        minScores.append(np.min(scores))
        avgScores.append(np.mean(scores))
    return pop, maxScores, minScores, avgScores

## Produces a number of offspring for a reproducing population
def produceOffspring(reproducers, prob_mutation):
    random.shuffle(reproducers)
    offspring = []
    for i in range(0, len(reproducers), 2):
        for j in range(numOffspring):
            child = generateChild(reproducers[i][1], reproducers[i+1][1], prob_mutation)
            offspring.append([evaluateSolution(child), child])
    return offspring

## Generates a child between two consenting parent solutions
def generateChild(parent0, parent1, prob_mutation):
    solution = {}
    for i in range(numEmployees):
        emptyPlaces = getEmptyDesks(solution.values())
        desk0, desk1 = parent0[i], parent1[i]
        if(random.random() >= 0.5):
            desk = desk0
            if(desk in solution.values()):
                desk = random.choice(emptyPlaces)
        else:
            desk = desk1
            if(desk in solution.values()):
                 desk = random.choice(emptyPlaces)
        solution[i] = desk
    cond = True
    i = 1
    while(cond):
        if(random.random() < prob_mutation**i):
            solution = getNeighbor(solution)
            i += 1
        else:
            cond = False
    return solution

## Kills off the weakest members of society
def eugenics(pop, numberToKill):
    return sorted(pop)[numberToKill:]

## Picks a number of reproducing solutions to "make babies"
def pickReproducingPopulation(pop):
    b = 2
    pop_rep = int(pop_size*.1)
    sortedPop = sorted(pop)
    probs = [(2-b+2.*i*(b-1)/(pop_size-1))/(pop_size) for i in range(pop_size)]
    #probs = calculateProbs(pop)
    reproducingIndices = pickDistinct(probs, pop_rep)
    reproducers = []
    for i in reproducingIndices:
        reproducers.append(sortedPop[i])
    return reproducers

## Calculates proportional weighted probabilities according to fitness
def calculateProbs(pop):
    totalFitness = 0.0
    for ind in pop:
        totalFitness += ind[0]
    return [ind[0]/totalFitness for ind in pop]

## Generates a population
def generatePopulation():
    pop = []
    for i in range(pop_size):
        sol = randomSolution()
        score = evaluateSolution(sol)
        pop.append([score, sol])
    return pop

# Finds the optimal through simulated annealing
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
    return Tmax*(1-nu)**2

## Calculates the Boltzmannn distribution probability
def boltzmann(x, T):
    return 1/(1+math.exp(-(x/T)))

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

## Picks k distinct numbers according to a sample distribution
def pickDistinct(probs, k):
    numList = []
    while(k > 0):
        newNum = sampleDistribution(probs)
        numList.append(newNum)
        condProb = probs[newNum]
        probs[newNum] = 0
        probs = [p/(1.-condProb) for p in probs]
        k -= 1
    return numList

## Samples a distribution and returns an index (probabilities must add up to 1)
def sampleDistribution(probs):
    markProb = random.random()
    tot = 0
    i = 0
    number = -1
    numberFound = False
    while(not(numberFound)):
        tot += probs[i]
        if(tot > markProb):
            number = i
            numberFound = True
        i+=1
    return number

## Calculates the Euclidean Square Distance
def squareDistance(point0, point1):
    return (point0[0]-point1[0])**2 + (point0[1]-point1[1])**2

####################################################################################################


if __name__ == '__main__':
    if(testing):
        runTests()
    else:
        run()
