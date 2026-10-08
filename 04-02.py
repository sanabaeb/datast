class Node():
    def __init__(self):
        self.data = None
        self.link = None

# 첫번째 노드 생성 - 링크 필요 없음

node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node5 = Node()

node1.data = "다현0"
node1.link = node2 # 첫번째 노드와 두번째 노드 연결

node2.data = "다현1"
node2.link = node3 # 두번째 노드와 세번째 노드 연결


node3.data = "다현2"
node3.link = node4 # 세번째 노드와 네번째 노드 연결


node4.data = "다현3"
node4.link = node5 # 네번째 노드와 다섯번째 노드 연결


node5.data = "다현4"
node5.link = None # 다섯번째 노드는 마지막 노드이므로 link는 None

# print(node1.data, end=" ")
# print(node1.link.data, end=" ")
# print(node1.link.link.data, end=" ")
# print(node1.link.link.link.data, end=" ")
# print(node1.link.link.link.link.data, end=" ")

current = node1
print("\n", current.data, end=" ")
while current.link != None:
    current = current.link
    print(current.data, end=" ")