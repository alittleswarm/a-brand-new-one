# 用所学的知识写一个斗地主随机发牌程序，将每个人的发牌以及多的三张牌的结果分别按照从大到小的顺序输出到player1.txt，player2.txt，player3.txt，others.txt四个文件中
import  random
class Card():
    def __init__(self, face, value):
        self._face=face
        self._value=value
    def __lt__(self, other):
        return self._value<other.value
    def __str__(self):
        ss=str(self._face)
        s=''
        if self._value<11 and self._value>1:
            s=ss+str(self._value)
        elif self._value ==11:
            s=ss+'J'
        elif self._value ==12:
            s=ss+'Q'
        elif self._value==13:
            s=ss+'K'
        elif self._value>=18:
            s=ss+'King'
        else :
            s=ss+'A'
        return s
    def __repr__(self):
        return self.__str__()
    @property
    def face(self):
        return self._face
    @property
    def value(self):
        return self._value
    @face.setter
    def face(self,face):
        self._face=face
    @value.setter
    def value(self,value):
        self._value=value
class Poker():
    def __init__(self):
        self._cards=[Card(face,value) for face in ['黑桃','梅花','方块','红桃']for value in range(2,15)]+[Card('小',20),Card('大',21)]
        self._now_pos=0
    @property
    def cards(self):
        return self._cards
    @property
    def now_pos(self):
        return self._now_pos
    def shuffle(self):
        random.shuffle(self._cards)
def main():
    poker=Poker()
    poker.shuffle()
    player1=[]
    player2=[]
    player3=[]
    list=[player1,player2,player3]
    cnt=0
    for x in range(1,18):
        for p in list:
            p.append(poker.cards[cnt])
            cnt+=1
    other=[poker.cards[52]]+[poker.cards[53]]
    x=1
    for p in list:
        p.sort(reverse=True)
        f=open(f"E:/player{x}.txt",'w',encoding="utf-8")# c盘进不去
        x+=1
        f.write(str(p))
        f.close()
    f=open(f"E:/other.txt",'w',encoding="utf-8")
    f.write(str(other))
    f.close()
if __name__ == '__main__':
    main()