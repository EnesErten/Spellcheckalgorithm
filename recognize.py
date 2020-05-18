result = []
datas=["one","two"]

# global variable it can be use is in functions

# this functions assign result to all permutation of data
# it is work by recursively
# it is used swap operation
def permute(data, i, len):
    if i == len:
        # base case
        result.append(''.join(data))

    else:
        # swap operation
        for j in range(i, len):
            data[i], data[j] = data[j], data[i]

            permute(data, i + 1, len)

            data[i], data[j] = data[j], data[i]


# this function is returning the combinations of string
def combination(data, combination_list=[""]):
    if length(data) == 0:
        return combination_list

    head, tail = data[0], data[1:]
    combination_list = combination_list + list(map(lambda x: x + head, combination_list))
    return combination(tail, combination_list)


def length(data):
    count = 0

    for i in list(data):
        count += 1

    return count


def compare_count(string, string1):
    count = 0
    count_1 = 0

    for i in string:

        if i == string1[count_1]:
            count += 1

        count_1 += 1

    return count

result_1=0
a="tw"
result_1=combination(a)
permute(list(a),0,length(a))
n_result=result_1+result
c=0
c_st=""
s=0

for j in n_result:
    for k in datas:
        if c<compare_count(j,k):
             c=compare_count(j,k)
             c_st=k


print(c_st)
