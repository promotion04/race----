import os
import shutil
import csv

# 기본 디렉토리 설정
base_directory = 'C:\\Users\\promo\\OneDrive\\바탕 화면\\can2' 

# 미리 생성된 폴더 삭제 함수
def remove_directory(path):
    if os.path.exists(path):
        shutil.rmtree(path)

# org_src, org_dst 폴더 삭제
remove_directory(base_directory + '\\org_src')
remove_directory(base_directory + '\\org_dst')


def organize_files_by_start(source_directory, target_directory):
    
    # 'START' 키워드 기준으로 파일들을 분리하고 정리.
    # :param source_directory: 원본 파일들이 위치한 디렉토리
    # :param target_directory: 정리된 파일을 저장할 디렉토리
    
    file_list = sorted(os.listdir(source_directory))
    
    # 'START' 키워드 포함 파일 인덱스 찾기
    start_indices = [i for i, f in enumerate(file_list) if 'START' in f]

    for i, start_index in enumerate(start_indices):
        # 범위 결정
        start = start_index - 1
        end = start_indices[i + 1] - 2 if i + 1 < len(start_indices) else len(file_list) - 1
        
        # 새로운 폴더 이름 생성
        foldername = file_list[start]
        new_folder_name = os.path.splitext(foldername)[0]  # 확장자 제거
        new_folder_path = os.path.join(target_directory, new_folder_name)
        os.makedirs(new_folder_path, exist_ok=True)

        # 범위 내 파일 복사
        for filename in file_list[start:end + 1]:
            if 'START' not in filename:
                shutil.copy(
                    os.path.join(source_directory, filename),
                    os.path.join(new_folder_path, filename)
                )

for folder_name in os.listdir(base_directory):
    source_directory = os.path.join(base_directory, folder_name)
    if not os.path.isdir(source_directory):
        continue

    target_directory = os.path.join(base_directory, 'org_src', folder_name)
    organize_files_by_start(source_directory, target_directory)



# ex) constlist = [2, 4, 1] 는 16,32,8 비트로 데이터를 패킹 reserved된 값이 있다면 list로 우선 뽑고 추후에 변형
def data_on(CAN_ID, constlist, line):
    if line[3] == CAN_ID and len(line) >= 10:
        data_list = []
        cnt = 0        
        for i in constlist:
            cnt += i
            if i == 8:
                data_list.append(int(line[cnt + 3] + line[cnt + 2] + line[cnt + 1] + line[cnt] + line[cnt - 1] + line[cnt - 2] + line[cnt - 3] + line[cnt - 4], 16))
            elif i == 4:
                data_list.append(int(line[cnt + 3] + line[cnt + 2] + line[cnt + 1] + line[cnt], 16))
            elif i == 2:
                data_list.append(int(line[cnt + 3] + line[cnt + 2], 16))
            elif i == 1:
                data_list.append(int(line[cnt + 3], 16))
        return data_list
    else:
        return None 

#32767 대소
def compareValues_32767(case_a):
    if case_a > 32767:
        case_a -= 65536
    return case_a
#127 대소
def compareValues_127(case_b):
    if case_b > 127:
        case_b -= 256
    return case_b


Org_file_list = sorted(os.listdir(base_directory + '\\org_src\\'))
for folder in Org_file_list:
    folder += '\\'
    folder_src = base_directory + '\\org_src\\' + folder
    folder_dst = base_directory + '\\org_dst\\' + folder

    directories = [name for name in os.listdir(folder_src) if os.path.isdir(os.path.join(folder_src, name))]


    for directory in directories:
        file_src = folder_src + directory + '\\'
        file_dst = folder_dst + directory + '\\'

        os.makedirs(file_dst)

        if os.path.exists(file_dst):
            for file in os.scandir(file_dst):
                os.remove(file)
        
        f_orion_bms1 = open(file_dst + directory + '_orion_bms1.csv', 'w', newline='')
        f_orion_bms2 = open(file_dst + directory + '_orion_bms2.csv', 'w', newline='')
        f_orion_bms3 = open(file_dst + directory + '_orion_bms3.csv', 'w', newline='')
        
        f_amk_setpoint1_rl = open(file_dst + directory + '_amk_setpoint1_rl.csv', 'w', newline='')
        f_amk_setpoint1_rr = open(file_dst + directory + '_amk_setpoint1_rr.csv', 'w', newline='')
        f_amk_actual_values1_rl = open(file_dst + directory + '_amk_actual_values1_rl.csv', 'w', newline='')
        f_amk_actual_values2_rl = open(file_dst + directory + '_amk_actual_values2_rl.csv', 'w', newline='')
        f_amk_actual_values1_rr = open(file_dst + directory + '_amk_actual_values1_rr.csv', 'w', newline='')
        f_amk_actual_values2_rr = open(file_dst + directory + '_amk_actual_values2_rr.csv', 'w', newline='')
        
        f_steering_wheel_msg2 = open(file_dst + directory + '_steering_wheel_msg2.csv', 'w', newline='')

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
        
        writer = csv.writer(f_steering_wheel_msg2)
        writer.writerow(['time', 'apps', 'bpps'])

        files = os.listdir(folder_src + directory)
        
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
                
                # orion_bms1
                            
                orion_bms1_DL = data_on('00001F00',[2,2,1],line)
                if orion_bms1_DL != None:
                    packCurrent = compareValues_32767(int(orion_bms1_DL[0]))
                    
                    packVoltage = int(orion_bms1_DL[1]) / 10
                        
                    packSoc = int(orion_bms1_DL[2]) / 2
                    
                    packPower = packCurrent * packVoltage // 1000

                    writer = csv.writer(f_orion_bms1)
                    writer.writerow([time, packCurrent, packVoltage, packSoc, packPower])

                # orion_bms2    
                                
                orion_bms2_DL = data_on('00001F01',[2,2],line)

                if orion_bms2_DL != None:                    
                    packChargeLimit = compareValues_32767(int(orion_bms2_DL[0]))
                    packDischargeLimit = compareValues_32767(int(orion_bms2_DL[1]))
                    packDischargeLimit /= 10 # A 단위 맞추기
                    
                    writer = csv.writer(f_orion_bms2)
                    writer.writerow([time, packChargeLimit, packDischargeLimit])

                # orion_bms3    
                
                orion_bms3_DL = data_on('00001F02',[1,1,1,1,2],line)
                if orion_bms3_DL != None:
                    highTemp = compareValues_127(int(orion_bms3_DL[0]))
                    highCell = int(orion_bms3_DL[1])
                    avgTemp = compareValues_127(int(orion_bms3_DL[2]))
                    bmsTemp = compareValues_127(int(orion_bms3_DL[3]))
                    lowVoltage = int(orion_bms3_DL[4]) / 10000

                    writer = csv.writer(f_orion_bms3)
                    writer.writerow([time, highTemp, highCell, avgTemp, bmsTemp, lowVoltage])
                
                # orion_bms4

                # orion_bms4_DL = data_on('00001F03',[2,2,2,2],line)
                # if orion_bms3_DL != None:
                #     LowCellVoltage = int(orion_bms3_DL[0])
                #     HighCellVoltage = int(orion_bms3_DL[1])
                #     LowOcv = int(orion_bms3_DL[2])
                #     HighOcv = int(orion_bms3_DL[3])

                #     writer = csv.writer(f_orion_bms3)
                #     writer.writerow([time, LowCellVoltage, HighCellVoltage, LowOcv, HighOcv])

                # Dash_error_status
                
                # Dash_error_status_DL = data_on('00081F00',[1,1,2,4])
                # if Dash_error_status_DL != None:
                #     Amkstate = int(Dash_error_status_DL[0])
                #     AMK_Control = int(Dash_error_status_DL[1])

                #     SdcAmsOk = (AMK_Control) & 0b1
                #     SdcImdOk = (AMK_Control >> 1) & 0b1
                #     SdcBspdOk = (AMK_Control >> 2) & 0b1
                #     SdcSen = (AMK_Control >> 3) & 0b1
                #     tsalOn = (AMK_Control >> 4) & 0b1
                #     reserved0 = (AMK_Control >> 5) & 0b1

                #     startCnt = int(Dash_error_status_DL[2])
                #     reserved2 = int(Dash_error_status_DL[3])
                
                Start_btn

                Start_btn_DL = data_on('00081F01',[])

                                
                # amk_setpoint1_rl
                                   
                amk_setpoint1_rl_DL = data_on('00275188',[1,1,2,2,2],line) ## amk_setpoint1_rl_DL[0] is reserved
                if amk_setpoint1_rl_DL != None:
                    AMK_Control = int(amk_setpoint1_rl_DL[1])

                    AMK_bInverterOn = (AMK_Control) & 0b1
                    AMK_bDcOn = (AMK_Control >> 1) & 0b1
                    AMK_bEnable = (AMK_Control >> 2) & 0b1
                    AMK_bErrorReset = (AMK_Control >> 3) & 0b1

                    AMK_Torque_setpoint = compareValues_32767(int(amk_setpoint1_rl_DL[2]))
                    AMK_TorqueLimitPositv = compareValues_32767(int(amk_setpoint1_rl_DL[3]))
                    AMK_TorqueLimitNegativ = compareValues_32767(int(amk_setpoint1_rl_DL[4]))

                    writer = csv.writer(f_amk_setpoint1_rl)
                    writer.writerow([time, AMK_bInverterOn, AMK_bDcOn, AMK_bEnable, AMK_bErrorReset, AMK_Torque_setpoint, AMK_TorqueLimitPositv, AMK_TorqueLimitNegativ])


                # amk_setpoint1_rr
           
                amk_setpoint1_rr_DL = data_on('00275189',[1,1,2,2,2],line) # amk_setpoint1_rr_DL[0] is reserved
                if amk_setpoint1_rr_DL != None:
                    AMK_Control = int(amk_setpoint1_rr_DL[1])

                    AMK_bInverterOn = (AMK_Control) & 0b1
                    AMK_bDcOn = (AMK_Control >> 1) & 0b1
                    AMK_bEnable = (AMK_Control >> 2) & 0b1
                    AMK_bErrorReset = (AMK_Control >> 3) & 0b1

                    AMK_Torque_setpoint = compareValues_32767(int(amk_setpoint1_rr_DL[2]))
                    AMK_TorqueLimitPositv = compareValues_32767(int(amk_setpoint1_rr_DL[3]))
                    AMK_TorqueLimitNegativ = compareValues_32767(int(amk_setpoint1_rr_DL[4]))

                    writer = csv.writer(f_amk_setpoint1_rr)
                    writer.writerow([time, AMK_bInverterOn, AMK_bDcOn, AMK_bEnable, AMK_bErrorReset, AMK_Torque_setpoint, AMK_TorqueLimitPositv, AMK_TorqueLimitNegativ])
                

                # amk_actual_values1_rl
                                                    
                    
                amk_actual_values1_rl_DL = data_on('00275287',[1,1,2,2,2],line) # amk_actual_values1_rl_DL[0] is reserved
                if amk_actual_values1_rl_DL != None:
                    AMK_Status = int(amk_actual_values1_rl_DL[1])

                    AMK_bSystemReady = (AMK_Status) & 0b1
                    AMK_bError = (AMK_Status >> 1) & 0b1
                    AMK_bWarn = (AMK_Status >> 2) & 0b1
                    AMK_bQuitDcOn  = (AMK_Status >> 3) & 0b1
                    AMK_bDcOn = (AMK_Status >> 4) & 0b1
                    AMK_bQuitInverterOn = (AMK_Status >> 5) & 0b1
                    AMK_bInverterOn = (AMK_Status >> 6) & 0b1
                    AMK_bDerating = (AMK_Status >> 7) & 0b1
                    
                    AMK_ActualVelocity = compareValues_32767(int(amk_actual_values1_rl_DL[2]))
                    AMK_TorqueCurrent = compareValues_32767(int(amk_actual_values1_rl_DL[3]))
                    AMK_MagnetizingCurrent = compareValues_32767(int(amk_actual_values1_rl_DL[4]))

                    writer = csv.writer(f_amk_actual_values1_rl)
                    writer.writerow([time, AMK_bSystemReady, AMK_bError, AMK_bWarn, AMK_bQuitDcOn, AMK_bDcOn, AMK_bQuitInverterOn, AMK_bInverterOn, AMK_bDerating, AMK_ActualVelocity, AMK_TorqueCurrent, AMK_MagnetizingCurrent])


                #  amk_actual_values1_rr
                                  
                
                amk_actual_values1_rr_DL = data_on('00275288',[1,1,2,2,2],line) # amk_actual_values1_rr_DL[0] is reserved
                if amk_actual_values1_rr_DL != None:
                    AMK_Status = int(amk_actual_values1_rr_DL[1])

                    AMK_bSystemReady = (AMK_Status) & 0b1
                    AMK_bError = (AMK_Status >> 1) & 0b1
                    AMK_bWarn = (AMK_Status >> 2) & 0b1
                    AMK_bQuitDcOn  = (AMK_Status >> 3) & 0b1
                    AMK_bDcOn = (AMK_Status >> 4) & 0b1
                    AMK_bQuitInverterOn = (AMK_Status >> 5) & 0b1
                    AMK_bInverterOn = (AMK_Status >> 6) & 0b1
                    AMK_bDerating = (AMK_Status >> 7) & 0b1
                    
                    AMK_ActualVelocity = compareValues_32767(int(amk_actual_values1_rr_DL[2]))
                    AMK_TorqueCurrent = compareValues_32767(int(amk_actual_values1_rr_DL[3]))
                    AMK_MagnetizingCurrent = compareValues_32767(int(amk_actual_values1_rr_DL[4]))

                    writer = csv.writer(f_amk_actual_values1_rr)
                    writer.writerow([time, AMK_bSystemReady, AMK_bError, AMK_bWarn, AMK_bQuitDcOn, AMK_bDcOn, AMK_bQuitInverterOn, AMK_bInverterOn, AMK_bDerating, AMK_ActualVelocity, AMK_TorqueCurrent, AMK_MagnetizingCurrent])


                # amk_actual_values2_rr
                               
                amk_actual_values2_rr_DL = data_on('00275289',[2,2,2,2],line)
                if amk_actual_values2_rr_DL != None:
                    AMK_TempMotor = compareValues_32767(int(amk_actual_values2_rr_DL[0])) / 10
                    AMK_TempInverter = compareValues_32767(int(amk_actual_values2_rr_DL[1])) / 10
                    AMK_ErrorInfo = int(amk_actual_values2_rr_DL[2])
                    AMK_TempIGBT = compareValues_32767(int(amk_actual_values2_rr_DL[3])) / 10

                    writer = csv.writer(f_amk_actual_values2_rr)
                    writer.writerow([time, AMK_TempMotor, AMK_TempInverter, AMK_ErrorInfo, AMK_TempIGBT])

                
                # amk_actual_values2_rl    
                
                amk_actual_values2_rl_DL = data_on('0027528A',[2,2,2,2],line)
                if amk_actual_values2_rl_DL != None:
                    AMK_TempMotor = compareValues_32767(int(amk_actual_values2_rl_DL[0])) / 10
                    AMK_TempInverter = compareValues_32767(int(amk_actual_values2_rl_DL[1])) / 10
                    AMK_ErrorInfo = int(amk_actual_values2_rl_DL[2])
                    AMK_TempIGBT = compareValues_32767(int(amk_actual_values2_rl_DL[3])) / 10

                    writer = csv.writer(f_amk_actual_values2_rr)
                    writer.writerow([time, AMK_TempMotor, AMK_TempInverter, AMK_ErrorInfo, AMK_TempIGBT])

                
                # steering_wheel_msg2
                
                steering_wheel_msg2_DL = data_on('00101F01',[2,2],line)
                if steering_wheel_msg2_DL != None:
                    apps = int(steering_wheel_msg2_DL[0]) / 100
                    bpps = int(steering_wheel_msg2_DL[1]) / 100

                    writer = csv.writer(f_steering_wheel_msg2)
                    writer.writerow([time, apps, bpps])               

            # print(f"파일들이 {file_dst}에 저장되었습니다.")

            f.close()
            
        f_orion_bms1.close()
        f_orion_bms2.close()
        f_orion_bms3.close()
        
        f_amk_setpoint1_rl.close()
        f_amk_setpoint1_rr.close()
        f_amk_actual_values1_rl.close()
        f_amk_actual_values2_rl.close()
        f_amk_actual_values1_rr.close()
        f_amk_actual_values2_rr.close()
        
        f_steering_wheel_msg2.close()
    
print('end')