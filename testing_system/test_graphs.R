# make a line graph of the humidity versus day
# log humidity, date, pump activity  data in a table 

# install packages and load libraries
#install.packages("dplyr")
#install.packages("tidyverse")
#install.packages("lubridate") #to use pythong
#install.packages("reticulate")
#install.packages("gridExtra")

library(ggplot2)
library(dplyr)
library(tidyverse)
library(lubridate)
library(reticulate)
library(gridExtra)

# data
humidity <- c(0.40,0.30,0.20,0.10,0.05,0.01)
time <- c(1,2,3,4,5,6)
pump_status <- c("OFF","OFF","OFF","OFF","OFF","OFF")

# make a table
table <- data.frame(Humidity=humidity,Day=time,Pump_status=pump_status)

# plot humidity against time
humidity_sensor_plot <- ggplot(table,aes(x=Day,y=Humidity))+
	geom_line(colour="red")+
	theme_minimal()+
	labs(title="Humidity Sensor Plot",x="Day",y="Sensor Value (V)")

# plot pump status against time
pump_status_plot <- ggplot(table,aes(x=Day,y=Pump_status))+
	geoom_line(colour="blue")+
	theme_minimal()+
	labs(title="Pump Status",x="Day",y="Pump status (0/1)")

# combine graphs
grid.arrange(humidity_sensor_plot,pump_status, ncol=1)

# save graphs
ggsave("humidity_sensor_plot.png",plot=humidity_sensor_plot,width=6,height=4)
ggsave("pump_status_plot.png",plot=humidity_sensor_plot,width=6,height=4)


