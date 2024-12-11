#collections
# list ,tuple,set,dictionary, 

# 1st list ------------------
fruits = ["mango", "apple","banana","orange","grapes"]
veg = ["tomato", "potato","daal","lauki","palak"]
# print(fruits)
# print(fruits[2])
# print(fruits[-3])
# print(fruits[1:4])

# fruits.append("pie")
# print(fruits)
# fruits.insert(2,"pie")
# fruits.extend(veg)
# print(fruits)

# fruits.remove("mango")
# fruits.pop(2)
# print(fruits)

# fruits.sort()
# print(fruits)

# fruits.sort(reverse=True)
# print(fruits)


# 2nd tuple:----------------------
# tuple is immutable but list is mutale baaki dono same hai har property
# vege = ("sabji","daal","tomato","potato")


# 3rd : Set 
# unordered , immuatable, unindexed, duplicates not allowed, any datatype, mix of different datatypes
vege = {"sabji","daal","tomato","potato"}
# # print(vege)
# # print(type(vege))
# vege.add("bhindi")
# print(vege)
# s1 = {1,2,3}
# s2 = {4,5,6}
# print(s1.union(s2))


# 4th dictionary : ordered , changeable, unindexed,duplicates,not allowed, any mix data type 

phones= {
    "ram": 13,
    "pradeep":432,
    "bhia":654
}

# print(phones)
# print(phones["pradeep"])
# print(phones.get("bhia"))
# print(phones.keys())
# phones["bhia"]=87
# print(phones)