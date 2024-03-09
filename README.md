# Reaction OOD


The conda environment can be prepared by using `environment.yaml`.


## data processing

### Dataset from RMG-database

#### RMG Docker Setting

1. Download the docker image.
```
docker pull reactionmechanismgenerator/rmg:3.2.0
```
2. Run the container.
```
docker run --name rmgcontainer -v "./rmg_data_processing:/rmg/RMG-Py/myrmgfiles" -p 8888:8888 -it reactionmechanismgenerator/rmg:3.2.0
```
3. Start the data processing notebook.
```
jupyter lab --ip 0.0.0.0 --no-browser --allow-root
```

And to resume the container, run
```
docker start rmgcontainer --attach --interactive
```

#### Extract RMG reaction record

There are two set of workarounds to build the RMG data from the dataset.

1. (Depreciated!!) The first one, see `rmg_data_processing/legancy/dataset_processing.ipynb`, parse the database files in RMG-database by python scripts. The file produced in this way is associated to the first version of the reaction OOD paper.
    - The disadvantage of the adhoc python parsers is that they sometimes result in errors because of some tailing spaces of the database file. To solve this parsing issue, one should modify the database files themselves, which is not recommended.
    - One could still reproduce the results by loading our pickle intermediate files `{reaction/molecules}_smiles_{families/libraries}.pickle`. Using the nodebook could produces a few csv files.
        - `family.csv`
        - `library_T_dependent_90k.csv`
        - `library_TP_dependent_120k.csv`

2. (Recommended!!) The second one, see `rmg_data_processing/native`, use RMG-Py database to load the database files. Therefore, this way of parsing data is expected to support future versions of RMG-database.

One could populate the dataset "RMG-Family MOOD" and "RMG-Library COOD" with jupyer notebook `rmg_data_processsing/native/family_MOOD_processing.ipynb` and `rmg_data_processsing/native/library_COOD_processing.ipynb`

#### Generate the prediction input and output for the reaction OOD dataset.

The input and output of the prediction can be then generated and modified in the notebook
```dataset_processing.ipynb```

#### AAM mapping

We handle RMG data into csvs within `data/rmg` folder

We should first map the atoms in the reaction data following the practice of chemprop

```
python3 reaction_mapping.py
```

### Dataset from chemprop.

## GOOD Benchmark

We add dataset loaders to `GOOD/data/good_datasets`. The processed dataset files can be accessed via `data/ReactionOOD`.
