from pandas import DataFrame

r_data = {
    "City": ["Seoul", "Daegu", "Busan", "Daejeon"],
    "Total1": [55000, 49000, 52000, 50000],
    "Total2": [65000, 59000, 62000, 60000],
}
i_data = ["One", "Two", "Three", "Four"]
d_frame = DataFrame(r_data, index=i_data)
print(d_frame)
print(d_frame.index)
print(d_frame.values)
print(d_frame["City"])
print(d_frame.ix["One"])  # Row data
for e in d_frame.values:
    for i, z in enumerate(e):
        print(i, z)
