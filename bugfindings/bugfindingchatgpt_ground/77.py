
def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    a = abs(a)
    return int(round(a ** (1. / 3))) == a
assert iscube(1) == True
assert iscube(8) == True
assert iscube(27) == True
assert iscube(64) == True
assert iscube(125) == True
assert iscube(216) == True
assert iscube(343) == True
assert iscube(512) == True
assert iscube(729) == True
assert iscube(1000) == True
assert iscube(2) == False
assert iscube(3) == False
assert iscube(4) == False
assert iscube(5) == False
assert iscube(6) == False
assert iscube(7) == False
assert iscube(9) == False
assert iscube(10) == False
assert iscube(11) == False
assert iscube(12) == False
assert iscube(1001) == False
assert iscube(1234) == False
assert iscube(999999) == False
assert iscube(1331) == True
assert iscube(1728) == True
assert iscube(2197) == True
assert iscube(2744) == True
assert iscube(3375) == True
assert iscube(4096) == True
assert iscube(4913) == True
assert iscube(5832) == True
assert iscube(6859) == True
assert iscube(8000) == True
assert iscube(9261) == True
assert iscube(10648) == True
assert iscube(12167) == True
assert iscube(13824) == True
assert iscube(15625) == True
assert iscube(17576) == True
assert iscube(19683) == True
assert iscube(21952) == True
assert iscube(24389) == True
assert iscube(27000) == True
assert iscube(29791) == True
assert iscube(32768) == True
assert iscube(35937) == True
assert iscube(39304) == True
assert iscube(42875) == True
assert iscube(46656) == True
assert iscube(50653) == True
assert iscube(54872) == True
assert iscube(59319) == True
assert iscube(64000) == True
assert iscube(68921) == True
assert iscube(74088) == True
assert iscube(79507) == True
assert iscube(85184) == True
assert iscube(91125) == True
assert iscube(97336) == True
assert iscube(103823) == True
assert iscube(110592) == True
assert iscube(117649) == True
assert iscube(125000) == True
assert iscube(132651) == True
assert iscube(140608) == True
assert iscube(148877) == True
assert iscube(157464) == True
assert iscube(166375) == True
assert iscube(175616) == True
assert iscube(185193) == True
assert iscube(195112) == True
assert iscube(205379) == True
assert iscube(216000) == True
assert iscube(226981) == True
assert iscube(238328) == True
assert iscube(250047) == True
assert iscube(262144) == True
assert iscube(274625) == True
assert iscube(287496) == True
assert iscube(300763) == True
assert iscube(314432) == True
assert iscube(328509) == True
assert iscube(343000) == True
assert iscube(357911) == True
assert iscube(373248) == True
assert iscube(389017) == True
assert iscube(405224) == True
assert iscube(421875) == True
assert iscube(438976) == True
assert iscube(456533) == True
assert iscube(474552) == True
assert iscube(493039) == True
assert iscube(512000) == True
assert iscube(531441) == True
assert iscube(551368) == True
assert iscube(571787) == True
assert iscube(592704) == True
assert iscube(614125) == True
assert iscube(636056) == True
assert iscube(658503) == True
assert iscube(681472) == True
assert iscube(704969) == True
assert iscube(729000) == True
assert iscube(753571) == True
assert iscube(778688) == True
assert iscube(804357) == True
assert iscube(830584) == True
assert iscube(857375) == True
assert iscube(884736) == True
assert iscube(912673) == True
assert iscube(941192) == True
assert iscube(970299) == True
assert iscube(1000000) == True
assert iscube(1002) == False
assert iscube(1003) == False
assert iscube(1004) == False
assert iscube(1005) == False
assert iscube(0) == True
assert iscube(999) == False
assert iscube(8) == True, 'Test Case 2 Failed'
assert iscube(27) == True, 'Test Case 3 Failed'
assert iscube(64) == True, 'Test Case 4 Failed'
assert iscube(125) == True, 'Test Case 5 Failed'
assert iscube(216) == True, 'Test Case 6 Failed'
assert iscube(343) == True, 'Test Case 7 Failed'
assert iscube(512) == True, 'Test Case 8 Failed'
assert iscube(729) == True, 'Test Case 9 Failed'
assert iscube(1000) == True, 'Test Case 10 Failed'
assert iscube(12) == False, 'Test Case 11 Failed'
assert iscube(28) == False, 'Test Case 12 Failed'
assert iscube(50) == False, 'Test Case 13 Failed'
assert iscube(70) == False, 'Test Case 14 Failed'
assert iscube(90) == False, 'Test Case 15 Failed'
assert iscube(110) == False, 'Test Case 16 Failed'
assert iscube(130) == False, 'Test Case 17 Failed'
assert iscube(150) == False, 'Test Case 18 Failed'
assert iscube(170) == False, 'Test Case 19 Failed'
assert iscube(190) == False, 'Test Case 20 Failed'
assert iscube(1000001) == False
assert iscube(1000000000) == True
assert iscube(1000000001) == False
assert iscube(1000000000000) == True
assert iscube(1000000000001) == False
assert iscube(1000000000000000) == True
assert iscube(1000000000000001) == False
assert iscube(10000) == False
assert iscube(123456789) == False
assert iscube(1001) == False, 'Test Case 11 Failed'
assert iscube(1000000) == True, 'Test Case 14 Failed'
assert iscube(1000001) == False, 'Test Case 15 Failed'
assert iscube(20) == False
assert iscube(50) == False
assert iscube(100) == False
assert iscube(200) == False
assert iscube(2000) == False
assert iscube(3000) == False
assert iscube(4000) == False
assert iscube(5000) == False
assert iscube(6000) == False
assert iscube(7000) == False
assert iscube(9000) == False
assert iscube(8) == True, "Test case 2 failed"
assert iscube(27) == True, "Test case 3 failed"
assert iscube(64) == True, "Test case 4 failed"
assert iscube(125) == True, "Test case 5 failed"
assert iscube(216) == True, "Test case 6 failed"
assert iscube(343) == True, "Test case 7 failed"
assert iscube(512) == True, "Test case 8 failed"
assert iscube(729) == True, "Test case 9 failed"
assert iscube(1000) == True, "Test case 10 failed"
assert iscube(1001) == False, "Test case 11 failed"
assert iscube(1002) == False, "Test case 12 failed"
assert iscube(1003) == False, "Test case 13 failed"
assert iscube(1004) == False, "Test case 14 failed"
assert iscube(1005) == False, "Test case 15 failed"
assert iscube(1006) == False, "Test case 16 failed"
assert iscube(1007) == False, "Test case 17 failed"
assert iscube(1008) == False, "Test case 18 failed"
assert iscube(1009) == False, "Test case 19 failed"
assert iscube(1010) == False, "Test case 20 failed"
assert iscube(500) == False
assert iscube(16) == False
assert iscube(30) == False
assert iscube(15) == False
assert iscube(100000) == False
assert iscube(999999999999999) == False
assert iscube(28) == False
assert iscube(65) == False
assert iscube(1024) == False
assert iscube(10001) == False
assert iscube(9999) == False
assert iscube(13) == False
assert iscube(14) == False
assert iscube(17) == False
assert iscube(18) == False
assert iscube(19) == False
assert iscube(100001) == False
assert iscube(21) == False
assert iscube(22) == False
assert iscube(23) == False
assert iscube(24) == False
assert iscube(25) == False
assert iscube(26) == False
assert iscube(29) == False
assert iscube(31) == False
assert iscube(32) == False
assert iscube(33) == False
assert iscube(34) == False
assert iscube(35) == False
assert iscube(36) == False
assert iscube(37) == False
assert iscube(38) == False
assert iscube(39) == False
assert iscube(40) == False
assert iscube(41) == False
assert iscube(42) == False
assert iscube(43) == False
assert iscube(44) == False
assert iscube(45) == False
assert iscube(46) == False
assert iscube(47) == False
assert iscube(48) == False
assert iscube(49) == False
assert iscube(51) == False
assert iscube(52) == False
assert iscube(53) == False
assert iscube(54) == False
assert iscube(55) == False
assert iscube(56) == False
assert iscube(57) == False
assert iscube(58) == False
assert iscube(59) == False
assert iscube(60) == False
assert iscube(61) == False
assert iscube(62) == False
assert iscube(63) == False
assert iscube(66) == False
assert iscube(67) == False
assert iscube(68) == False
assert iscube(69) == False
assert iscube(70) == False
assert iscube(71) == False
assert iscube(72) == False
assert iscube(73) == False
assert iscube(74) == False
assert iscube(75) == False
assert iscube(76) == False
assert iscube(77) == False
assert iscube(78) == False
assert iscube(79) == False
assert iscube(80) == False
assert iscube(81) == False
assert iscube(82) == False
assert iscube(83) == False
assert iscube(84) == False
assert iscube(85) == False
assert iscube(86) == False
assert iscube(87) == False
assert iscube(88) == False
assert iscube(89) == False
assert iscube(90) == False
assert iscube(91) == False
assert iscube(92) == False
assert iscube(93) == False
assert iscube(94) == False
assert iscube(95) == False
assert iscube(96) == False
assert iscube(97) == False
assert iscube(98) == False
assert iscube(99) == False
assert iscube(101) == False
assert iscube(102) == False
assert iscube(103) == False
assert iscube(104) == False
assert iscube(105) == False
assert iscube(106) == False
assert iscube(107) == False
assert iscube(108) == False
assert iscube(99999) == False
assert iscube(8) == True, "Error: Test Case 2"
assert iscube(27) == True, "Error: Test Case 3"
assert iscube(64) == True, "Error: Test Case 4"
assert iscube(125) == True, "Error: Test Case 5"
assert iscube(216) == True, "Error: Test Case 6"
assert iscube(343) == True, "Error: Test Case 7"
assert iscube(512) == True, "Error: Test Case 8"
assert iscube(729) == True, "Error: Test Case 9"
assert iscube(1000) == True, "Error: Test Case 10"
assert iscube(2) == False, "Error: Test Case 11"
assert iscube(10) == False, "Error: Test Case 12"
assert iscube(20) == False, "Error: Test Case 13"
assert iscube(30) == False, "Error: Test Case 14"
assert iscube(40) == False, "Error: Test Case 15"
assert iscube(50) == False, "Error: Test Case 16"
assert iscube(60) == False, "Error: Test Case 17"
assert iscube(70) == False, "Error: Test Case 18"
assert iscube(80) == False, "Error: Test Case 19"
assert iscube(90) == False, "Error: Test Case 20"
assert iscube(7) == False, "Error: Test Case 7"
assert iscube(12) == False, "Error: Test Case 8"
assert iscube(30) == False, "Error: Test Case 9"
assert iscube(50) == False, "Error: Test Case 10"
assert iscube(1001) == False, "Error: Test Case 11"
assert iscube(10001) == False, "Error: Test Case 13"
assert iscube(100001) == False, "Error: Test Case 15"
assert iscube(123456) == False
assert iscube(1006) == False
assert iscube(1007) == False
assert iscube(1008) == False
assert iscube(1009) == False
assert iscube(1010) == False
assert iscube(1011) == False
assert iscube(1012) == False
assert iscube(1013) == False
assert iscube(1014) == False
assert iscube(1015) == False
assert iscube(1016) == False
assert iscube(1017) == False
assert iscube(1018) == False
assert iscube(1019) == False
assert iscube(1020) == False
assert iscube(1021) == False
assert iscube(1022) == False
assert iscube(1023) == False
assert iscube(1025) == False
assert iscube(1026) == False
assert iscube(1027) == False
assert iscube(1028) == False
assert iscube(1029) == False
assert iscube(1030) == False
assert iscube(1031) == False
assert iscube(1032) == False
assert iscube(1033) == False
assert iscube(1034) == False
assert iscube(1035) == False
assert iscube(1036) == False
assert iscube(1037) == False
assert iscube(1038) == False
assert iscube(1039) == False
assert iscube(1040) == False
assert iscube(1041) == False
assert iscube(1042) == False
assert iscube(1043) == False
assert iscube(1044) == False
assert iscube(1045) == False
assert iscube(1046) == False
assert iscube(1047) == False
assert iscube(1048) == False
assert iscube(1049) == False
assert iscube(1050) == False
assert iscube(1051) == False
assert iscube(1052) == False
assert iscube(1053) == False
assert iscube(1054) == False
assert iscube(1055) == False
assert iscube(1056) == False
assert iscube(1057) == False
assert iscube(1058) == False
assert iscube(1059) == False
assert iscube(1060) == False
assert iscube(1061) == False
assert iscube(1062) == False
assert iscube(1063) == False
assert iscube(1064) == False
assert iscube(1065) == False
assert iscube(1066) == False
assert iscube(1067) == False
assert iscube(1068) == False
assert iscube(1069) == False
assert iscube(1070) == False
assert iscube(1071) == False
assert iscube(1072) == False
assert iscube(1073) == False
assert iscube(1074) == False
assert iscube(1075) == False
assert iscube(1076) == False
assert iscube(1077) == False
assert iscube(1078) == False
assert iscube(1079) == False
assert iscube(1080) == False
assert iscube(1081) == False
assert iscube(1082) == False
assert iscube(1083) == False
assert iscube(1084) == False
assert iscube(1085) == False
assert iscube(1086) == False
assert iscube(1087) == False
assert iscube(1088) == False
assert iscube(1090) == False
assert iscube(1091) == False
assert iscube(1092) == False
assert iscube(1093) == False
assert iscube(987654321) == False
assert iscube(10000) == False, 'Test Case 12 Failed'
assert iscube(100000) == False, 'Test Case 13 Failed'
assert iscube(10000001) == False
assert iscube(100000001) == False
assert iscube(126) == False
assert iscube(12345) == False
