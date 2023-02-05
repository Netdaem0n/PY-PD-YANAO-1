file_names = ["task3_1", "task3_2", "task3_3"]


def my_out(names):
    temp = []
    for i in names:
        with (open(i, "r", encoding="UTF-8")) as f:
            data = f.read()
            count_data = data.count("\n")
        temp.append((i, count_data + 1, data))
    return sorted(temp, key=lambda x: x[1])


def write_mydata(data, myfilename):
    with open(myfilename, "w", encoding="UTF-8") as f:
        for i in data:
            f.write(i[0] + "\n")
            f.write(str(i[1]) + "\n")
            f.write(i[2] + "\n")


my_data = my_out(file_names)
write_mydata(my_data, "task3_OUT")
