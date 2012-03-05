library(gpclib)       # loads polygon clipping library
library(maptools)     # loads sp library too
library(RColorBrewer) # creates nice color schemes
library(classInt)     # finds class intervals for continuous variables
library(shape)
library(rgdal)
# Oregon county census data (polygons)
# browse to orcounty.shp
world.shp <- readShapePoly(file.choose(), 
     proj4string=CRS("+proj=longlat"))

final_coordinates <- read.csv("C:\\Users\\chitrita\\Desktop\\maps\\our_project\\first_cluster_citiescount.csv")

#plotvar <- orstationc$tann
#nclr <- 8
plotclr <- brewer.pal(nclr,"BuPu")
plotclr <- plotclr[nclr:1] # reorder colors
class <- classIntervals(plotvar, nclr, style="equal")
colcode <- findColours(class, plotclr)

#family <- as.factor(final_coordinates$lat)

symbol.size <- final_coordinates$CNT


plot(world.shp)
points(final_coordinates$lon, final_coordinates$lat, pch=19, col=colcode, cex=symbol.size)
#points(final_coordinates$lon, final_coordinates$lat, cex=symbol.size)
title("Geographic overlay map",
    sub="Equal-Interval Class Intervals")
#legend(-117, 44, legend=names(attr(colcode, "table")), 
 #   fill=attr(colcode, "palette"), cex=0.6, bty="n")

