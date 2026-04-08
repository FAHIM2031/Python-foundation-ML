data=[1,2,3,4,5,6,7,8]
batch_size=3

def get_list(data,batch_size):
    for i in range(0,len(data),batch_size):
        yield data[i:i+batch_size]

x=get_list(data,batch_size)
print(next(x))
print(next(x))
print(next(x))