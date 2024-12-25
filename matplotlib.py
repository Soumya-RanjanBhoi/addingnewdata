import matplotlib.pyplot as plt
import numpy as np


# BAR PLOT
# x=["c","cpp","python","java"]
# y=[10,30,50,30]
# y1=[5,20,45,20]

# w=0.2
# p=np.arange(len(x))
# p1=[j+w for j in p]

# plt.bar(p,y,color=["r","y","g","b"],width=w,align="center",edgecolor="m",alpha=1,linewidth=1,label="Graph")
# plt.bar(p1,y1,width=w,color="m",align="center",edgecolor="m",alpha=1,linewidth=1.5,linestyle=":")
# plt.xlabel("Languages",fontsize=20)
# plt.ylabel("number",fontsize=20)

# plt.xticks(p+w/2,x,rotation=10)
# plt.legend(fontsize=20,loc=1)
# plt.show()




# SCATTER PLOT
# x=[20,30,40,50]
# y=[2,3,5,6]


# plt.xlabel("Data",fontsize=20)
# plt.ylabel("frequency",fontsize=20)
# plt.title("MARks",fontsize=30)


# plt.scatter(x,y,marker="*",alpha=0.4,sizes=[100,200,300,400],edgecolor="g",color=["m","r","b","y"],linewidths=1,cmap="viridis")
# plt.colorbar()
# plt.show()





#HISTOGRAM PLOT
# l=[39, 40, 49, 44, 24, 10, 17, 17, 55, 42, 11, 10, 36, 55, 24, 26, 42, 51, 39, 51, 23, 24, 15, 26, 38, 52, 53, 27, 57, 31, 49, 29, 51, 17, 56, 13, 54, 56, 14, 14, 33, 54, 46, 44, 34, 58, 10, 52, 46, 56]

# b=[10,20,30,40,50]
# plt.xlabel("DATA",fontsize=20)
# plt.ylabel("frequency",fontsize=20)
# plt.title("MARKS",fontsize=30)


# plt.hist(l,color="r",edgecolor="b",bins=b,cumulative=-1,align="mid",histtype="step",orientation="vertical",rwidth=0.2,log=True,label="random")
# # plt.hist(l,"auto",(0,100),edgecolor="b")
# plt.axvline(45,color="g",label="LINE")

# plt.legend(fontsize=20)
# plt.grid()

# plt.show()





# PIE PLOT
# x=[25,30,25,20]
# y=["java","python","cpp","c"]

# plt.title("DATA",fontsize=20)

# # plt.pie(x,labels=y,colors=["g","b","y","r"],autopct="%.2f",explode=[0.2,0.0,0.0,0.0],radius=1.5,labeldistance=1,rotatelabels=True,textprops={"fontsize":10},wedgeprops={"linewidth":4,"width":2,"edgecolor":"g"})
# plt.pie(x,labels=y,colors=["g","b","y","r"],autopct="%.2f",explode=[0.2,0.0,0.0,0.0],radius=1.5,labeldistance=1,rotatelabels=True,textprops={"fontsize":10})
# # plt.pie([1],colors="w")


# c=plt.Circle(xy=(0,0),radius=1,facecolor="w")
# plt.gca().add_artist(c)


# plt.show()




# STEM PLOT
# x=[1,2,3,4,5]
# y=[10,20,30,40,50]

# plt.stem(x,y,linefmt=":",markerfmt="r+",bottom=10,basefmt="g",label="DATA",orientation="vertical",use_line_collection=False)

# plt.legend(fontsize=20,loc=1)

# plt.show()




# BOX PLOT AND WHISKER PLOT
# x=[8.7,14.2,18.3,18.4,23.2,25.9,29.7,35.2,51.2,54.7,65.9,75,90,120]
# x1=[10,20,30,40,50,60,70,80,90]
# y=[x,x1]

# plt.boxplot(y,notch=False,showmeans=True,widths=0.8,labels=["python","cpp"],vert=True,patch_artist=True,boxprops={"color":"m"},
#             capprops={"color":"r"},filerprops={"markeredgecolor":"g"})
# # whis=2, sym="g+" for outlier g-- color + ==sign wiskerprops={"color":'r}

# plt.show()




# STACK PLOT
# x=[1,2,3,4,5,6]
# area1=[2,4,6,8,10,12]
# area2=[3,6,9,12,15,18]
# area3=[4,8,12,16,20,24]


# plt.xlabel("X--",fontsize=23)
# plt.ylabel("AREA",fontsize=23)
# plt.title("Graph",fontsize=23)


# plt.stackplot(x,area1,area2,area3,labels=["area1","area2","area3"],colors=["g","r","m"],baseline="sym")
# plt.grid()
# plt.legend(loc=2,fontsize=10)

# plt.show()




# step plot
# x=[1,2,3,4,5,6]
# y=[2,4,6,8,10,12]

# plt.xlabel("x-",fontsize=12)
# plt.ylabel("y",fontsize=12)
# plt.title(" step plot",fontsize=23)


# plt.step(x,y,color="g",marker="o",mfc="g",ms=8,label="data")
# plt.grid()
# plt.legend(fontsize=10,loc=2)

# plt.show()




#fill_between plot
# x=[1,2,3,4,5]
# y=[2,4,9,16,4]

# plt.xlabel("x--",fontsize=10)
# plt.ylabel("y--",fontsize=12)
# plt.title("fill_between",fontsize=12)

# plt.plot(x,y,color="r",label="data")
# plt.fill_between(x,y,color="g",alpha=0.4)
# # x=[start,end],y1,y2
# # where(x>2 & x<4) x must be in array np.array()
# plt.show()




# sub-plot and saving file
# x=[1,2,3,4,5]
# y=[1,4,9,4,9]
# plt.subplot(2,2,1)
# plt.plot(x,y)

# a=[20,40,20,20]
# plt.subplot(2,2,2)
# plt.pie(a,autopct="%.2f")

# plt.subplot(2,2,3)
# plt.pie([1])

# y=["python","java","cpp","c"]
# plt.subplot(2,2,4)
# plt.bar(y,a)


# plt.savefig("file2.pdf",dpi=1200,facecolor="g",transparent=False,bbox_inches="tight")
# plt.show()



