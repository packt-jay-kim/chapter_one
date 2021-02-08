import ray

ray.init()

@ray.remote
def test(x):
    return x * x 

answer = [test.remote(i) for i in range(40)]
print (ray.get(answer))


