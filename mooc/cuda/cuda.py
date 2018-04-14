import numpy as np
from timeit import default_timer as timer
from numba import vectorize

@vectorize(["float32(int32)"], target="cuda")
def VectorRand(n):
	return np.random.randn(n)

# @vectorize(["float32(float32, float32)"], target="cuda")
def VectorAdd(a, b):
	return a + b

# @vectorize(["float32(float32, float32)"], target="cuda")
def Vectortime(a, b):
	return a * b

def main():
	N = 32000000

	A = np.ones(N, dtype=np.float32)
	B = np.ones(N, dtype=np.float32)
	C = np.zeros(N, dtype=np.float32)

	start = timer()
	A = VectorRand(N)
	# C = VectorAdd(A, B)
	# C = Vectortime(C, 4.0)
	end = timer() - start

	print("A[:5] = " + str(A[:5]))
	print("A[-5:] = " + str(A[-5:]))

	print("B[:5] = " + str(B[:5]))
	print("B[-5:] = " + str(B[-5:]))

	print("C[:5] = " + str(C[:5]))
	print("C[-5:] = " + str(C[-5:]))

	print("time took %f" % end)

if __name__ == '__main__':
	main()

