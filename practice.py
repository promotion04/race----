constlist = [2, 2, 1]
line = ["0001", "0", "86", "00001F00", "00", "00", "BC", "0E", "C1", "8B"]

# ex) constlist = [2, 4, 1] 는 16,32,8 비트로 데이터를 패킹 reserved된 값이 있다면 list로 뽑고 추후에 변형
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

# 첫 번째 line 데이터 추출
if line[3] == '00001F00' and len(line) >= 10:
    packCurrent = int(line[5] + line[4], 16)
    packVoltage = int(line[7] + line[6], 16)
    packSoc = int(line[8], 16)
    
    print(f"packCurrent: {packCurrent}")
    print(f"packVoltage: {packVoltage}")
    print(f"packSoc: {packSoc}")
else:
    print("line 조건이 맞지 않아서 데이터를 추출할 수 없습니다.")

# data_on 함수 호출
datalist = data_on('00001F00', constlist, line)
print("datalist:", datalist)

# 두 번째 line 설정 후 AMK_Control 데이터 추출
line = ["0001", "0", "88", "00275188", "00", "07", "00", "00", "5F", "08", "A1", "F7"]

if line[3] == '00275188' and len(line) >= 10:
    AMK_Control = int(line[5], 16) # line[4] is reserved
    AMK_Torque_setpoint = int(line[7] + line[6], 16)
    AMK_TorqueLimitPositv = int(line[9] + line[8], 16)
    AMK_TorqueLimitNegativ = int(line[11] + line[10], 16)

    print(f"AMK_Control: {AMK_Control}")
    print(f"AMK_Torque_setpoint: {AMK_Torque_setpoint}")
    print(f"AMK_TorqueLimitPositv: {AMK_TorqueLimitPositv}")
    print(f"AMK_TorqueLimitNegativ: {AMK_TorqueLimitNegativ}")

# 두 번째 line으로 data_on 함수 호출
datalist = data_on('00275188', [1, 1, 2, 2, 2], line)
print("datalist:", datalist)
