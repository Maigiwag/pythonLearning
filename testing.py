import random, time, statistics


def getList(SIZE):
    '''
    return a sorted list of approximately size SIZE
    :param SIZE: int
    :return: list
    '''

    NUMBERS = []
    for i in range(2*SIZE):
        if random.randrange(2) == 1:
            NUMBERS.append(i)
    return NUMBERS


def getRandomList(SIZE):
    '''
    return a random list approximately size SIZE
    :param SIZE: int
    :return: list
    '''

    SORTED_LIST = getList(SIZE)
    RANDOM_LIST = []

    for i in range(len(SORTED_LIST)):
        RANDOM_LIST.append(SORTED_LIST.pop(random.randrange(len(SORTED_LIST))))

    return RANDOM_LIST

def getTime():
    '''
    returns the performance counter
    :return: float
    '''

    return time.perf_counter()


def getAverage(TIMES):
    '''
    returns the average of the given list
    :param TIMES: list(floats)
    :return: float
    '''

    return statistics.mean(TIMES)



class mergeSort():


    def sortlist(self, list):
        '''
        Reocursive split of the merge sort
        :param list: list [int]
        :return:
        '''

        if len(list) <= 1:
            #base case
            return list
        else:
            midpoint = len(list)//2
            left = list[:midpoint]
            right = list[midpoint:]
            return self.mergeSortedList(self.sortlist(left), self.sortlist(right))


    def mergeSortedList(self, leftList, rightList):
        '''
        Iterative merge of two sorted list
        :param leftList: list [int]
        :param rightList: list [int]
        :return: list[int]
        '''
        # special case one or both lists are empty
        if len(leftList) == 0:
            return rightList
        elif len(rightList) == 0:
            return leftList

        #general case
        indexLeft = 0
        indexRight = 0
        listMerged = [] # list to build and return
        listLenTotal = len(leftList) + len(rightList)
        while len(listMerged) < listLenTotal:
            if leftList[indexLeft] <= rightList[indexRight]:
                listMerged.append(leftList[indexLeft])
                indexLeft += 1
            else:
                listMerged.append(rightList[indexRight])
                indexRight += 1
            # test if we are at the end of one of the lists
            if indexRight == len(rightList):
                listMerged += leftList[indexLeft:]
            elif indexLeft == len(leftList):
                listMerged += rightList[indexRight:]

        return listMerged





if __name__ == '__main__':
    import random

    TIMES = []
    for i in range(30):
        NUMBERS = getList(10000)
        START = getTime()
        sort = mergeSort()
        sort.sortlist(NUMBERS)
        END = getTime()
        TIMES.append(END - START)
        print(END - START)
    print("the average is", getAverage(TIMES))
