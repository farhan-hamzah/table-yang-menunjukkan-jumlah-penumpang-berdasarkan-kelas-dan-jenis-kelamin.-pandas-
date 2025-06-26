import pandas as pd
data = pd.read_csv('kapal_titanic.csv')
pivot_result = pd.pivot_table(
    data,
    index='pclass',
    columns='sex',
    values='survived',    
    aggfunc='count',     
    fill_value=0         
)
print(pivot_result)