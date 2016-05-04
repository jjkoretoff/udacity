#set the working directory to the location of the dataset
getwd()
setwd("/Users/johnkoretoff/code/udacity/data-analysis-with-r/EDA_Course_Materials/lesson2")

#read in the data from the csv file
statesInfo <- read.csv('stateData.csv')

#subset the data for the NE
stateSubset <- subset(statesInfo, state.region == 1)
head(stateSubset, 2)
dim(stateSubset)

#alternative subsetting option
stateSubsetBracket <- statesInfo[statesInfo$state.region == 1, ]
head(stateSubsetBracket)
dim(stateSubsetBracket)
