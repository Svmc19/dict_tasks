# Task1
# input1 = input("Darth Vader / Leia / Han / R2D2\n""Who can't you remember?:")
# def relation_to_luke(input1):
#     relations = {
#         "Darth Vader": "father",
#         "Leia": "sister",
#         "Han": "brother in law",
#         "R2D2": "droid"
#     }
#     for x in relations:
#         if x == input1:
#             return f"Luke, I'm your {relations[x]}."
#     return "Luke hasn't got a relation with this name?!"
#
# print(relation_to_luke(input1))

# Task2
# def maximum_score(dict):
#     result = 0
#     for x in dict:
#         for key,value in x.items():
#             if key == "score":
#                 result += value
#     return result
#
# print(maximum_score([
#     { "title": "N","score": 1 },
#     { "title": "K","score": 5 },
#     { "title": "Z","score": 10 },
#     { "title": "X","score": 8 },
#     { "title": "D","score": 2 },
#     { "title": "A","score": 1 },
#     { "title": "E","score": 1 },
# ]))



#Task3
# def mapping(lst):
#     vocab = {}
#     for x in lst:
#         vocab[x] = x.upper()
#     return vocab
#
# print(mapping(["p", 's']))
# print(mapping(['a', 'b', 'c']))
# print(mapping(['a', 'v', 'y', 'z']))
#

#Task4
# def count_all(string):
#     son = {
#     }
#     result = 0
#     result_num = 0
#     for x in string:
#         if x.isalpha():
#             result += 1
#         if x.isdigit():
#             result_num += 1
#     son["LETTERS"] = result
#     son["DIGITS"] = result_num
#     return son
#
# print(count_all("Hello world"))
# print(count_all("H3ll0 wor1d"))
# print(count_all("149990"))

# # Task5
# def calc_diff(dict,int):
#     result =0
#     for values in dict.values():
#         result +=values
#     return result - int
#
# print(calc_diff({"baseball bat":20},5))
# print(calc_diff({"skate":10,"painting":20},19))
# print(calc_diff({"skate":200,"painting":200,"shoes":1},400))
#
# Task6
# def lst(dict1, dict2):
#     return ((dict2['x'] - dict1['x'])** 2 + (dict2["y"] - dict1["y"]) ** 2) ** (1/2)
#
# print(lst(dict(x=-2, y=1), dict(x=4, y=3)))
# print(lst(dict(x=0, y=0), dict(x=1, y=1)))
# print(lst(dict(x=10, y=-5), dict(x=8, y=16)))

# Task7
# def compare_age():
#         str = ""
#         p1 = ("Samuel", 24)
#         p2 = ("Joel", 36)
#         p3 = ("Lily", 24)
#         if p1[1] < p2[1]:
#             str+= f"{p2[0]} is older than me.\n"
#         if p2[1] > p1[1]:
#             str+= f"{p1[0]} is younger than me.\n"
#         if p1[1] == p3[1]:
#             str+= f"{p3[0]} is the same age as me.\n"
#         return str
# print(compare_age())


# Task8
# def dict_to_list(dict):
#     lst =[]
#     for x in dict.items():
#         lst.append(tuple(x))
#     return sorted(lst)
#
# print(dict_to_list({
#     "D":1,
#     "B":2,
#     "C":3
# }
# ))

# Task9
# Task10
# def count(lst):
#     lst1 = []
#     dict = {}
#     for x in lst:
#         if x not in lst1:
#             lst1.append(x)
#     for z in lst1:
#         if z in lst:
#             counting = lst.count(z)
#             dict[z] = counting
#     return dict
#
# print(count(["A","B","A","A","A","B"]))
# print(count([1,1,2,3,4,4,2,5,6]))

# # Task11
# def oldest(dict):
#     lst =[]
#     for value in dict.values():
#         lst.append(value)
#     maximum = max(lst)
#     for key in dict:
#         if dict[key] == maximum:
#             return key
#
# print(oldest({
#     "Emma": 48,
#     "Jake": 71,
#     "Amy": 15,
#     "Ben": 29
# })
# )
# print(oldest({
#     "Max": 9,
#     "Josh": 13,
#     "Sam": 48,
#     "Anne": 33
# }))

# Task12
# def top_note(dict):
#     for key,value in dict.items():
#         if key == "notes":
#             x = max(value)
#             dict.popitem()
#             dict["top_notes"] = x
#             return dict
#
# print(top_note({
#     "name":"John",
#     "notes": [3,5,4]
# }))

# Task13
# def profit(dict):
#     lst = []
#     for value in dict.values():
#         lst.append(value)
#     return (lst[1] - lst[0]) * lst[2]
#
# print(profit({
#     "cost_price": 32.67,
#     "sell_price": 45,
#     "inventory": 1200
# }))
# print(profit({
#     "cost_price": 225.89,
#     "sell_price": 550.00,
#     "inventory": 100
# }))
# # Task14
# def inver(dict):
#     dict_new ={}
#     for key,value in dict.items():
#             dict_new[value] = key
#     return dict_new
#
# print(inver({
#     "z": "q","w": "f"
# }))
# print(inver({
#     "a": 1,"b":2,"c":3
# }))
#
# Task15
# def p1(inform):
#     take = inform[0]
#     all = ''
#     for x in inform:
#         if x == inform[1]:
#             pop = f"{take}'s age is {x}years\n"
#             all += pop
#         if x == inform[2]:
#             pop = f"{take}'s height is {x}cm\n"
#             all += pop
#         if x == inform[3]:
#             pop = f"{take}'s weight is  {x}kg\n"
#             all += pop
#     return all
# print(p1(["David Jones", 25, 175, 75]))
# print(p1(["Steve Brown",47,167,65]))





















#
# person =[{
#     "name":"Ali",
#     "age":25,
#     "friend":{
#         "name":"Vali",
#         "age":24,
#         "friend":{
#             "name":"Shohrux",
#             "age":22,
#
#         }
#     }
# }]

# def people():
#     p1 = ("Samuel",24)
#     p2 = ("Joey",36)
#     p3 =("Lily",24)
#
# print(people())

# def is_subset(lst1,lst2):
#     set1 = set(lst1)
#     set2 = set(lst2)
#     return set1.issubset(set2)
#
# print(is_subset([3,2,5],[5,3,7,9,2])),
# print(is_subset([8,9],[7,1,9,8,4,5,6])),
# print(is_subset([1,2],[3,5,9,1]))
#
# def lists(lst1,lst2):
#    lst = []
#    for x in lst1:
#       if x in lst2:
#          lst.append(x)
#    if len(lst) == len(lst1):
#       return True
#    return False
#
#
# print(lists([3,2,5],[5,3,7,9,2])),
# print(lists([8,9],[7,1,9,8,4,5,6])),
# print(lists([1,2],[3,5,9,1]))
# person = {
#    "user1":{
#       "name":"Maftuna",
#       "age":16
#    },
#    "user2":{
#       "name":"Malika",
#       "age":16
#    },
#    "user3":{
#       "name":"Bunyod",
#       "age":12
#    }
# }
# result = 0
# for x in person:
#    z = person[x]
#    for i in z:
#       if i == "age":
#          result+= person[x][i]
# print(result)



