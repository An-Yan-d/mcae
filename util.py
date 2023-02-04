import shutil
import os


# 将目录的文件复制到指定目录
def copy2there(src_dir, dst_dir):
    """
    复制src_dir目录下的所有内容到dst_dir目录
    :param src_dir: 源文件目录
    :param dst_dir: 目标目录
    :return:
    """
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    if os.path.exists(src_dir):
        for file in os.listdir(src_dir):
            file_path = os.path.join(src_dir, file)
            dst_path = os.path.join(dst_dir, file)
            if os.path.isfile(os.path.join(src_dir, file)):
                shutil.copy2(file_path, dst_path) # 这里使用的coyp2()，不会改变文件原有的信息
            else:
                copy2there(file_path, dst_path)
                # print("存在多级文件夹，正在复制。")

if __name__=='__main__':
    # 源文件路径
    source_path = r'D:\source'
    # 目标路径
    target_path = r'D:\target'
    copy2there(source_path, target_path)