#TCatv3_TankInfoList
#TankCombat_alpha-test_ver_3의 전차 정보 리스트. Made By PYS3301man.
#제작기간 = 시작: 2025-11-01 | 종료: 2025-1
#이전 버젼(TCatv2_TankInfoList)를 계승한 코드.

# 포탄 리스트 ['포탄 이름', '포탄 종류', '관통력', '피해량(고폭탄은 작약량)', '작약량(날대탄은 관-피-작 으로 기입)']
#|WW2_Early_USAm_Tank_List
weSM51B1_37M6                                  = [ 'M51B1',  'APCBC', 84,  35]                             #M3A1_Stuart
weSM61_75M3, weSM48_75M3_o                     = [   'M61',  'APCBC',102,  75], [   'M48',  'HE', 10, 666] #M4A1_Sherman
weSM51B1_37M5                                  = [ 'M51B1',  'APCBC', 84,  25]                             #M3_Lee_MG
weSM61_75M2, weSM48_75M2_s                     = [   'M61',  'APCBC', 95,  75], [   'M48',  'HE', 10, 666] #M3_Lee_SG
weSM62_76M7, weSM42A1_76M7                     = [   'M62',  'APCBC',146, 110], [ 'M42A1',  'HE', 16, 390] #M10_GMC
#|WW2_Middle_USAm_Tank_List
wmSM62_76M1_o, wmSM42A1_76M1_o, wmSM93_76M1_o  = [   'M62',  'APCBC',146, 120], [ 'M42A1',  'HE', 16, 390], [   'M93',   'APCR',191, 60] #M18_GMC
wmSM82_90M3_o, wmSM71_90M3_o, wmSM304_90M3_o   = [   'M82',  'APCBC',183, 190], [   'M71',  'HE', 20,1200], [  'M304',   'APCR',281, 80] #M26_Pershing
wmSM62_76M1_s, wmSM42A1_76M1_s, wmSM93_76M1_s  = [   'M62',  'APCBC',146, 180], [ 'M42A1',  'HE', 16, 390], [   'M93',   'APCR',191, 60] #M4A3E2_76_W_Jumbo
wmSM82_90M3_s, wmSM71_90M3_s, wmSM304_90M3_s, wmSM348_90M3_o = [   'M82',  'APCBC',183, 200], [   'M71',  'HE', 20,1200], [  'M304',   'APCR',281, 80], [  'M348', 'HEATFS',305, 220, 930] #M36B2
#|WW2_Late_USAm_Tank_List
wlSM331A2_76M32_o, wlSM352_76M32_o             = ['M331A2',   'APDS',296, 180], [  'M352',  'HE', 15, 662]          #M41A1_WalkerBulldog
wlSM348_90M3_s, wlSM82_90M3_s, wlSM71_90M3_o   = [  'M348', 'HEATFS',305, 260, 930], [   'M82',  'APCBC',183, 210], [   'M71',  'HE', 20,1200] #M46_Patton
wlST14E3_120T53, wlSM73_120T53                 = [ 'T14E3',  'APCBC',279, 300], [   'M73',  'HE', 31,2400]          #T34
wlSM431_90M54, wlSM71_90M54                    = [  'M431', 'HEATFS',320, 290, 710], [   'M71',     'HE', 20,1200]  #M56_Scorpion
#|Korean_War_USAm_Tank_List
kwSM331A2_76M32_s, kwSM352_76M32_s             = ['M331A2',   'APDS',296, 180], [  'M352',  'HE', 15, 662]          #M41A1_WalkerBulldog_s
kwSM348_90M3_t, kwSM82_90M3_t, kwSM71_90M3_s   = [  'M348', 'HEATFS',305, 260, 930], [   'M82',  'APCBC',183, 210], [   'M71',  'HE', 20,1200] #M46_Patton_s
kwSM62_76M1_t, kwSM42A1_76M1_t, kwSM93_76M1_t  = [   'M62',  'APCBC',146, 180], [ 'M42A1',  'HE', 16, 390], [   'M93',   'APCR',191, 60]                   #M4A3E8_76_W_HVSS
kwSM82_90M3_t, kwSM71_90M3_t, kwSM304_90M3_t, kwSM348_90M3_s = [   'M82',  'APCBC',183, 200], [   'M71',  'HE', 20,1200], [  'M304',   'APCR',281, 80], [  'M348', 'HEATFS',305, 220, 930] #M36B2_s

# 전차 형체 리스트 [체력, 차체장갑, 포탑장갑, 속도]
#|WW2_Early_USAm_Tank_List
M3A1_I                  = [100, 38, 38,  58]
M4A1_I                  = [210, 51, 76,  39]
M3_I                    = [215, 51, 50,  39]
M10_I                   = [190, 51, 57,  39]
#|WW2_Middle_USAm_Tank_List
M18_I                   = [100, 12, 25,  80]
M26_I                   = [300,101,101,  48]
M4A3E2_76J_I            = [375,101,177,  42]
M38B2_o_I               = [220, 38, 76,  40]
#|WW2_Late_USAm_Tank_List
M41A1_o_I               = [300, 31, 25,  72]
M46_o_I                 = [400,101,101,  48]
M34_I                   = [550,102,203,  35]
M56_I                   = [280,  0,  5,  45]
#|Korean_War_USAm_Tank_List
M41A1_s_I               = [300, 31, 25,  72]
M46_s_I                 = [400,101,101,  48]
M4A3E8_76HVSS_I         = [370,101,177,  48]
M38B2_s_I               = [220, 38, 76,  40]

# 전차 주포 리스트 [주포 이름, 재장전 시간, 사용하는 포탄]
#|WW2_Early_USAm_Tank_List
weC37mmM6               = [ '37mm M6', 3.7,    weSM51B1_37M6]                                     #M3A1_Stuart
weC75mmM3               = [ '75mm M3', 6.5,      weSM61_75M3,    weSM48_75M3_o]                   #M4A1_Sherman
weC37mmM5, weC75mmM2    = [ '37mm M5', 3.7,    weSM51B1_37M5], ['75mm M2', 6.2, weSM61_75M2, weSM48_75M2_s] #M3_Lee
weC76mmM7               = [ '76mm M7', 6.5,      weSM62_76M7,    weSM42A1_76M7]                   #M10_GMC
#|WW2_Middle_USAm_Tank_List
wmC76mmM1               = [ '76mm M1', 7.9,    wmSM62_76M1_o, wmSM42A1_76M1_o,  wmSM93_76M1_o]     #M18_GMC
wmC90mmM3_o             = [ '90mm M3', 9.7,    wmSM82_90M3_o,   wmSM71_90M3_o, wmSM304_90M3_o]     #M26_Pershing
wmC76mmM1               = [ '76mm M1', 7.6,    wmSM62_76M1_s, wmSM42A1_76M1_s,  wmSM93_76M1_s]     #M4A3E2_76_W_Jumbo
wmC90mmM3_s             = [ '90mm M3', 9.7,    wmSM82_90M3_s,   wmSM71_90M3_s, wmSM304_90M3_s, wmSM348_90M3_o] #M36B2
#|WW2_Late_USAm_Tank_List
wlC76mmM32_o            = ['76mm M32', 7.6,wlSM331A2_76M32_o, wlSM352_76M32_o]                   #M41A1_WalkerBulldog
wlC90mmM3A1_o           = ['90mmM3A1', 9.7,   wlSM348_90M3_s,   wlSM82_90M3_s,  wlSM71_90M3_o]                   #M46_Patton
wlC120mmT53             = ['120mmT53',19.4,  wlST14E3_120T53,   wlSM73_120T53]                   #T34
wlC90mmM54              = [ '90mmM54', 9.7,    wlSM431_90M54,    wlSM71_90M54]                   #M56_Scorpion
#|Korean_War_USAm_Tank_List
kwC76mmM32_s            = [ '76mmM32', 7.6,kwSM331A2_76M32_s, kwSM352_76M32_s]                   #M41A1_WalkerBulldog_s
kwC90mmM3A1_s           = ['90mmM3A1', 9.7,   kwSM348_90M3_t,   kwSM82_90M3_t,  kwSM71_90M3_s]                   #M46_Patton_s
kwC76mmM1A2             = ['76mmM1A2', 7.6,    kwSM62_76M1_t, kwSM42A1_76M1_t,  kwSM93_76M1_t]                   #M4A3E8_76_W_HVSS
kwC90mmM3_t             = [  '90mmM3', 9.7,    kwSM82_90M3_t,   kwSM71_90M3_t, kwSM304_90M3_t, kwSM348_90M3_s]                   #M36B2_s

# 난이도 리스트 [난이도 이름, 등장하는 적 전차의 수, 적의 명중률, 보상 배율]
# 참고용: W2E W2M W2L KRW VNW CDW IRW MDW FTW
SafeZone      = [        'Test',  5,    0, 0.0] # 0
VeryEasy      = [    'VeryEasy',  5,   15, 1.0] # 1
Easy          = [        'Easy',  6,   20, 1.1] # 2
Normal        = [      'Normal',  7,   33, 1.2] # 3
Abnormal      = [    'Abnormal', 10,   45, 1.3] # 4
LittleHard    = [ 'Little Hard', 12,   60, 1.4] # 5
Hard          = [        'Hard', 12,   70, 1.6] # 6
VertHard      = [    'VertHard', 15,   75, 1.7] # 7
Danger        = [      'Danger', 15,   80, 1.8] # 8
Extreme       = [     'Extreme', 17,   90, 2.0] # 9

DFC_L = [SafeZone, VeryEasy, Easy, Normal, Abnormal, LittleHard, Hard, VertHard, Danger, Extreme]

# 맵 리스트   = [                               맵 이름,       표시상 난이도, 티어(Idx), 선택 가능한 난이도 시작(Idx), 끝]
AbndFctr      = [           'Abandoned Factory:버려진 공장',           'Stable:안정적', 0,  0,  2] # 0
ArdnBtfd      = [      'Ardennes Battlefield:아르덴 교전지',         'Low-Risk:저위험', 0,  1,  3] # 1
NO_AfrcFrnt   = [      'North-Africa Front:북아프리카 전선',        'Caution:주의필요', 1,  1,  4] # 2
NrmdFild      = [           'Normandy Fields:노르망디 들판',       'Unstable:불안정됨', 1,  2,  5] # 3
Btle_Aras     = [           'Battle of Arras:아라스 전차전',        'High-Risk:고위험', 1,  3,  6] # 4
LnvdPlnd      = [               'Invade Poland:폴란드 침공',        'High-Risk:고위험', 2,  4,  7] # 5
Sige_Stlg     = ['Siege of Stalingrad: 스탈린그라드 포위전', 'EMGC-situation:비상상황', 2,  5,  8] # 6
BrlnAtck      = [               'Berlin Attack:베를린 공습','Before-Collapse:붕괴직전', 2,  6, 10] # 7
Btle_Chch     = [            'Battle of CHUNCHEON:춘천대첩', 'EMGC-situation:비상상황', 3,  ]


MAP_L = [AbndFctr, ArdnBtfd, NO_AfrcFrnt, NrmdFild, Btle_Aras, LnvdPlnd, Sige_Stlg, BrlnAtck]

#이 코드를 보고 있는 파이썬 입문자분들은 이런 노가다 짓 하지마세요
    
