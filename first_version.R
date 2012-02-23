library(gpclib)       # loads polygon clipping library
library(maptools)     # loads sp library too
library(RColorBrewer) # creates nice color schemes
library(classInt)     # finds class intervals for continuous variables
library(shape)
library(rgdal)
world.shp <- readShapePoly(file.choose(), 
     proj4string=CRS("+proj=longlat"))

final_coordinates <- read.csv("C:\\Users\\chitrita\\Desktop\\maps\\our_project\\final_coordinates.csv")

plotclr <- brewer.pal(nclr,"BuPu")
plotclr <- plotclr[nclr:1] # reorder colors
class <- classIntervals(plotvar, nclr, style="equal")
colcode <- findColours(class, plotclr)

plot(world.shp)
points(final_coordinates$lon, final_coordinates$lat, pch=16, col=colcode, cex=2)
#points(final_coordinates$lon, final_coordinates$lat, cex=2)
title("Geographic overlay map",
    sub="Equal-Interval Class Intervals")
#legend(-117, 44, legend=names(attr(colcode, "table")), 
 #   fill=attr(colcode, "palette"), cex=0.6, bty="n")

