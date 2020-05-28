
#The following arrays are sorted by BG, NYT, and WP scores respectively. I obtained them via the python code in main.py.
articleFlesch = c(65.73733253364323, 31.17559511434513, 54.91958649719382, 75.05713724164168, 53.09729455709714, 
                  28.3745271629779, 31.638799992482348, 63.218393586492795, 56.31988297793299, 54.0694970161978, 
                  28.170187908496757, 42.87420493341128, 36.05410234614078, 35.9335214785215, 36.72083333333336, 
                  59.75238242647936, 28.200202794819376, 46.17216152945767, 40.71401062363151, 37.553146302034236,
                  61.25693181818184, 55.568579785909876, 46.97833835275634, 56.90929844097997, 44.891600101295154, 
                  45.63042271335377, 45.06408424908429, 40.82797123623013, 31.867047522750283, 60.86585495701557, 
                  50.94425407925411, 38.758395252838, 33.15309128025666, 41.969657408947285, 42.33668564816506, 
                  57.6761259338314)
editorialFlesch = c(54.949984805984116, 43.431414603960434, 44.43590163934428, 34.44680962757528, 
                    32.44274514200299, 50.964908175069894, 60.882937710437744, 27.216678122863215, 
                    57.77308139021375, 32.03633210332106, 47.57773494860501, 52.673898457684174, 
                    27.73693954659953, 52.711472805202504, 40.98621012658228, 42.95604269972455, 
                    40.23683639633569, 35.480228375677996, 27.870275601766167, 39.04289308176104, 
                    54.06586842105264, 34.59676790950988, 42.20628920863314,41.97984277799381, 
                    39.7529284369115, 40.16899156885438, 39.3021424829754, 45.86320312500001, 
                    25.140715996805966, 37.59338267322744, 48.4234454734455, 29.214325699745558, 
                    25.348675605340617, 18.792806347930906, 47.939624329159216, 42.3256102540835)
bothFlesch = c(articleFlesch, editorialFlesch)


#THE FOLLOWING ARE FOR INDIVIDUAL NEWSPAPERS
NYTFlesch = c(36.05410234614078, 35.9335214785215, 36.72083333333336, 59.75238242647936, 28.200202794819376, 
              46.17216152945767, 40.71401062363151, 37.553146302034236, 61.25693181818184, 55.568579785909876, 
              46.97833835275634, 56.90929844097997, 27.73693954659953, 52.711472805202504, 40.98621012658228, 
              42.95604269972455, 40.23683639633569, 35.480228375677996, 27.870275601766167, 39.04289308176104, 
              54.06586842105264, 34.59676790950988, 42.20628920863314,41.97984277799381)
BGFlesch = c(65.73733253364323, 31.17559511434513, 54.91958649719382, 75.05713724164168, 53.09729455709714, 
             28.3745271629779, 31.638799992482348, 63.218393586492795, 56.31988297793299, 54.0694970161978, 
             28.170187908496757, 42.87420493341128, 54.949984805984116, 43.431414603960434, 44.43590163934428,
             34.44680962757528, 32.44274514200299, 50.964908175069894, 60.882937710437744, 27.216678122863215,
             57.77308139021375, 32.03633210332106, 47.57773494860501, 52.673898457684174)

WPFlesch = c(44.891600101295154, 45.63042271335377, 45.06408424908429, 40.82797123623013, 31.867047522750283, 
             60.86585495701557, 50.94425407925411, 38.758395252838, 33.15309128025666, 41.969657408947285, 
             42.33668564816506, 57.6761259338314, 39.7529284369115, 40.16899156885438, 39.3021424829754, 
             45.86320312500001, 25.140715996805966, 37.59338267322744, 48.4234454734455, 29.214325699745558, 
             25.348675605340617, 18.792806347930906, 47.939624329159216, 42.3256102540835)
#boxplot(NYTFlesch, BGFlesch, WPFlesch, ylab="Flesch Score", col=c("cornflowerblue", "mediumpurple3", "plum"), names=c("New York Times", "Boston Globe", "Washington Post"), main="Flesch Scores for Each Newspaper")

WPArtFlesch = c(44.891600101295154, 45.63042271335377, 45.06408424908429, 40.82797123623013, 31.867047522750283, 
                60.86585495701557, 50.94425407925411, 38.758395252838, 33.15309128025666, 41.969657408947285,
                42.33668564816506, 57.6761259338314)
WPEdFlesch =c(39.7529284369115, 40.16899156885438, 39.3021424829754, 45.86320312500001, 25.140715996805966, 
              37.59338267322744, 48.4234454734455, 29.214325699745558, 25.348675605340617, 18.792806347930906,
              47.939624329159216, 42.3256102540835)

NYTArtFlesch = c(36.05410234614078, 35.9335214785215, 36.72083333333336, 59.75238242647936, 28.200202794819376,
                 46.17216152945767, 40.71401062363151, 37.553146302034236, 61.25693181818184, 
                 55.568579785909876, 46.97833835275634, 56.90929844097997)
NYTEdFlesch = c(27.73693954659953, 52.711472805202504, 40.98621012658228, 42.95604269972455, 40.23683639633569, 
                35.480228375677996, 27.870275601766167, 39.04289308176104, 54.06586842105264, 34.59676790950988, 
                42.20628920863314,41.97984277799381)

BGArtFlesch = c(65.73733253364323, 31.17559511434513, 54.91958649719382, 75.05713724164168, 53.09729455709714, 
                28.3745271629779, 31.638799992482348, 63.218393586492795, 56.31988297793299, 54.0694970161978,
                28.170187908496757, 42.87420493341128)

BGEdFlesch = c(54.949984805984116, 43.431414603960434, 44.43590163934428, 34.44680962757528, 32.44274514200299,
               50.964908175069894, 60.882937710437744, 27.216678122863215, 57.77308139021375, 32.03633210332106, 
               47.57773494860501, 52.673898457684174)


averages = c(mean(WPArtFlesch), mean(WPEdFlesch), mean(NYTArtFlesch), mean(NYTEdFlesch), mean(BGArtFlesch), mean(BGEdFlesch))


hist(bothFlesch, main = "Histogram of Flesch Scores for All Articles and Editorials",  ylim=c(0, 0.035), xlab = "Flesch Scores", col="lightskyblue", border="gray", prob=TRUE)lines(density(bothFlesch), lty=1, lwd=1)




ybar = mean(bothFlesch)
s = sd(bothFlesch)

#this gives the two curves as desired

hist(bothFlesch, main = "Histogram of Flesch Scores for All Articles and Editorials", ylim=c(0, 0.035), xlab = "Flesch Scores", col="lightskyblue", border="gray", prob=TRUE)
lines(density(bothFlesch), lty=1, col="darkolivegreen4", lwd=2)
#The above plots a density curve on the histogram.

#Below, I plot a line along the histogram to see what a normal distribution would look like.
curve(dnorm(x, mean=ybar, sd=s), add=TRUE, col="hotpink", lwd=2)
legend("topright", legend=c("Normal Distribution", "Density"), col=c("hotpink", "darkolivegreen4"), lty=1, lwd=2, cex=1)
#The black line represents the distribution of our empirical data, and the red line represents what our
# Flesch scores would look like if they were normally distributed. Judging visually, we see that the two lines
# almost follow the same general pattern, although there are clear differences. So we can say that the 
#distribution of Flesch scores is not fully normal although it is close to it.

#Making a QQ PLOT:
qqnorm(bothFlesch, col="skyblue", pch=16, main="Normal Q-Q Plot of All Flesch Scores")
#The theoretical quantiles represented on the x-axis are the quantiles for normal distribution. 
#So the 0th quantile is where the mean is. As you can see the corresponding y-value for x=0 is a little above 
# 40, which is what our mean is (43). Because the distribution is normal, the standard deviation is 1, so 
#the quantiles are spaced one apart from each other.

#The dots represent the actual flesch scores for each of our 72 articles. We put a line going from the 
# second to the third quantiles of our data, which is what our sample points would look like if they were
# normally distributed. Visually, we can see that the line and our empirical data seem to be close, so 
# we can say that the distribution of Flesch scores for our articles are almost normally distributed.

qqline(bothFlesch, col="goldenrod", lty=1, lwd=2) 
#this is a line going from the second to the third quantiles of the data, 
#or how the dots would be positioned if it were a pure normal distribution.


#What I have so far for editorial and article histograms combined:
# hist(articleFlesch, xlim=c(20, 80), ylim=c(0,9), col=rgb(30,144,255,50, maxColorValue=255), main = "Histogram of Flesch Scores for Articles and Editorials", xlab="Flesch Scores")
# hist(editorialFlesch, add=T, xlim=c(20, 80), col=rgb(255,140,0,50, maxColorValue=255))
#legend("topright", c("Articles", "Editorials"), fill=c("lightblue", "orange"))

# This is to make two histograms--one for the articles, the other for editorials.
par(mfrow=c(2, 1))
hist(articleFlesch, xlim=c(15, 80), col="turquoise3", ylim=c(0,9), main = "Histogram of Flesch Scores for Articles", xlab="Flesch Scores")
abline(v=46.1, col = "sienna2", lty=2, angle=90)
#text(50,7,"avg = 46.1", col="sienna2")
legend("topright", legend="average (46.1)", col="sienna2", lty = 2, angle=45)


hist(editorialFlesch, xlim=c(15, 80), col="sienna2", ylim=c(0,9), main = "Histogram of Flesch Scores for Editorials", xlab="Flesch Scores")
abline(v=46.1, col = "turquoise4", lty=2)
legend("topright", legend="average (40.5)", lty=2, col = "turquoise4")
#text(40, 7, "average (40.5)", col="turquoise3")


#VOCABULARY RANGE / DIFFICULTY

#Order sorted: BG, NYT, WP
editorialsUnique = c(0.55, 0.62, 0.6, 0.57, 0.56, 0.52, 0.57, 0.57, 0.6, 0.55, 0.55, 0.64,
                     0.61, 0.57, 0.56, 0.59, 0.59, 0.58, 0.62, 0.6, 0.54, 0.53, 0.63, 0.53,
                     0.57, 0.59, 0.61, 0.6, 0.53, 0.6, 0.58, 0.57, 0.62, 0.61, 0.59, 0.62)


articlesUnique = c(0.56, 0.54, 0.56, 0.52, 0.65, 0.66, 0.57, 0.57, 0.51, 0.58, 0.55, 0.53,
                   0.51, 0.59, 0.46, 0.66, 0.49, 0.54, 0.54, 0.58, 0.55, 0.51, 0.6, 0.62, 
                   0.53, 0.54, 0.61, 0.58, 0.54, 0.48, 0.58, 0.55, 0.58, 0.58, 0.54, 0.55)
bothUnique = c(articlesUnique, editorialsUnique)

par(mfrow=c(1,1))
plot(bothFlesch, bothUnique, pch=16, col="deepskyblue3", xlab = "Flesch Scores", ylab = "% of Unique Words", main="Vocabulary Range and Flesch Scores")
#legend("topright", legend="Correlation Coeefficient = 0.019")
#CORRELATION COEFFICIENT
cor(bothUnique, bothFlesch)

#Instead of using percentage of unique words to measure vocabulary, I put all the articles through a tool to determine
# vocabulary difficulty.
#Order sorted: BG, NYT, WP (same order as for Flesch scores)
articlesRange3 = c(8,13,14,19,13,7,18,14,17,13,15,16,13,11,11,11,10,10,14,13,14,17,8,15,23,11,19,18,15,
                   22,15,16,17,19,17,11)

editorialsRange3 = c(15,12,6,9,7,10,11,12,13,19,11,11,14,13,10,10,9,10,11,8,8,9,11,9,18,13,10,12,19,
                     19,12,11,17,9,13,13)
bothRange3 = c(articlesRange3, editorialsRange3)

plot(bothFlesch, bothRange3, pch=16, col="deepskyblue3", xlab = "Flesch Scores", ylab = "% of Low-Frequency Words", main="Vocabulary Level and Flesch Scores")
legend("topright", legend="Correlation Coeefficient = 0.09")
cor(bothFlesch, bothRange3)
par(mfrow=c(1,1))
plot(bothRange3, bothUnique)
cor(bothRange3, bothUnique)


#Data obtained via main.py
sentenceLengths = c(21.58, 23.06, 22.5, 23.08, 20.31, 19.82)
test = c(4, 9, 16)
test2 = sqrt(test)
varSenLen = c(11.69, 16.27, 15.28, 8.66, 28.94, 11.98)
stdSenLen = sqrt(varSenLen)


#arrows(barCenters, means-standardErrors*2, barCenters, means+standardErrors*2, lwd=2, angle=90, code=3)
bar <- barplot(sentenceLengths, ylim=c(0,30), ylab="Average Sentence Length", xlab="Category", col=c("powderblue", "thistle1"), main="Average Sentence Lengths of Articles and Editorials", names=c("WP Articles", "WP Editorials", "NYT Articles", "NYT Editorials", "BG Articles", "BG Editorials"))
segments(bar, sentenceLengths-stdSenLen*2, bar, sentenceLengths+stdSenLen*2, lwd=1, lty=2)
legend("topright", legend="Standard Deviation", lty=2, lwd=2)

 