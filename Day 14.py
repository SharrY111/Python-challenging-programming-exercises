# # Create a function that tkes string of list and return the list sorted by occurance
# def check_occurance(str):
#     lst_sorted=[]
#     d=sorted(str)
#     lst_sorted.append(d)
#     return lst_sorted

# str=("hii","sharjeel","b","a","c")
# print(check_occurance(str))


# # Create a function that tkes string of list and return the list sorted by lenggth
# def check_length(str):
#     lst_sorted=[]
#     d=sorted(str ,key=len)
#     lst_sorted.append(d)
#     return lst_sorted

# str=["abc","def","g","hi","a","vvvvv"]
# print(check_length(str))


# # Implement a function that takes two lists and return their union (all unique items)
# def return_unique(lst1,lst2):
#     lst=[]
#     for i in lst1:
#                 if i not in lst2:
#                         lst.append(i)
#     for r in lst2:
#                 if r not in lst1:
#                         lst.append(r)                        
                        
#     return lst
# lst1=["a","b","c","d"]
# lst2=["b","e","f","g"]
# print(return_unique(lst1,lst2))