In case you would like to cite this: 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4054866.svg)](https://doi.org/10.5281/zenodo.4054866)

## 1. MolMapNet Dataset

* the following datasets are reported in the paper of <code> <i>"Out-of-the-Box Deep Learning Prediction of Pharmaceutical Properties by Broadly Learned Knowledge-Based Molecular Representations"</i> </code>, please find details of these datasets in this paper

<table>
<thead>
  <tr>
    <th>Data Class</th>
    <th>Dataset</th>
    <th>No. of Molecules</th>
    <th>No. of Tasks</th>
    <th>Task Metric</th>
    <th>Task Type</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="3">Physico-chemical</td>
    <td>ESOL Water solubility</td>
    <td>1128</td>
    <td>1</td>
    <td>RMSE</td>
    <td>Regression</td>
  </tr>
  <tr>
    <td>FreeSolv Solvation free energy</td>
    <td>642</td>
    <td>1</td>
    <td>RMSE</td>
    <td>Regression</td>
  </tr>
  <tr>
    <td>Lipop Lipophilicity</td>
    <td>4200</td>
    <td>1</td>
    <td>RMSE</td>
    <td>Regression</td>
  </tr>
  <tr>
    <td>Molecular binding</td>
    <td>PDBbind-F, PDBbind-C, PDBbind-R Ligand-protein binding: full, core, refined (3 datasets)</td>
    <td>9880, 168, 3040</td>
    <td>1 for each</td>
    <td>RMSE</td>
    <td>Regression</td>
  </tr>
  <tr>
    <td rowspan="7">Bio-activity</td>
    <td>PCBA PubChem HTS bioAssay</td>
    <td>437929</td>
    <td>128</td>
    <td>PRC-AUC</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>MUV PubChem bioAssay</td>
    <td>93087</td>
    <td>17</td>
    <td>PRC-AUC</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>ChEMBL bioassay activity dataset</td>
    <td>456331</td>
    <td>1310</td>
    <td>ROC_AUC</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>Cancer cell-line IC50 A2780, CCRF-CEM12, DU-14512, HCT-1512, KB12, LoVo12, PC-312, SK-OV-312 (8 datasets)</td>
    <td>2255, 3047, 2512,994, 2731, 1120, 4294, 1589</td>
    <td>1 for each</td>
    <td>R2</td>
    <td>Regression</td>
  </tr>
  <tr>
    <td>Malaria Anti-malarial EC508</td>
    <td>9998</td>
    <td>1</td>
    <td>RMSE</td>
    <td>Regression</td>
  </tr>
  <tr>
    <td>BACE-1 benchmark set, ChEMBL novel set, ChEMBL common set, Clinical drugs</td>
    <td>1513, 395, 5324, 26</td>
    <td>1</td>
    <td>ROC_AUC</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>HIV replication inhibition</td>
    <td>41127</td>
    <td>1</td>
    <td>ROC_AUC</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td rowspan="3">Toxicity</td>
    <td>Tox21Toxicology in the 21st century</td>
    <td>7831</td>
    <td>12</td>
    <td>ROC_AUC</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>SIDER Adverse drug reactions of marketed drugs</td>
    <td>1427</td>
    <td>27</td>
    <td>ROC_AUC</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>ClinTox Clinical trial toxicity</td>
    <td>1478</td>
    <td>2</td>
    <td>ROC_AUC</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td rowspan="3">Pharmacokinetic</td>
    <td>CYP PubChem BioAssay CYP 1A2, 2C9, 2C19, 2D6, 3A4 inhibition</td>
    <td>16896</td>
    <td>5</td>
    <td>ROC_AUC</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>LMC-H, LMC-R, LMC-M (Liver Mocrosomal Clearance in human, rat, mouse)</td>
    <td>8755</td>
    <td>3</td>
    <td>R2</td>
    <td>Regression</td>
  </tr>
  <tr>
    <td>BBBP Blood-brain barrier penetration</td>
    <td>2039</td>
    <td>1</td>
    <td>ROC_AUC</td>
    <td>Classification</td>
  </tr>
</tbody>
</table>

### 2. Benchmark DataSet in MolNet and Chemprop

These benchmark datasets and the split induces have benn generated in this repo, the following table is the summary of these datasets.

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>task_name</th>      <th>task_type</th>      <th>n_samples</th>      <th>n_task</th>      <th>split_method</th>      <th>n_cross_split</th>      <th>task_metrics</th>    </tr>    <tr>      <th>task_id</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>01</th>      <td>ESOL</td>      <td>regression</td>      <td>1128</td>      <td>1</td>      <td>random</td>      <td>3</td>      <td>RMSE</td>    </tr>    <tr>      <th>02</th>      <td>FreeSolv</td>      <td>regression</td>      <td>642</td>      <td>1</td>      <td>random</td>      <td>3</td>      <td>RMSE</td>    </tr>    <tr>      <th>03</th>      <td>Lipop</td>      <td>regression</td>      <td>4200</td>      <td>1</td>      <td>random</td>      <td>3</td>      <td>RMSE</td>    </tr>    <tr>      <th>04</th>      <td>PDBbind-full</td>      <td>regression</td>      <td>9880</td>      <td>1</td>      <td>time</td>      <td>1</td>      <td>RMSE</td>    </tr>    <tr>      <th>05</th>      <td>PDBbind-core</td>      <td>regression</td>      <td>168</td>      <td>1</td>      <td>time</td>      <td>1</td>      <td>RMSE</td>    </tr>    <tr>      <th>06</th>      <td>PDBbind-refined</td>      <td>regression</td>      <td>3040</td>      <td>1</td>      <td>time</td>      <td>1</td>      <td>RMSE</td>    </tr>    <tr>      <th>07</th>      <td>PCBA</td>      <td>classification</td>      <td>437929</td>      <td>128</td>      <td>random</td>      <td>3</td>      <td>PRC_AUC</td>    </tr>    <tr>      <th>08</th>      <td>MUV</td>      <td>classification</td>      <td>93087</td>      <td>17</td>      <td>random</td>      <td>3</td>      <td>PRC_AUC</td>    </tr>    <tr>      <th>09</th>      <td>HIV</td>      <td>classification</td>      <td>41127</td>      <td>1</td>      <td>scaffold</td>      <td>3</td>      <td>ROC_AUC</td>    </tr>    <tr>      <th>10</th>      <td>BACE</td>      <td>classification</td>      <td>1513</td>      <td>1</td>      <td>scaffold</td>      <td>3</td>      <td>ROC_AUC</td>    </tr>    <tr>      <th>11</th>      <td>BBBP</td>      <td>classification</td>      <td>2039</td>      <td>1</td>      <td>scaffold</td>      <td>3</td>      <td>ROC_AUC</td>    </tr>    <tr>      <th>12</th>      <td>Tox21</td>      <td>classification</td>      <td>7831</td>      <td>12</td>      <td>random</td>      <td>3</td>      <td>ROC_AUC</td>    </tr>    <tr>      <th>13</th>      <td>ToxCast</td>      <td>classification</td>      <td>8576</td>      <td>617</td>      <td>random</td>      <td>3</td>      <td>ROC_AUC</td>    </tr>    <tr>      <th>14</th>      <td>SIDER</td>      <td>classification</td>      <td>1427</td>      <td>27</td>      <td>random</td>      <td>3</td>      <td>ROC_AUC</td>    </tr>    <tr>      <th>15</th>      <td>ClinTox</td>      <td>classification</td>      <td>1478</td>      <td>2</td>      <td>random</td>      <td>3</td>      <td>ROC_AUC</td>    </tr>    <tr>      <th>16</th>      <td>ChEMBL</td>      <td>classification</td>      <td>456331</td>      <td>1310</td>      <td>scaffold</td>      <td>3</td>      <td>ROC_AUC</td>    </tr>  </tbody></table>

----

### Installation

Direct installation:

```bash
pip install git+https://github.com/shenwanxiang/ChemBench.git
```

Developer installation:

```bash
git clone https://github.com/shenwanxiang/ChemBench.git
cd ChemBench
pip install -e .
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
----

### Usage-3: Load Cluster Splits

the cluster split results is [here](https://github.com/shenwanxiang/ChemBench/tree/master/chembench/cluster/cluster_split/cluster_split_results), for example, load the cluster splits and random splits for dataset ESOL:
```python
from chembench import get_cluster_induces
induces1 = get_cluster_induces("ESOL", induces = "random_5fcv_5rpts")
induces2 = get_cluster_induces("ESOL", induces = "scaffold_5fcv_1rpts")
print(len(induces1))
print(len(induces2))
```

For example, the chemical space of the ESOL dataset using 5fold cluster split : 
![ESOL split chemical space](https://github.com/shenwanxiang/ChemBench/blob/master/chembench/cluster/cluster_split/cluster_split_results/ESOL/ESOL.png)

the Kolmogorov-Smirnov statistic on the distribution for the pairwise groups(clusters): 
![ESOL split distribution test](https://github.com/shenwanxiang/ChemBench/blob/master/chembench/cluster/cluster_split/cluster_split_results/ESOL/ESOL_stat_test.png)
