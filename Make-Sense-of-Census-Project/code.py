# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

data=np.genfromtxt(path, delimiter=",", skip_header=1)
print("\nData: \n\n", data)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census=np.concatenate((new_record,data),axis =0)
print(census)
#Code starts here



# --------------
#Code starts here
age=census[:,0]
print(age)
max_age=age.max()
print(max_age)
min_age=age.min()
print(min_age)
age_mean=age.mean()
print(age_mean)
age_std=age.std()
print(age_std)


# --------------
#Code starts here

#Creating new subsets based on 'Age'
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]


#Finding the length of the above created subsets
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

#Printing the length of the above created subsets
print('Race_0: ', len_0)
print('Race_1: ', len_1)
print('Race_2: ', len_2)
print('Race_3: ', len_3)
print('Race_4: ', len_4)

#Storing the different race lengths with appropriate indexes
race_list=[len_0, len_1,len_2, len_3, len_4]
print(race_list)

#Storing the race with minimum length into a variable 
minority_race=race_list.index(min(race_list))

#Code ends here





# --------------
#Code starts here

#Create a new subset array called 'senior_citizens'

senior_citizens=census[census[:,0] >60]
#print(senior_citizens)

#Add all the working hours

working_hours_sum=senior_citizens.sum(axis=0)[6]
#print(working_hours_sum)

#the length of 'senior_citizens'

senior_citizens_len=len(senior_citizens)
print(senior_citizens_len)

#the average working hours of the senior citizens
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)



# --------------
#Code starts here
high=census[census[:,1]>10]

low=census[census[:,1]<=10]
avg_pay_high=high[:,7].mean()
print(avg_pay_high)
avg_pay_low=low[:,7].mean()
print(avg_pay_low)


