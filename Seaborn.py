import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data=sns.load_dataset("tips")

# # Relational /Statistical Plot--> Scatter Plot,Line Plot(time based), FaceGrid(plotting multiple graph side by side)


# # Scatter plot
# # Scatter plot is used to show the relationship between two variables(multivarient analysis)
# # It is a type of bivariate data that shows the relationship between two variables.
# # The x-axis represents the first variable, and the y-axis represents the second variable.
# # Each point on the scatter plot represents a data point, and the distance between the points represents the relationship between the variables.
# # The scatter plot can be used to identify patterns, trends, and correlations between the variables.
# # Here is an example of a scatter plot using seaborn library in Python.
# #Mostly used for NUmerical Data
# #Two ways to draw scatterplot
# #1.relplot(Figure Level Function)
# #2.scatter plot(Axes level function)


# sns.relplot(x="total_bill",y="tip",kind="scatter",data=data) #kind=scatter/line

# #hue parameter
# #hue parameter is used to color the points in the scatter plot.
# # It is used to represent the third variable in the scatter plot.
# sns.relplot(x="total_bill",y="tip",kind="scatter",hue="smoker",data=data)


# #style parameter
# #style parameter is used to change the style of the scatter plot.
# # It is used to change the color, marker, and line style of the scatter plot.
# sns.relplot(x="total_bill",y="tip",kind="scatter",hue="smoker",style="sex",data=data)


# #size parameter
# #for hue and style paramter categorial data is used bu for size parameter numerical data is used
# sns.relplot(x="total_bill",y="tip",kind="scatter",hue="smoker",size="size",sizes=(15,20),data=data)


# #same for scatter plot sns.scatter()
# sns.scatterplot(x="total_bill", y="tip", hue="sex", data=data)
# plt.show()

#Categorial data
#Categorial Scatterplot --> stripplt , Swarmplot
#categorial distribution plots -->boxplot ,Violonplot
#Categorial estimate plots--> Pointplot,barplot,Countplot
#Categorial relationship plots-->Jointplot,Pairplot

#Categorial Scatterplot x_axis-categorial data, y_axis-Numerical data
# sns.catplot(x="day",y="tip",kind="strip",jitter=5,data=data)

# #swarm plot
# sns.catplot(x="day",y="tip",kind="swarm",data=data)
# #can't use style and size par only hue and col
# sns.catplot(x="day",y="tip",kind="swarm",hue="sex",data=data) #catplot or swarmplot
# plt.show()

#Boxplot
#Boxplot is used to represent the distribution of a numerical variable.
# It is used to compare the distribution of different groups.
#univarient 
# sns.boxplot(x="tip",data=data)
#Mulitvarient
# sns.set_style("darkgrid")  # Options: "whitegrid", "darkgrid", "white", "dark", "ticks"
# sns.set_style("whitegrid")  # Clean background with grid
# sns.set_context("poster")  # Options: "paper", "notebook", "talk", "poster"
# sns.catplot(x="day",y="tip",kind="box",data=data)
# sns.catplot(x="day",y="tip",kind="box",hue="sex",palette="coolwarm",data=data)
# sns.catplot(x="day",y="tip",kind="box",hue="sex",palette="coolwarm",showfliers=False,data=data) #showfilter remove outliers
# plt.show()
#Violinplot boxplot +kde/pdf
# sns.violinplot(x="day", y="total_bill", hue="size", data=data, split=True)
# plt.show()

#barplot and countplot(cat data and their count like histogram) ->central tendency
#num and cat data
# sns.catplot(x="smoker",y="total_bill",hue="sex",kind="bar",data=data)
# sns.catplot(x="smoker",y="total_bill",hue="sex",kind="bar",estimator=np.median,data=data)
# sns.pointplot(x="day", y="total_bill", data=data, estimator=np.mean, color='red', markers="o")
# plt.title("Box Plot with Mean Overlay (Red Dots)")
# plt.show()
#

#heatmap
# flight=sns.load_dataset('flights')
# sns.set_style("whitegrid")
# x=flight.pivot_table(index="year",columns="month",values="passengers",aggfunc="sum")
# sns.heatmap(x,cbar=True,linewidths=0.5,annot=True,fmt="d",cmap="viridis") #cmap=summer ,winter
# plt.show()

#cluster map
#cluster row and column on the basis of simalarity
# flights_pivot = flight.pivot(index="month", columns="year", values="passengers")
# sns.clustermap(flights_pivot,cmap="viridis")
# #par--> annot,row_cluster=false,(clustring on the basis of col not row)col_cluster,z_score,metric="euclidean" or ward cprrealtion
# plt.show()

#joint plot def kind=scatter
#sctter plt,hexbin(2d hist),kde,regplot
# sns.jointplot(x="total_bill",y="tip",data=data)
# sns.jointplot(x="total_bill",y="tip",kind="hex",data=data)
# sns.jointplot(x="total_bill",y="tip",kind="kde",data=data)
# sns.jointplot(x="total_bill",y="tip",kind="reg",data=data)
# plt.show()

#pair plot
#plot multiple pairwise bivarient distribution
# iris=sns.load_dataset("iris")
# print(iris)
# sns.pairplot(iris,hue="species")
# plt.show()

#distplt
#univarient analysis on continous data
# titanic = pd.read_csv(r"C:\Users\soumy\Downloads\train.csv")
# titanic["Age"].fillna(titanic["Age"].mean,inplace=True)
# sns.distplot(titanic["Age"],kde=False,bins=100) #kde =False only histogram hist=False --> only histogram
# # rug=True --> add rug plot kde,hist=false
# #sns.distplot(titanic[titanic["survived"]==1]["Age"])
# plt.show()