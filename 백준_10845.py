'''
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
class Queue:
    def __init__(self):#초기화
        self.item = []
    
    def enqueue(self, a):#삽입
        self.item.append(a)

    def dequeue(self):#삭제
        if len(self.item) < 1:
            print("error")
            return
        data = self.item[0]
        del self.item[0]
        return data
    
    def is_empty(self):#큐 상태
        if len(self.item) > 0:
            return 0
        else:
            return 1

    def front(self):
        if self.is_empty == 1:
            return -1
        else:
            return self.item[0]
    
    def back(self):
        if self.is_empty == 1:
            return -1
        else:
            return self.item[-1]


test = Queue()
line = input()

for i in range(int(line)):
    req = input().split(' ')

    if req[0] == "push":
        test.enqueue(req[1])
    elif req[0] == "pop":
        print(test.dequeue())
    elif req[0] == "size":
        print(test.item.index)
    elif req[0] == "empty":
        print(test.is_empty())
    elif req[0] == "front":
        print(test.front)
    elif req[0] == "back":
        print(test.back)