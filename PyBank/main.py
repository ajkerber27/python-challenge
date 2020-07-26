#import dependencies
import csv
import os
#import csv file
Budget_Data_File = os.path.join("Resources","02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

#define variables
total_months = 0
net_change_list=[]
greatest_increase=["",0]
greatest_decrease=["",99999999]
total_net=0 
with open (Budget_Data_File) as Budget_Data:
    reader= csv.reader(Budget_Data)
    header= next(reader)
    print(header)

    #extract header
    First_Row=next(reader)
    total_months=1
    total_net=int(First_Row[1])
    previous_net=int(First_Row[1])

    #forloop
    for row in reader:
        #tracking the total
        total_months=total_months+1
        total_net=total_net+int(row[1])
        #tracking the net change
        net_change=int(row[1])-previous_net
        previous_net=int(row[1])
        net_change_list=net_change_list+[net_change]

        #track increases and decreases
        if net_change > greatest_increase[1]:
            greatest_increase[0]=row[0]
            greatest_increase[1]=net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0]=row[0]
            greatest_decrease[1]=net_change

#calculate average net change
average_net_change=sum(net_change_list)/len(net_change_list)

#output of data
output=(
    f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${total_net}\n"
f"Average  Change: ${average_net_change}\n"
f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

print(output)

with open ("Output.txt","w") as textfile: 
    textfile.write(output)


