import numpy as np
import pandas as pd

Faa_data = pd.read_csv(r'C:\Users\hpups\Downloads\1574406018_lesson71\Lesson 7 -1\faa_ai_prelim\faa_ai_prelim\faa_ai_prelim.csv')
print(Faa_data.head(5))

#replacing fatalflag NaN data with "No"
Faa_data['FATAL_FLAG'].fillna('No',inplace=True)
print(Faa_data.shape)

#dropping all aircraft names with No Name
Faa_final = Faa_data.dropna(subset = ['ACFT_MAKE_NAME'])

print(Faa_final.shape)

#getting the number of aircraft types and their occurances
aircraft_type = Faa_final.groupby('ACFT_MAKE_NAME')
print(aircraft_type.size())

#grouping the fatalflag
fatal_flag_group = Faa_final.groupby('FATAL_FLAG')
print(fatal_flag_group.size())

#just seeing the accidents which were Fatal
accidents_fatal = fatal_flag_group.get_group('Yes')

#final Data with accidents with Fatality
accidents_fatal