class agent:
    def __init__(self,name,score):
        self.name=name
        self.score=score

arr=[]

for i in range(5):
    name,score=tuple(input().split())
    score=int(score)
    a=agent(name,score)
    arr.append(a)

ans=(arr[0].name,arr[0].score)

for agent in arr:
    if agent.score<=ans[1]:
        ans=(agent.name,agent.score)

name,score=ans

print(f'{name} {score}')