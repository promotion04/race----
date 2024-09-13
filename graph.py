import pandas as pd
import matplotlib.pyplot as plt
import os 
# plt.close('all')

base_directory = 'C:\\Users\\promo\\OneDrive\\바탕 화면\\can' 

dst_direct = base_directory + '\\org_dst\\'

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
def save_ALL_plot():
    plt.figure(figsize=(10, 6))
    plt.plot(time1, AMK_ActualVelocity_rl, label='AMK_ActualVelocity_rl', color='red')
    plt.plot(time2, AMK_ActualVelocity_rr, label='AMK_ActualVelocity_rr', color='orange')
    plt.plot(time3, AMK_Torque_setpoint_rl, label='AMK_Torque_setpoint_rl', color='yellow')
    plt.plot(time4, AMK_Torque_setpoint_rr, label='AMK_Torque_setpoint_rr', color='green')
    plt.plot(time5, packCurrent, label='packCurrent', color='blue')
    plt.plot(time6, packDischargeLimit, label='packDischargeLimit', color='purple')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('All in One')
    plt.legend()
    plt.grid(True)
    plt.savefig(dst_direct + file + '\\' + forder + '\\PDF\\' + forder + '_ALL_in_one.pdf')
    plt.close()

can2024_XX_list = sorted(os.listdir(dst_direct))

for file in can2024_XX_list:

    can2024_XX_forder_list = sorted(os.listdir(dst_direct + file + '\\'))

    for forder in can2024_XX_forder_list:
        file_forder_directory = dst_direct + file + '\\' + forder + '\\' + forder
        file_path1 = file_forder_directory + '_amk_actual_values1_rl.csv'
        file_path2 = file_forder_directory + '_amk_actual_values1_rr.csv'
        file_path3 = file_forder_directory + '_amk_setpoint1_rl.csv'
        file_path4 = file_forder_directory + '_amk_setpoint1_rr.csv'
        file_path5 = file_forder_directory + '_orion_bms1.csv'
        file_path6 = file_forder_directory + '_orion_bms2.csv'

        df1 = pd.read_csv(file_path1)
        df2 = pd.read_csv(file_path2)
        df3 = pd.read_csv(file_path3)
        df4 = pd.read_csv(file_path4)
        df5 = pd.read_csv(file_path5)
        df6 = pd.read_csv(file_path6)

        time1 = df1['time']
        AMK_ActualVelocity_rl = df1['AMK_ActualVelocity']
        time2 = df2['time']
        AMK_ActualVelocity_rr = df2['AMK_ActualVelocity']
        time3 = df3['time']
        AMK_Torque_setpoint_rl = df3['AMK_Torque_setpoint']
        time4 = df4['time']
        AMK_Torque_setpoint_rr = df4['AMK_Torque_setpoint']
        time5 = df5['time']
        packCurrent = df5['packCurrent']
        time6 = df6['time']
        packDischargeLimit = df6['packDischargeLimit']

        pdf_directory = os.path.join(dst_direct + file + '\\' + forder + '\\PDF\\')

        if not os.path.exists(pdf_directory):
            os.makedirs(pdf_directory)

        # 개별 그래프 저장
        save_plot(time1, AMK_ActualVelocity_rl, 'AMK_ActualVelocity_rl', 'red', dst_direct + file + '\\' + forder + '\\PDF\\' + forder + '_AMK_ActualVelocity_rl.pdf')
        save_plot(time2, AMK_ActualVelocity_rr, 'AMK_ActualVelocity_rr', 'orange', dst_direct + file + '\\' + forder + '\\PDF\\' + forder + '_AMK_ActualVelocity_rr.pdf')
        save_plot(time3, AMK_Torque_setpoint_rl, 'AMK_Torque_setpoint_rl', 'yellow', dst_direct + file + '\\' + forder + '\\PDF\\' + forder + '_AMK_Torque_setpoint_rl.pdf')
        save_plot(time4, AMK_Torque_setpoint_rr, 'AMK_Torque_setpoint_rr', 'green', dst_direct + file + '\\' + forder + '\\PDF\\' + forder + '_AMK_Torque_setpoint_rr.pdf')
        save_plot(time5, packCurrent, 'packCurrent', 'blue', dst_direct + file + '\\' + forder + '\\PDF\\' + forder + '_packCurrent.pdf')
        save_plot(time6, packDischargeLimit, 'packDischargeLimit', 'purple', dst_direct + file + '\\' + forder + '\\PDF\\' + forder + '_packDischargeLimit.pdf')

        # 올인원 그래프 저장
        save_ALL_plot()
        # print(f"모든 pdf 파일이 {dst_direct + file + '\\' + forder + '\\PDF'}에 저장되었습니다.")

print('end')
