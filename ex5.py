# Scrieți un program care va uni două dicționare date (d1 și d2) în cel de-al treilea (d3)?

d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for item in (d1, d2):
	d3 = d1.copy()
	d3.update(d2) 

print(d3)
