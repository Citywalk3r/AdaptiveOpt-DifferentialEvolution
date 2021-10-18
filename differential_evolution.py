import random
import numpy as np

class Differential_Evolution:

    def __init__(self,):
        pass

    def generate_init_pop(self, seed, ps):
        """
        Generates the initial population given population size ps.
        """
        rng = np.random.default_rng(seed)
        init_generation = [np.ndarray.tolist(rng.uniform(-512,512,2)) for _ in range(ps)]
        return init_generation


    def generateMutantVector(self, pop, target, F, strategy, eval_f):
            """Generates the mutant (or donor) Vector.
           
            Parameters:
                pop: current population
                target : Main parent, or target vector (2D array of format [x,y])
                F: proportion of difference between two mutant parents (normally between 0 and 1)
                strategy: Bin or best , where 
                    Bin: 𝑉^𝑖 = 𝑋^(𝑛_1 ) + 𝐹(𝑋^(𝑛_2 )−𝑋^(𝑛_3 ))
                    Best: 𝑉^𝑖 = 𝑋^𝑏𝑒𝑠𝑡 + 𝐹(𝑋^(𝑛_1 )−𝑋^(𝑛_2 ))

            Returns:
                Mutant : mutant vector (𝑉^𝑖) = 𝑋^(𝑛_1 )+𝐹(𝑋^(𝑛_2 )−𝑋^(𝑛_3 ))

            """

            mutant = np.ndarray.tolist(np.random.uniform(-512,512,2))

            population = pop.copy()
            population.remove(target)

            if strategy=="bin":
                parents = random.sample(population, 3)
            else:
                best = sorted(population, key=lambda parent: eval_f(parent))[0]
                population.remove(best)
                parents = [best] + random.sample(population, 2)

            tmp_X = parents[0][0] + F*(parents[1][0] - parents[2][0])
            tmp_Y = parents[0][1] + F*(parents[1][1] - parents[2][1])

            if tmp_X >=-512 and tmp_X <=512:
                mutant[0] = tmp_X
            if tmp_Y >=-512 and tmp_Y <=512:
                mutant[1] = tmp_Y

            return mutant
    
    def generateTrialVector(self, target, mutant, CR, jrand):
            """Generates the trial Vector.
           
            Parameters:
                target : Main parent, or target vector (2D array of format [x,y])
                mutant: Individual generated after mutation
                CR: crossover probability
                jrand: Dimension where mutant value is inserted by default.
            Returns:
                Trial : Trial vector (2D array of format [x,y])

            """
            trial = np.ndarray.tolist(np.random.uniform(-512,512,2))

            for i in range(len(trial)):
                if i==jrand:
                    trial[i] = mutant[i]
                elif np.random.uniform(0,1) <= CR:
                    trial[i] = mutant[i]
                else:
                    trial[i] = target[i]
            
            return trial


    def de(self, ps, g_max, eval_f, seed, CR, F, strategy):

            """Evolutionary Strategies

            Parameters:
                ps: population size
                g_max : max number of generations
                eval_f : evaluation function
                seed: Random seed for population initialization
                CR: Determines which components in the trial vector come from either the target or the mutant. (between 0 and 1)
                F: proportion of difference between two mutant parents (normally between 0 and 1)
                strategy: string "k+l" or "k,l"

            Returns:
                x_final : final state array
                generation_list : list of historical states

            """
            
            print("Running the evolutionary strategies algorithm...")

            # region initialization

            # final populations for each generation (used for visualization)
            generation_list = []
            g = 0
            initial_population = self.generate_init_pop(seed, ps)

            # endregion
            pop = initial_population

            while (g<g_max):
                if F=="random":
                    F = np.random.uniform(0.5, 1.0)
                for target in pop:
                    mutant = self.generateMutantVector(pop, target, F, strategy, eval_f)
                    trial = self.generateTrialVector(target, mutant, CR, np.random.randint(0, 2))
                    if eval_f(trial) <= eval_f(target):
                        idx = pop.index(target)
                        pop[idx]=trial
                generation_list.append(list(pop))
                g+=1
            return generation_list