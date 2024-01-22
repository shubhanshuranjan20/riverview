import pandas as pd



# Use a raw string to avoid the 'unicodeescape' error

#df = pd.read_csv(r'C:\Users\shubh\OneDrive\Desktop\python\pokemon_data.csv')

#print(df.head(3)) #print first 3

#print(df.tail(3)) 

# df_xls=pd.read_excel(r'C:\Users\shubh\OneDrive\Desktop\python\pokemon_data.xlsx')

# print(df_xls)

df = pd.read_excel(r'C:\Users\shubh\OneDrive\Desktop\python\pokemon_data.xlsx')



#print(df.head(5))
# print(df.columns)

# print(df['Name'])
# print(df['Name'][0:5])

# print(df.Name[0:5])

# print(df[['Name','Type 1','Type 2']])

#Read each row

# print(df.iloc[0:4])

# for index,row in df.iterrows():
#     print(index,row['Name'])

#print specific position

# print(df.iloc[2,1])

# print(df.columns)

# df=df.loc[df['Type 1'] == "Fire"]

#print(df.describe()) #return cnt,mean,std,max,25%,50% etc

# print(df.sort_values('Name'))
# print(df.sort_values('Name',ascending=False))

#print(df.sort_values(['Type 1','HP']))

#print(df.sort_values(['Type 1','HP'],ascending=False))
# print(df.sort_values(['Type 1','HP'],ascending=[1,0]))

# df['Total']=df['HP']+df['Attack']  #add columns and drop columns


# df=df.drop(columns='Total')
# print(df.head(5))

df['Total']=df.iloc[:,4:10].sum(axis=1) 
print(df)



