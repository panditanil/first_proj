import pandas as pd

data = {
    'Name' : ['Ram','Shyam','Sita', 'Dhiraj'],
    'Age' : [25,30,23,22],
    'City' : ['BRj', 'KTM','Gaur','JKP']
}

df = pd.DataFrame(data)

print(df)