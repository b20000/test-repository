import pickle

data = (1.4,42)
output = open('data.pkl', 'w')
pickle.dump(data, output, protocol=2)
output.close()

f = open("data.pkl")
data = pickle.load(f)
print data