import numpy as np
from differential_evolution import Differential_Evolution
import matplotlib.pyplot as plt
import math
import random
import csv
from queue import Queue
import pandas as pd

class EGGHOLDER:

    def __init__(self, is_debug):
        self.is_debug = is_debug
    
    def eval_func(self, individual):
        """
        Evaluates the current state by
        calculating the function result.
        """
        # print(individual)

        x1 = individual[0]
        x2 = individual[1]
        f = -(x2+47)*math.sin(math.sqrt(abs(x2 + x1/2 +47))) -x1*math.sin(math.sqrt(abs(x1-(x2+47))))
        return f
    
    def solve_eggholder(self):
        """
        Calls the DE for the eggholder function problem and plots the results.
        """

        data = []

        # sensitivity_analysis, one_trial
        mode = "one_trial"

        if mode == "sensitivity_analysis":

            
            headers = ['gmax', 'ps', 'CR', 'F', 776, 1, 234, 9238, 123556]
            seeds = [776, 1, 234, 9238, 123556]

            DE = Differential_Evolution()
            ps_list= [10, 20, 30, 60, 80, 100]
            g_max_list=[5, 20, 50, 100, 200, 500]
            CR_list = [0.2, 0.4, 0.5, 0.6, 0.8, 0.9]
            F_list = [0.1, 0.2, 0.4, 0.6, 0.7, 0.9]

            data = []

            for g_max in g_max_list:
                for ps in ps_list:
                    for CR in CR_list:
                        for F in F_list:
                
                            best_per_seed = []
                            for seed in seeds:
                                generation_list = DE.de(ps=ps, g_max=g_max, eval_f=self.eval_func, seed=seed, CR=CR, F=F, strategy="bin")

                                generation_eval_list = [[self.eval_func(individual) for individual in generation] for generation in generation_list]
                                gen_eval_list_np = np.array(generation_eval_list)
                                # print(generation_eval_list)

                                # list of mins of each generation
                                gen_mins = np.min(gen_eval_list_np, 1)
                                # print(gen_mins)
                                plt.plot(range(g_max), gen_mins, label=str(seed))

                                # best solution
                                best = np.min(gen_mins)
                                print("Best solution: ", best)
                                best_per_seed.append(best)

                            tmp = [g_max, ps, CR, F]
                            tmp.extend(best_per_seed)
                            data.append(tmp)
            df= pd.DataFrame(data=data,
                        columns= list(map(str, headers)))
            print(df)
            df.to_excel("../de_5_seeds.xlsx")
        
        if mode == "one_trial":

            
            headers = ['gmax', 'ps', 'CR', 'F', 776, 1, 234, 9238, 123556]
            seeds = [776, 1, 234, 9238, 123556]

            DE = Differential_Evolution()
            ps_list= [100]
            g_max_list=[150]
            # CR_list = [0.2, 0.4, 0.5, 0.6, 0.8, 0.9]
            CR_list = [0.9]
            # F_list = [0.1, 0.2, 0.4, 0.6, 0.7, 0.9]
            # F_list = [0.4]
            F_list = ["random"]

            data = []

            for g_max in g_max_list:
                plt.title('g_max={:}'.format(g_max))
                plt.axes(xlabel="generations", ylabel="best individual score")
                for ps in ps_list:
                    for CR in CR_list:
                        for F in F_list:
                
                            best_per_seed = []
                            for seed in seeds:
                                generation_list = DE.de(ps=ps, g_max=g_max, eval_f=self.eval_func, seed=seed, CR=CR, F=F, strategy="bin")

                                generation_eval_list = [[self.eval_func(individual) for individual in generation] for generation in generation_list]
                                gen_eval_list_np = np.array(generation_eval_list)
                                # print(generation_eval_list)

                                # list of mins of each generation
                                gen_mins = np.min(gen_eval_list_np, 1)
                                # print(gen_mins)
                                plt.plot(range(g_max), gen_mins, label=str(seed))

                                # best solution
                                best = np.min(gen_mins)
                                print("Best solution: ", best)
                                best_per_seed.append(best)

                            tmp = [g_max, ps, CR, F]
                            tmp.extend(best_per_seed)
                            data.append(tmp)
            df= pd.DataFrame(data=data,
                            columns= list(map(str, headers)))
            print(df)
            df.to_excel("../de_bin_pop100_gen150_CR09_RandomF_5_seeds.xlsx")
            plt.legend()
            plt.show()


if __name__ == "__main__":
    EGGHOLDER = EGGHOLDER(is_debug=False)
    
    # -959.6407
    print("Global optimum is: ", EGGHOLDER.eval_func([512, 404.2319]))

    EGGHOLDER.solve_eggholder()