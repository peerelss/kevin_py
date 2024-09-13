import os
import shutil


def move_large_files(source_folder, target_folder, size_threshold):
    # 检查目标文件夹是否存在，如果不存在则创建
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 遍历源文件夹及其子文件夹中的所有文件
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            # 获取文件大小（字节）
            file_size = os.path.getsize(file_path)

            # 如果文件大小大于指定阈值，则移动到目标文件夹
            if file_size > size_threshold:
                target_file_path = os.path.join(target_folder, file)

                # 检查目标文件夹中是否存在同名文件
                if os.path.exists(target_file_path):
                    target_file_size = os.path.getsize(target_file_path)

                    # 如果目标文件夹中存在同名文件且大小相同，删除源文件
                    if file_size == target_file_size:
                        os.remove(file_path)
                        print(f'Deleted original: {file_path} (same size as target)')
                    else:
                        print(f'Skipped (different size): {file_path}')
                else:
                    shutil.move(file_path, target_folder)
                    print(f'Moved: {file_path} to {target_folder}')


# 示例参数
source_folder = r'n:\p'  # 替换为你的源文件夹路径
target_folder = r'n:\after'  # 替换为你的目标文件夹路径
size_threshold = 30 * 1000 * 1000  # 以字节为单位，例如这里是1MB

move_large_files(source_folder, target_folder, size_threshold)
