student_names = "Samantha,Mcgrath,Peyton,Kerim,Nadia,Sandra,Sarah,Alex"
names_list = student_names.split(",")
print(names_list)

tech_stack = "Angular Node Mongo Express"
tech_stack = tech_stack.replace("Angular", "React")
tech_stack_list = tech_stack.split()
print(tech_stack_list)

old_top_movies = "The Power of the Dog - Trapped - Tenet"
new_top_movies = old_top_movies.replace("Trapped", "Moonfall")
print(new_top_movies)