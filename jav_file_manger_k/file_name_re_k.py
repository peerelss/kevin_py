import os
import string
import shutil


def list_all_files(folder_path):
    # 遍历文件夹及其子文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            print(file)


prefix_list = [
    '@九游@5jy.cc-', '@九游@5jy.cc-', 'aavv333.com@', 'aavv38.xyz@', 'aaxv.xyz-', 'amav.xyz-', 'avav66.xyz', '[99u.me]',
    'baixn.xyz-', 'bbsxv.xyz-', 'boby+mimip2p(', 'fuckman+mimip2p(', 'hhd800.com@', 'Japan_Incest_Madonna_', '[thz.la]',
    'kcf9.com@', 'kcf9.com@', 'HD-', 'kpxvs.com-', 'Miyase Riko ', 'ppjav.com.', 'rh2048.com@', 'zzpp08.com@',
    'supermax_akiba-online.com_', 't2jav.com_', 'taxv.xyz-', 'Touch99@', 'DivX+nike(', 'FFJAV.com', 'ffjav.com_',
    'xhd1080.com@', 'zzpp06.com@', '[22y.me]', '[44x.me]', '[456k.me]', '[bbs.yzkof.com]', '[FHD]', '[Madonna](',
    '[Madonna]_[夫の前で調教して下さい]_(', '[NoDRM]-', '[ThZu.Cc]', '[土豆丝]', '[鱼香肉丝]', '【thz.la】', '【TXH】',
    '【亞瑟王】【SEX8.CC】', '【曰上天空】', '【狼王008】', '【贴心话】', '【雪光梦想】', '國產無碼@', '(', '@', '[Madonna][',
    '[44x.me]', 'kckc13.com@', '【sex8.cc】', '[Thz.la]', 'Watch ', 'hjd2048.com-', 'hhd800.com@', 'fangyuanli-',
    'gg999.cc-'
]


def rename_files_by_prefix(folder_path, prefix_list):
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件名是否以列表中的任意前缀开头
            for prefix in prefix_list:
                if file.startswith(prefix):
                    # 构建新的文件名，去掉前缀
                    new_name = file[len(prefix):]
                    old_file_path = os.path.join(root, file)
                    new_file_path = os.path.join(root, new_name)

                    # 重命名文件
                    if os.path.exists(new_file_path):
                        print(f'Skipped (exists): {new_file_path}')
                    else:
                        os.rename(old_file_path, new_file_path)
                        print(f'Renamed: {old_file_path} to {new_file_path}')
                    break  # 如果已经匹配并重命名，跳过其他前缀的检查


def make_dir_a_z(folder_path):
    for letter in string.ascii_lowercase:
        letter_folder = os.path.join(folder_path, letter)
        if not os.path.exists(letter_folder):
            os.makedirs(letter_folder)


def move_file_to_right_folder(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # 检查是否是文件而不是文件夹
        if os.path.isfile(file_path):
            # 检查文件名是否以字母开头
            first_letter = file[0].lower()
            if first_letter in string.ascii_lowercase:
                # 构建目标文件夹路径
                target_folder = os.path.join(folder_path, first_letter)
                target_file_path = os.path.join(target_folder, file)

                # 如果目标文件夹中没有同名文件，移动文件
                if not os.path.exists(target_file_path):
                    shutil.move(file_path, target_folder)
                    print(f'Moved: {file} to {target_folder}')
                else:
                    print(f'Skipped (exists): {file}')


def move_files_to_matching_folders(base_folder):
    # 遍历文件夹中的所有文件夹
    for root, dirs, files in os.walk(base_folder):
        # 排除子文件夹，确保只处理当前目录下的文件和文件夹
        if root == base_folder:
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)

                # 遍历当前目录下的所有文件
                for file in files:
                    file_path = os.path.join(root, file)

                    # 检查文件名是否以文件夹名开头，忽略大小写
                    if file.lower().startswith(dir_name.lower()):
                        target_path = os.path.join(dir_path, file)

                        # 如果目标文件夹中没有同名文件，移动文件
                        if not os.path.exists(target_path):
                            shutil.move(file_path, dir_path)
                            print(f'Moved: {file} to {dir_name}')
                        else:
                            print(f'Skipped (exists): {file}')


def delete_duplicate_files(folder_path):
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件名是否包含(1)
            if '(1)' in file:
                original_file_name = file.replace('(1)', '')
                file_path = os.path.join(root, file)
                original_file_path = os.path.join(root, original_file_name)

                # 检查移除(1)后文件名的文件是否存在且文件大小相同
                if os.path.exists(original_file_path):
                    if os.path.getsize(file_path) == os.path.getsize(original_file_path):
                        # 删除包含(1)的文件
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")


# 示例参数
folder_path_r = r'O:\after'  # 替换为你的文件夹路径

if __name__ == "__main__":
    #   move_files_to_matching_folders(folder_path_r)
    # delete_duplicate_files(folder_path_r)
     rename_files_by_prefix(folder_path_r, prefix_list)
    # move_file_to_right_folder(folder_path_r)
    #move_files_to_matching_folders(folder_path_r)
    # move_file_to_right_folder(folder_path_r)