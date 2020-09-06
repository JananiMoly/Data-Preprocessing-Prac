import pandas as pd

FDNY = pd.read_csv(r'C:\Users\hpups\Downloads\1574406430_lesson72\Lesson 7 -2\FDNY\FDNY\FDNY.csv')
FDNY.head()

#Removing the first row
FDNY=pd.read_csv(r'C:\Users\hpups\Downloads\1574406430_lesson72\Lesson 7 -2\FDNY\FDNY\FDNY.csv',skiprows=1)

print(FDNY.shape)

FDNY.columns

FDNY['FacilityName'].duplicated()

FDNY['FacilityName'].drop_duplicates()

print(FDNY.shape)

Total_facilities = FDNY.groupby('FacilityName')
print(sum(Total_facilities.size()))

Total_borough = FDNY.groupby('Borough')
print(Total_borough.size())

Facility_names_in_manhattan = Total_borough.get_group('Manhattan')
Facility_names_in_manhattan