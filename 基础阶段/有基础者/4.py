class MyZoo():
    def __init__(self,dict:dict={}):
        self.animal=dict
        print("My Zoo!")
    def __str__(self):
        s=''
        for x in self.animal:
            s+=f"{x},{self.animal[x]}"
            s+='\n'
        return s
    def __eq__(self, other):
        flag = True
        for keys in self.animal:
            if keys in other.animal:
                pass
            else:
                flag=False
                break
        return flag
    def __len__(self):
        lenth = 0
        for keys in self.animal:
            lenth+=self.animal[keys]
        return lenth

