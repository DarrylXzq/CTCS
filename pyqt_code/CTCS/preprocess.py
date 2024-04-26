import pickle

import pandas as pd
from sklearn import preprocessing
from sklearn.decomposition import PCA, IncrementalPCA
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import warnings


def common_preprocess(data):
    print("Applying common_preprocess")
    data_columns = ["duration", "protocol_type", "service", "flag", "src_bytes",
                    "dst_bytes", "land", "wrong_fragment", "urgent", "hot", "num_failed_logins",
                    "logged_in", "num_compromised", "root_shell", "su_attempted", "num_root",
                    "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",
                    "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate",
                    "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",
                    "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
                    "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
                    "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",
                    "dst_host_rerror_rate", "dst_host_srv_rerror_rate"]
    # 加载数据
    detect_data = pd.read_csv(data, header=None, names=data_columns)
    # 删除常数列和无用列
    detect_data.drop(['num_outbound_cmds'], axis=1, inplace=True)
    return detect_data


def label_encoding(data):
    print("Applying label_encoding")
    # selecting numeric attributes columns from data
    numeric_col = data.select_dtypes(include='number').columns
    # 使用这些列名来创建一个新的数据帧，只包含数值类型的列
    numeric_data = data[numeric_col]
    # 加载保存的编码器
    with open('./resource/preprocessor/label_encoders.pkl', 'rb') as f:
        loaded_encoders = pickle.load(f)

    cf = ['protocol_type', 'service', 'flag']
    categorical = data[cf]

    # 应用保存的编码器来转换新数据
    for column in cf:
        # 先检查新数据中的类别是否存在于原编码器中
        # known_labels = set(loaded_encoders[column].classes_)
        # new_data[column] = new_data[column].apply(lambda x: x if x in known_labels else 'Unknown')
        # 只忽略特定类型的警告
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            categorical[column] = loaded_encoders[column].transform(categorical[column])
    mix_data = pd.concat([numeric_data, categorical], axis=1)
    return mix_data


def label_std_scaler(data):
    print("Applying label_std_scaler")
    # 加载保存的标准化模型
    std_scaler = StandardScaler()
    # with open('./resource/preprocessor/label_std_scaler.pkl', 'rb') as file:
    #     scaler_loaded = pickle.load(file)
    try:
        cols = data.columns
        # 对所选列进行标准化处理
        for col in cols:
            data[col] = std_scaler.fit_transform(data[[col]])
    except Exception as e:
        print("Error during scaling:", e)
        return None
    return data


def label_pearson(data):
    print("Applying label_pearson")
    # 实现第二步预处理逻辑
    label_encoding_pearson = data[['logged_in', 'same_srv_rate', 'dst_host_srv_count', 'dst_host_same_srv_rate',
                                   'dst_host_diff_srv_rate', 'flag']]
    return label_encoding_pearson


def label_mi(data):
    print("Applying label_mi")
    # 实现第三步预处理逻辑
    label_encoding_mi = data[['srv_rerror_rate', 'protocol_type', 'duration', 'dst_host_srv_rerror_rate', 'rerror_rate',
                              'dst_host_rerror_rate', 'srv_diff_host_rate', 'srv_count', 'dst_host_count',
                              'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'logged_in',
                              'srv_serror_rate',
                              'dst_host_srv_serror_rate', 'serror_rate', 'dst_host_serror_rate',
                              'dst_host_same_srv_rate',
                              'dst_host_srv_count', 'count', 'dst_host_diff_srv_rate', 'same_srv_rate', 'flag',
                              'diff_srv_rate',
                              'dst_bytes', 'service', 'src_bytes']]
    return label_encoding_mi


def label_pca(data):
    print("Applying label_pca")
    # 假设n_components是你确定的组件数
    batch_size = 10
    n_components = 21
    n_batches = (len(data) + batch_size - 1) // batch_size  # 计算需要的批次数量
    pca = IncrementalPCA(n_components=n_components)

    # 分批次处理数据
    for i in range(n_batches):
        start = i * batch_size
        end = start + batch_size
        batch = data[start:end]
        pca.partial_fit(batch)  # 使用当前批次数据更新 PCA 模型

    # 在所有数据上应用 PCA 变换
    X_pca = pca.transform(data)
    return X_pca


def label_lda(data):
    print("Applying label_lda")
    # 加载保存的PCA模型
    with open('./resource/preprocessor/label_lda_model.pkl', 'rb') as file:
        lda_loaded = pickle.load(file)
    # 假设new_X是新的特征数据，new_y是对应的标签，确保先进行相同的预处理
    # 应用LDA转换
    new_X_lda = lda_loaded.transform(data)
    return new_X_lda


def load_and_transform(filename):
    # 读取 CSV 文件，将第一行作为列名
    df = pd.read_csv(filename, header=0)
    # 转置 DataFrame
    df = df.T
    # 设置新的列名：取第一行作为列名
    new_header = df.iloc[0]
    df = df[1:]  # 去掉原来的第一行
    df.columns = new_header  # 设置新列名
    return df


def one_hot_encoding(data):
    print("Applying one_hot_encoding")
    # 选择数据中的数值类型列
    numeric_col = data.select_dtypes(include='number').columns
    # 使用这些列名来创建一个新的数据帧，只包含数值类型的列
    numeric_data = data[numeric_col]

    # 读取并转换 CSV 文件
    template_df = load_and_transform("./resource/preprocessor/one_hot_encoded_columns.csv")
    all_possible_columns = template_df.columns.tolist()

    # 定义分类属性
    cf = ['protocol_type', 'service', 'flag']
    categorical = data[cf]
    # 使用pandas.get_dummies()函数进行one-hot编码
    categorical = pd.get_dummies(categorical, columns=cf)
    categorical = categorical.astype(int)

    # 确保新数据集有相同的列，缺少的用0填充
    new_categorical = categorical.reindex(columns=all_possible_columns, fill_value=0)
    # 将数值数据与分类数据合并
    mix_data = pd.concat([numeric_data, new_categorical], axis=1)
    return mix_data


def one_hot_std_scaler(data):
    print("Applying one_hot_std_scaler")
    # 加载保存的标准化模型
    std_scaler = StandardScaler()
    # with open('./resource/preprocessor/one_hot_std_scaler.pkl', 'rb') as file:
    #     scaler_loaded = pickle.load(file)
    try:
        cols = data.columns
        # 对所选列进行标准化处理
        for col in cols:
            data[col] = std_scaler.fit_transform(data[[col]])
    except Exception as e:
        print("Error during scaling:", e)
        return None
    return data


def one_hot_pearson(data):
    print("Applying one_hot_pearson")
    one_hot_pearson = data[['logged_in', 'same_srv_rate', 'dst_host_srv_count', 'dst_host_same_srv_rate',
                            'dst_host_diff_srv_rate', 'service_http', 'service_private', 'flag_SF']]
    return one_hot_pearson


def one_hot_mi(data):
    print("Applying one_hot_mi")
    one_hot_mi = data[['service_eco_i', 'srv_rerror_rate', 'duration', 'dst_host_srv_rerror_rate', 'rerror_rate',
                       'service_private', 'dst_host_rerror_rate', 'srv_diff_host_rate', 'srv_count',
                       'dst_host_count',
                       'service_http', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'logged_in',
                       'srv_serror_rate', 'flag_S0', 'dst_host_srv_serror_rate', 'serror_rate',
                       'dst_host_serror_rate',
                       'flag_SF', 'dst_host_same_srv_rate', 'dst_host_srv_count', 'count',
                       'dst_host_diff_srv_rate',
                       'same_srv_rate', 'diff_srv_rate', 'dst_bytes', 'src_bytes']]
    return one_hot_mi


def one_hot_pca(data):
    print("Applying one_hot_pca")
    # 加载保存的PCA模型
    with open('./resource/preprocessor/one_hot_pca_model.pkl', 'rb') as file:
        pca_loaded = pickle.load(file)
    # 假设new_X是新的特征数据，new_y是对应的标签，确保先进行相同的预处理
    # 应用LDA转换
    new_X_pca = pca_loaded.transform(data)
    return new_X_pca


def one_hot_lda(data):
    print("Applying one_hot_lda")
    # 加载保存的PCA模型
    with open('./resource/preprocessor/one_hot_lda_model.pkl', 'rb') as file:
        lda_loaded = pickle.load(file)
    # 假设new_X是新的特征数据，new_y是对应的标签，确保先进行相同的预处理
    # 应用LDA转换
    new_X_lda = lda_loaded.transform(data)
    return new_X_lda


# 字典映射预处理步骤字符串到对应的函数
preprocessing_steps = {
    "S": common_preprocess,
    "L1": label_encoding,
    "L2": label_std_scaler,
    "L3": label_pearson,
    "L4": label_mi,
    "L5": label_pca,
    "L6": label_lda,
    "H1": one_hot_encoding,
    "H2": one_hot_std_scaler,
    "H3": one_hot_pearson,
    "H4": one_hot_mi,
    "H5": one_hot_pca,
    "H6": one_hot_lda,
}
