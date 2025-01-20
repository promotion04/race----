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


for folder_name in os.listdir(base_directory): # 최상위 폴더에 있는 모든 하위폴더 처리
    source_directory = os.path.join(base_directory, folder_name)
    
    if not os.path.isdir(source_directory):
        continue
    
    New_directory = os.path.join(base_directory, 'org_src', folder_name)

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
        new_folder_name = os.path.splitext(foldername)[0] # 폴더 이름에서 파일 확장자 제거
        new_folder_path = os.path.join(New_directory, new_folder_name)
        
        os.makedirs(new_folder_path, exist_ok=True)
        
               
        for filename in Detail_file_list[start:end + 1]:
            if 'START' not in filename:
                source_file = os.path.join(source_directory, filename)
                destination_file = os.path.join(new_folder_path, filename)
                shutil.copy(source_file, destination_file)
        
    #     print(f"파일들이 {new_folder_path}에 저장되었습니다.")
    
    # print(f"모든 파일이 {New_directory}에 저장되었습니다.")

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
        return []
# 캡슐화
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
                
                # orion_bms1_DL = data_on('00001F00',[2,2,1],line)
                # packCurrent = compareValues_32767(int(orion_bms1_DL[0]))
                
                # packVoltage = int(orion_bms1_DL[1]) / 10
                
                # packSoc = int(orion_bms1_DL[2]) / 2
                
                # packPower = packCurrent * packVoltage // 1000

                # writer = csv.writer(f_orion_bms1)
                # writer.writerow([time, packCurrent, packVoltage, packSoc, packPower])

                # orion_bms2    
                if line[3] == '00001F01':
                    if len(line) < 10:
                        continue
                        
                    packChargeLimit = int(line[5] + line[4], 16)
                    if packChargeLimit > 32767:
                        packChargeLimit -= 65536
                        
                    packDischargeLimit = int(line[7] + line[6], 16)
                    if packDischargeLimit > 32767:
                        packDischargeLimit -= 65536
                    packDischargeLimit /= 10 # A 단위 맞추기
                    
                    writer = csv.writer(f_orion_bms2)
                    writer.writerow([time, packChargeLimit, packDischargeLimit])
                
                # orion_bms2_DL = data_on('00001F01',[2,2],line)

                # packChargeLimit = compareValues_32767(int(orion_bms2_DL[0]))
                # packDischargeLimit = compareValues_32767(int(orion_bms2_DL[1]))
                # packDischargeLimit /= 10 # A 단위 맞추기
                
                # writer = csv.writer(f_orion_bms2)
                # writer.writerow([time, packChargeLimit, packDischargeLimit])

                # orion_bms3    
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

                # orion_bms3_DL = data_on('00001F02',[1,1,1,1,2],line)

                # highTemp = compareValues_127(int(orion_bms3_DL[0]))
                # highCell = int(orion_bms3_DL[1])
                # avgTemp = compareValues_127(int(orion_bms3_DL[2]))
                # bmsTemp = compareValues_127(int(orion_bms3_DL[3]))
                # lowVoltage = int(orion_bms3_DL[4]) / 10000

                # writer = csv.writer(f_orion_bms3)
                # writer.writerow([time, highTemp, highCell, avgTemp, bmsTemp, lowVoltage])

                
                # amk_setpoint1_rl
                if line[3] == '00275188':
                    if len(line) < 12:
                        continue
                        
                    AMK_Control = int(line[5], 16) # line[4] is reserved

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

                # amk_setpoint1_rl_DL = data_on('00275188',[1,1,2,2,2],line) ## amk_setpoint1_rl_DL[0] is reserved

                # AMK_Control = int(amk_setpoint1_rl_DL[1])
                # AMK_Torque_setpoint = compareValues_32767(int(amk_setpoint1_rl_DL[2]))
                # AMK_TorqueLimitPositv = compareValues_32767(int(amk_setpoint1_rl_DL[3]))
                # AMK_TorqueLimitNegativ = compareValues_32767(int(amk_setpoint1_rl_DL[4]))

                # writer = csv.writer(f_amk_setpoint1_rl)
                # writer.writerow([time, AMK_bInverterOn, AMK_bDcOn, AMK_bEnable, AMK_bErrorReset, AMK_Torque_setpoint, AMK_TorqueLimitPositv, AMK_TorqueLimitNegativ])


                # amk_setpoint1_rr
                if line[3] == '00275189':
                    if len(line) < 12:
                        continue
                
                    AMK_Control = int(line[5], 16) # line[4] is reserved

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
                
                # amk_setpoint1_rr_DL = data_on('00275189',[1,1,2,2,2],line) # amk_setpoint1_rr_DL[0] is reserved

                # AMK_Control = int(amk_setpoint1_rr_DL[1])
                # AMK_Torque_setpoint = compareValues_32767(int(amk_setpoint1_rr_DL[2]))
                # AMK_TorqueLimitPositv = compareValues_32767(int(amk_setpoint1_rr_DL[3]))
                # AMK_TorqueLimitNegativ = compareValues_32767(int(amk_setpoint1_rr_DL[4]))

                # writer = csv.writer(f_amk_setpoint1_rr)
                # writer.writerow([time, AMK_bInverterOn, AMK_bDcOn, AMK_bEnable, AMK_bErrorReset, AMK_Torque_setpoint, AMK_TorqueLimitPositv, AMK_TorqueLimitNegativ])
              

                # amk_actual_values1_rl
                if line[3] == '00275287':
                    if len(line) < 12:
                        continue
                    
                    AMK_Status = int(line[5], 16) # line[4] is reserved
                    
                    AMK_bSystemReady = (AMK_Status) & 0b1
                    AMK_bError = (AMK_Status >> 1) & 0b1
                    AMK_bWarn = (AMK_Status >> 2) & 0b1
                    AMK_bQuitDcOn  = (AMK_Status >> 3) & 0b1
                    AMK_bDcOn = (AMK_Status >> 4) & 0b1
                    AMK_bQuitInverterOn = (AMK_Status >> 5) & 0b1
                    AMK_bInverterOn = (AMK_Status >> 6) & 0b1
                    AMK_bDerating = (AMK_Status >> 7) & 0b1
                    
                    AMK_ActualVelocity = int(line[7] + line[6], 16)
                    if AMK_ActualVelocity > 32767:
                        AMK_ActualVelocity -= 65536
                        
                    AMK_TorqueCurrent = int(line[9] + line[8], 16)
                    if AMK_TorqueCurrent > 32767:
                        AMK_TorqueCurrent -= 65536
                        
                    AMK_MagnetizingCurrent = int(line[11] + line[10], 16)
                    if AMK_MagnetizingCurrent > 32767:
                        AMK_MagnetizingCurrent -= 65536
                        
                    writer = csv.writer(f_amk_actual_values1_rl)
                    writer.writerow([time, AMK_bSystemReady, AMK_bError, AMK_bWarn, AMK_bQuitDcOn, AMK_bDcOn, AMK_bQuitInverterOn, AMK_bInverterOn, AMK_bDerating, AMK_ActualVelocity, AMK_TorqueCurrent, AMK_MagnetizingCurrent])

                # amk_actual_values1_rl_DL = data_on('00275287',[1,1,2,2,2],line) # amk_actual_values1_rl_DL[0] is reserved

                # AMK_Status = int(amk_actual_values1_rl_DL[1])
                # AMK_ActualVelocity = compareValues_32767(int(amk_actual_values1_rl_DL[2]))
                # AMK_TorqueCurrent = compareValues_32767(int(amk_actual_values1_rl_DL[3]))
                # AMK_MagnetizingCurrent = compareValues_32767(int(amk_actual_values1_rl_DL[4]))

                # writer = csv.writer(f_amk_actual_values1_rl)
                # writer.writerow([time, AMK_bSystemReady, AMK_bError, AMK_bWarn, AMK_bQuitDcOn, AMK_bDcOn, AMK_bQuitInverterOn, AMK_bInverterOn, AMK_bDerating, AMK_ActualVelocity, AMK_TorqueCurrent, AMK_MagnetizingCurrent])


                #  amk_actual_values1_rr
                if line[3] == '00275288':
                    if len(line) < 12:
                        continue
                    
                    AMK_Status = int(line[5], 16) # line[4] is reserved
                    
                    AMK_bSystemReady = (AMK_Status) & 0b1
                    AMK_bError = (AMK_Status >> 1) & 0b1
                    AMK_bWarn = (AMK_Status >> 2) & 0b1
                    AMK_bQuitDcOn  = (AMK_Status >> 3) & 0b1
                    AMK_bDcOn = (AMK_Status >> 4) & 0b1
                    AMK_bQuitInverterOn = (AMK_Status >> 5) & 0b1
                    AMK_bInverterOn = (AMK_Status >> 6) & 0b1
                    AMK_bDerating = (AMK_Status >> 7) & 0b1
                    
                    AMK_ActualVelocity = int(line[7] + line[6], 16)
                    if AMK_ActualVelocity > 32767:
                        AMK_ActualVelocity -= 65536
                        
                    AMK_TorqueCurrent = int(line[9] + line[8], 16)
                    if AMK_TorqueCurrent > 32767:
                        AMK_TorqueCurrent -= 65536
                        
                    AMK_MagnetizingCurrent = int(line[11] + line[10], 16)
                    if AMK_MagnetizingCurrent > 32767:
                        AMK_MagnetizingCurrent -= 65536
                        
                    writer = csv.writer(f_amk_actual_values1_rr)
                    writer.writerow([time, AMK_bSystemReady, AMK_bError, AMK_bWarn, AMK_bQuitDcOn, AMK_bDcOn, AMK_bQuitInverterOn, AMK_bInverterOn, AMK_bDerating, AMK_ActualVelocity, AMK_TorqueCurrent, AMK_MagnetizingCurrent])

                # amk_actual_values1_rr_DL = data_on('00275288',[1,1,2,2,2],line) # amk_actual_values1_rr_DL[0] is reserved

                # AMK_Status = int(amk_actual_values1_rr_DL[1])
                # AMK_ActualVelocity = compareValues_32767(int(amk_actual_values1_rr_DL[2]))
                # AMK_TorqueCurrent = compareValues_32767(int(amk_actual_values1_rr_DL[3]))
                # AMK_MagnetizingCurrent = compareValues_32767(int(amk_actual_values1_rr_DL[4]))

                # writer = csv.writer(f_amk_actual_values1_rr)
                # writer.writerow([time, AMK_bSystemReady, AMK_bError, AMK_bWarn, AMK_bQuitDcOn, AMK_bDcOn, AMK_bQuitInverterOn, AMK_bInverterOn, AMK_bDerating, AMK_ActualVelocity, AMK_TorqueCurrent, AMK_MagnetizingCurrent])


                # amk_actual_values2_rr
                if line[3] == '00275289':
                    if len(line) < 12:
                        continue
                    
                    AMK_TempMotor  = int(line[5] + line[4], 16)
                    if AMK_TempMotor > 32767:
                        AMK_TempMotor -= 65536
                        
                    AMK_TempMotor /= 10
                        
                    AMK_TempInverter = int(line[7] + line[6], 16)
                    if AMK_TempInverter > 32767:
                        AMK_TempInverter -= 65536
                        
                    AMK_TempInverter /= 10
                        
                    AMK_ErrorInfo = int(line[9] + line[8], 16)
                    
                    AMK_TempIGBT = int(line[11] + line[10], 16)
                    if AMK_TempIGBT > 32767:
                        AMK_TempIGBT -= 65536
                        
                    AMK_TempIGBT /= 10
                    
                    writer = csv.writer(f_amk_actual_values2_rr)
                    writer.writerow([time, AMK_TempMotor, AMK_TempInverter, AMK_ErrorInfo, AMK_TempIGBT])
                
                
                # amk_actual_values2_rr_DL = data_on('00275289',[2,2,2,2],line)

                # AMK_TempMotor = compareValues_32767(int(amk_actual_values2_rr_DL[0])) / 10
                # AMK_TempInverter = compareValues_32767(int(amk_actual_values2_rr_DL[1])) / 10
                # AMK_TempInverter = int(amk_actual_values2_rr_DL[2])
                # AMK_TempIGBT = compareValues_32767(int(amk_actual_values2_rr_DL[3])) / 10

                # writer = csv.writer(f_amk_actual_values2_rr)
                # writer.writerow([time, AMK_TempMotor, AMK_TempInverter, AMK_ErrorInfo, AMK_TempIGBT])

                
                # amk_actual_values2_rl    
                if line[3] == '0027528A':
                    if len(line) < 12:
                        continue
                    
                    AMK_TempMotor  = int(line[5] + line[4], 16)
                    if AMK_TempMotor > 32767:
                        AMK_TempMotor -= 65536
                        
                    AMK_TempMotor /= 10
                        
                    AMK_TempInverter = int(line[7] + line[6], 16)
                    if AMK_TempInverter > 32767:
                        AMK_TempInverter -= 65536
                        
                    AMK_TempInverter /= 10
                        
                    AMK_ErrorInfo = int(line[9] + line[8], 16)
                    
                    AMK_TempIGBT = int(line[11] + line[10], 16)
                    if AMK_TempIGBT > 32767:
                        AMK_TempIGBT -= 65536
                        
                    AMK_TempIGBT /= 10
                    
                    writer = csv.writer(f_amk_actual_values2_rl)
                    writer.writerow([time, AMK_TempMotor, AMK_TempInverter, AMK_ErrorInfo, AMK_TempIGBT])

                # amk_actual_values2_rl_DL = data_on('0027528A',[2,2,2,2],line)

                # AMK_TempMotor = compareValues_32767(int(amk_actual_values2_rl_DL[0])) / 10
                # AMK_TempInverter = compareValues_32767(int(amk_actual_values2_rl_DL[1])) / 10
                # AMK_TempInverter = int(amk_actual_values2_rl_DL[2])
                # AMK_TempIGBT = compareValues_32767(int(amk_actual_values2_rl_DL[3])) / 10

                # writer = csv.writer(f_amk_actual_values2_rr)
                # writer.writerow([time, AMK_TempMotor, AMK_TempInverter, AMK_ErrorInfo, AMK_TempIGBT])

                
                # steering_wheel_msg2
                if line[3] == '00101F01':
                    if len(line) < 12:
                        continue
                    
                    apps = int(line[5] + line[4], 16)
                    apps /= 100
                    
                    bpps = int(line[7] + line[6], 16)
                    bpps /= 100
                    
                    writer = csv.writer(f_steering_wheel_msg2)
                    writer.writerow([time, apps, bpps])

                # steering_wheel_msg2_DL = data_on('00101F01',[2,2],line)

                # apps = int(steering_wheel_msg2_DL[0]) / 100
                # bpps = int(steering_wheel_msg2_DL[1]) / 100

                # writer = csv.writer(f_steering_wheel_msg2)
                # writer.writerow([time, apps, bpps])               

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
