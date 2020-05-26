result = []
datas = []


# global variable it can be use is in functions
# result will be the permute of a string
# data's keeps data's from file
# used list because of the mutability


# this functions assign result to all permutation of data
# it is work by recursively
# it is used swap operation
# returns None
# takes 3 argument first is string second
# is initial point 3 rd is length of string
def permute(data, i, len):
    if i == len:
        # base case
        result.append(''.join(data))
        # append the list

    else:
        # swap operation

        for j in range(i, len):
            # swap values
            data[i], data[j] = data[j], data[i]
            # recursively call
            permute(data, i + 1, len)
            # after recursively call
            data[i], data[j] = data[j], data[i]


# this function is returning the combinations of string
# it is a recursively functions
# takes 2 argument
# 1st is string 2nd is List initialized with ""
# returns the combination list
def combination(data, combination_list=[""]):
    if length(data) == 0:
        # base case
        return combination_list
        # return comblist
    head, tail = data[0], data[1:]
    # head tail head is keeping the firs element of the data
    # tail is keeping the rest of string
    combination_list = combination_list + list(map(lambda x: x + head, combination_list))
    # shuffling the words
    return combination(tail, combination_list)
    # recursively call


# this functions returns the length of the string

def length(data):
    # create a counter initialize to 0
    count = 0
    # for loop loops data times
    # make data to list
    for i in list(data):
        # count the elements of list(data)
        count += 1

    # return the count length of the string
    return count


# this functions comparing the strings and counting
# counting the common letters used collections library
# returns the common letters number

def compare_count(string, string1):
    # import library collections
    # use Counter functions
    from collections import Counter

    return sum((Counter(string) & Counter(string1)).values())
    # return the number of common letters


# main function

if __name__ == "__main__":
    result = []
    datas = []

    # assign ch ""
    ch = ""
    # open file common_words.dat 
    with open("common_words.dat", "r") as file:
        # loops 1000 times
        for i in range(1001):
            # read one line
            ch = file.readline()
            # take len-1
            ch = ch[:-1]
            # append to the list
            datas.append(ch)

    # take string from user
    word = input("Enter a word\n>>")
    # send to the function
    comb = combination(word)
    # send to the function
    permute(list(word), 0, length(word))
    # get all combinations
    all_comb = result
    # assign 0 and ""
    c = 0
    c_st = ""

    # for loop, loops datas
    for k in datas:
        # for loop, loops all_comb
        for j in all_comb:
            # if statement is true
            if c < compare_count(j, k):
                # update c value
                c = compare_count(j, k)
                # update c_st
                c_st = k

    # display the result
    print("Did you mean : ", c_st)