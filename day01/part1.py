if __name__ == "__main__":
    list1 = []
    list2 = []
    # with open("./day01/example_input") as file:
    with open("./day01/input") as file:
        for line in file:
            parts = line.strip().split(" ")
            list1.append(parts[0])
            list2.append(parts[-1])
    distances = [abs(int(a) - int(b)) for a, b in zip(sorted(list1), sorted(list2))]
    total_distance = sum(distances)
    print(f"Total distance between lists: {total_distance}")
