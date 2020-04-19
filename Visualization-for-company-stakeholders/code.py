# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Code starts here
# Load the dataframe using pd.read_csv() and store the dataframe in a variable called data
data=pd.read_csv(path)
#Save the value counts of Loan_Status in a variable called loan_status using value_counts()
loan_status=data['Loan_Status'].value_counts()
#Plot a bar graph of loan_status
loan_status.plot(kind='bar')
#Display a plot
plt.show()


# --------------
#Code starts here
#Group by 'data' dataframe
property_and_loan=data.groupby(['Property_Area',"Loan_Status"])
#Use the .size() method on 'property_and_loan' and then use .unstack() and save it back to 'property_and_loan
property_and_loan=property_and_loan.size().unstack()
#Draw a stacked plot
property_and_loan.plot(kind="bar",stacked=False)
#Name the x-axis as Property Area
plt.xlabel('Property Area')
#Name the y-axis as Loan Status
plt.ylabel('Loan Status')
#Rotate the labels of x-axis by 45o
plt.xticks(rotation=45)

#Display plot
plt.show()





# --------------
#Code starts here
#Creation of dataframe Education
education_and_loan=data.groupby(['Education','Loan_Status'])

education_and_loan=education_and_loan.size().unstack()

#Plot an stacked bar plot of education_and_loan
education_and_loan.plot(kind='bar',stacked=False)
#Name the x-axis as Education Status
plt.xlabel('Education Status')
#Name the y-axis as Loan Status
plt.ylabel('Loan Status')

#Rotate the labels of x-axis by 45o
plt.xticks(rotation=45)
#Display plot
plt.show()



# --------------
#Code starts here

graduate=data[data['Education'] == 'Graduate']

not_graduate=data[data['Education'] =='Not Graduate']

graduate['LoanAmount'].plot(kind='density', label='Graduate')

#Code ends here

#For automatic legend display
plt.legend()
plt.show()


# --------------
#Code starts here
#Create three subplots with (nrows = 3 , ncols = 1) and store it in variable's fig ,(ax_1,ax_2,ax_3)
fig,(ax_1,ax_2,ax_3)=plt.subplots(nrows=3,ncols=1,figsize=(10,10))
#Since both are continuous variables, plot scatter plot between 'ApplicantIncome' and LoanAmount using ax_1. Set axis title as Applicant Incom
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])
plt.title("ApplicantIncome")
#Plot scatter plot between 'CoapplicantIncome' and LoanAmount using ax_2. Set axis title as Coapplicant Income
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])
plt.title("CoapplicantIncome")
#Create a new column in the dataframe called 'TotalIncome' which is a sum of the values of columns ApplicantIncome and CoapplicantIncome
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
#Plot scatter plot between 'TotalIncome' and LoanAmount using ax_3. Set axis title as Total Income
ax_3.scatter(data['TotalIncome'],data['LoanAmount'])
plt.title("TotalIncome")



