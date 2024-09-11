import os
import shutil
import csv

# 원본 파일들이 있는 최상위 폴더 아마 D or E 드라이브지 않을까?
base_directory = 'C:\\Users\\promo\\OneDrive\\바탕 화면\\can' 

for folder_name in os.listdir(base_directory): # 최상위 폴더에 있는 모든 하위폴더 처리
    source_directory = os.path.join(base_directory, folder_name)
    
    if not os.path.isdir(source_directory):
        continue
    
    New_directory = os.path.join(base_directory, 'organize', folder_name)

    # 새 폴더가 존재하면 삭제하고 새로 만듬
    if os.path.exists(New_directory):
        shutil.rmtree(New_directory)
    
    os.makedirs(New_directory)
    
    Detail_file_list = sorted(os.listdir(source_directory))
    
    # 'START'가 포함된 파일의 인덱스 생성
    start_indices = []
    
    # 파일 목록에서 'START'가 포함된 파일의 인덱스 찾기
    for i, filename in enumerate(Detail_file_list):
        if 'START' in filename:
            start_indices.append(i)
    
    for i in range(len(start_indices)): # 파일 생성

        start = start_indices[i] - 1  # 현재 'START' 파일 전부터
        
        # 마지막 'START' 파일 이후의 파일 범위 처리
        if i + 1 < len(start_indices):
            end = start_indices[i + 1] - 2 # 다음 'START' 파일의 -2 까지
        else:
            end = len(Detail_file_list) - 1 # 마지막 'START' 파일 이후엔 끝까지

        start_file_name = Detail_file_list[start_indices[i]]
        foldername = Detail_file_list[start]
        new_folder_name = f"{foldername}"
        new_folder_path = os.path.join(New_directory, new_folder_name)
        
        os.makedirs(new_folder_path, exist_ok=True)
        
               
        for filename in Detail_file_list[start:end + 1]:
            if 'START' not in filename:
                source_file = os.path.join(source_directory, filename)
                destination_file = os.path.join(new_folder_path, filename)
                shutil.copy(source_file, destination_file)
        
        # print(f"파일들이 {new_folder_path}에 저장되었습니다.")
    
    # print(f"모든 파일이 {New_directory}에 저장되었습니다.")

Org_file_list = sorted(os.listdir(base_directory + '\\organize\\'))
for folder in Org_file_list:
    folder_src = base_directory + '\\organize\\' + folder
    folder_dst = base_directory + '\\org_dst\\' + folder

    # 하위 디렉토리 목록 생성
    directories = [name for name in os.listdir(folder_src) if os.path.isdir(os.path.join(folder_src, name))]

    for directory in directories:
        file_src = os.path.join(folder_src, directory) + '\\'
        file_dst = os.path.join(folder_dst, directory) + '\\'
        
        # 디렉터리가 존재하지 않으면 생성
        if not os.path.exists(file_dst):
            os.makedirs(file_dst)
        
        # 기존 파일 삭제
        if os.path.exists(file_dst):
            for file in os.scandir(file_dst):
                os.remove(file.path) 
        
        # 파일 열기
        f_orion_bms1 = open(file_dst + directory + '_orion_bms1.csv', 'w', newline='')
        f_orion_bms2 = open(file_dst + directory + '_orion_bms2.csv', 'w', newline='')
        f_orion_bms3 = open(file_dst + directory + '_orion_bms3.csv', 'w', newline='')
        
        f_amk_setpoint1_rl = open(file_dst + directory + '_amk_setpoint1_rl.csv', 'w', newline='')
        f_amk_setpoint1_rr = open(file_dst + directory + '_amk_setpoint1_rr.csv', 'w', newline='')
        f_amk_actual_values1_rl = open(file_dst + directory + '_amk_actual_values1_rl.csv', 'w', newline='')
        f_amk_actual_values2_rl = open(file_dst + directory + '_amk_actual_values2_rl.csv', 'w', newline='')
        f_amk_actual_values1_rr = open(file_dst + directory + '_amk_actual_values1_rr.csv', 'w', newline='')
        f_amk_actual_values2_rr = open(file_dst + directory + '_amk_actual_values2_rr.csv', 'w', newline='')
        
        f_steeting_wheel_msg2 = open(file_dst + directory + '_steeting_wheel_msg2.csv', 'w', newline='')

        writer = csv.writer(f_orion_bms1)
        writer.writerow(['time', 'packCurrent', 'packVoltage', 'packSoc', 'packPower'])
        writer = csv.writer(f_orion_bms2)
        writer.writerow(['time', 'packChargeLimit', 'packDischargeLimit'])
        writer = csv.writer(f_orion_bms3)
        writer.writerow(['time', 'highTemp', 'highCell', 'avgTemp', 'bmsTemp', 'lowVoltage'])
        
        writer = csv.writer(f_amk_setpoint1_rl)
        writer.writerow(['time', 'AMK_bInverterOn', 'AMK_bDcOn', 'AMK_bEnable', 'AMK_bErrorReset', 'AMK_Torque_setpoint', 'AMK_TorqueLimitPositv', 'AMK_TorqueLimitNegativ'])
        writer = csv.writer(f_amk_setpoint1_rr)
        writer.writerow(['time', 'AMK_bInverterOn', 'AMK_bDcOn', 'AMK_bEnable', 'AMK_bErrorReset', 'AMK_Torque_setpoint', 'AMK_TorqueLimitPositv', 'AMK_TorqueLimitNegativ'])
        writer = csv.writer(f_amk_actual_values1_rl)
        writer.writerow(['time', 'AMK_bSystemReady', 'AMK_bError', 'AMK_bWarn', 'AMK_bQuitDcOn', 'AMK_bDcOn', 'AMK_bQuitInverterOn', 'AMK_bInverterOn', 'AMK_bDerating', 'AMK_ActualVelocity', 'AMK_TorqueCurrent', 'AMK_MagnetizingCurrent'])
        writer = csv.writer(f_amk_actual_values2_rl)
        writer.writerow(['time', 'AMK_TempMotor', 'AMK_TempInverter', 'AMK_ErrorInfo', 'AMK_TempIGBT'])
        writer = csv.writer(f_amk_actual_values1_rr)
        writer.writerow(['time', 'AMK_bSystemReady', 'AMK_bError', 'AMK_bWarn', 'AMK_bQuitDcOn', 'AMK_bDcOn', 'AMK_bQuitInverterOn', 'AMK_bInverterOn', 'AMK_bDerating', 'AMK_ActualVelocity', 'AMK_TorqueCurrent', 'AMK_MagnetizingCurrent'])
        writer = csv.writer(f_amk_actual_values2_rr)
        writer.writerow(['time', 'AMK_TempMotor', 'AMK_TempInverter', 'AMK_ErrorInfo', 'AMK_TempIGBT'])
        
        writer = csv.writer(f_steeting_wheel_msg2)
        writer.writerow(['time', 'apps', 'bpps'])

        files = os.listdir(file_src)
        
        time = 0

        for file in files:
            f = open(file_src + file)
            lines = csv.reader(f)
            
            for line in lines:
                if len(line) < 4:
                    continue
                
                if len(line[0]) < 4:
                    continue
                
                time += (int(line[0], 16) / 10)
                
                if line[3] == '00001F00':
                    if len(line) < 10:
                        continue
                    
                    packCurrent = int(line[5] + line[4], 16)
                    if packCurrent > 32767:
                        packCurrent -= 65536
                        
                    packCurrent /= 10
                        
                    packVoltage = int(line[7] + line[6], 16)
                    packVoltage /= 10
                    
                    packSoc = int(line[8], 16)
                    packSoc /= 2
                    
                    packPower = packCurrent * packVoltage // 1000
                    
                    writer = csv.writer(f_orion_bms1)
                    writer.writerow([time, packCurrent, packVoltage, packSoc, packPower])
                    
                if line[3] == '00001F01':
                    if len(line) < 10:
                        continue
                    
                    packChargeLimit = int(line[5] + line[4], 16)
                    if packChargeLimit > 32767:
                        packChargeLimit -= 65536
                        
                    packDischargeLimit = int(line[7] + line[6], 16)
                    if packDischargeLimit > 32767:
                        packDischargeLimit -= 65536
                    
                    writer = csv.writer(f_orion_bms2)
                    writer.writerow([time, packChargeLimit, packDischargeLimit])
                    
                if line[3] == '00001F02':
                    if len(line) < 10:
                        continue
                    
                    highTemp = int(line[4], 16)
                    if highTemp > 127:
                        highTemp -= 256
                        
                    highCell = int(line[5], 16)
                    avgTemp = int(line[6], 16)
                    if avgTemp > 127:
                        avgTemp -= 256
                        
                    bmsTemp = int(line[7], 16)
                    if bmsTemp > 127:
                        bmsTemp -= 256
                        
                    lowVoltage = int(line[9] + line[8], 16)
                    lowVoltage /= 10000
                    
                    writer = csv.writer(f_orion_bms3)
                    writer.writerow([time, highTemp, highCell, avgTemp, bmsTemp, lowVoltage])

                if line[3] == '00275188':
                    if len(line) < 12:
                        continue
                        
                    AMK_Control = int(line[5], 16)

                    AMK_bInverterOn = (AMK_Control) & 0b1
                    AMK_bDcOn = (AMK_Control >> 1) & 0b1
                    AMK_bEnable = (AMK_Control >> 2) & 0b1
                    AMK_bErrorReset = (AMK_Control >> 3) & 0b1

                    AMK_Torque_setpoint = int(line[7] + line[6], 16)
                    if AMK_Torque_setpoint > 32767:
                        AMK_Torque_setpoint -= 65536

                    AMK_TorqueLimitPositv = int(line[9] + line[8], 16)
                    if AMK_TorqueLimitPositv > 32767:
                        AMK_TorqueLimitPositv -= 65536

                    AMK_TorqueLimitNegativ = int(line[11] + line[10], 16)
                    if AMK_TorqueLimitNegativ > 32767:
                        AMK_TorqueLimitNegativ -= 65536

                    writer = csv.writer(f_amk_setpoint1_rl)
                    writer.writerow([time, AMK_bInverterOn, AMK_bDcOn, AMK_bEnable, AMK_bErrorReset, AMK_Torque_setpoint, AMK_TorqueLimitPositv, AMK_TorqueLimitNegativ])

                if line[3] == '00275189':
                    if len(line) < 12:
                        continue
                
                    AMK_Control = int(line[5], 16)

                    AMK_bInverterOn = (AMK_Control) & 0b1
                    AMK_bDcOn = (AMK_Control >> 1) & 0b1
                    AMK_bEnable = (AMK_Control >> 2) & 0b1
                    AMK_bErrorReset = (AMK_Control >> 3) & 0b1

                    AMK_Torque_setpoint = int(line[7] + line[6], 16)
                    if AMK_Torque_setpoint > 32767:
                        AMK_Torque_setpoint -= 65536

                    AMK_TorqueLimitPositv = int(line[9] + line[8], 16)
                    if AMK_TorqueLimitPositv > 32767:
                        AMK_TorqueLimitPositv -= 65536

                    AMK_TorqueLimitNegativ = int(line[11] + line[10], 16)
                    if AMK_TorqueLimitNegativ > 32767:
                        AMK_TorqueLimitNegativ -= 65536

                    writer = csv.writer(f_amk_setpoint1_rr)
                    writer.writerow([time, AMK_bInverterOn, AMK_bDcOn, AMK_bEnable, AMK_bErrorReset, AMK_Torque_setpoint, AMK_TorqueLimitPositv, AMK_TorqueLimitNegativ])

                if line[3] == '0027520B':
                    if len(line) < 12:
                        continue

                    AMK_bSystemReady = (int(line[4], 16)) & 0b1
                    AMK_bError = (int(line[4], 16) >> 1) & 0b1
                    AMK_bWarn = (int(line[4], 16) >> 2) & 0b1
                    AMK_bQuitDcOn = (int(line[4], 16) >> 3) & 0b1
                    AMK_bDcOn = (int(line[4], 16) >> 4) & 0b1
                    AMK_bQuitInverterOn = (int(line[4], 16) >> 5) & 0b1
                    AMK_bInverterOn = (int(line[4], 16) >> 6) & 0b1
                    AMK_bDerating = (int(line[4], 16) >> 7) & 0b1

                    AMK_ActualVelocity = int(line[6] + line[5], 16)
                    if AMK_ActualVelocity > 32767:
                        AMK_ActualVelocity -= 65536

                    AMK_TorqueCurrent = int(line[8] + line[7], 16)
                    if AMK_TorqueCurrent > 32767:
                        AMK_TorqueCurrent -= 65536

                    AMK_MagnetizingCurrent = int(line[10] + line[9], 16)
                    if AMK_MagnetizingCurrent > 32767:
                        AMK_MagnetizingCurrent -= 65536

                    writer = csv.writer(f_amk_actual_values1_rl)
                    writer.writerow([time, AMK_bSystemReady, AMK_bError, AMK_bWarn, AMK_bQuitDcOn, AMK_bDcOn, AMK_bQuitInverterOn, AMK_bInverterOn, AMK_bDerating, AMK_ActualVelocity, AMK_TorqueCurrent, AMK_MagnetizingCurrent])

                if line[3] == '0027520C':
                    if len(line) < 12:
                        continue

                    AMK_TempMotor = int(line[4], 16)
                    if AMK_TempMotor > 127:
                        AMK_TempMotor -= 256

                    AMK_TempInverter = int(line[5], 16)
                    if AMK_TempInverter > 127:
                        AMK_TempInverter -= 256

                    AMK_ErrorInfo = int(line[6], 16)
                    AMK_TempIGBT = int(line[7], 16)
                    if AMK_TempIGBT > 127:
                        AMK_TempIGBT -= 256

                    writer = csv.writer(f_amk_actual_values2_rl)
                    writer.writerow([time, AMK_TempMotor, AMK_TempInverter, AMK_ErrorInfo, AMK_TempIGBT])

                if line[3] == '0027520D':
                    if len(line) < 12:
                        continue

                    AMK_bSystemReady = (int(line[4], 16)) & 0b1
                    AMK_bError = (int(line[4], 16) >> 1) & 0b1
                    AMK_bWarn = (int(line[4], 16) >> 2) & 0b1
                    AMK_bQuitDcOn = (int(line[4], 16) >> 3) & 0b1
                    AMK_bDcOn = (int(line[4], 16) >> 4) & 0b1
                    AMK_bQuitInverterOn = (int(line[4], 16) >> 5) & 0b1
                    AMK_bInverterOn = (int(line[4], 16) >> 6) & 0b1
                    AMK_bDerating = (int(line[4], 16) >> 7) & 0b1

                    AMK_ActualVelocity = int(line[6] + line[5], 16)
                    if AMK_ActualVelocity > 32767:
                        AMK_ActualVelocity -= 65536

                    AMK_TorqueCurrent = int(line[8] + line[7], 16)
                    if AMK_TorqueCurrent > 32767:
                        AMK_TorqueCurrent -= 65536

                    AMK_MagnetizingCurrent = int(line[10] + line[9], 16)
                    if AMK_MagnetizingCurrent > 32767:
                        AMK_MagnetizingCurrent -= 65536

                    writer = csv.writer(f_amk_actual_values1_rr)
                    writer.writerow([time, AMK_bSystemReady, AMK_bError, AMK_bWarn, AMK_bQuitDcOn, AMK_bDcOn, AMK_bQuitInverterOn, AMK_bInverterOn, AMK_bDerating, AMK_ActualVelocity, AMK_TorqueCurrent, AMK_MagnetizingCurrent])

                if line[3] == '0027520E':
                    if len(line) < 12:
                        continue

                    AMK_TempMotor = int(line[4], 16)
                    if AMK_TempMotor > 127:
                        AMK_TempMotor -= 256

                    AMK_TempInverter = int(line[5], 16)
                    if AMK_TempInverter > 127:
                        AMK_TempInverter -= 256

                    AMK_ErrorInfo = int(line[6], 16)
                    AMK_TempIGBT = int(line[7], 16)
                    if AMK_TempIGBT > 127:
                        AMK_TempIGBT -= 256

                    writer = csv.writer(f_amk_actual_values2_rr)
                    writer.writerow([time, AMK_TempMotor, AMK_TempInverter, AMK_ErrorInfo, AMK_TempIGBT])

                if line[3] == '0027520F':
                    if len(line) < 12:
                        continue
                    
                    steering_wheel_msg2_apps = int(line[5], 16)
                    steering_wheel_msg2_bpps = int(line[6], 16)

                    writer = csv.writer(f_steeting_wheel_msg2)
                    writer.writerow([time, steering_wheel_msg2_apps, steering_wheel_msg2_bpps])
            print(f"파일들이 {file_dst}에 저장되었습니다.")
        f_orion_bms1.close()
        f_orion_bms2.close()
        f_orion_bms3.close()
        
        f_amk_setpoint1_rl.close()
        f_amk_setpoint1_rr.close()
        f_amk_actual_values1_rl.close()
        f_amk_actual_values2_rl.close()
        f_amk_actual_values1_rr.close()
        f_amk_actual_values2_rr.close()
        
        f_steeting_wheel_msg2.close()
    
print('end')