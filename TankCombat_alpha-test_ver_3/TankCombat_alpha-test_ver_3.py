#TankCombat_alpha-test_ver_3. Made by PYS3301man.
#제작기간 = 시작: 2025-11-01 | 종료: 2025-1
#이전 버젼(TankCombat_alpha-test_ver_2)를 계승한 코드.
from TCatv3_InfoList import *
try:
    import time
    import random
    import pygame
except:
    pass

#해당 코드는 ChatGPT의 조언과 실제 역사 기반의 위키, 문서, 전쟁기념관 문서 등의 도움을 받았습니다.
#이 코드를 읽는 사람중 만약 파이썬 입문자가 있다면, 신속히 Ctrl + S 입력후 Alt + F4 를 입력하세요.

Time_list = ["WW2_E","WW2_M", "WW2_L", "K_W", "VN_W", "C_W", "IRQ_W", "M_W", "F_W"]

#시대별 전차 리스트 (참조용)

#|미국(+ 남베트남, 남한)
#example_example_List =       [''                    , ''                   , ''                   , ''                  ] #예시
WW2_Early_USAm_Tank_List =    ['M3A1_Stuart'         , 'M4A1_Sherman'       , 'M3_Lee'             , 'M10_GMC'           ] #WW2 초기
WW2_Middle_USAm_Tank_List =   ['M18_GMC'             , 'M26_Pershing'       , 'M4A3E2_(76)_W_Jumbo', 'M36B2'             ] #WW2 중기
WW2_Late_USAm_Tank_List =     ['M41A1_WalkerBulldog' , 'M46_Patton'         , 'T34'                , 'M56_Scorpion'      ] #WW2 후기
Korean_War_USAm_Tank_List =   ['M41A1_WalkerBulldog' , 'M46_Patton'         , 'M4A3E8_(76)_W_HVSS' , 'M36B2'             ] #6.25 전쟁
Vietnam_War_USAm_Tank_List =  ['M551_Sheridan'       , 'M48_Patton'         , 'M60_SuperPatton'    , 'M50_Ontos'         ] #베트남 전쟁
Cold_War_USAm_Tank_List =     ['M551_Sheridan'       , 'MBT-70'             , 'M103'               , 'M50_Ontos'         ] #냉전
Iraq_War_USAm_Tank_List =     ['M2_Bradley'          , 'M1A1'               , 'M1A1HA'             , 'M103'              ] #이라크 전쟁
Modern_War_USAm_Tank_List =   ['M3_Bradley'          , 'M1A2_SEP_v2'        , 'M1A2_SEP_v3'        , 'M1128_MGS'         ] #현대

IdxTnk = 0
call = 0
SltdCntrIdx = 0
SltdTimeIdx = 0
SltdTankIdx = 0
SltdTank = 0
SltdMap = 0
#자원 (war bond:전시 채권)
WB = 0

#|소련(+ 러시아, 북베트남, 북한)
#USSR_Tank_List =  []

#|독일
#GARM_Tank_List =  []

#일부 CGPT 사용됨
class Tanks:
    def __init__(self, Name, Class, HulInfo, MG_I_List, SG_I_List, RsiBm):
        self.Name = Name
        self.Class = Class
        self.HulInfo = HulInfo
        self.MG_I_List = MG_I_List
        self.SG_I_List = SG_I_List
        self.RsiBm = RsiBm

    def __str__(self):
        return f'{self.Name}, {self.Class}, {self.HulInfo}, {self.MG_I_List}, {self.SG_I_List}, {self.RsiBm}'

    def ReturnTankInfo(self):
        TankInfo = [self.Name, self.HulInfo, self.MG_I_List, self.SG_I_List, RsiBm]
        return TankInfo

#|전차 객체 생성

#||전차              = Exa_Tanks("전차 이름"         ,  분류       , 전차 정보,     주포 정보, 부포 정보, 폭압저항력)
#|||WW2_Early_USAm_Tank_List
M3A1_Stuart          = Tanks("M3A1 스튜어트"     , '[경전차]'  ,          M3A1_I,     weC37mmM6,      None, 2000)
M4A1_Sherman         = Tanks("M4A1 셔먼"         , '[중형전차]',          M4A1_I,     weC75mmM3,      None, 3000)
M3_Lee               = Tanks("M3 리"             , '[중전차]'  ,            M3_I,     weC37mmM5, weC75mmM2, 3000)
M10_GMC              = Tanks("M10 GMC"           , '[구축전차]',           M10_I,     weC76mmM7,      None,  300)
#|||WW2_Middle_USAm_Tank_List
M18_GMC              = Tanks("M18 GMC"           , '[경전차]'  ,           M18_I,     wmC76mmM1,      None,  300)
M26_Pershing         = Tanks("M26 퍼싱"          , '[중형전차]',           M26_I,   wmC90mmM3_o,      None, 3500)
M4A3E2_76_W_Jumbo    = Tanks("M4A3E2 점보셔먼"   , '[중전차]'  ,    M4A3E2_76J_I,     wmC76mmM1,      None, 3400)
M36B2_o              = Tanks("M36B2"             , '[구축전차]',       M38B2_o_I,   wmC90mmM3_s,      None,  500)
#|||WW2_Late_USAm_Tank_List
M41A1_WalkerBulldog_o= Tanks("M41A1 워커불독"    , '[경전차]'  ,       M41A1_o_I,  wlC76mmM32_o,      None, 2000)
M46_Patton_o         = Tanks("M46 패튼"          , '[중형전차]',         M46_o_I, wlC90mmM3A1_o,      None, 4000)
T34                  = Tanks("T34"               , '[중전차]'  ,           M34_I,   wlC120mmT53,      None, 4000)
M56_Scorpion         = Tanks("M56 스콜피온"      , '[구축전차]',           M56_I,    wlC90mmM54,      None,  400)
#|||Korean_War_USAm_Tank_List
M41A1_WalkerBulldog_s= Tanks("M41A1 워커불독"    , '[경전차]'  ,       M41A1_s_I,  kwC76mmM32_s,      None, 2000)
M46_Patton_s         = Tanks("M46 패튼"          , '[중형전차]',         M46_s_I, kwC90mmM3A1_s,      None, 4000)
M4A3E8_76_W_HVSS     = Tanks("M4A3E8 이지에잇 셔먼", '[중전차]', M4A3E8_76HVSS_I,   kwC76mmM1A2,      None, 3500)
M36B2_s              = Tanks("M36B2"             , '[구축전차]',       M38B2_s_I,   kwC90mmM3_t,      None,  500)

#||리스트로 묶기


W2E_UT_L = [M3A1_Stuart          , M4A1_Sherman         , M3_Lee               , M10_GMC              ]
W2M_UT_L = [M18_GMC              , M26_Pershing         , M4A3E2_76_W_Jumbo    , M36B2_o              ]
W2L_UT_L = [M41A1_WalkerBulldog_o, M46_Patton_o         , T34                  , M56_Scorpion         ]
KoW_UT_L = [M41A1_WalkerBulldog_s, M46_Patton_s         , M4A3E8_76_W_HVSS     , M36B2_s              ]

UT_L = [W2E_UT_L, W2M_UT_L, W2L_UT_L, KoW_UT_L]

#함수 정의
#순서: 메인메뉴 - 국가 선택 - 시간대 선택 - 전차선택

    
#                                           포탄 종류 지정
def CekSayShlTpe(Tpe):
    re = []
    if Tpe == 'AP':
        re.append('철갑탄')
        re.append('n')
        return re
    if Tpe == 'APC':
        re.append('피모철갑탄')
        re.append('n')
        return re
    if Tpe == 'APCBC':
        re.append('저저항피모철갑탄')
        re.append('n')
        return re
    if Tpe == 'APCR':
        re.append('경심철갑탄')
        re.append('n')
        return re
    if Tpe == 'APHE':
        re.append('철갑유탄')
        re.append('y')
        return re
    if Tpe == 'APHECBC':
        re.append('저저항피모철갑유탄')
        re.append('y')
        return re
    if Tpe == 'APDS':
        re.append('분리철갑탄')
        re.append('n')
        return re
    if Tpe == 'APFSDS':
        re.append('날개안정분리철갑탄')
        re.append('n')
        return re
    if Tpe == 'HE':
        re.append('고폭탄')
        re.append('y')
        return re
    if Tpe == 'HEAT':
        re.append('대전차고폭탄')
        re.append('y')
        return re
    if Tpe == 'HEATFS':
        re.append('날개안정대전차고폭탄')
        re.append('y')
        return re

#                                           전차 설명
def ShwGun_Info(STI, MG_I_List, SG_I_List):
    SayShlTpe = ''
    print(f'''주포 정보:
 |주포: {MG_I_List[0]}
 |재장전 시간: {MG_I_List[1]} 초
 |사용 가능한 포탄:''')
    for i in range(2,len(MG_I_List)):
        SayShlTpe = CekSayShlTpe(MG_I_List[i][1])
        print(f'''=포탄: {MG_I_List[i][0]} ({MG_I_List[i][1]}, {SayShlTpe[0]})
  |관통력: {MG_I_List[i][2]}mm''')
        if SayShlTpe[1] == 'y':
            print(f'  |작약량: {MG_I_List[i][3]}g')
        elif SayShlTpe[1] == 'n':
            print(f'  |피해량: {MG_I_List[i][3]}')
    if SG_I_List != None:
        print(f'''부포 정보:
 |부포: {SG_I_List[0]}
 |재장전 시간: {SG_I_List[1]} 초
 |사용 가능한 포탄:''')
        for i in range(2,len(SG_I_List)):
            SayShlTpe = CekSayShlTpe(SG_I_List[i][1])
            print(f'''=포탄: {SG_I_List[i][0]} ({SG_I_List[i][1]}, {SayShlTpe[0]})
  |관통력: {SG_I_List[i][2]}mm
  |피해량: {SG_I_List[i][3]}''')


#                                           난이도 선택
def Slt_Dfclt():
#    global
    print('t')
    Check = input("번호를 입력하세요: ")
    if Check == '0':
        SltdTankIdx = 0
        SltdTank = 0
        Slt_Map()


#                                           Map 선택
def Slt_Map():
    global SltdTankIdx, SltdTimeIdx, SltdCntrIdx, SltdMap
    SltdTank = UT_L[SltdTimeIdx][SltdTankIdx]
    ShwSelInfo = []
    print("==" * 10)
    print(f"선택된 전차: {UT_L[SltdTimeIdx][SltdTankIdx].Name} | 티어: {SltdTimeIdx + 1}")
    print("사용 가능한 탄: ", end = '')
    for i in range(2, len(SltdTank.MG_I_List)):
        ShwSelInfo.append(SltdTank.MG_I_List[i][0])
    for j in range(len(ShwSelInfo)):
        if j == len(ShwSelInfo) - 1:
            print(ShwSelInfo[j])
        else:
            print(ShwSelInfo[j], end = ", ")
    if UT_L[SltdTimeIdx][SltdTankIdx].SG_I_List != None:
        ShwSelInfo = []
        print("사용 가능한 탄(부포): ", end = '')
        for i in range(2, len(SltdTank.SG_I_List)):
            ShwSelInfo.append(SltdTank.SG_I_List[i][0])
        for j in range(len(ShwSelInfo)):
            print(ShwSelInfo[j], end = ' ')
        print(' ')
    print("맵 목록:")
    for a in range(len(MAP_L)):
        print(f"{a + 1}. {MAP_L[a][0]}")
        print(f"| 상황: {MAP_L[a][1]} | 티어: {MAP_L[a][2] + 1}")
        
    print(SltdTimeIdx)
    Check = int(input("번호를 입력하세요: "))
    if 1 <= Check <= 8:
        if SltdTimeIdx == MAP_L[Check - 1][2]:
            SltdMap = Check -1
            print(SltdMap)
            return Slt_Dfclt()
        else:
            print('ERROR')        # 여기에 오류 메세지 넣어라 (2025-11-06)
            
    print(SltdMap)
#        print(f"선택된 전차의 티어와 같은 티어의 맵에만 입장할수 있습니다.")
    
    if Check == 0:
        SltdTankIdx = 0
        SltdTank = 0
        Slt_UT()
    else :
        print("#ERROR!#")
        return Slt_Map()

#                                           USA_TANK 표시
def Shw_UT():
    global UT_L, SltdTankIdx, SltdTimeIdx, SltdCntrIdx
    print("==" * 10)
    print(f"이름: {UT_L[SltdTimeIdx][SltdTankIdx].Name}")
    print(f"분류: {UT_L[SltdTimeIdx][SltdTankIdx].Class}")
    print(f'''체력(HP): {UT_L[SltdTimeIdx][SltdTankIdx].HulInfo[0]}
|차체 장갑: {UT_L[SltdTimeIdx][SltdTankIdx].HulInfo[1]}mm
|포탑 장갑: {UT_L[SltdTimeIdx][SltdTankIdx].HulInfo[2]}mm
|속도: {UT_L[SltdTimeIdx][SltdTankIdx].HulInfo[3]}km/h
''', end = '')
    ShwGun_Info(SltdTankIdx, UT_L[SltdTimeIdx][SltdTankIdx].MG_I_List, UT_L[SltdTimeIdx][SltdTankIdx].SG_I_List)
    print("1. 시작 | 0. 돌아가기")
    print(SltdCntrIdx, SltdTimeIdx, SltdTankIdx)
    Check = input("번호를 입력하세요: ")
    if Check == '1':
        print(SltdCntrIdx, SltdTimeIdx, SltdTankIdx)
        return Slt_Map()
    elif Check == '0':
        SltdTankIdx = 0
        return Slt_UT()
    else :
        print("#ERROR!#")
        return Shw_UT()

#                                           WW2_Early_USA_TANK 선택
def Slt_UT():
    global UT_L, SltdTankIdx, SltdTimeIdx
    SltdTankIdx = 0
    print("==" * 10)
    print("전차 선택: ")
    print(f'''1. {UT_L[SltdTimeIdx][0].Name} {UT_L[SltdTimeIdx][0].Class}
2. {UT_L[SltdTimeIdx][1].Name} {UT_L[SltdTimeIdx][1].Class}
3. {UT_L[SltdTimeIdx][2].Name} {UT_L[SltdTimeIdx][2].Class}
4. {UT_L[SltdTimeIdx][3].Name} {UT_L[SltdTimeIdx][3].Class}
0. 돌아가기''')
    Selected_W2E_UTank = input("번호를 입력하세요: ")
    if Selected_W2E_UTank == '1':
        SltdTankIdx = 0
        return Shw_UT()
    elif Selected_W2E_UTank == '2':
        SltdTankIdx = 1
        return Shw_UT()
    elif Selected_W2E_UTank == '3':
        SltdTankIdx = 2
        return Shw_UT()
    elif Selected_W2E_UTank == '4':
        SltdTankIdx = 3
        return Shw_UT()
    elif Selected_W2E_UTank == '0':
        SltdTankIdx = 0
        return Slt_America_Time()
    else :
        print("#ERROR!#")
        return Slt_UT()

#                                           시간대 선택
def Slt_America_Time():
    global SltdTimeIdx
    SltdTimeIdx = 0
    print("==" * 10)
    print("시간 선택: ")
    print('''1. 세계 2차 대전 전기
2. 세계 2차 대전 중기
3. 세계 2차 대전 후기
4. 6.25 전쟁(남한측)
0. 돌아가기''')
    Selected_Time = input("번호를 입력하세요: ")
    if Selected_Time == '1':
        SltdTimeIdx = 0
        return Slt_UT()
    elif Selected_Time == '2':
        SltdTimeIdx = 1
        return Slt_UT()
    elif Selected_Time == '3':
        SltdTimeIdx = 2
        return Slt_UT()
    elif Selected_Time == '4':
        SltdTimeIdx = 3
        return Slt_UT()
    elif Selected_Time == '0':
        SltdTimeIdx = 0
        return Slt_Country()
    else :
        print("#ERROR!#")
        return Slt_America_Time()

#                                           국가 선택
def Slt_Country():
    global SltdCntrIdx
    SltdCntrIdx = 0
    print("==" * 10)
    print("국가 선택: ")
    print('''1. 미국 | 2. 소련(러시아) | 3. 독일
0. 돌아가기''')
    Selected_Country = input("번호를 입력하세요: ")
    if Selected_Country == '1':
        SltdCntrIdx = 0
        return Slt_America_Time()
    elif Selected_Country == '2':
        return 'Soviet'
    elif Selected_Country == '3':
        return 'Germany'
    elif Selected_Country == '0':
        SltdCntrIdx = 0
        return Main_Menu()
    else :
        print("#ERROR!#")
        return Slt_Country()

#                                           메인 메뉴
def Main_Menu():
    print("==" * 10)
    print("TankCombat alpha-test ver.3")
    print("1 을 입력하여 플레이")
    start = input("번호를 입력하세요: ")
    if start == '1':
        return Slt_Country()
    else :
        print("#ERROR!#")
        return Main_Menu()


Main_Menu()
