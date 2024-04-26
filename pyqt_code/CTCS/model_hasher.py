import hashlib
import os
from collections import defaultdict


def compute_hash(filepath):
    """计算指定文件的SHA-256哈希值"""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"Error: File not found {filepath}")
        return None
    except Exception as e:
        print(f"Error computing hash for {filepath}: {e}")
        return None


def print_hash_tree(directory, prefix=''):
    """递归地打印目录结构和对应文件的哈希值"""
    if os.path.isdir(directory):
        for filename in sorted(os.listdir(directory)):
            path = os.path.join(directory, filename)
            if os.path.isdir(path):
                print(f"{prefix}{filename}/")
                print_hash_tree(path, prefix + "    ")
            else:
                if path.endswith('.h5') or path.endswith('.pkl'):
                    hash_value = compute_hash(path)
                    print(f"{prefix}{filename}: {hash_value}")
    else:
        print("Provided path is not a directory")


def nested_dict():
    """工厂函数用于生成无限深度的默认字典"""
    return defaultdict(nested_dict)


def add_model_hash(model_dict, model_type, encoding, preprocessing, augmentation, hash_value, prep_method):
    """添加模型及其哈希值和预处理方式到嵌套字典中"""
    model_dict[model_type][encoding][preprocessing][augmentation] = {
        'hash': hash_value,
        'preprocessing': prep_method
    }

# if __name__ == "__main__":
# process_model("path/to/your/model/file")

# directory_path = r'D:\Download\zyFile\Cyberthreat_Cognitive_System\CTCS_Code\pyqt_code\CTCS\resource\NSL-KDD'  # 修改为你的文件夹路径
# print_hash_tree(directory_path)
# 初始化模型哈希字典
# model_hashes = nested_dict()
# # 示例添加模型哈希与预处理方式
# print(json.dumps(model_hashes, indent=4))
