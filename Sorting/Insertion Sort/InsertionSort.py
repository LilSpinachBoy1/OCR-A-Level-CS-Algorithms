# Create dataset
data = ["Wicker Man", "The Smiler", "Th13teen", "Rita", "Oblivion", "Nemesis", "Galactica"]

#TODO: This is awful and wrong
for index in range(1, len(data)):
    temp_store = data[index]
    checking = index - 1
    while checking > 0 and data[checking] < data[index]:
        data[index] = data[checking]
        checking -= 1

    data[checking]
