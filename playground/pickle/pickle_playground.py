import pickle


bin_fname = "./test.bin"
txt_fname = "./test.txt"

data1 = 77
data2 = "Hello, World!"
data3 = ["apple", "banana", "orange"]

with open(bin_fname, "wb") as f:
    pickle.dump(data1, f)
    pickle.dump(data2, f)
    pickle.dump(data3, f)

with open(bin_fname, "rb") as f:
    binary = pickle.load(f)
    print("Binary Read 1: ", binary)
    binary = pickle.load(f)
    print("Binary Read 2: ", binary)
    binary = pickle.load(f)
    print("Binary Read 3: ", binary)

with open(txt_fname, "wt") as f:
    f.write(str(data1))
    f.write("\n")
    f.write(data2)
    f.write("\n")
    f.writelines("\n".join(data3))

with open(txt_fname, "rt") as f:
    for i, line in enumerate(f, 1):
        print("Text Read", str(i), ": ", line, end="")


class TestClass:
    def __str__(self):
        return "HoYa"


if __name__ == "__main__":
    print()

    obj1 = TestClass()
    print("Object: ", obj1)

    pickled = pickle.dumps(obj1)
    print("Pickle Dumps: ", pickled)

    obj2 = pickle.loads(pickled)
    print("Pickle Loads: ", obj2)
