import pickle
import numpy as np

#load the model from disk
filename = 'finalized_model.sav'

a = [-0.90068117,  1.03205722, -1.3412724, -1.31297673]
b = [-1.02184904,  0.80065426, -1.2844067, -1.31297673]
c = [0.068661, -0.12495, 0.7627, 0.7905907]

loaded_model = pickle.load(open(filename, 'rb'))
result_a = loaded_model.predict(np.reshape(a, [1, 4]))
result_b = loaded_model.predict(np.reshape(b, [1, 4]))
result_c = loaded_model.predict(np.reshape(c, [1, 4]))

print(result_a, "hello result")
print(result_b, "hello result")
print(result_c, "hello result")
