from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")
slices=[60,40,10,13]
labels=["sixty","forty","extra_1","extra_2"]
explode=[0.1,0,0,0]


colors=["#CD5C5C","#808080","#000000","#FF0000"]
plt.pie(slices,labels=labels,shadow=True,startangle=90,autopct="%1.1f%%",
        explode=explode,colors=colors,wedgeprops={"edgecolor":"black"})
plt.title("MY Awesome pie Chart")
plt.tight_layout()
plt.show()
