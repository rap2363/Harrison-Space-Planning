## Space planning code for the Harrison Space
import spaceplandata
import math
import random
import numpy as np
import pylab as plt


employees,desks, teams = spaceplandata.data()
numEmployees = len(employees)
numDesks = len(desks)
Tmax = 6
numOffspring = 2 ## Number of offspring to produce per couple
pmut = .3 #Probability of mutation
pop_size = 100 #Population size
ITERS = 10000
MAX_DIST_SQUARED = 1.1296

def run():
    random.seed(15)
    pop, maxScores, minScores, avgScores = geneticAlgorithm(ITERS, pmut)
    best = pop[pop_size-1]
    print 'Score:' +str(best[0])
    for deskID, name in sorted(zip(best[1].values(), best[1].keys())):
        print str(deskID)+': '+name +',' +str(evaluateIndividualPreAtDesk(name, deskID))+', '+str(evaluateIndividual(name, deskID))
    plt.plot(range(ITERS), avgScores, range(ITERS), maxScores, range(ITERS), minScores)
    plt.show()
    plt.figure()
    for name, deskID in best[1].items():
        loc = desks[deskID]['location']
        x,y = loc[0],loc[1]
        plt.text(x, y, name, fontsize=8)
    plt.xlim(0,.7)
    plt.ylim(0,1)
    plt.show()

## Generates a Random solution
def randomSolution():
    return dict(zip(employees.keys(),random.sample(range(numDesks), numEmployees)))

## Evaluates a solution
def evaluateSolution(solution):
    scores = []
    teamScores = []
    for indID, deskID in solution.items():
        scores.append(evaluateIndividual(indID, deskID))
        teamScores.append(evaluateTeamScore(indID, deskID, solution))
    # worstTeamScore = evaluateWorstTeamScore(solution)
    # return sum(scores)/numEmployees + worstTeamScore
    return (sum(scores)+sum(teamScores))/numEmployees
    #return min(scores)+min(teamScores)

## Evaluates an individual solution
def evaluateIndividual(name, deskID):
    prefs = employees[name]['preferences']
    deskprefs = [prefs['lightScore'], prefs['loudnessScore'], prefs['heatScore']]
    deskparams = desks[deskID]['preferences']
    deskScore = [deskparams['lightScore'], deskparams['loudnessScore'], deskparams['heatScore']]
    return employees[name]['atDeskLikelihood']*sum([nu*score for nu,score in zip(deskprefs, deskScore)])

## Evaluates an individual solution
def evaluateIndividualPreAtDesk(name, deskID):
    prefs = employees[name]['preferences']
    deskprefs = [prefs['lightScore'], prefs['loudnessScore'], prefs['heatScore']]
    deskparams = desks[deskID]['preferences']
    deskScore = [deskparams['lightScore'], deskparams['loudnessScore'], deskparams['heatScore']]
    return sum([nu*score for nu,score in zip(deskprefs, deskScore)])

## Evaluates the worst team score (i.e. the furthest distance in a team)
def evaluateWorstTeamScore(solution):
    totalMaxDist = 0
    for team in teams:
        maxDist = -1
        for i in range(len(team)):
            for j in range(i+1, len(team)):
                dist = squareDistance(desks[solution[team[i]]]['location'], desks[solution[team[j]]]['location'])
                if(dist > maxDist):
                    maxDist = dist
        totalMaxDist += maxDist/len(teams)
    return -totalMaxDist/MAX_DIST_SQUARED
## Evaluates the individual's team score
def evaluateTeamScore(indID, deskID, solution):
    indTeams = [team for team in teams if (indID in team)]
    totdist = 0
    for indTeam in indTeams:
        dist = 0
        for otherInd in indTeam:
            dist += squareDistance(desks[deskID]['location'], desks[solution[otherInd]]['location'])
        #totdist += dist/(len(indTeams)*len(indTeam))
        totdist += dist
    return employees[indID]['preferences']['individualScore']*(1-2*totdist)

## Algorithms to Solve #############################################################################

## Finds the optimal through a genetic algorithm
def geneticAlgorithm(ITERS, prob_mutation):
    pop = generatePopulation()
    minScores,maxScores,avgScores=[],[],[]
    for k in range(ITERS):
        reproducers = pickReproducingPopulation(pop)
        offspring = produceOffspring(reproducers, prob_mutation)
        for i in range(10):
            offspring.append(randomSolution())
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
    for i in employees.keys():
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
        if(random.random() < prob_mutation):
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
    #probs = [(2-b+2.*i*(b-1)/(pop_size-1))/(pop_size) for i in range(pop_size)]
    probs = calculateProbs(pop)
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

## Calculates a neighbor by swapping two people's locations and moving someone to a random, empty location
def getNeighbor(solution):
    n1,n2 = random.sample(employees.keys(), 2)
    solution[n1], solution[n2] = solution[n2], solution[n1]
    emptyPlaces = getEmptyDesks(solution.values())
    nmove = random.choice(employees.keys())
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
    run()
