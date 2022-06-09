set1 = set([10, 20, 30, 40])
set2 = set([30, 40, 50, 60])
set3 = set1.difference(set2)
print(set3)

set4 = set1.symmetric_difference(set2)
print(set4)

set1 = set([10, 20, 30, 40, 50, 60])
set2 = set([10, 20, 30, 40])

print(set2.issubset(set1))
print(set1.issuperset(set2))
