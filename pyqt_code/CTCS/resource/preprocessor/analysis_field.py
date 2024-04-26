import pandas as pd

# 读取文件
df1 = pd.read_csv('KDDTest+.csv')
df2 = pd.read_csv('KDDTrain+.csv')
df3 = pd.read_csv('KDDTest-21.csv')
df4 = pd.read_csv('KDDTrain+_20Percent.csv')

# 定义列名，匹配您的数据结构描述
column_names = [
    'Duration', 'Protocol Type', 'Service', 'Flag', 'Src Bytes', 'Dst Bytes', 'Land',
    'Wrong Fragment', 'Urgent', 'Hot', 'Num Failed Logins', 'Logged In', 'Num Compromised',
    'Root Shell', 'Su Attempted', 'Num Root', 'Num File Creations', 'Num Shells',
    'Num Access Files', 'Num Outbound Cmds', 'Is Hot Logins', 'Is Guest Login', 'Count',
    'Srv Count', 'Serror Rate', 'Srv Serror Rate', 'Rerror Rate', 'Srv Rerror Rate',
    'Same Srv Rate', 'Diff Srv Rate', 'Srv Diff Host Rate', 'Dst Host Count', 'Dst Host Srv Count',
    'Dst Host Same Srv Rate', 'Dst Host Diff Srv Rate', 'Dst Host Same Src Port Rate',
    'Dst Host Srv Diff Host Rate', 'Dst Host Serror Rate', 'Dst Host Srv Serror Rate',
    'Dst Host Rerror Rate', 'Dst Host Srv Rerror Rate'
]

# 读取文件并指定没有头部（header=None），且指定列名
df1 = pd.read_csv('KDDTrain+.csv', header=None, names=column_names)
df2 = pd.read_csv('KDDTest+.csv', header=None, names=column_names)
df3 = pd.read_csv('KDDTest-21.csv', header=None, names=column_names)
df4 = pd.read_csv('KDDTrain+_20Percent.csv', header=None, names=column_names)

# 合并文件
df_combined = pd.concat([df1, df2, df3, df4], ignore_index=True)

# 定义每列的类型
# 定义每列的数据类型
column_details = {
    'Duration': 'Continuous',
    'Protocol Type': 'Categorical',
    'Service': 'Categorical',
    'Flag': 'Categorical',
    'Src Bytes': 'Continuous',
    'Dst Bytes': 'Continuous',
    'Land': 'Binary',
    'Wrong Fragment': 'Discrete',
    'Urgent': 'Discrete',
    'Hot': 'Continuous',
    'Num Failed Logins': 'Continuous',
    'Logged In': 'Binary',
    'Num Compromised': 'Continuous',
    'Root Shell': 'Binary',
    'Su Attempted': 'Discrete',
    'Num Root': 'Continuous',
    'Num File Creations': 'Continuous',
    'Num Shells': 'Continuous',
    'Num Access Files': 'Continuous',
    'Num Outbound Cmds': 'Continuous',
    'Is Hot Logins': 'Binary',
    'Is Guest Login': 'Binary',
    'Count': 'Discrete',
    'Srv Count': 'Discrete',
    'Serror Rate': 'Discrete',
    'Srv Serror Rate': 'Discrete',
    'Rerror Rate': 'Discrete',
    'Srv Rerror Rate': 'Discrete',
    'Same Srv Rate': 'Discrete',
    'Diff Srv Rate': 'Discrete',
    'Srv Diff Host Rate': 'Discrete',
    'Dst Host Count': 'Discrete',
    'Dst Host Srv Count': 'Discrete',
    'Dst Host Same Srv Rate': 'Discrete',
    'Dst Host Diff Srv Rate': 'Discrete',
    'Dst Host Same Src Port Rate': 'Discrete',
    'Dst Host Srv Diff Host Rate': 'Discrete',
    'Dst Host Serror Rate': 'Discrete',
    'Dst Host Srv Serror Rate': 'Discrete',
    'Dst Host Rerror Rate': 'Discrete',
    'Dst Host Srv Rerror Rate': 'Discrete'
}


# 创建一个空的字典来存储统计信息
statistics = {}

# 根据数据类型收集统计信息
for col, col_type in column_details.items():
    if col_type == 'Continuous':
        statistics[col] = {'min': df_combined[col].min(), 'max': df_combined[col].max()}
    elif col_type == 'Categorical' or col_type == 'Binary':
        statistics[col] = df_combined[col].value_counts().to_dict()
    elif col_type == 'Discrete':
        if df_combined[col].dtype == float:
            statistics[col] = {'min': df_combined[col].min(), 'max': df_combined[col].max()}
        else:
            statistics[col] = df_combined[col].value_counts().to_dict()

# 按照原始列的顺序输出统计结果
for col in column_details.keys():
    stats = statistics.get(col, {})
    print(f'{col}: {stats}')
