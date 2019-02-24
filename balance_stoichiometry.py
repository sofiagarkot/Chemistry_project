git remote add origin remote repository URLfrom chempy import balance_stoichiometry
try:
    reac, prod = balance_stoichiometry({'C6H5Br','C6H7NO'}, {'C12H11NO'})
except:
    # an error when there is not enough information about reaction
    reac, prod = balance_stoichiometry({'C6H5Br','C6H7NO'}, {'C12H11NO','HBr'})
reac1, prod1 = balance_stoichiometry({'NH4ClO4', 'Al'}, {'Al2O3', 'HCl', 'H2O', 'N2'})
from pprint import pprint
print("For elements C6H5Br and C6H7NO coeficients will be : ")
pprint(dict(reac))
pprint(dict(prod))
from chempy import mass_fractions
print("The mass fractions for these elements will be :")
for fractions in map(mass_fractions, [reac, prod]):
    pprint({k: '{0:.3g} wt%'.format(v * 100) for k, v in fractions.items()})
print("For elements NH4ClO4 and Al the coeficients will be : ")
pprint(dict(reac1))
pprint(dict(prod1))