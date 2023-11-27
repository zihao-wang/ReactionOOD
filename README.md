# Reaction OOD

## data processing

### RMG data

#### RMG Docker Setting

1. Download the docker image.
```
docker pull reactionmechanismgenerator/rmg:3.2.0
```
2. Run the container.
```
docker run --name rmgcontainer -v "./rmg_data_processing:/rmg/RMG-Py/myrmgfiles" -p 8888:8888 reactionmechanismgenerator/rmg:3.2.0
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

1. (Depreciated)The first one, see `rmg_data_processing/legancy`, parse the database file in RMG database by python scripts. The file produced in this way is associated to the first version of the reaction OOD paper.
2. (Recommended!!) The second one, see `rmg_data_processing/legancy`, use RMG-Py database to load the database files.

One could populate the dataset "RMG-Family MOOD" and "RMG-Library COOD" with jupyer notebook `rmg_data_processsing/native/family_MOOD_processing.ipynb` and `rmg_data_processsing/native/library_COOD_processing.ipynb`

#### Generate the prediction input and output for the reaction OOD dataset.

The input and output of the prediction can be then generated and modified in the notebook
```dataset_processing.ipynb```

#### Processed

We handle RMG data into csvs within `data/rmg` folder

We should first map the atoms in the reaction data following the practice of chemprop

```
python3 reaction_mapping.py
```

### GOOD Benchmark

We add dataset loaders to `GOOD/data/good_datasets`. The processed dataset files can be accessed via `TODO`.
