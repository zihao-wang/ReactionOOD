from chemprop.data.utils import get_data

data = get_data(
    path="data/rmg/family_mapped.csv",
    smiles_columns=["mapped_smiles"],
    skip_invalid_smiles=False,
    target_columns=["A_value_si", "Ea_value_si", "n_value_si"]
)

print(data)