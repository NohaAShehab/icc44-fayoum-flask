name = 'ahmed'
print(name)

# each python script has main --> main is the entry point of the script ??
# __name__='__main__'

# lambda

# function without name , use once at time

res=lambda x:x+4
print(res)
print(res(10))

# filter ?

nums = [3,4,10, 445, 100]
# filter even number
newnums = filter(lambda num: num % 2 == 0, nums)
print(newnums)
print(list(newnums))

students = [
        {"id": 1, "name": "Mazen", "image": "pic1.png", "grade": 100},
        {"id": 2, "name": "Safa", "image": "pic2.png", "grade": 100},
        {"id": 3, "name": "Israa", "image": "pic3.png", "grade": 100},
        {"id": 4, "name": "Omar", "image": "pic4.png", "grade": 100},
        {"id": 5, "name": "Helana", "image": "pic4.png", "grade": 100},
    ]

# for loop
def search_std(id):
    students = [
        {"id": 1, "name": "Mazen", "image": "pic1.png", "grade": 100},
        {"id": 2, "name": "Safa", "image": "pic2.png", "grade": 100},
        {"id": 3, "name": "Israa", "image": "pic3.png", "grade": 100},
        {"id": 4, "name": "Omar", "image": "pic4.png", "grade": 100},
        {"id": 5, "name": "Helana", "image": "pic4.png", "grade": 100},
    ]
    # for student in students:
    #     if student["id"] == id:
    #         return student
    # else:
    #     return None
    std = filter(lambda s: s["id"] == id, students)
    return list(std)

res= search_std(1)
print(res)