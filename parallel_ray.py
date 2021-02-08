import ray

ray.init()

@ray.remote
class Number(object):
    def __init__(self):
       self.n = 0
    def add(self):
       self.n += 1
    def show(self):
       return self.n


numbers = [Number.remote() for i in range(30)]
[x.add.remote() for x in numbers]
answer = [x.show.remote() for x in numbers]

print(ray.get(answer))

