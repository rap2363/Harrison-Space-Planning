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

if __name__ == '__main__':
    run()