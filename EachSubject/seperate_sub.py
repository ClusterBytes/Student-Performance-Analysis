import pandas as pd

import sys

subject = sys.argv[1]
position = sys.argv[2]

data = pd.read_csv('/home/lince/ClusterBytes/Student-Performance-Analysis/core/dataset_v2.csv')

columns_to_keep = ["Reg_No", subject, "A" + position, "I" + position, "G" + position]

new_df = data[columns_to_keep]

new_df.to_csv(subject + ".csv", index=False)
print("extracted the subject " + subject)
