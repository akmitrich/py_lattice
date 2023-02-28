# This is a simple Python script.
def lattice(cells, basis, result, current, n):
    current.append(0.0)
    for i in range(cells[n]):
        current[n] = basis[n] * i
        if len(current) == len(basis):
            result.append(current.copy())
        else:
            lattice(cells, basis, result, current, n + 1)
    current.pop(-1)

if __name__ == '__main__':
    basis = [1, 1, 1, 1, 1, 1]
    cells = [10, 10, 10, 10, 10, 10]
    result = []
    lattice(cells, basis, result, [], 0)
    print(len(result))
    print(result)

