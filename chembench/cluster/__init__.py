# load random split , cluster split induces
from chembench import dataset
import os
from glob import glob
import pandas as pd
import numpy as np
from tqdm import tqdm
tqdm.pandas(ascii=True)


curr_path = os.path.dirname(__file__)



def get_clsuter_induces(task_name = 'ESOL', induces = "scaffold_5fcv_1rpts"):
    """
    task_name: {"ESOL", "Lipop", "Malaria", "BACE", "BBBP", "HIV", "PDBbind-full"} 
    induces: {"scaffold_5fcv_1rpts", "random_5fcv_5rpts"}
    """
    
    if induces == 'scaffold_5fcv_1rpts':
        f = os.path.join(curr_path, 'cluster_split', 'cluster_split_results', task_name, "cluster_split_%s.idx" % task_name)
        dfidx = pd.read_pickle(f)
        induces = []
        for i in dfidx.columns:
            rd1 = dfidx.groupby(i).apply(lambda x:x.index.tolist()).tolist()
            induces.append(rd1)

    else:
        f = os.path.join(curr_path, 'random_split', 
                         'rand_split_results', "rd_split_%s.csv" % task_name)
        dfidx = pd.read_csv(f, index_col = 0)
        induces = []
        for i in dfidx.columns:
            rd1 = dfidx.groupby(i).apply(lambda x:x.index.tolist()).tolist()
            induces.append(rd1)
        
    return induces



def load_random_5fcv_5rpts(task_name = 'ESOL'):
    

    
    return induces



    
    
