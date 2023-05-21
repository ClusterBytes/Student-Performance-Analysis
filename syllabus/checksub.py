from sub_slots import sub_slot

# print(sub_slot)

count=0

for i,val in sub_slot.items():
    # print(val)
    for keys in val:
        count+=1
# print(count)

import pandas as pd
import numpy as np
# Assuming your DataFrame is named 'df'
start_row = 2
end_row = 6
df=pd.read_csv("slot_wise.csv")
non_empty_values_count = df.iloc[start_row:end_row + 1].count().sum()
print(non_empty_values_count)
non_empty_values = df.iloc[start_row:end_row + 1].values.flatten()
non_empty_values = non_empty_values[pd.notna(non_empty_values)]
print(non_empty_values)

arr=['MA101','PH100','BE100','BE10101','BE103','CE100','PH110','CE110','MA102'
 'BE102','CS100','CS120','MAT101','PHT100','EST100','EST120','HUN101'
 'PHL120','ESL120','MAT102','HUN102','EST102','CY100','BE110','BE10102'
 'EC100','CY110','EC110','PHT110','EST110','EST130','CYL120','ESL130'
 'BE10103','EE100','EE110','CYT100','BE10104','ME100','ME110','BE10105'
 'CS110']

print(len(arr))