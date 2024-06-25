# For choice 1: generating temperature data / temperature and pressure data automatically
#               One should input the starting data, the ending data, and the number of data points
#
# For choice 2: generating temperature data / temperature and pressure data based on user defined
#               One should upload the csv file "T_data.csv" or "TP_data.csv" to the same path as this script
#               T_data.csv should have a column "temperature_list"
#               TP_data.csv should have two columns "temperature_list" and "pressure_list"
#               sample csv files are provided in `rmg_data_processing/native` directory


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
    
print("loading library_reaction_list from the pickle file ...")
with open("library_reactions.pickle", "rb") as f:
    library_reaction_list = pickle.load(f)
print(f"{len(library_reaction_list)} reactions are collected")

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

T_smiles_key_dict = defaultdict(list)
T_reaction_list = []

TP_smiles_key_dict = defaultdict(list)
TP_reaction_list = []

for sample in library_reaction_list:
    k = sample.kinetics_property
    smiles = input2reaction_smiles(sample)

    if k.is_pressure_dependent():
        TP_smiles_key_dict[smiles].append(sample)
        TP_reaction_list.append(sample)
    else:
        T_smiles_key_dict[smiles].append(sample)
        T_reaction_list.append(sample)
        
T_reaction_list_reduced = []
for smiles in T_smiles_key_dict:
    redundancy_counts = len(T_smiles_key_dict[smiles])
    if redundancy_counts == 1:
        T_reaction_list_reduced.extend(T_smiles_key_dict[smiles])
        
TP_reaction_list_reduced = []
for smiles in TP_smiles_key_dict:
    redundancy_counts = len(TP_smiles_key_dict[smiles])
    if redundancy_counts == 1:
        TP_reaction_list_reduced.extend(TP_smiles_key_dict[smiles])

# Temperature dependence
def T_dependent_data_generator(sample_list, temperature_list):
    data = defaultdict(list)
    reaction_count = 0
    for sample in sample_list:
        k = sample.kinetics_property

        for T in temperature_list:
            if not k.is_temperature_valid(T):
                continue

            try:
                rate = k.get_rate_coefficient(T)
                assert not np.isnan(np.log10(rate))
                data['library'].append(sample.family_name)
                data['label'].append(input2reaction_label(sample))
                data['smiles'].append(input2reaction_smiles(sample))
                data['domain_index'].append(T)
                data['target'].append(np.log10(rate))
            except:
                continue
            
        reaction_count += 1
    
    print(reaction_count)
    return data

while 1:
    print("1. generating temperature data automatically")
    print("2. generating temperature data based on user defined")
    print("3. exit")
    print("4. continue")
    n = input("1/2/3/4 : ")
    
    if n == "3":
        break

    if n == "4":
        continue

    if n == "1":
        start = input("start = ")
        stop = input("stop = ")
        num = input("num = ")
        temperature_list= np.linspace(float(start), float(stop), int(num)).tolist()

    elif n == "2":
        # Uploading a csv file "T_data.csv" is required
        temperature_data = pd.read_csv("T_data.csv")
        temperature_list = temperature_data["temperature_list"].tolist()

    # redundancy reduced
    data = T_dependent_data_generator(T_reaction_list_reduced, temperature_list)
    df = pd.DataFrame(data)
    print(len(df))
    df.to_csv(f"library_T_dependent_reduced_{len(df)/1000}.csv", index=False)
    
    # redundancy remained
    data = T_dependent_data_generator(T_reaction_list, temperature_list)
    df = pd.DataFrame(data)
    print(len(df))
    df.to_csv(f"library_T_dependent_{len(df)/1000}k.csv", index=False)
        
    
# Temperature and Pressure dependence
def TP_dependent_data_generator(sample_list, temperature_list, pressure_list):
    data = defaultdict(list)
    reaction_count = 0
    for sample in sample_list:
        k = sample.kinetics_property

        for T in temperature_list:
            for P in pressure_list:
                if not k.is_temperature_valid(T) or not k.is_pressure_valid(P):
                    continue

                try:
                    rate = k.get_rate_coefficient(T, P)
                    assert not np.isnan(np.log10(rate))
                    data['library'].append(sample.family_name)
                    data['label'].append(input2reaction_label(sample))
                    data['smiles'].append(input2reaction_smiles(sample))
                    data['domain_index'].append((T, P))
                    data['target'].append(np.log10(rate))
                except:
                    continue

        reaction_count += 1

    print(reaction_count)
    return data

while 1:
    print("1. generating temperature and pressure data automatically")
    print("2. generating temperature and pressure data based on user defined")
    print("3. exit")
    print("4. continue")
    n = input("1/2/3/4 : ")

    if n == "3":
        break

    if n=="4":
        continue

    if n == "1":
        T_start = input("T_start = ")
        T_stop = input("T_stop = ")
        T_num = input("T_num = ")
        P_start = input("P_start = ")
        P_stop = input("P_stop = ")
        P_num = input("P_num = ")
        temperature_list= np.linspace(float(T_start), float(T_stop), int(T_num)).tolist()
        pressure_list = np.logspace(np.log10(float(P_start)), np.log10(float(P_stop)), int(P_num)).tolist()
    
    elif n == "2":
        # Uploading a csv file "TP_data.csv" is required
        TP_data = pd.read_csv("TP_data.csv")
        temperature_list = TP_data["temperature_list"].tolist()
        pressure_list = TP_data["pressure_list"].tolist()
    
    # redundancy reduced
    data = TP_dependent_data_generator(TP_reaction_list_reduced, temperature_list, pressure_list)
    df = pd.DataFrame(data)
    print(len(df))
    df.to_csv(f"library_TP_dependent_reduced_{len(df)/1000}.csv", index=False)

    # redundancy remained
    data = TP_dependent_data_generator(TP_reaction_list, temperature_list, pressure_list)
    df = pd.DataFrame(data)
    print(len(df))
    df.to_csv(f"library_TP_dependent_{len(df)/1000}.csv", index=False)
