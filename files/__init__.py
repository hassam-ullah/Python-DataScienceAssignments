import collections
import csv
import random

def cloneDataSet():
     ind=0
     with open('toy_dataset.csv') as csvFile:
          csvReader= csv.reader(csvFile, delimiter=',')

          with open('new_toy_dataset.csv','w',newline='') as new_csv_file:
               csvWriter=csv.writer(new_csv_file)

               for line in csvReader:
                    if ind==0:
                         ind+=1
                         continue
                    csvWriter.writerow(line)
toy_list= []
def convertToList():

     f=open("new_toy_dataset.csv",'r')
     reader=csv.reader(f)

     for row in reader:
          toy_list.append([int(row[0]),row[1],row[2],int(row[3]),int(row[4]),row[5]])

five_list=[]
def fiveList():
     ind=0
     for row in toy_list:
          if ind<500:
               five_list.append(random.choice(toy_list))
               ind+=1
     print(ind)
     print(five_list)
     f=open("randomRecords.csv",'w',newline='')
     writer=csv.writer(f)
     for row in five_list:
          writer.writerow(row)

def avg_newYork():
     x=0
     sum=0
     for row in toy_list:
          if row[1] == "New York City":
               sum=sum+row[4]
               x+=1
     print("Total Records Read : ")
     print(x)
     print("Average Income of New Yorkers : ",)
     print(sum/x)

newList=[]

def list_maker():
     count=0
     for row in toy_list:
          if(row[1]=="New York City"):
               newList.append(row[4])
               count+=1
     newList.sort()

     for row in newList:
          print(row)
     print(count)

def median():

     print("Total Records Read : ")
     print(len(newList))
     print("Number of Records")
     if len(newList)%2==0:
          print("Even")
          print("So the median is the middle-most value i.e")
     else:
          print ("odd")

     median=int((int(len(newList))+1)/2)
     print("Median = ",median,"th value")
     print("So Median is = ",newList[median])

def moder():
     data=collections.Counter(newList)
     data_list=dict(data)
     print(data_list)
     print(len(data_list))
     max_value = max(list(data.values()))
     mode_val = [num for num, freq in data_list.items() if freq == max_value]
     if len(mode_val) == len(newList):
          print("No mode in the list")
     else:
          print("The Mode of the list is : " + ', '.join(map(str, mode_val)))

def annualIncome():
     print("Annual Incomes of each Person : ")
     for i in newList:

          print(i*12)


cloneDataSet()
convertToList()
avg_newYork()
list_maker()
median()
moder()
annualIncome()
fiveList()
