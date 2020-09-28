In case you want to cite this repo:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4016649.svg)](https://doi.org/10.5281/zenodo.4016649)

## 1. MolMapNet Dataset
<style type="text/css">
.tg  {border-collapse:collapse;border-color:#aaa;border-spacing:0;}
.tg td{background-color:#fff;border-color:#aaa;border-style:solid;border-width:1px;color:#333;
  font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{background-color:#f38630;border-color:#aaa;border-style:solid;border-width:1px;color:#fff;
  font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-6rx6{background-color:#FCFBE3;border-color:inherit;font-family:Arial, Helvetica, sans-serif !important;;text-align:left;
  vertical-align:top}
.tg .tg-zda1{border-color:inherit;font-family:Arial, Helvetica, sans-serif !important;;text-align:center;vertical-align:top}
.tg .tg-wgsn{border-color:inherit;font-family:Arial, Helvetica, sans-serif !important;;text-align:left;vertical-align:top}
.tg .tg-qho4{background-color:#FCFBE3;border-color:inherit;font-family:Arial, Helvetica, sans-serif !important;;text-align:center;
  vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-zda1">Data Class</th>
    <th class="tg-wgsn">Dataset</th>
    <th class="tg-wgsn">No. of Molecules</th>
    <th class="tg-wgsn">No. of Tasks</th>
    <th class="tg-wgsn">Task Metric</th>
    <th class="tg-wgsn">Task Type</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-qho4" rowspan="3">Physico-chemical</td>
    <td class="tg-6rx6">ESOL Water solubility</td>
    <td class="tg-6rx6">1128</td>
    <td class="tg-6rx6">1</td>
    <td class="tg-6rx6">RMSE</td>
    <td class="tg-6rx6">Regression</td>
  </tr>
  <tr>
    <td class="tg-wgsn">FreeSolv Solvation free energy</td>
    <td class="tg-wgsn">642</td>
    <td class="tg-wgsn">1</td>
    <td class="tg-wgsn">RMSE</td>
    <td class="tg-wgsn">Regression</td>
  </tr>
  <tr>
    <td class="tg-6rx6">Lipop Lipophilicity</td>
    <td class="tg-6rx6">4200</td>
    <td class="tg-6rx6">1</td>
    <td class="tg-6rx6">RMSE</td>
    <td class="tg-6rx6">Regression</td>
  </tr>
  <tr>
    <td class="tg-zda1">Molecular binding</td>
    <td class="tg-wgsn">PDBbind-F, PDBbind-C, PDBbind-R Ligand-protein binding: full, core, refined (3 datasets)</td>
    <td class="tg-wgsn">9880, 168, 3040</td>
    <td class="tg-wgsn">1 for each</td>
    <td class="tg-wgsn">RMSE</td>
    <td class="tg-wgsn">Regression</td>
  </tr>
  <tr>
    <td class="tg-qho4" rowspan="7">Bio-activity</td>
    <td class="tg-6rx6">PCBA PubChem HTS bioAssay</td>
    <td class="tg-6rx6">437929</td>
    <td class="tg-6rx6">128</td>
    <td class="tg-6rx6">PRC-AUC</td>
    <td class="tg-6rx6">Classification</td>
  </tr>
  <tr>
    <td class="tg-wgsn">MUV PubChem bioAssay</td>
    <td class="tg-wgsn">93087</td>
    <td class="tg-wgsn">17</td>
    <td class="tg-wgsn">PRC-AUC</td>
    <td class="tg-wgsn">Classification</td>
  </tr>
  <tr>
    <td class="tg-6rx6">ChEMBL bioassay activity dataset</td>
    <td class="tg-6rx6">456331</td>
    <td class="tg-6rx6">1310</td>
    <td class="tg-6rx6">ROC_AUC</td>
    <td class="tg-6rx6">Classification</td>
  </tr>
  <tr>
    <td class="tg-wgsn">Cancer cell-line IC50 A2780, CCRF-CEM12, DU-14512, HCT-1512, KB12, LoVo12, PC-312, SK-OV-312 (8 datasets)</td>
    <td class="tg-wgsn">2255, 3047, 2512,994, 2731, 1120, 4294, 1589</td>
    <td class="tg-wgsn">1 for each</td>
    <td class="tg-wgsn">R2</td>
    <td class="tg-wgsn">Regression</td>
  </tr>
  <tr>
    <td class="tg-6rx6">Malaria Anti-malarial EC508</td>
    <td class="tg-6rx6">9998</td>
    <td class="tg-6rx6">1</td>
    <td class="tg-6rx6">RMSE</td>
    <td class="tg-6rx6">Regression</td>
  </tr>
  <tr>
    <td class="tg-wgsn">BACE-1 benchmark set, ChEMBL novel set, ChEMBL common set, Clinical drugs</td>
    <td class="tg-wgsn">1513, 395, 5324, 26</td>
    <td class="tg-wgsn">1</td>
    <td class="tg-wgsn">ROC_AUC</td>
    <td class="tg-wgsn">Classification</td>
  </tr>
  <tr>
    <td class="tg-6rx6">HIV replication inhibition</td>
    <td class="tg-6rx6">41127</td>
    <td class="tg-6rx6">1</td>
    <td class="tg-6rx6">ROC_AUC</td>
    <td class="tg-6rx6">Classification</td>
  </tr>
  <tr>
    <td class="tg-zda1" rowspan="3">Toxicity</td>
    <td class="tg-wgsn">Tox21Toxicology in the 21st century</td>
    <td class="tg-wgsn">7831</td>
    <td class="tg-wgsn">12</td>
    <td class="tg-wgsn">ROC_AUC</td>
    <td class="tg-wgsn">Classification</td>
  </tr>
  <tr>
    <td class="tg-6rx6">SIDER Adverse drug reactions of marketed drugs</td>
    <td class="tg-6rx6">1427</td>
    <td class="tg-6rx6">27</td>
    <td class="tg-6rx6">ROC_AUC</td>
    <td class="tg-6rx6">Classification</td>
  </tr>
  <tr>
    <td class="tg-wgsn">ClinTox Clinical trial toxicity</td>
    <td class="tg-wgsn">1484</td>
    <td class="tg-wgsn">2</td>
    <td class="tg-wgsn">ROC_AUC</td>
    <td class="tg-wgsn">Classification</td>
  </tr>
  <tr>
    <td class="tg-qho4" rowspan="3">Pharmacokinetic</td>
    <td class="tg-6rx6">CYP PubChem BioAssay CYP 1A2, 2C9, 2C19, 2D6, 3A4 inhibition</td>
    <td class="tg-6rx6">16896</td>
    <td class="tg-6rx6">5</td>
    <td class="tg-6rx6">ROC_AUC</td>
    <td class="tg-6rx6">Classification</td>
  </tr>
  <tr>
    <td class="tg-wgsn">LMC-H, LMC-R, LMC-M (Liver Mocrosomal Clearance in human, rat, mouse)</td>
    <td class="tg-wgsn">8755</td>
    <td class="tg-wgsn">3</td>
    <td class="tg-wgsn">R2</td>
    <td class="tg-wgsn">Regression</td>
  </tr>
  <tr>
    <td class="tg-6rx6">BBBP Blood¨Cbrain barrier penetration</td>
    <td class="tg-6rx6">2050</td>
    <td class="tg-6rx6">1</td>
    <td class="tg-6rx6">ROC_AUC</td>
    <td class="tg-6rx6">Classification</td>
  </tr>
</tbody>
</table>

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
----

### Usage-3: Load Robustness Splits

the cluster split results is [here](https://github.com/shenwanxiang/ChemBench/tree/master/chembench/robustness/cluster_split/cluster_split_results), for example, load the cluster splits and random splits for dataset ESOL:
```python
from chembench import get_clsuter_induces
induces1 = get_clsuter_induces("ESOL", induces = "random_5fcv_5rpts")
induces2 = get_clsuter_induces("ESOL", induces = "scaffold_5fcv_1rpts")
print(len(induces1))
print(len(induces2))
```

For example, the chemical space of the ESOL dataset using 5fold cluster split : 
![ESOL split chemical space](https://github.com/shenwanxiang/ChemBench/blob/master/chembench/robustness/cluster_split/cluster_split_results/ESOL/ESOL.png)

the Kolmogorov-Smirnov statistic on the distribution for the pairwise groups(clusters): 
![ESOL split distribution test](https://github.com/shenwanxiang/ChemBench/blob/master/chembench/robustness/cluster_split/cluster_split_results/ESOL/ESOL_stat_test.png)
