from numpy import base_repr
import time


scope = range(3)

tt = [[i, j] for i in scope for j in scope]


def bpi(matrix):
    return [[k, m] for k in matrix for m in matrix]


def check_pol(fun, mat):
    # print(mat)
    # print(bpi(mat))
    # print(fun.__name__)
    cases = len(bpi(mat))
    case = 0
    while case < cases:
        # print('cases', cases)
        # print('case', case)
        result = [
            fun(bpi(mat)[case][0][k], bpi(mat)[case][1][k])
            for k in range(len(mat[0]))
        ]
        if result in mat:
            # print(f'{result} still in matrix')
            case = case + 1
            if case == cases:
                return True

        else:
            # print(f'relation = {mat}')
            # print(f'{fun.__name__} is a counter-polimorphism of this relation: {bpi(mat)[case]} => {result}')
            case = cases
            return False


# fun_graph could perhaps be faster using zip(tt, ternary) or something like that


def fun_graph(nine_tuple):
    return [
        [0, 0, int(nine_tuple[0])],
        [0, 1, int(nine_tuple[1])],
        [0, 2, int(nine_tuple[2])],
        [1, 0, int(nine_tuple[3])],
        [1, 1, int(nine_tuple[4])],
        [1, 2, int(nine_tuple[5])],
        [2, 0, int(nine_tuple[6])],
        [2, 1, int(nine_tuple[7])],
        [2, 2, int(nine_tuple[8])],
    ]


def ternary(n):
    return base_repr(n, base=3).zfill(9)


def real_fun_k3(function_number):
    def make_fun(arg1, arg2):
        for i in tt:
            if [arg1, arg2] == i:
                return int(ternary(function_number)[tt.index(i)])

    return make_fun


def converse(ter_fun):
    return (
        ter_fun[0]
        + ter_fun[3]
        + ter_fun[6]
        + ter_fun[1]
        + ter_fun[4]
        + ter_fun[7]
        + ter_fun[2]
        + ter_fun[5]
        + ter_fun[8]
    )


# def conv(ter_fun):


def decimal_repr(ternary_num):
    dec_repr = 0
    for i in range(9):
        dec_repr = dec_repr + int(ternary_num[i]) * 3 ** (8 - i)

    return dec_repr


def dec_repr(ternary_num):
    return sum(
        [int(ternary_num[i]) * 3 ** (8 - i) for i in range(len(ternary_num))]
    )


def formated_ter_fun(ter_fun):
    print(ternary(ter_fun)[:3], ternary(ter_fun)[3:6], ternary(ter_fun)[6:])


fun_num = 9999

formated_ter_fun(fun_num)
print(real_fun_k3(fun_num)(0, 2))

print(fun_num)
print(ternary(fun_num))
print(converse(ternary(fun_num)))
print(decimal_repr(converse(ternary(fun_num))))
print(dec_repr(ternary(fun_num)))

print("=" * 90)

# print(dec_repr(ternary(fun_num)))
# for fun_num in range(8000, 8050):
#     print(fun_num)
#     print(ternary(fun_num))
#     print(converse(ternary(fun_num)))
#     print(decimal_repr(converse(ternary(fun_num))))
#     print("-" * 10)

t0 = time.time()

one_converse_only = []
for fun_num in range(3**9):
    if converse(ternary(fun_num)) not in one_converse_only:
        one_converse_only.append(ternary(fun_num))
        # print(converse(ternary(fun_num)))

with open("one_converse_only.txt", "w") as f:
    for i in one_converse_only:
        f.write(i + "\n")

projections = ["000111222", "012012012"]
core_func = [i for i in one_converse_only if i not in projections]

print(projections[0] in one_converse_only)
print(projections[0] in core_func)

centralizers = []
first_witness = []

with open("core_centralizers.txt", "w") as f:
    for i in range(len(core_func)):
        # print(i)
        commutators = []
        for j in range(len(core_func)):
            if check_pol(real_fun_k3(j), fun_graph(ternary(i))):
                commutators.append(j)
        if commutators not in centralizers:
            centralizers.append(commutators)
            print(i, ternary(i), "centralizers len is now", len(centralizers))

    for cent in centralizers:
        f.write(str(cent) + " wit: " + str(ternary(i)) + "\n")

t1 = time.time()
print(t1 - t0)
