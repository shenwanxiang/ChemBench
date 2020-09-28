import os
from glob import glob
import pandas as pd
import numpy as np
from tqdm import tqdm
tqdm.pandas(ascii=True)
import os

from .cluster import get_cluster_induces

curr_path = os.path.dirname(__file__)

def load_data(task_name):
    '''
    parameters
    -------------
        task_name: 'ESOL','FreeSolv','Lipop','PDBbind-full', 'PDBbind-core', 'PDBbind-refined','PCBA', 'MUV', 'HIV', 'BACE', 'BBBP', 'Tox21', 'ToxCast','SIDER', 'ClinTox', 'ChEMBL'

        
    return 
    --------
        dataframe table and the split induces
    '''
    file = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    assert os.path.exists(file), 'no such file: %s !' % file
    

    pkl_file_match = os.path.join(curr_path, 'data_and_index', task_name, '*.pkl')
    pklfiles = glob(pkl_file_match)
    assert len(pklfiles) != 0, 'No induces pkl files !'
    print( 'loading dataset: %s' % task_name, 'number of split times: %s' % (len(pklfiles)))

    induces = []
    for pklf in pklfiles:
        s = pd.read_pickle(pklf)
        induces.append(s.to_list())

    df = pd.read_csv(file, compression = 'gzip')
    
    
    return df, induces



