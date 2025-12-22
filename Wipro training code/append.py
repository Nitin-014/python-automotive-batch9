food=["biriyani","Dosa","Rice","roti","burger","Pizza"]
print(food)
food.append("Chicken")
food.pop(2)
food.remove("roti")
print(food)


#squares of a number
nums=[1,2,3,4,5]
squares=[x**2 for x in nums]
print(squares)



capitals={'india':'Delhi',"USA":"Washington DC","china":"beijing"}
print(capitals)
print(capitals.get("Russia"))
capitals.update({"Russia":"Moscow"})
print(capitals)