def rose_cost(rose_count):
    return rose_count*10

def delivery_cost(dist):
    if dist<=5:
        return 25
    elif dist>5 and dist<=10:
        return 50
    elif dist>10:
        return 75

def main():
    rose_count = int(input("Enter the number of roses: "))
    dist = int(input("Enter the distance to deliver in km: "))

    print("Total cost: {}".format(rose_cost(rose_count)+delivery_cost(dist)))


main()