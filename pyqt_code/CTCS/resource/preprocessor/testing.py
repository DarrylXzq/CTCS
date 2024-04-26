import pickle

import pandas as pd
from sklearn import preprocessing
from sklearn.decomposition import PCA
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# =====================Load data=====================
# 加载数据
file_path_train = r"D:\Download\zyFile\Cyberthreat_Cognitive_System\CTCS_Code\attack_datasets\NSL-KDD\KDDTrain+.txt"
file_path_test = r"D:\Download\zyFile\Cyberthreat_Cognitive_System\CTCS_Code\attack_datasets\NSL-KDD\KDDTest+.txt"
# 定义列名
data_columns = ["duration", "protocol_type", "service", "flag", "src_bytes",
                "dst_bytes", "land", "wrong_fragment", "urgent", "hot", "num_failed_logins",
                "logged_in", "num_compromised", "root_shell", "su_attempted", "num_root",
                "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",
                "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate",
                "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",
                "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
                "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
                "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",
                "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label", "difficulty"]
# 加载数据
train_data = pd.read_csv(file_path_train, header=None, names=data_columns)
test_data = pd.read_csv(file_path_test, header=None, names=data_columns)

attack_mapping = {}
with open(r'D:\Download\zyFile\Cyberthreat_Cognitive_System\CTCS_Code\attack_datasets\NSL-KDD\attack_name',
          'r') as file:
    for line in file:
        parts = line.strip().split(' ')
        if len(parts) == 2:
            attack, category = parts
            attack_mapping[attack] = category
# 然后像之前那样使用这个映射字典
train_data['label'] = train_data['label'].map(attack_mapping)
test_data['label'] = test_data['label'].map(attack_mapping)

# 合并数据集
combined_data = pd.concat([train_data, test_data], axis=0)

# 检查每列是否是常数
constant_columns = [col for col in combined_data.columns if combined_data[col].nunique() == 1]
# 打印常数特征列的名称
print("Constant columns:", constant_columns)

# 删除常数列和无用列
combined_data.drop(['difficulty'], axis=1, inplace=True)
combined_data.drop(['num_outbound_cmds'], axis=1, inplace=True)

# selecting numeric attributes columns from data
numeric_col = combined_data.select_dtypes(include='number').columns
# 使用这些列名来创建一个新的数据帧，只包含数值类型的列
numeric_data = combined_data[numeric_col]
# 显示新数据帧以验证结果
numeric_data.head()

# ======================One-Hot Encoding=====================
# cf = ['protocol_type', 'service', 'flag']
# categorical = combined_data[cf]
# # one-hot-encoding categorical attributes using pandas.get_dummies() function
# categorical = pd.get_dummies(categorical, columns=cf)
# categorical = categorical.astype(int)
#
# # 保存列名到文件
# categorical.columns.to_series().to_csv(r'./resource/preprocessor/one_hot_encoded_columns.csv', index=False)
#
# # 创建一个包含 combined-data 标签的 DataFrame
# label = pd.DataFrame(combined_data['label'])
# # 定义您想要的标签顺序
# order = {'normal': 0, 'dos': 1, 'probe': 2, 'r2l': 3, 'u2r': 4}
# # 使用 map 函数根据指定顺序将标签转换为整数
# enc_label = label['label'].map(order)
#
# # 将 categorical 数据帧加入到 numeric_data 中
# mix_data = pd.concat([numeric_data, categorical, enc_label], axis=1)
#
# std_scaler = StandardScaler()
# # 假设 mix_data 是你的数据集
# cols = mix_data.iloc[:, :-1].columns  # 选择除最后一列之外的所有列
#
# # 对所选列进行标准化处理
# for col in cols:
#     mix_data[col] = std_scaler.fit_transform(mix_data[[col]])
#
# print(mix_data.head())
# # 保存 StandardScaler 对象
# with open(r'./resource/preprocessor/one_hot_std_scaler.pkl', 'wb') as f:
#     pickle.dump(std_scaler, f)

# =================label========================
from sklearn.preprocessing import LabelEncoder

# 定义字符字段
cf = ['protocol_type', 'service', 'flag']
categorical = combined_data[cf]
# 使用LabelEncoder进行编码
# 创建一个字典来存储每个列的LabelEncoder对象，并进行编码

encoders = {}
for column in cf:
    le = LabelEncoder()
    categorical[column] = le.fit_transform(categorical[column])
    encoders[column] = le  # 保存编码器

# 保存编码器到磁盘
# with open(r'./resource/preprocessor/label_encoders.pkl', 'wb') as f:
#     pickle.dump(encoders, f)

# 创建一个包含 combined-data 标签的 DataFrame
label = pd.DataFrame(combined_data['label'])
# 定义您想要的标签顺序
order = {'normal': 0, 'dos': 1, 'probe': 2, 'r2l': 3, 'u2r': 4}
# 使用 map 函数根据指定顺序将标签转换为整数
enc_label = label['label'].map(order)

# 将 categorical 数据帧加入到 numeric_data 中
mix_data = pd.concat([numeric_data, categorical, enc_label], axis=1)
mix_data.drop(['label'], axis=1, inplace=True)
print(mix_data.head())
cols = mix_data.columns
# mix_data.to_csv(r'1.csv', index=False)
std_scaler = StandardScaler()
# 假设 mix_data 是你的数据集
# cols = mix_data.iloc[:, :-1].columns  # 选择除最后一列之外的所有列
# new_X = mix_data.iloc[:, :-1]

# 对所选列进行标准化处理
for col in cols:
    print(col)
    mix_data[col] = std_scaler.fit_transform(mix_data[[col]])  # 注意：这里使用 [[col]] 以保持 DataFrame 格式
print(mix_data.columns)
print(mix_data.head())
# 保存 StandardScaler 对象
with open(r'label_std_scaler.pkl', 'wb') as f:
    pickle.dump(std_scaler, f)
# #

# ===============one-hot apply================
# import pandas as pd
#
# # 加载新数据集
# new_data = pd.read_csv('path_to_new_data.csv')
# new_categorical = pd.get_dummies(new_data[cf], columns=cf)
# new_categorical = new_categorical.astype(int)
#
# # 加载保存的列名
# encoded_columns = pd.read_csv('one_hot_encoded_columns.csv', squeeze=True)
#
# # 确保新数据集有相同的列，缺少的用0填充
# new_categorical = new_categorical.reindex(columns=encoded_columns, fill_value=0)
#
# # 查看新的数据帧
# new_categorical.head()
# ===============label apply================
# import pandas as pd
# import pickle
#
# # 加载保存的编码器
# with open('encoders.pkl', 'rb') as f:
#     loaded_encoders = pickle.load(f)
#
# # 加载新数据
# new_data = pd.read_csv('path_to_new_data.csv')
#
# # 应用保存的编码器来转换新数据
# for column in cf:
#     # 先检查新数据中的类别是否存在于原编码器中
#     known_labels = set(loaded_encoders[column].classes_)
#     new_data[column] = new_data[column].apply(lambda x: x if x in known_labels else 'Unknown')
#
#     # 转换新数据
#     new_data[column] = loaded_encoders[column].transform(new_data[column])
#
# # 保存或进一步处理新的编码后的数据
# new_data.to_csv('new_encoded_data.csv', index=False)

# ===================stand scaler===================
# import pandas as pd
# import pickle
#
# # 加载保存的 StandardScaler
# with open('std_scaler.pkl', 'rb') as f:
#     loaded_scaler = pickle.load(f)
#
# # 加载新数据
# new_data = pd.read_csv('path_to_new_data.csv')
#
# # 应用保存的 StandardScaler 来标准化新数据
# cols = new_data.iloc[:, :-1].columns  # 假设新数据有相同的结构
# for col in cols:
#     new_data[col] = loaded_scaler.transform(new_data[[col]])
#
# # 显示或保存标准化后的新数据
# new_data.head()


# # ===================label-PCA===================
# # 加载保存的PCA模型
# with open('pca_model.pkl', 'rb') as file:
#     pca_loaded = pickle.load(file)
#
# # ===================label-LDA====================
# import pickle
#
# # 加载保存的LDA模型
# with open('lda_model.pkl', 'rb') as file:
#     lda_loaded = pickle.load(file)
#
# # 假设new_X是新的特征数据，new_y是对应的标签，确保先进行相同的预处理
# # 应用LDA转换
# new_X_lda = lda_loaded.transform(new_X)
#
# # ===================label-pearson===================
# Label_Encoding_Pearson = ['logged_in', 'same_srv_rate', 'dst_host_srv_count', 'dst_host_same_srv_rate',
#                           'dst_host_diff_srv_rate', 'flag', 'label']
#
# # ===================label mutual information===================
# Label_Encoding_MI = ['srv_rerror_rate', 'protocol_type', 'duration', 'dst_host_srv_rerror_rate', 'rerror_rate',
#                      'dst_host_rerror_rate', 'srv_diff_host_rate', 'srv_count', 'dst_host_count',
#                      'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'logged_in', 'srv_serror_rate',
#                      'dst_host_srv_serror_rate', 'serror_rate', 'dst_host_serror_rate', 'dst_host_same_srv_rate',
#                      'dst_host_srv_count', 'count', 'dst_host_diff_srv_rate', 'same_srv_rate', 'flag', 'diff_srv_rate',
#                      'dst_bytes', 'service', 'src_bytes', 'label']
#
# # ===================One-Hot-PCA===================
# # 加载保存的PCA模型
# with open('pca_model.pkl', 'rb') as file:
#     pca_loaded = pickle.load(file)
#
# # 假设new_X是新数据，需要先进行相同的预处理（例如，标准化）
# # 应用PCA转换
# new_X_pca = pca_loaded.transform(new_X)
# # ===================One-Hot-LDA===================
# import pickle
#
# # 加载保存的LDA模型
# with open('lda_model.pkl', 'rb') as file:
#     lda_loaded = pickle.load(file)
#
# # 假设new_X是新的特征数据，new_y是对应的标签，确保先进行相同的预处理
# # 应用LDA转换
# new_X_lda = lda_loaded.transform(new_X)
# # ===================One-Hot-Pearson===================
# One_Hot_Pearson = ['logged_in', 'same_srv_rate', 'dst_host_srv_count', 'dst_host_same_srv_rate',
#                    'dst_host_diff_srv_rate', 'service_http', 'service_private', 'flag_SF', 'label']
#
# # ===================One-Hot-MI===================
# One_Hot_MI = ['service_eco_i', 'srv_rerror_rate', 'duration', 'dst_host_srv_rerror_rate', 'rerror_rate',
#               'service_private', 'dst_host_rerror_rate', 'srv_diff_host_rate', 'srv_count', 'dst_host_count',
#               'service_http', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'logged_in',
#               'srv_serror_rate', 'flag_S0', 'dst_host_srv_serror_rate', 'serror_rate', 'dst_host_serror_rate',
#               'flag_SF', 'dst_host_same_srv_rate', 'dst_host_srv_count', 'count', 'dst_host_diff_srv_rate',
#               'same_srv_rate', 'diff_srv_rate', 'dst_bytes', 'src_bytes', 'label']
