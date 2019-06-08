import datetime
import FinanceDataReader as fdr
from pandas.plotting import register_matplotlib_converters
import matplotlib.pyplot as plt

register_matplotlib_converters()
start = datetime.datetime(2019, 6, 1)
end = datetime.datetime(2019, 6, 7)

gs_naver = fdr.DataReader("035420", start, end)
gs_daum = fdr.DataReader("035720", start, end)
print(gs_naver)
print(gs_daum)

fig = plt.figure("Charts Test")
fig.set_size_inches(10, 6, forward=True)
plt.plot(gs_naver.index, gs_naver["Close"], "b", label="Naver")
plt.plot(gs_daum.index, gs_daum["Close"], "r", label="Kakao")
plt.legend(loc="upper left")
plt.title("Naver & Daum")
plt.xlabel("Date")
plt.ylabel("Close")
plt.show()
