from rxnmapper import BatchedMapper
import pandas as pd

from chython import smiles

rxn_mapper = BatchedMapper(batch_size=32)

def map_smiles(s):
    raw_output = list(rxn_mapper.map_reactions([s]))[-1]

def map_smiles2(s):
    r = smiles(s)
    r.reset_mapping()
    return format(r, 'm')


if __name__ == "__main__":
    df = pd.read_csv('data/rmg/family.csv')
    mapped_smiles = []
    for i in range(len(df)):
        premapped_str = df.iloc[i]['smiles']
        mapped_str = map_smiles2(premapped_str)
        print(i, premapped_str, mapped_str)
        mapped_smiles.append(map_smiles2(premapped_str))

    df["mapped_smiles"] = mapped_smiles
    df.to_csv('data/rmg/family_mapped2.csv', index=False)