# import statistics
# list_valeur = []
# statistics.mean(list_valeur)

for file in ["ImageUrl.py","Exo1_Thread.py","Exo11_Thread.py"]:
    with open(file,"r") as file:
        exec(file.read())

