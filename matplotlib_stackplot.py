from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")
minutes=[1,2,3,4,5,6,7,8,9]
player1=[1,2,3,4,4,4,5,5,6]
player2=[1,1,1,1,1,2,2,2,3]
player3=[1,1,1,2,2,2,3,3,3]

labels=["player1","player2","player3"]
colors=["blue","green","red"]

plt.stackplot(minutes,player1,player2,player3,labels=labels,colors=colors)
plt.legend(loc=(8.05,1.05))
plt.title("My Awesome Stack Plot")
plt.tight_layout()
plt.show()
