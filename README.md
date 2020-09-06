# MoleculeNet & Chemprop Benchmark Dataset and Split Induces

This code repo is focused on the data splitting of the benchmarked dataset in the previous study of MelculeNet. Besides, in order to test the robustness of a model, I created a random 5fold cross validation induces and 5fold cluster split incudes for some of the dataset (ESOL, Lipop, Malaria, PDBbind-full, HIV, BACP, BBBP), I suggest the model performance should also be tested on these splits. 


### 1. Backgroud
To date, many researchers have developed different molecule deep learning models, However, I found these paper use different random seed to split their dataset in the "Random Split" option, besides, the different scaffold splitting methods are also used.
In order to provide easy-to-use and not confusing data split results, here I provide the indexes of the training set, validation set, and test set corresponding to the benchmark dataset. 

The basis of the split is from the literature： [Wu et al's work](https://pubs.rsc.org/en/content/articlelanding/2018/sc/c7sc02664a#!divAbstract) except for the ChEMBL dataset

Note that the ChEMBL dataset is originally from [Mayr et al's work](https://pubs.rsc.org/en/Content/ArticleLanding/2018/SC/c8sc00148k#!divAbstract), the processed data from [Yang et al's work]( https://pubs-acs-org.libproxy1.nus.edu.sg/doi/pdf/10.1021/acs.jcim.9b00237). This dataset is split by the scaffold split method,
the induces of 0,1,2 is taken from their code repo [chemprop](https://github.com/swansonk14/chemprop/blob/master/splits.tar.gz)

I sincerely hope that all the later research will be able to split the data set based on these indexes, so that we can make a comparison to each other, otherwise misleading results may be caused by different data splitting results, for example in the paper of [Xiong et al's work](https://pubs.acs.org/doi/abs/10.1021/acs.jmedchem.9b00959), they used the different random seed to split their dataset in random split, details can be seen in their code repo: [AttentiveFP](https://github.com/OpenDrugAI/AttentiveFP/tree/master/code)

Lastly, We also have discussed this issue here: https://github.com/deepchem/deepchem/issues/1711

### 2. Benchmark DataSet in MolNet and Chemprop

These benchmark datasets and the split induces have benn generated in this repo, the following table is the summary of these datasets.

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>task_name</th>      <th>task_type</th>      <th>n_samples</th>      <th>n_task</th>      <th>split_method</th>      <th>n_cross_split</th>      <th>task_metrics</th>    </tr>    <tr>      <th>task_id</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>01</th>      <td>ESOL</td>      <td>regression</td>      <td>1128</td>      <td>1</td>      <td>random</td>      <td>3</td>      <td>RMSE</td>    </tr>    <tr>      <th>02</th>      <td>FreeSolv</td>      <td>regression</td>      <td>642</td>      <td>1</td>      <td>random</td>      <td>3</td>      <td>RMSE</td>    </tr>    <tr>      <th>03</th>      <td>Lipop</td>      <td>regression</td>      <td>4200</td>      <td>1</td>      <td>random</td>      <td>3</td>      <td>RMSE</td>    </tr>    <tr>      <th>04</th>      <td>PDBbind-full</td>      <td>regression</td>      <td>9880</td>      <td>1</td>      <td>time</td>      <td>1</td>      <td>RMSE</td>    </tr>    <tr>      <th>05</th>      <td>PDBbind-core</td>      <td>regression</td>      <td>168</td>      <td>1</td>      <td>time</td>      <td>1</td>      <td>RMSE</td>    </tr>    <tr>      <th>06</th>      <td>PDBbind-refined</td>      <td>regression</td>      <td>3040</td>      <td>1</td>      <td>time</td>      <td>1</td>      <td>RMSE</td>    </tr>    <tr>      <th>07</th>      <td>PCBA</td>      <td>classification</td>      <td>437929</td>      <td>128</td>      <td>random</td>      <td>3</td>      <td>PRC_AUC</td>    </tr>    <tr>      <th>08</th>      <td>MUV</td>      <td>classification</td>      <td>93087</td>      <td>17</td>      <td>random</td>      <td>3</td>      <td>PRC_AUC</td>    </tr>    <tr>      <th>09</th>      <td>HIV</td>      <td>classification</td>      <td>41127</td>      <td>1</td>      <td>scaffold</td>      <td>3</td>      <td>ROC_AUC</td>    </tr>    <tr>      <th>10</th>      <td>BACE</td>      <td>classification</td>      <td>1513</td>      <td>1</td>      <td>scaffold</td>      <td>3</td>      <td>ROC_AUC</td>    </tr>    <tr>      <th>11</th>      <td>BBBP</td>      <td>classification</td>      <td>2039</td>      <td>1</td>      <td>scaffold</td>      <td>3</td>      <td>ROC_AUC</td>    </tr>    <tr>      <th>12</th>      <td>Tox21</td>      <td>classification</td>      <td>7831</td>      <td>12</td>      <td>random</td>      <td>3</td>      <td>ROC_AUC</td>    </tr>    <tr>      <th>13</th>      <td>ToxCast</td>      <td>classification</td>      <td>8576</td>      <td>617</td>      <td>random</td>      <td>3</td>      <td>ROC_AUC</td>    </tr>    <tr>      <th>14</th>      <td>SIDER</td>      <td>classification</td>      <td>1427</td>      <td>27</td>      <td>random</td>      <td>3</td>      <td>ROC_AUC</td>    </tr>    <tr>      <th>15</th>      <td>ClinTox</td>      <td>classification</td>      <td>1478</td>      <td>2</td>      <td>random</td>      <td>3</td>      <td>ROC_AUC</td>    </tr>    <tr>      <th>16</th>      <td>ChEMBL</td>      <td>classification</td>      <td>456331</td>      <td>1310</td>      <td>scaffold</td>      <td>3</td>      <td>ROC_AUC</td>    </tr>  </tbody></table>

----

### Installation
```bash
git clone https://github.com/shenwanxiang/ChemBench.git
cd ChemBench
# add to PYTHONPATH
echo export PYTHONPATH="\$PYTHONPATH:`pwd`" >> ~/.bashrc
source ~/.bashrc
```

### Usage-1: Load the Dataset and  MoleculeNet's Split Induces  

```python
from chembench import load_data
df, induces = load_data('ESOL')

# get the 3 times random split induces
train_idx, valid_idx, test_idx = induces[0]
train_idx, valid_idx, test_idx = induces[1]
train_idx, valid_idx, test_idx = induces[2]
```
----

### Usage-2: Load Dataset As Data Object 

```python
from chembench import dataset
data = dataset.load_ESOL()
data.x
data.y
data.description


## regression 
dataset.load_Lipop()
dataset.load_ESOL()
dataset.load_FreeSolv()
dataset.load_Malaria()
dataset.load_LMC()
dataset.load_PDBF()
dataset.load_PDBC()
dataset.load_PDBR()


### classification
dataset.load_BBBP()
dataset.load_BACE()
dataset.load_HIV()
dataset.load_MUV()
dataset.load_Tox21()
dataset.load_SIDER()
dataset.load_CYP450()
dataset.load_ToxCast()
dataset.load_ClinTox()
dataset.load_ChEMBL()
dataset.load_PCBA()

```

### Usage-3: Load Robustness Splits

the cluster split results is [here](https://github.com/shenwanxiang/ChemBench/tree/master/chembench/robustness/cluster_split/cluster_split_results), for example, load the cluster splits and random splits for dataset ESOL:
```python
from chembench import get_robustness_induces
induces1 = get_robustness_induces("ESOL", induces = "random_5fcv_5rpts")
induces2 = get_robustness_induces("ESOL", induces = "scaffold_5fcv_1rpts")
print(len(induces1))
print(len(induces2))
```

For example, the chemical space of compounds and labels distribution of the ESOL dataset using cluster split : 
![ESOL split chemical space](https://github.com/shenwanxiang/ChemBench/blob/master/chembench/robustness/cluster_split/cluster_split_results/ESOL/ESOL.png)

the Kolmogorov-Smirnov statistic on the distribution for the pairwise groups(clusters): 
![ESOL split distribution test](https://github.com/shenwanxiang/ChemBench/blob/master/chembench/robustness/cluster_split/cluster_split_results/ESOL/ESOL_stat_test.png)
