import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

base_directory = 'C:\\Users\\promo\\OneDrive\\바탕 화면\\can2'
dst_direct = os.path.join(base_directory, 'org_dst')

# 개별 그래프 저장 함수
def save_plot(time, data, label, color, file_name):
    plt.figure(figsize=(10, 6))
    plt.plot(time, data, label=label, color=color)
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title(label)
    plt.legend()
    plt.grid(True)
    plt.savefig(file_name)
    plt.close()

# 모든 그래프 저장 함수

def save_ALL_plot(times, data_list, labels, colors, file_name):
    num_plots = len(data_list)
    fig, axes = plt.subplots(num_plots, 1, figsize=(21, 3 * num_plots), sharex=True)
    
    if num_plots == 1:  # 데이터가 하나인 경우, axes가 배열이 아니라 단일 객체로 반환됨
        axes = [axes]
        
    for ax, time, data, label, color in zip(axes, times, data_list, labels, colors):
        ax.plot(time, data, label=label, color=color)
        ax.set_ylabel(label, color=color)
        ax.tick_params(axis='y', labelcolor=color)
        ax.grid(True)
    
    axes[-1].set_xlabel('Time')
    plt.suptitle('All in One (Separate Subplots)')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # 타이틀과 서브플롯 간격 조정
    plt.savefig(file_name)
    plt.close()

can2024_XX_list = sorted(os.listdir(dst_direct))

for file in can2024_XX_list:
    can2024_XX_forder_list = sorted(os.listdir(os.path.join(dst_direct, file)))
    
    for forder in can2024_XX_forder_list:
        file_forder_directory = os.path.join(dst_direct, file, forder, forder)
        file_paths = [
            file_forder_directory + '_amk_actual_values1_rl.csv',
            file_forder_directory + '_amk_actual_values1_rr.csv',
            # file_forder_directory + '_amk_actual_values2_rl.csv',
            # file_forder_directory + '_amk_actual_values2_rr.csv',
            file_forder_directory + '_amk_setpoint1_rl.csv',
            file_forder_directory + '_amk_setpoint1_rr.csv',
            file_forder_directory + '_orion_bms1.csv',
            file_forder_directory + '_orion_bms2.csv',
            # file_forder_directory + '_orion_bms3.csv',
            # file_forder_directory + '_steering_wheel_msg2'
        ]
        
        try:
            dfs = [pd.read_csv(path) for path in file_paths]
        except FileNotFoundError:
            print(f"{file_paths} 중 일부 파일을 찾을 수 없습니다.")
            continue
        
        times = [df['time'] for df in dfs]
        data_list = [
            dfs[0]['AMK_ActualVelocity'], dfs[1]['AMK_ActualVelocity'],
            dfs[2]['AMK_Torque_setpoint'], dfs[3]['AMK_Torque_setpoint'],
            dfs[4]['packCurrent'], dfs[5]['packDischargeLimit']
        ]
        # list up
        labels = [
            'AMK_ActualVelocity','AMK_ActualVelocity',
            'AMK_Torque_setpoint','AMK_Torque_setpoint',
            'packCurrent','packDischargeLimit'
        ]
        # for i in range(len(dfs)):  
        #     for t in range(len(dfs[i].columns)):  
        #         data_list.append(dfs[i].iloc[:, t])


        # for i in range(len(dfs)):  
        #     labels.extend(dfs[i].columns) 

        colors = ['black', 'navy', 'darkorange', 'seagreen', 'maroon', 'purple']
        colors = colors * (len(data_list) // len(colors)) + colors[:len(data_list) % len(colors)]

        
        pdf_directory = os.path.join(dst_direct, file, forder, 'PDF')
        if not os.path.exists(pdf_directory):
            os.makedirs(pdf_directory)
        
        # 개별 그래프 저장
        for time, data, label, color in zip(times, data_list, labels, colors):
            file_name = os.path.join(pdf_directory, f"{forder}_{label}.pdf")
            save_plot(time, data, label, color, file_name)
        
        # 올인원 그래프 저장
        save_ALL_plot(times, data_list, labels, colors, os.path.join(pdf_directory, f"{forder}_ALL_in_one.pdf"))

print('end')
