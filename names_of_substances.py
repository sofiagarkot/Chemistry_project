import pubchempy as pcp
c = pcp.Compound.from_cid(5090)
# getting name of substance by code
print (c.molecular_formula)
print (c.synonyms)