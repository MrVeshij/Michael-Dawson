import pickle, shelve

print('Pickle cucumber')
variety = ['Cucumbers', 'Tomatoes', 'cabbage']
shape = ['whole', 'cubes', 'straw']
brand = ['Glavproduct', 'Chumak', 'Bonduel']
f = open('pickles.dat', 'wb')
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print('unPickle lists')
f = open('pickles.dat', 'rb')
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

print(variety)
print(shape)
print(brand)
f.close()

print('\nPutting lists on the shelf')
s = shelve.open('pickle2.dat')
s['variety'] = ['cucumbers', 'tomatoes', 'cabbage']
s['shape'] = ['wholly', 'cubes', 'draw']
s['brand'] = ['Glavproduct', 'Chumak', 'Bonduel']

print('\nCheck module shelve')
print('brand marks = ', s['brand'])
print('shape = ', s['shape'])
print('variety produce = ', s['variety'])
s.close()
