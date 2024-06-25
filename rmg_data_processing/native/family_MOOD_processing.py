from collections import defaultdict
import pickle
from dataclasses import dataclass
from typing import List
import numpy as np
import pandas as pd
from rmgpy.data.kinetics import KineticsDatabase
from rmgpy.kinetics import (Arrhenius, ArrheniusBM, ArrheniusEP, Chebyshev,
                            KineticsData, Lindemann, MultiArrhenius,
                            MultiPDepArrhenius, PDepArrhenius,
                            StickingCoefficient, StickingCoefficientBEP,
                            SurfaceArrhenius, SurfaceArrheniusBEP, ThirdBody,
                            Troe)
from rmgpy.kinetics.model import KineticsModel
from rmgpy.reaction import Reaction

@dataclass
class Reaction:
    family_name: str
    depo_label: str
    indepo_index: int
    reaction: Reaction
    kinetics_property: KineticsModel
    rank: int
    
print("loading family_reaction_list from the pickle file ...")
with open("family_reactions.pickle", 'rb') as f:
    family_reaction_list = pickle.load(f)
print(f"{len(family_reaction_list)} reactions are collected")
    
def input2reaction_smiles(sample: Reaction):
    reaction_smiles = ""
    smiles = []
    for sp in sample.reaction.reactants:
        smiles.append(sp.smiles) 
    reaction_smiles += ".".join(smiles)
    reaction_smiles += ">>"
    smiles = []
    for sp in sample.reaction.products:
        smiles.append(sp.smiles)
    reaction_smiles += ".".join(smiles)
    return reaction_smiles

def input2reaction_label(sample: Reaction):
    return sample.reaction.to_labeled_str()

def input2Arrenius_coefs(sample: Reaction):
    return {
        'A': sample.kinetics_property.A.value_si,
        'n': sample.kinetics_property.n.value_si,
        'Ea': sample.kinetics_property.Ea.value_si/1000
    }
    
data = defaultdict(list)

for sample_id, sample in enumerate(family_reaction_list):
    if not isinstance(sample.kinetics_property, Arrhenius):
        continue
    data['sample_id'].append(sample_id)
    data['smiles'].append(input2reaction_smiles(sample))
    data['label'].append(input2reaction_label(sample))
    data['domain_index'].append(sample.family_name)
    data['indepo_index'].append(sample.indepo_index)
    data['depository'].append(sample.depo_label)
    data['rank'].append(sample.rank)
    data['target'].append(input2Arrenius_coefs(sample)['Ea'])
    
family_MOOD_df = pd.DataFrame(data)
family_MOOD_df.to_csv("family_MOOD.csv", index=False)

reduced_subdfs = [
    subdf for smiles, subdf in family_MOOD_df.groupby('smiles') 
    if len(subdf) == 1
]

family_MOOD_df_reduced = pd.concat(reduced_subdfs)
family_MOOD_df_reduced.to_csv("family_MOOD_reduced.csv", index=False)