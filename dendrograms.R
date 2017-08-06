##
library(stringdist)

setwd("C:/Users/Gonzalo/Desktop/GitHub/linguistic-distance")

data=read.csv("lingT.csv")
data2=subset(data,Consider==1)

dimens=length(data2$Consider)

dist_matrix=matrix(, nrow = dimens, ncol = dimens)

for (i in 1:dimens){
	for (j in 1:dimens){
		dist_matrix[i,j]=stringdist(data2[i,2],data2[j,2])
	}
}

colnames(dist_matrix)=data2$Lang

Matriz_Idiomas=as.dist(dist_matrix)

pdf('ddg1.pdf')
par(mfrow=c(2, 2))

hc1 <- hclust(Matriz_Idiomas,method="mcquitty")#,members=data$Lang)                # apply hirarchical clustering 
hcp1=plot(hc1,main="Method: McQuitty",
	xlab=NULL,ylab="Distancia relativa",type = "unrooted",sub="")


hc2 <- hclust(Matriz_Idiomas,method="average")#,members=data$Lang)                # apply hirarchical clustering 
hcp2=plot(hc2,main="Method: Average",
	xlab=NULL,ylab="Distancia relativa",type = "unrooted",sub="")


hc3 <- hclust(Matriz_Idiomas,method="single")#,members=data$Lang)                # apply hirarchical clustering 
hcp3=plot(hc3,main="Method: Single",
	xlab=NULL,ylab="Distancia relativa",type = "unrooted",sub="")


hc4 <- hclust(Matriz_Idiomas,method="complete")#,members=data$Lang)                # apply hirarchical clustering 
hcp4=plot(hc4,main="Method: Complete",
	xlab=NULL,ylab="Distancia relativa", sub="")#,type = "unrooted")
###hclust methods: ward.D, ward.D2, single, complete, average, mcquitty, median, centroid
dev.off()
#par(mfrow=c(2, 2))



#############################USANDO APE
#install.packages("ape")
library("ape")
colors = c("red", "blue", "green", "black","brown","steelblue","darkorange",
	"tomato","purple","gray")
clus4 = cutree(hc1, 10)#9)
pdf('ddg2.pdf')
plot(as.phylo(hc1), type = "fan", tip.color = colors[clus4],
     label.offset = 1, cex = 0.7)
dev.off()
############################USANDO ggdendro
library(ggplot2)
library(ggdendro)
library(plotly)
library(htmlwidgets)


#### ggplot2
pdf('ddg3.pdf')
ggdendrogram(hc1)
dev.off()

saveWidget(gg_den_plot, file="test.htm")