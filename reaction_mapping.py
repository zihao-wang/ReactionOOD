from rxnmapper import BatchedMapper
import pandas as pd

if __name__ == "__main__":
    rxn_mapper = BatchedMapper(batch_size=32)
    df = pd.read_csv('data/rmg/family.csv')

    df['mapped_smiles'] = df['smiles'].apply(lambda x: list(rxn_mapper.map_reactions([x]))[0])
    df.to_csv('data/rmg/family_mapped.csv', index=False)