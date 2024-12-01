if __name__ == "__main__":
    list1 = []
    list2 = []
    # with open("./day01/example_input") as file:
    with open("./day01/input") as file:
        for line in file:
            parts = line.strip().split(" ")
            list1.append(parts[0])
            list2.append(parts[-1])
    scores = [int(a) * list2.count(a) for a in list1]
    similarity_score = sum(scores)
    print(f"Similarity score: {similarity_score}")
