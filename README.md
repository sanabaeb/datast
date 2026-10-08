# 30229 이창준
## 10월 8일(5주차 강의)
파이썬 - 단순 연결 리스트의 응용

## 10월 1일(4주차 강의)
파이썬 - 단순 연결 리스트

### 4주차 파이썬 코드
```
class Node():
    def __init__(self):
        self.data = None
        self.link = None

# 첫번째 노드 생성 - 링크 필요 없음

node1 = Node()
node2 = Node()5
node3 = Node()
node4 = Node()
node5 = Node()

node1.data = "다현0"
node1.link = node2 # 첫번째 노드와 두번째 노드 연결

#두번째 노드 생성 - 첫번째 노드와 연결

node2.data = "다현1"
node2.link = node3 # 두번째 노드와 세번째 노드 연결


node3.data = "다현2"
node3.link = node4 # 세번째 노드와 네번째 노드 연결


node4.data = "다현3"
node4.link = node5 # 네번째 노드와 다섯번째 노드 연결


node5.data = "다현4"
node5.link = None # 다섯번째 노드는 마지막 노드이므로 link는 None

print(node1.data, end=" ")
print(node1.link.data, end=" ")
print(node1.link.link.data, end=" ")
print(node1.link.link.link.data, end=" ")
print(node1.link.link.link.link.data, end=" ")
```

### 실행결과
```
다현0 다현1 다현2 다현3 다현4 
```

## 9월 17일(3주차 강의)
파이썬 설치 및 파이썬 기초(리스트 등)

### 3주차 파이썬 코드
```
# print("Hello, World!")

kakao = ["가나", "다라", "마바", "사아", "자차"]
print(kakao)
print(kakao[0])
print(kakao[4])
kakao.append(None)
print(kakao)
# kakao.append("카타")
kakao[5] = "카타"
print(kakao)
```

### 실행결과
```
['가나', '다라', '마바', '사아', '자차']
가나
자차
['가나', '다라', '마바', '사아', '자차', None]
['가나', '다라', '마바', '사아', '자차', '카타']
```



## 9월 10일(2주차 강의)
마크다운


# html의 h1부터 h6까지 표현

# h1크기

## h2 크기

### h3 크기 

#### h4크기 

##### h5크기 

###### h6크기

*이텔릭체*

enter 두번으로 줄바꿈 가능

~~취소선~~

**볼드**

*** 이텔릭 + 볼드 ***

~~~
 1.사과
 2.배
 3.감

 *사과
    *깎은 사과
    *맛있는 사과
    * *째
*배
*감
~~~
##코드 블럭
```
    #주석
    print('Hello, World')
```

##링크 

[구글 바로가기](https://www.google.com/)

[이름](#이창준)

## 이미지 삽입
![임시이름](파일이름)


