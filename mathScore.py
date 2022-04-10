import random
import statistics
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("StudentsPerformance.csv")
mathScore = df["math score"].tolist()

mean = sum(mathScore)/len(mathScore)
median = statistics.median(mathScore)
mode = statistics.mode(mathScore)
std_dev = statistics.stdev(mathScore)
print("mean of the data is: ", mean)
print("median of the data is: ", median)
print("mode of the data is: ", mode)
print("standard deviation of the data is", std_dev)

firstStdDevStart = mean-std_dev
firstStdDevEnd = mean+std_dev
secondStdDevStart = mean-(2*std_dev)
secondStdDevEnd = mean+(2*std_dev)
thirdStdDevStart = mean-(3*std_dev)
thirdStdDevEnd = mean+(3*std_dev)

list_of_data_within_first_std_dev = [result for result in mathScore if result>firstStdDevStart and result<firstStdDevEnd]
print("{}% of data lying between 1st std dev is".format(len(list_of_data_within_first_std_dev)*100/len(mathScore)))
list_of_data_within_second_std_dev = [result for result in mathScore if result>secondStdDevStart and result<secondStdDevEnd]
print("{}% of data lying between 2nd std dev is".format(len(list_of_data_within_second_std_dev)*100/len(mathScore)))
list_of_data_within_third_std_dev = [result for result in mathScore if result>thirdStdDevStart and result<thirdStdDevEnd]
print("{}% of data lying between 3rd std dev is".format(len(list_of_data_within_third_std_dev)*100/len(mathScore)))



