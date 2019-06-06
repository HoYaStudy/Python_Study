import pandas as pd
import numpy as np

# df = pd.read_csv("./pandas/csv1.csv")
# print(df)

# df = pd.read_csv('./pandas/csv1.csv', skiprows=[0, 1])
# print(df)

# df = pd.read_csv("./pandas/csv1.csv", skiprows=[0], header=None)
# print(df)

# df = pd.read_csv(
#     "./pandas/csv1.csv", skiprows=[0], header=None, names=["Month", 2017, 2018, 2019]
# )
# print(df)

# df = pd.read_csv(
#     "./pandas/csv1.csv",
#     skiprows=[0],
#     header=None,
#     names=["Month", 2017, 2018, 2019],
#     index_col=[1],
# )
# print(df)

# df = pd.read_csv(
#     "./pandas/csv1.csv",
#     skiprows=[0],
#     header=None,
#     names=["Month", 2017, 2018, 2019],
#     index_col=[0],
#     na_values=["JAN"],
# )
# print(pd.isnull(df))

# df = pd.read_csv(
#     "./pandas/csv1.csv", skiprows=[0], header=None, names=["Month", 2017, 2018, 2019]
# )
# print(df.index)
# print(list(df.index))
# print(df.index.values.tolist())
# print(df.rename(index={0: "aa", 1: "bb", 2: "cc"}))
# print(df.rename(index=lambda x: x + 1))

# df2 = pd.read_csv(
#     "./pandas/csv2.csv",
#     sep=";",
#     skiprows=[0],
#     header=None,
#     names=["Name", "Test1", "Test2", "Test3", "Final", "Grade"],
# )
# df2["Grade"] = df2["Grade"].str.replace("C", "A++")
# print(df2)

# df2 = pd.read_csv(
#     "./pandas/csv2.csv",
#     sep=";",
#     skiprows=[0],
#     header=None,
#     names=["Name", "Test1", "Test2", "Test3", "Final", "Grade"],
# )
# df2["Sum"] = df2[["Test1", "Test2", "Test3", "Final"]].sum(axis=1)  # axis=1 => Row
# df2["Avg"] = df2[["Test1", "Test2", "Test3", "Final"]].mean(axis=1)  # axis=1 => Row
# df2.to_csv("./pandas/result.csv", index=False)

# df3 = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list("ABCD"))
# print(df3)

# df3 = pd.DataFrame(np.random.randn(100, 4), columns=["One", "Two", "Three", "Four"])
# df3.to_csv("./pandas/result.csv", index=False, header=False)
