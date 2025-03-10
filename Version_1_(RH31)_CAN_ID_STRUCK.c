// id 0x010
// inv_sequence
// VCU to INVERTER_BOARD

typedef union InvSequence
{
    // infineon tc (VCU)
    // -> uint32_t rx_data[2];
    // stm32 (Dashboard)
    // -> uint8_t rx_data[8];
    // board spec에 따라 다름 위 주석 참조
    uint32_t data[2];
    struct
    {
      struct 
      {
        bool on_ef                :1; // [0]
        bool on_be1               :1; // [1]
        bool on_be2               :1; // [2]
        bool AMK_bSystemReady     :1; // [3]
        bool AMK_bWarn            :1; // [4]
        bool AMK_bSError          :1; // [5]
        bool AMK_bQuitDcOn        :1; // [6]
        bool AMK_bQuitInverterOn  :1; // [7]
      } inv1;
      struct 
      {
        bool on_ef                :1; // [8]
        bool on_be1               :1; // [9]
        bool on_be2               :1; // [10]
        bool AMK_bSystemReady     :1; // [11]
        bool AMK_bWarn            :1; // [12]
        bool AMK_bSError          :1; // [13]
        bool AMK_bQuitDcOn        :1; // [14]
        bool AMK_bQuitInverterOn  :1; // [15]
      } inv2;
      struct 
      {
        bool on_ef                :1; // [16]
        bool on_be1               :1; // [17]
        bool on_be2               :1; // [18]
        bool AMK_bSystemReady     :1; // [19]
        bool AMK_bWarn            :1; // [20]
        bool AMK_bSError          :1; // [21]
        bool AMK_bQuitDcOn        :1; // [22]
        bool AMK_bQuitInverterOn  :1; // [23]
      } inv3;
      struct 
      {
        bool on_ef                :1; // [24]
        bool on_be1               :1; // [25]
        bool on_be2               :1; // [26]
        bool AMK_bSystemReady     :1; // [27]
        bool AMK_bWarn            :1; // [28]
        bool AMK_bSError          :1; // [29]
        bool AMK_bQuitDcOn        :1; // [30]
        bool AMK_bQuitInverterOn  :1; // [31]
      } inv4;
      uint32_t reserved_0         :32; // [32-63]
    } s;
} inv_sequence_t;

// id 0x130
// error_list
// VCU to Dash

typedef union ErrorList
{
    // infineon tc (VCU)
    // -> uint32_t tx_data[2];
    // stm32 (Dashboard)
    // -> uint8_t rx_data[8];
    // board spec에 따라 다름 위 주석 참조
    uint32_t data[2];
    struct
    {
        bool bms_ok                 :1; // [0]
        bool imd_ok                 :1; // [1]
        bool bspd_ok                :1; // [2]
        bool apps_ok                :1; // [3]
        bool bpps_ok                :1; // [4]
        bool tsal_on                :1; // [5]
        bool rtd_on                 :1; // [6]
        bool sdc_sen                :1; // [7]

        struct
        {
            bool AMK_bSystemReady       :1; // [8]
            bool AMK_bError             :1; // [9]
            bool AMK_bWarn              :1; // [10]     
            bool AMK_bQuitDcOn          :1; // [11]
            bool AMK_bQuitInverterOn    :1; // [12]
            bool AMK_bDerating          :1; // [13]
        } fl;

        struct
        {
            bool AMK_bSystemReady       :1; // [14]
            bool AMK_bError             :1; // [15]
            bool AMK_bWarn              :1; // [16]     
            bool AMK_bQuitDcOn          :1; // [17]
            bool AMK_bQuitInverterOn    :1; // [18]
            bool AMK_bDerating          :1; // [19]
        } fr;

        struct
        {
            bool AMK_bSystemReady       :1; // [20]
            bool AMK_bError             :1; // [21]
            bool AMK_bWarn              :1; // [22]     
            bool AMK_bQuitDcOn          :1; // [23]
            bool AMK_bQuitInverterOn    :1; // [24]
            bool AMK_bDerating          :1; // [25]
        } rl;

        struct
        {
            bool AMK_bSystemReady       :1; // [26]
            bool AMK_bError             :1; // [27]
            bool AMK_bWarn              :1; // [28]     
            bool AMK_bQuitDcOn          :1; // [29]
            bool AMK_bQuitInverterOn    :1; // [30]
            bool AMK_bDerating          :1; // [31]
        } rr;
    } s;
} error_list_t;

// id 0x300
// power_limit
// BMS to VCU

typedef union PowerLimit
{
    // infineon tc (VCU)
    // -> uint32_t rx_data[2];
    uint32_t data[2];
    struct
    {
        uint16_t pack_current                   :16;    //[0-15]
        uint16_t pack_voltage                   :16;    //[16-31]
        uint16_t pack_charge_current_limit      :16;    //[32-47]
        uint16_t pack_discharge_current_limit   :16;    //[48-63]
    } s;
} power_limit_t;

// id 0x10000
// battery_diagnose
// BATTERY to VCU

typedef union BatteryDiagnose
{
    // stm32 (battery_board)
    // -> uint32_t tx_data[2];
    // infineon tc (VCU)
    // -> uint32_t rx_data[2];
    uint32_t data[2];
    struct
    {
        uint8_t precharge_state_signal1     :8; //[0-7]
        uint8_t precharge_state_signal2     :8; //[8-15]
        uint8_t relay_contact_signal1       :8; //[16-23]
        uint8_t relay_contact_signal2	    :8; //[24-31]
        uint8_t relay_contact_signal3	    :8; //[32-39]
        uint8_t tsal_signal			        :8; //[40-47]
        uint8_t IMD_status_frequency	    :8; //[48-55]
        uint8_t reserved			        :8; //[56-63]
    } s;
} battery_diagnose_t;

// id 0x20000
// cooling_on
// VCU to COOLING

typedef union CoolingOn
{
    // infineon tc (VCU)
    // -> uint32_t tx_data[2];
    uint32_t data[2];
    struct
    {
        bool manual_mode_on         :1;     //[0]
        bool water_pump0_on         :1;     //[1]
        bool water_pump1_on         :1;     //[2]
        bool radiator0_on           :1;     //[3]
        bool radiator1_on           :1;     //[4]
        bool external_fan           :1;     //[5]
        bool on_all                 :1;     //[6]
        bool rst                    :1;     //[7]
        uint8_t reserved_0          :8;     //[8-15]
        uint16_t reserved_1         :16;    //[16-31]
        uint32_t reserved_2         :32;    //[32-63]
    } s;
} cooling_on_t;

// id 0x20001
// fan_status_data
// BATTERY to VCU

typedef union FanStatusData
{
    // stm32 (battery_board)
    // -> uint32_t tx_data[2];
    // infineon tc (VCU)
    // -> uint32_t rx_data[2];
    uint32_t data[2];
    struct
    {
        uint8_t FanFlag			    :8; //[0-7]
        uint8_t TIM15_Dutycycle     :8; //[8-15]
        uint8_t TIM15_Frequency     :8; //[16-23]
        uint8_t TIM16_Dutycycle     :8; //[24-31]
        uint8_t TIM16_Frequency     :8; //[32-39]
        uint8_t TIM17_Dutycycle     :8; //[40-47]
        uint8_t TIM17_Frequency     :8; //[48-55]
        uint8_t desiredDuty			:8; //[56-63]
    } s;
} fan_status_data_t;

// id 0x20002
// fan_target_duty
// BATTERY to VCU

typedef union FanTargetDuty
{
    // stm32 (battery_board)
    // -> uint32_t tx_data[2];
    // infineon tc (VCU)
    // -> uint32_t rx_data[2];
    uint32_t data[2];
    struct
    {
        uint8_t TargetDuty_SideIntake           :8;     //[0-7]
        uint8_t TargetDuty_SegmentIntake70      :8;     //[8-15]
        uint8_t TargetDuty_SegmentExhaust60     :8;     //[16-23]
        uint8_t TargetDuty_SegmentExhaust80     :8;     //[24-31]
        uint32_t reserved_0                     :32;    //[32-63]
    } s;
} fan_target_duty_t;

// id 0x30000
// bms_temp_and_soc
// BMS to VCU

typedef union BmsTempAndSoc
{
    // infineon tc (VCU)
    // -> uint32_t rx_data[2];
    uint32_t data[2];
    struct
    {
        uint8_t   high_temp     :8;     // [0-7]
        uint8_t   avg_temp      :8;     // [8-15]
        uint8_t   bms_temp      :8;     // [16-23]
        uint8_t   pack_soc      :8;     // [24-31]
        uint16_t  dtc_status_1  :16;    // [32-47]
        uint8_t   dtc_status_2  :8;     // [48-55]
        uint8_t   reserved_0    :8;     // [56-63]
    } s;
} bms_temp_and_soc_t;

// id 0x40000
// bms_voltage
// BMS to VCU

typedef union BmsVoltage
{
    // infineon tc (VCU)
    // -> uint32_t rx_data[2];
    uint32_t data[2];
    struct
    {
        uint16_t low_cell_voltage           :16;    //[0-15]
        uint16_t high_cell_voltage          :16;    //[16-31]
        uint16_t low_open_cell_voltage      :16;    //[32-47]
        uint16_t high_open_cell_voltage     :16;    //[48-63]
    } s;
} bms_voltage_t;

// id 0x40100
// amk_setpoint1_fl
// VCU to LOGGER

typedef union AmkSetpoint1_FL
{
    // infineon tc (VCU)
    // -> uint32_t tx_data[2];
    uint32_t data[2];
    struct
    {
        uint8_t AMK_bReserve1           :8;         //[0-7]
        bool AMK_bInverterOn            :1;         //[8]
        bool AMK_bDcOn                  :1;         //[9]
        bool AMK_bEnable                :1;         //[10]
        bool AMK_bErrorReset            :1;         //[11]
        uint8_t AMK_bReserve2           :4;         //[12-15]
        sint16_t AMK_Torque_setpoint    :16;	    //[16-31]
        sint16_t AMK_TorqueLimitPositv  :16;        //[32-47]
        sint16_t AMK_TorqueLimitNegativ :16;        //[48-63]
    } s;
} amk_setpoint1_fl_t;

// id 0x40101
// amk_setpoint1_fr
// VCU to LOGGER

typedef union AmkSetpoint1_FR
{
    // infineon tc (VCU)
    // -> uint32_t tx_data[2];
    uint32_t data[2];
    struct
    {
        uint8_t AMK_bReserve1           :8;         //[0-7]
        bool AMK_bInverterOn            :1;         //[8]
        bool AMK_bDcOn                  :1;         //[9]
        bool AMK_bEnable                :1;         //[10]
        bool AMK_bErrorReset            :1;         //[11]
        uint8_t AMK_bReserve2           :4;         //[12-15]
        sint16_t AMK_Torque_setpoint    :16;	    //[16-31]
        sint16_t AMK_TorqueLimitPositv  :16;        //[32-47]
        sint16_t AMK_TorqueLimitNegativ :16;        //[48-63]
    } s;
} amk_setpoint1_fr_t;

// id 0x40102
// amk_actual_values1_fl
// VCU to LOGGER

typedef union AmkActualValues1_FL
{
    // infineon tc (VCU)
    // -> uint32_t tx_data[2];
    uint32_t data[2];
    struct
    {
        uint8_t AMK_bReserve                    :8;         //[0-7]
        bool AMK_bSystemReady                   :1;         //[8]
        bool AMK_bSError                        :1;         //[9]
        bool AMK_bWarn                          :1;         //[10]
        bool AMK_bQuitDcOn                      :1;         //[11]
        bool AMK_bDcOn                          :1;         //[12]
        bool AMK_bQuitInverterOn                :1;         //[13]
        bool AMK_bInverterOn                    :1;         //[14]
        bool AMK_bDerating                      :1;         //[15]
        sint16_t AMK_ActualVelocity             :16;        //[16-31]
        sint16_t AMK_TorqueCurrent              :16;        //[32-47]
        sint16_t AMK_MagnetizingCurrent         :16;        //[48-63]
    } s;
} amk_actual_values1_fl_t;

// id 0x40103
// amk_actual_values1_fr
// VCU to LOGGER

typedef union AmkActualValues1_FR
{
    // infineon tc (VCU)
    // -> uint32_t tx_data[2];
    uint32_t data[2];
    struct
    {
        uint8_t AMK_bReserve                    :8;     //[0-7]
        bool AMK_bSystemReady                   :1;     //[8]
        bool AMK_bSError                        :1;     //[9]
        bool AMK_bWarn                          :1;     //[10]
        bool AMK_bQuitDcOn                      :1;     //[11]
        bool AMK_bDcOn                          :1;     //[12]
        bool AMK_bQuitInverterOn                :1;     //[13]
        bool AMK_bInverterOn                    :1;     //[14]
        bool AMK_bDerating                      :1;     //[15]
        sint16_t AMK_ActualVelocity             :16;    //[16-31]
        sint16_t AMK_TorqueCurrent              :16;    //[32-47]
        sint16_t AMK_MagnetizingCurrent         :16;    //[48-63]
    } s;
} amk_actual_values1_fr_t;

// id 0x40104
// amk_actual_values2_fl
// VCU to LOGGER

typedef union AmkActualValues2_FL
{
    // infineon tc (VCU)
    // -> uint32_t tx_data[2];
    uint32_t data[2];
    struct
    {
        sint16_t AMK_TempMotor      :16;    //[0-15]
        sint16_t AMK_TempInverter   :16;    //[16-31]
        uint16_t AMK_ErrorInfo      :16;    //[32-47]
        sint16_t AMK_TempIGBT       :16;    //[48-63]
    } s;
} amk_actual_values2_fl_t;

// id 0x40105
// amk_actual_values2_fr
// VCU to LOGGER

typedef union AmkActualValues2_FR
{
    // infineon tc (VCU)
    // -> uint32_t tx_data[2];
    uint32_t data[2];
    struct
    {
        sint16_t AMK_TempMotor      :16;    //[0-15]
        sint16_t AMK_TempInverter   :16;    //[16-31]
        uint16_t AMK_ErrorInfo      :16;    //[32-47]
        sint16_t AMK_TempIGBT       :16;    //[48-63]
    } s;
} amk_actual_values2_fr_t;

// id 0x40300
// steering_and_pedal
// VCU to LOGGER

typedef union SteeringAndPedal
{
    // infineon tc (VCU)
    // -> uint32_t tx_data[2];
    uint32_t data[2];
    struct
    {
        uint16_t steering_angel     :16;    //[0-15]
        uint8_t apps                :8;     //[16-23]
        uint8_t bpps                :8;     //[24-31]
        uint16_t brake_pressure     :16;    //[32-47]
        uint16_t reserved_0         :16;    //[48-63]
    } s;
} steering_and_pedal_t;

// id 0x40301
// gear_temp
// INVERTOR_BOARD to LOGGER

typedef union GearTemp
{
    // stm32 (invertor_board)
    // -> uint32_t tx_data[2];
    uint32_t data[2];
    struct
    {
        uint16_t gear_temp_fl     :16;    //[0-15]
        uint16_t gear_temp_fr     :16;    //[16-31]
        uint16_t gear_temp_rl     :16;    //[32-47]
        uint16_t gear_temp_rr     :16;    //[48-63]
    } s;
} gear_temp_t;

