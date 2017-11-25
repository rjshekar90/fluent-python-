


lax_coord = [(33.9425, -118.408056), (90.25, 98.36)]
lst =[]
lst1=[]

for latlong, _ in lax_coord:    #gets first value only
    lst.append(latlong)
for _, latlong in lax_coord:    #gets second value only
    lst1.append(latlong)
print(lst)
print(lst1)



'''
traveller_id = [('usa', '31256'), ('bra', '98765')]

for passport in sorted(traveller_id):
    print('%s/%s' % passport)

for country, _ in traveller_id:
    print(country)  '''
