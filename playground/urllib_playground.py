import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

imgURL = "http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg"
htmlURL = "http://google.com"

savePath1 = "./test1.jpg"
savePath2 = "./index.html"

# dw.urlretrieve(imgURL, savePath1)
f = dw.urlopen(imgURL)
saveFile1 = open(savePath1, 'wb')
saveFile1.write(f.read())
saveFile1.close()

# dw.urlretrieve(htmlURL, savePath2)
f2 = dw.urlopen(htmlURL).read()
with open(savePath2, 'wb') as saveFile2:
	saveFile2.write(f2)

print("Complete!")
