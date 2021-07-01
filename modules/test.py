
a = [{'hey': '1' },{ 'yo': '2'}]

b = [{'hey': '3' }, {'yo': '2'}, {'ko': '2'}, {'do': '2'}]

print(b[2:])



z = [d for d in a if d not in b]
print(z)