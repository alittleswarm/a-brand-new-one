from collections import OrderedDict
def cnt_num(list):
    return_dict={}
    for elm in list:
        snum=str(elm)
        for n in snum:
            if n in return_dict:
                return_dict[n]+=1
            else:
                return_dict[n]=1
    return_dict=OrderedDict(sorted(return_dict.items(),key=lambda x: x[0],reverse=False))
    return dict(return_dict)
def main():
    re = cnt_num([111, 22216662135, 21, 651, 6, 1654, 21654, 65198, 98412, 16, 8, 5, 2, 3363, 444, 5])
    print(re)
if __name__ == '__main__':
    main()
