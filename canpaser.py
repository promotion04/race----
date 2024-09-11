import os
import shutil

# 원본 파일 폴더
source_directory = r'C:\Users\promo\OneDrive\바탕 화면\can\can2024-08-29'
# 생성할 파일 폴더
New_directory = r'C:\바탕 화면\test\can2024-08-29'

if os.path.exists(New_directory) == True: # 생성할 파일 이름과 같은게 있다면 삭제
    shutil.rmtree(New_directory)

Detail_file_list = sorted(os.listdir(source_directory))

# 'START'가 포함된 파일의 인덱스 생성
start_indices = []

# 파일 목록에서 'START'가 포함된 파일의 인덱스 찾기.
for i, filename in enumerate(Detail_file_list):
    if 'START' in filename:
        start_indices.append(i)

for i in range(len(start_indices)): # 파일 생성
    start_file_name = Detail_file_list[start_indices[i]]
    new_folder_name = f"collection_{start_file_name}"
    new_folder_path = os.path.join(New_directory, new_folder_name)
    
    os.makedirs(new_folder_path, exist_ok=True)
    
    start = start_indices[i] - 1  # 현재 'START' 파일 전부터
    
    # 마지막 'START' 파일 이후의 파일 범위 처리
    if i + 1 < len(start_indices):
        end = start_indices[i + 1] - 2 # 다음 'START' 파일의 -2 까지
    else:
        end = len(Detail_file_list) - 1 # 마지막 'START' 파일 이후엔 끝까지
    
    for filename in Detail_file_list[start:end + 1]:
        if 'START' not in filename:
            source_file = os.path.join(source_directory, filename)
            destination_file = os.path.join(new_folder_path, filename)
            shutil.copy(source_file, destination_file)
    
    print(f"파일들이 {new_folder_path}에 저장되었습니다.")

print("모든 파일이 새 폴더에 저장되었습니다.")
