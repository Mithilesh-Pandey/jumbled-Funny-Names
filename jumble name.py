import random

def jumbleName():
    first_name = [name.split()[0] for name in names]
    last_name = [name.split()[1] for name in names]
    # print(first_name)
    # print(last_name)

    for _ in names:
        random_fname = random.choice(first_name)
        random_lname = random.choice(last_name)
        
        print(f"{random_fname} {random_lname}")   
        first_name.remove(random_fname)
        last_name.remove(random_lname) 


if __name__ == "__main__":
    numofname = int(input("How many number of the names to input?"))
    names =[]

    for i in range(numofname):
        names.append(input("Enter the firstname and lastname:"))   
    jumbleName()    
        
        
      