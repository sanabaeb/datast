# 큐 초기화 함수
def init_queue(size):
    global test_queue, front, rear
    test_queue = [None] * size
    front = -1
    rear = -1
    return print("큐가 초기화 되었습니다. 큐 크기는"+str(size)+"입니다.")

def is_queue_full():
    global rear
    if rear == len(test_queue) - 1:
        return True #print("큐가 가득 찼습니다.") 
    else:
        return False #print("큐가 가득 차지 않았습니다.")

def is_queue_empty():
    global front, rear
    if front == rear:
        return True #print("큐가 비어 있습니다.")
    else:
        return False #print("큐가 비어 있지 않습니다.")

def enqueue(data):
    global rear
    if is_queue_full():
        return print("큐가 가득 찼습니다.")
        return 
    rear += 1
    test_queue[rear] = data

def dequeue():
    global front
    front += 1
    return test_queue[front]
    test_queue[front] = None
    

def queue_print():
    print("=== 큐 상태 ===")
    for i in range(len(test_queue)):
        print(test_queue[i])
    print("==============")
    print("front:", front)
    print("rear:", rear)
    print("==============")

init_queue(5)
enqueue("커피")
enqueue("녹차")
enqueue("꿀물")
queue_print()

dequeue()
dequeue()
dequeue()
dequeue()
queue_print()
enqueue("콜라")
print("enqueue 후 상태:")
queue_print()