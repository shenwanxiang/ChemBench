import os
from glob import glob
import pandas as pd
import numpy as np
from tqdm import tqdm
tqdm.pandas(ascii=True)
import os



curr_path = os.path.dirname(__file__)


class data(object):
    
    def __init__(self, df, smiles_col, target_cols, task_name, task_type, description):
                
        assert type(target_cols) == list

        self.df = df
        self.x = df[smiles_col].values        
        self.y = df[target_cols].values.astype(float)
        self.y_cols = target_cols
        self.task_name = task_name
        self.task_type = task_type
        self.description = description
        self.n_samples = len(df)
        
        print('total samples: %s' % self.n_samples)
        

    def clear(self):
        
        self.df = None
        self.x = None
        self.y = None
        
        
################################ regression task  #####################################

def load_Lipop():
    
    description = """The Lipop (Lipophilicity) dataset has 4200 compounds and and their corresponding experimental lipophilicity values."""
    
    task_name = 'Lipop'
    task_type = 'regression'
    
    filename = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    
    df = pd.read_csv(filename, compression = 'gzip')
    target_cols = ['exp']
    smiles_col = 'smiles' 


    return data(df, smiles_col, target_cols, task_name, task_type, description)


def load_ESOL():
    
    description = """The ESOL dataset includes 1128 compounds and their experimental water solubility """
    
    task_name = 'ESOL'
    task_type = 'regression'
    filename = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    df = pd.read_csv(filename, compression = 'gzip')
    target_cols = ['measured log solubility in mols per litre']
    smiles_col = 'smiles'


    return data(df, smiles_col, target_cols, task_name, task_type, description)


def load_FreeSolv():
    
    description = """The FreeSolv dataset contains 642 small molecules' experimental hydration free energy in water """
    
    task_name = 'FreeSolv'
    task_type = 'regression'
    filename = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    df = pd.read_csv(filename, compression = 'gzip')
    target_cols = ['expt']
    smiles_col = 'smiles'
    return data(df, smiles_col,target_cols, task_name, task_type, description)        
    
    
def load_Malaria():
    
    description = """the Malaria dataset includes 9998 compounds that experimentally measured EC50 values of a sulfide-resistant strain of Plasmodium falciparum, which is the source of malaria"""
    
    task_name = 'Malaria'
    task_type = 'regression'
    
    filename = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    df = pd.read_csv(filename, compression = 'gzip')
    target_cols = ['activity']
    smiles_col = 'smiles'

    return data(df, smiles_col, target_cols, task_name, task_type, description)

def load_LMC():
    
    description = """the Clearance dataset includes 8755 compounds that are human, rat, mouse liver microsome clearance data(mL.min-1.g-1), ref: https://pubs.acs.org/doi/10.1021/acs.jcim.8b00785 """
    
    task_name = 'LMC'
    task_type = 'regression'
    
    
    filename = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    df = pd.read_csv(filename, compression = 'gzip')
    target_cols = [ 'hlm_clearance[mL.min-1.g-1]',  'rlm_clearance[mL.min-1.g-1]', 'mlm_clearance[mL.min-1.g-1]' ]
    smiles_col = 'Canonical_Smiles'

    return data(df, smiles_col, target_cols, task_name, task_type, description)




def load_PDBF():

    description = """PDBbind-F (full): this dataset contains 9880 compounds with their logKd/Ki binding affinity, this data set is split by time-split method in previous paper """
    
    task_name = 'PDBbind-full'
    task_type = 'regression'

    filename = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    df = pd.read_csv(filename, compression = 'gzip')
    target_cols = ['-logKd/Ki']
    smiles_col = 'smiles'

    return data(df, smiles_col, target_cols, task_name, task_type, description)


def load_PDBC():
    description = """PDBbind-C (core): this subset of PDB-binding database contains 168 compounds with their logKd/Ki binding affinity, it is compiled as high-quality data sets of protein-ligand complexes for docking/scoring studies. This data set is split by time-split method in previous paper"""
    task_name = 'PDBbind-core'
    task_type = 'regression'
    filename = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    df = pd.read_csv(filename, compression = 'gzip')
    target_cols = ['-logKd/Ki']
    smiles_col = 'smiles'
    return data(df, smiles_col, target_cols, task_name, task_type, description)


def load_PDBR():
    
    description = """PDBbind-R (refined): this dataset contains 3040 compounds with their logKd/Ki binding affinity, it contains protein-ligand structures at higher resolution and excludes any complexes with IC50 affinity data only. This data set is split by time-split method in previous paper"""
    task_name = 'PDBbind-refined'
    task_type = 'regression'

    filename = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    df = pd.read_csv(filename, compression = 'gzip')
    target_cols = ['-logKd/Ki']
    smiles_col = 'smiles'

    return data(df, smiles_col, target_cols, task_name, task_type, description)



################################ classification task #####################################

def load_ChEMBL():
    description = """ChEMBL: this dataset contains about 456331 compounds and more than 1310 assays. These assays correspond to a variety of target classes (e.g. enzymes, ion channels and receptors) and differ in size12. This dataset is split by scaffold-split method"""

    task_name = 'ChEMBL'
    task_type = 'classification'

    filename = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    df = pd.read_csv(filename, compression = 'gzip')
    target_cols = df.columns[1:].tolist()
    smiles_col = 'smiles'
    return data(df, smiles_col, target_cols, task_name, task_type, description)



def load_PCBA():
    description = """PCBA:  this dataset comes from PubChem Bioassay and contains 437929 compounds on 128 tasks that are related to biological activities,  This data set is split by random-split method in previous papers11"""
    task_name = 'PCBA'
    task_type = 'classification'

    filename = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    df = pd.read_csv(filename, compression = 'gzip')
    target_cols = df.columns[1:].tolist()
    smiles_col = 'smiles'
    return data(df, smiles_col, target_cols, task_name, task_type, description)



def load_BBBP():
    task_name = 'BBBP'
    task_type = 'classification'
    description = """The BBBP dataset contains 2039 compounds with their binary permeability properties of Blood-brain barrier"""

    filename = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    df = pd.read_csv(filename, compression = 'gzip')
    target_cols = ['p_np']
    smiles_col = 'smiles'
    
    return data(df, smiles_col, target_cols, task_name, task_type, description)



def load_BACE():
    task_name = 'BACE'
    task_type = 'classification'
    description = """The BACE dataset contains 1513 inhibitors with their binary inhibition labels for the target of BACE-1"""

    filename = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    df = pd.read_csv(filename, compression = 'gzip')
    df = df.rename(columns = {'mol': 'smiles'})
    target_cols = ['Class']
    smiles_col = 'smiles'
    

    return data(df, smiles_col, target_cols, task_name, task_type, description)


def load_HIV():
    task_name = 'HIV'
    task_type = 'classification'
    description = """The HIV dataset conatins 41127 compounds and their binnary ability to inhibit HIV replication."""

    filename = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    df = pd.read_csv(filename, compression = 'gzip')    
    target_cols = ['HIV_active']
    smiles_col = 'smiles'
    

    return data(df, smiles_col, target_cols, task_name, task_type, description)


def load_MUV():
    task_name = 'MUV'
    task_type = 'classification'
    description = """The MUV(Maximum Unbiased Validation) dataset contains 93087 compounds with 17 challenging tasks which is specifically designed for validation of virtual screening techniques."""

    filename = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    df = pd.read_csv(filename, compression = 'gzip')
    target_cols =   ['MUV-466',
                     'MUV-548',
                     'MUV-600',
                     'MUV-644',
                     'MUV-652',
                     'MUV-689',
                     'MUV-692',
                     'MUV-712',
                     'MUV-713',
                     'MUV-733',
                     'MUV-737',
                     'MUV-810',
                     'MUV-832',
                     'MUV-846',
                     'MUV-852',
                     'MUV-858',
                     'MUV-859']
    smiles_col = 'smiles'
    return data(df, smiles_col, target_cols, task_name, task_type, description)    



def load_Tox21():
    task_name = 'Tox21'
    task_type = 'classification'
    description = """The Tox21 dataset contains 7831 compounds and corresponding toxicity data against 12 targets."""

    filename = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    df = pd.read_csv(filename, compression = 'gzip')
    target_cols = ['NR-AR', 'NR-AR-LBD', 'NR-AhR', 'NR-Aromatase', 'NR-ER', 'NR-ER-LBD',
                    'NR-PPAR-gamma', 'SR-ARE', 'SR-ATAD5', 'SR-HSE', 'SR-MMP', 'SR-p53']
    smiles_col = 'smiles'
    return data(df, smiles_col, target_cols, task_name, task_type, description)




def load_SIDER():
    task_name = 'SIDER'
    task_type = 'classification'
    description = """The SIDER dataset contains 1427 marketed drugs and their adverse drug reactions (ADR) against 27 System-Organs Class."""

    
    filename = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    df = pd.read_csv(filename, compression = 'gzip')
    target_cols = df.columns[1:].tolist()
    smiles_col = 'smiles'
    return data(df, smiles_col, target_cols, task_name, task_type, description)



def load_CYP450():
    task_name = 'CYP450'
    task_type = 'classification'
    description = """The CYP450 dataset contains 16896 compounds against of five main CYP450 isozymes: 1A2, 2C9, 2C19, 2D6, and 3A4. This data should split training and test set by aids, ref: https://pubmed.ncbi.nlm.nih.gov/29775322/"""
    filename = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    df = pd.read_csv(filename, compression = 'gzip')
    target_cols = ['label_1a2', 'label_2c9', 'label_2c19', 'label_2d6', 'label_3a4']
    smiles_col = 'smiles'
    return data(df, smiles_col, target_cols, task_name, task_type, description)




def load_ToxCast():
    task_name = 'ToxCast'
    task_type = 'classification'
    description = """The ToxCast dataset contains 8576 compounds and corresponding binary toxicity levels over 600 experiments."""

    filename = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    df = pd.read_csv(filename, compression = 'gzip')
    target_cols = df.columns[1:].tolist()
    smiles_col = 'smiles'
    return data(df, smiles_col, target_cols, task_name, task_type, description)



def load_ClinTox():
    task_name = 'ClinTox'
    task_type = 'classification'
    description = """The ClinTox dataset contains 1478 drugs or compounds, the labels are FDA approval status and clinical traial toxicity results."""

    filename = os.path.join(curr_path, 'data_and_index', task_name, '%s.csv.gz' % task_name)
    df = pd.read_csv(filename, compression = 'gzip')
    target_cols = ['FDA_APPROVED','CT_TOX']
    smiles_col = 'smiles'
    return data(df, smiles_col, target_cols, task_name, task_type, description)
