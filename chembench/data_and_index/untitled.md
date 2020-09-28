This code repo is focused on the data splitting of the benchmarked dataset in the previous study of MelculeNet. Besides, in order to test the robustness of a model, I created a random 5fold cross validation induces and 5fold cluster split incudes for some of the dataset (ESOL, Lipop, Malaria, PDBbind-full, HIV, BACP, BBBP), I suggest the model performance should also be tested on these splits. 


### 1. Backgroud
To date, many researchers have developed different molecule deep learning models, However, I found these paper use different random seed to split their dataset in the "Random Split" option, besides, the different scaffold splitting methods are also used.
In order to provide easy-to-use and not confusing data split results, here I provide the indexes of the training set, validation set, and test set corresponding to the benchmark dataset. 

The basis of the split is from the literature： [Wu et al's work](https://pubs.rsc.org/en/content/articlelanding/2018/sc/c7sc02664a#!divAbstract) except for the ChEMBL dataset

Note that the ChEMBL dataset is originally from [Mayr et al's work](https://pubs.rsc.org/en/Content/ArticleLanding/2018/SC/c8sc00148k#!divAbstract), the processed data from [Yang et al's work]( https://pubs-acs-org.libproxy1.nus.edu.sg/doi/pdf/10.1021/acs.jcim.9b00237). This dataset is split by the scaffold split method,
the induces of 0,1,2 is taken from their code repo [chemprop](https://github.com/swansonk14/chemprop/blob/master/splits.tar.gz)

I sincerely hope that all the later research will be able to split the data set based on these indexes, so that we can make a comparison to each other, otherwise misleading results may be caused by different data splitting results, for example in the paper of [Xiong et al's work](https://pubs.acs.org/doi/abs/10.1021/acs.jmedchem.9b00959), they used the different random seed to split their dataset in random split, details can be seen in their code repo: [AttentiveFP](https://github.com/OpenDrugAI/AttentiveFP/tree/master/code)

Lastly, We also have discussed this issue here: https://github.com/deepchem/deepchem/issues/1711
