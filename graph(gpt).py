import pandas as pd
import matplotlib.pyplot as plt
import os

base_directory = 'C:\\Users\\promo\\OneDrive\\바탕 화면\\can2' 
dst_direct = os.path.join(base_directory, 'org_dst')

# 개별 그래프 저장 함수
def save_plot(time, data, label, color, file_name):
    if len(time) != len(data):
        print(f"경고: '{label}' 그래프에서 'time'과 'data'의 길이가 일치하지 않습니다.")
        return
    plt.figure(figsize=(10, 6))
    plt.plot(time, data, label=label, color=color)
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title(label)
    plt.legend()
    plt.grid(True)
    plt.savefig(file_name)
    plt.close()
    print(file_name + ' 개별 그래프가 저장되었습니다.')

# 모든 그래프 저장 함수
def save_ALL_plot(times, data_list, labels, colors, file_name):
    num_plots = len(data_list)
    fig, axes = plt.subplots(num_plots, 1, figsize=(21, 3 * num_plots), sharex=True)
    axes = axes if num_plots > 1 else [axes]
    
    # 그래프 그리기
    for ax, time, data, label, color in zip(axes, times, data_list, labels, colors):
        if len(time) != len(data):
            print(f"경고: '{label}' 그래프에서 'time'과 'data'의 길이가 일치하지 않습니다.")
            continue
        ax.plot(time, data, label=label, color=color)
        ax.set_ylabel(label, color=color)
        ax.tick_params(axis='y', labelcolor=color)
        ax.grid(True)
    
    axes[-1].set_xlabel('Time')
    plt.suptitle('All in One (Separate Subplots)')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(file_name)
    plt.close()
    print(file_name + ' 올인원 그래프가 저장되었습니다.')

# 데이터를 읽고, 그래프를 그리는 함수
def process_and_save_graphs(file_path_list, dst_path):
    # CSV 파일을 읽고 DataFrame을 리스트로 저장
    dfs = []
    for file in file_path_list:
        if os.path.exists(file):
            dfs.append(pd.read_csv(file))
        else:
            print(f"파일이 존재하지 않습니다: {file}")
            continue

    if not dfs:
        print("유효한 CSV 파일이 없습니다.")
        return

    data_list = []
    labels = []
    
    # 데이터 및 레이블 추출
    for df in dfs:
        if 'time' not in df.columns:
            print(f"'{df}' 파일에 'time' 컬럼이 없습니다.")
            continue
        data_list.extend([df[col] for col in df.columns if col != 'time'])
        labels.extend([col for col in df.columns if col != 'time'])

    # 색상 리스트를 데이터 컬럼 수에 맞게 확장
    colors = plt.colormaps.get_cmap('tab10', len(data_list))  # 색상은 최대 10개로 지정

    # 개별 그래프 저장
    for time, data, label, color in zip(dfs[0]['time'], data_list, labels, colors.colors):
        save_plot(dfs[0]['time'], data, label, color, os.path.join(dst_path, label + '.pdf'))

    # 올인원 그래프 저장
    save_ALL_plot(
        times=[df['time'] for df in dfs],
        data_list=data_list,
        labels=labels,
        colors=colors.colors,
        file_name=os.path.join(dst_path, 'ALL_in_one.pdf')
    )

# 디렉토리 탐색 및 파일 경로 생성
can2024_XX_list = sorted(os.listdir(dst_direct))

for file in can2024_XX_list:
    can2024_XX_forder_list = sorted(os.listdir(os.path.join(dst_direct, file)))

    for forder in can2024_XX_forder_list:
        file_forder_directory = os.path.join(dst_direct, file, forder, forder)
        
        file_path_list = [
            f'{file_forder_directory}_amk_actual_values1_rl.csv',
            f'{file_forder_directory}_amk_actual_values1_rr.csv',
            f'{file_forder_directory}_amk_setpoint1_rl.csv',
            f'{file_forder_directory}_amk_setpoint1_rr.csv',
            f'{file_forder_directory}_orion_bms1.csv',
            f'{file_forder_directory}_orion_bms2.csv'
        ]
        
        pdf_directory = os.path.join(dst_direct, file, forder, 'PDF')

        if not os.path.exists(pdf_directory):
            os.makedirs(pdf_directory)
        
        process_and_save_graphs(file_path_list, pdf_directory)

print('end')
