def cuber(num):
    cube_dict = {}

    for i in range(1,num+1):
        cube_dict[i] = i ** 3
    return cube_dict


print(cuber(5))
