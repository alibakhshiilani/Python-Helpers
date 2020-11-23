
def check_index_exsist(mylist, index):
    try:
        mylist[index]
        return True
    except IndexError:
        return False


def check_squence_exist(mylist, mysquence):
    status = False
    for i in range(len(mylist)):
        if mylist[i] == mysquence[0]:
            status = True
            tmpI = i
            for x in range(len(mysquence)):
                if not check_index_exsist(mylist, tmpI) or not mysquence[x] == mylist[tmpI]:
                    status = False
                if status :
                    return status    
                tmpI += 1
    return status

