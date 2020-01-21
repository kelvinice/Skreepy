class Combination:

    # Program to print all combination
    # of size r in an array of size n

    # The main function that prints all
    # combinations of size r in arr[] of
    # size n. This function mainly uses
    # combinationUtil()
    def print_combination(self, arr, n, r):
        # A temporary array to store
        # all combination one by one
        data = [0] * r

        # Print all combination using
        # temprary array 'data[]'
        self.combination_util(arr, n, r, 0, data, 0)

    ''' arr[] ---> Input Array 
    n     ---> Size of input array 
    r     ---> Size of a combination to be printed 
    index ---> Current index in data[] 
    data[] ---> Temporary array to store 
                current combination 
    i     ---> index of current element in arr[]     '''

    def combination_util(self, arr, n, r, index, data, i):
        # Current cobination is ready,
        # print it
        if index == r:
            temp = []
            for j in range(r):
                temp.append(data[j])
            self.combinations.append(temp)
            return

        # When no more elements are
        # there to put in data[]
        if i >= n:
            return

        # current is included, put
        # next at next location
        data[index] = arr[i]
        self.combination_util(arr, n, r, index + 1,
                              data, i + 1)

        # current is excluded, replace it
        # with next (Note that i+1 is passed,
        # but index is not changed)
        self.combination_util(arr, n, r, index,
                              data, i + 1)

    def __init__(self, data_set):
        self.combinations = []
        n = len(data_set)

        for r in range(0, n):
            self.print_combination(data_set, n, r)
        self.combinations.append(data_set)

    def get_result(self):
        com = self.combinations.copy()
        self.combinations.clear()
        return com

    def get_result_reversed(self):
        com = self.combinations.copy()
        com.reverse()
        self.combinations.clear()
        return com
