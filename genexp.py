

# lax_coord = [(33.9425, -118.408056), (90.25, 98.36)]
# lst =[]
# lst1=[]
#
# for latlong, _ in lax_coord:    #gets first value only
#     lst.append(latlong)
# for _, latlong in lax_coord:    #gets second value only
#     lst1.append(latlong)
# print(lst)
# print(lst1)




# traveller_id = [('usa', '31256'), ('nms', '98765')]
#
# for passport in sorted(traveller_id):
#     print('%s/%s' % passport)
#
# for country, _ in traveller_id:
#     print(country)


# lax_coord = (33.94, -118.23)
# lat, long = lax_coord
# print(lat)
# print(long)


# t = (20, 8)
# quotient, remainder = (divmod(*t))
# print(quotient)


#underscore is used for dummy variable
# import os
# _, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
# print(filename)



# metro_areas = [
#     ('Tokyo', 'JP', 36.933, (35.689722, -139.691667)),
#     ('Delhi NCR', 'IN', 21.935, (28.613889, -77.208889)),
#      ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
#        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
#          ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),]
#
#
# print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
# fmt = '{:15} | {:9.4f} | {:9.4f}'
# for name, cc, pop, (lat, long) in metro_areas:
#     if long <= 0:
#         print(fmt.format(name, lat, long))


# from collections import namedtuple
# City = namedtuple('City', 'name country population coordinates')
# tokyo = City('Tokyo', 'JP', 369988789, (35.86, 98.65))
# print(tokyo)
#
# print(tokyo[1])


# board = [['_'] * 3 for i in range(3)]
# print(board)
# board[2][1] = 'U'
# print(board)

# import bisect
# def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
#     i=bisect.bisect(breakpoints, score)
#     return grades[i]
#
# print[grade(score) for score in [33,25,90,80,70]]
