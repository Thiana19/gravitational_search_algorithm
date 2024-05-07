import random
import math
import numpy as np
import time

def read(filename):
    fields = []
    i = 0
    with open(filename) as f:
        for x in f:
            fields += [x.rstrip('\n').split(" ")]
            fields[i][0] = float(fields[i][0])
            fields[i][1] = float(fields[i][1])
            i += 1
        return fields

def count(mutants):
    """
    Counts the number of mutants
    """
    count = 0
    for i in mutants:
        count += 1
    return count
        
def total(selected_mutants):
    """
    Calculates the total value and total weight of the selected list of mutants
    """
    total_value = 0
    total_weight = 0
    for i in selected_mutants:
        total_value += i[0]
        total_weight += i[1]
    return total_value, total_weight

def value_per_stone(mutants):
    vps = []
    for i, item in enumerate(mutants):
        vps.append(mutants[i][0]/mutants[i][1] if mutants[i][1] > 0 else 100)
    return vps

mutants = read("mutants.txt")

class gsa():
    
    epsilon = 0.001

    def mass(i, best, worst):
        m = (total(i)[0] - total(worst)[0])/(total(best)[0]-total(worst)[0])
        return m

    def fit(solution):
        return total(solution)[0] / total(solution)[1]

    def getBitmap(solution):
        bitmap = [0] * 32
        for index, mutant in enumerate(solution):
            if(mutant == mutants[index]):
                bitmap[index] = 1
        return bitmap

    def equalize(arr1, arr2):
        if(arr1.shape > arr2.shape):
            arr2 = np.concatenate((arr2, np.zeros((arr1.shape[0] - arr2.shape[0], 2))))
        else:
            arr1 = np.concatenate((arr1, np.zeros((arr2.shape[0] - arr1.shape[0], 2))))
        return arr1, arr2

    def force(solution, massInertial, population, bits, Kbest, iter, maxiter):
        force = random.uniform(0,1) * sum([gsa.gf(solution, otherSolutions, massInertial, population, bits, iter, maxiter) for otherSolutions in Kbest if solution != otherSolutions])
        return force

    def gf(solution1, solution2, massInertial, population, bits, iter, maxiter):
        g = iter
        gmax = 100
        G0 = 1
        thetha = 23
        iarr = np.array(bits[population.index(solution1)])
        jarr = np.array(bits[population.index(solution2)])
        #iarr, jarr = gsa.equalize(iarr, jarr)
        G = G0 * math.exp(-thetha * g/gmax)
        eucd = np.linalg.norm(iarr - jarr)
        hamm = np.count_nonzero(iarr!=jarr)
        F = G * massInertial[population.index(solution1)] * massInertial[population.index(solution2)] * (solution2[0][0] - solution1[0][0]) / (eucd + gsa.epsilon)
        return F

    def accel(solution, force, population, massInertial):
        return force[population.index(solution)]/(massInertial[population.index(solution)] + gsa.epsilon)

    def probability(vel, solution, population):
        return (math.exp(vel[population.index(solution)]) - math.exp(-vel[population.index(solution)])) / ((math.exp(vel[population.index(solution)]) + math.exp(-vel[population.index(solution)])))

    def __init__(self):
        #Initializing population of solutions
        population = []
        bits = []
        N = 50
        maxiter = 100
        Kbest = []
        bestAllGen = []
        for cnt in range(N):
            bit = [0] * 32
            num = 1
            solution = [random.choice(mutants)]
            bit[mutants.index(solution[0])] = 1
            while(total(solution)[1] < 65):
                bit[random.randint(0,31)] = 1
                solution = [s for i, s in enumerate(mutants) if bit[i] == 1]
                num += 1
            if(total(solution)[1] > 65):
                while(total(solution)[1] > 65):
                    bit[random.randint(0,31)] = 0
                    solution = [s for i, s in enumerate(mutants) if bit[i] == 1]
            bits.append(bit)
            population.append(solution)
        
        vel = [0] * N
        pos = bits

        for iter in range(maxiter):
            #Evaluating fitness of the solutions
            population.sort(reverse=True, key=lambda pair:total(pair)[0])

            #Update best, worst, massInertial
            best = max(population, key=lambda pair: total(pair)[0])
            bestAllGen = sorted(population + bestAllGen, key=lambda pair:total(pair)[0], reverse=True)[:][:1]
            Kbest = sorted(population, key=lambda pair:total(pair)[0], reverse=True)[:][:maxiter-iter]
            print(total(best))
            worst = min(population, key=lambda pair: total(pair)[0])
            masses = [gsa.mass(solution, best, worst) for solution in population]
            massInertial = [mass/sum(masses) for mass in masses]
            
            force = []
            accel = []
            for solution in population:
                #Compute total force acting on a solution
                force += [gsa.force(solution, massInertial, population, bits, Kbest, iter, maxiter)]
                #Compute the acceleration
                accel += [gsa.accel(solution, force, population, massInertial)]
                #Update velocity
                vel[population.index(solution)] = random.uniform(0,1) * vel[population.index(solution)] + accel[population.index(solution)]

            li = [0, 0]
            for a, i in enumerate(bits):
                while(1):
                    for b, j in enumerate(bits[a]):
                        rand = random.uniform(0,1)
                        if rand < abs(gsa.probability(vel, i, bits)):
                            bits[a][b] = -~-bits[a][b]
                            li = [a, b]
                    population = [[s for i, s in enumerate(mutants) if bits[j][i] == 1] for j in range(N)]
                    if(total(population[li[0]])[1] <= 65):
                        break
            pos = bits
            population = [[s for i, s in enumerate(mutants) if bits[j][i] == 1] for j in range(N)]
            if(iter == maxiter-1):
                print("Converged mutant combination: ", best)
        print("Best mutant value among all generation: ", total(bestAllGen[0]))
        print("Best mutant combination among all generation: ", bestAllGen)

gsa()