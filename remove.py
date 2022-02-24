# pop() :-
# Using the pop( ) method we can remove a specified element from the dictionary.
# CAR_DETAILS={
#     "brand": "Ford",
#     "model": "jason",
#     "year": 1964
# }
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS)

# popitem():-
# The popitem() method removes the last inserted item:
person={
    'name':'jack',
    'id':22,
    'place':'dharamsala'
}
person.popitem()
print(person)

# del :-
# Using the del keyword we can remove a specified element from the dictionary.
# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }

# del person['place']
# print(person)