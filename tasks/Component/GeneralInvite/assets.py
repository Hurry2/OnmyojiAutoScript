from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by module/dev_tools/assets_extract.py.
# Don't modify it manually.
class GeneralInviteAssets: 


	# Image Rule Assets
	# 中间的邀请图片 
	I_ADD_1 = RuleImage(roi_front=(592,288,114,51), roi_back=(592,288,114,51), threshold=0.9, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_add_1.png")
	# 最右边的邀请 
	I_ADD_2 = RuleImage(roi_front=(1039,205,100,100), roi_back=(1039,205,100,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_add_2.png")
	# description 
	I_FIRE_FAIL = RuleImage(roi_front=(1177,604,81,74), roi_back=(1177,604,81,74), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_fire_fail.png")
	# description 
	I_FIRE = RuleImage(roi_front=(1179,602,81,87), roi_back=(1179,602,81,87), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_fire.png")
	# 锁定阵容的图片 
	I_LOCK = RuleImage(roi_front=(29,644,29,32), roi_back=(29,644,29,32), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_lock.png")
	# 还没有锁定阵容 
	I_UNLOCK = RuleImage(roi_front=(30,647,23,30), roi_back=(30,647,23,30), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_unlock.png")
	# 如果是到时间会退出房间，这个右边显示一个匹配的图片 
	I_MATCHING = RuleImage(roi_front=(1200,110,52,114), roi_back=(1200,110,52,114), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_matching.png")
	# 永生之海挑战（还未有队友的图片） 
	I_FIRE_FAIL_SEA = RuleImage(roi_front=(1160,585,100,100), roi_back=(1160,585,100,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_fire_fail_sea.png")
	# description 
	I_FIRE_SEA = RuleImage(roi_front=(1160,586,100,97), roi_back=(1160,586,100,97), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_fire_sea.png")
	# description 
	I_LOCK_SEA = RuleImage(roi_front=(781,658,27,28), roi_back=(781,658,27,28), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_lock_sea.png")
	# 永生之海 没有锁定队伍的图片 
	I_UNLOCK_SEA = RuleImage(roi_front=(781,656,27,30), roi_back=(781,656,27,30), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_unlock_sea.png")
	# 五人的队伍的第一个加号 
	I_ADD_5_1 = RuleImage(roi_front=(370,243,100,100), roi_back=(370,243,100,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_add_5_1.png")
	# description 
	I_ADD_5_2 = RuleImage(roi_front=(612,263,100,100), roi_back=(612,263,100,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_add_5_2.png")
	# description 
	I_ADD_5_3 = RuleImage(roi_front=(862,243,100,100), roi_back=(862,243,100,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_add_5_3.png")
	# description 
	I_ADD_5_4 = RuleImage(roi_front=(1118,228,100,100), roi_back=(1118,228,100,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_add_5_4.png")
	# 游戏服务器获取在线好友时等待的图片 
	I_LOAD_FRIEND = RuleImage(roi_front=(709,546,134,60), roi_back=(709,546,134,60), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_load_friend.png")
	# 左上角退出 
	I_BACK_YELLOW = RuleImage(roi_front=(19,13,58,55), roi_back=(19,13,58,55), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_back_yellow.png")
	# 点击邀请 
	I_INVITE_ENSURE = RuleImage(roi_front=(712,544,132,60), roi_back=(712,544,132,60), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_invite_ensure.png")
	# 判断是否点中好友了 
	I_SELECTED = RuleImage(roi_front=(895,373,33,32), roi_back=(541,157,407,350), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_selected.png")
	# 用来判断当前的列表是哪儿的 
	I_FLAG_1_ON = RuleImage(roi_front=(354,126,62,21), roi_back=(354,126,62,21), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_flag_1_on.png")
	# description 
	I_FLAG_1_OFF = RuleImage(roi_front=(353,126,58,22), roi_back=(353,126,58,22), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_flag_1_off.png")
	# description 
	I_FLAG_2_ON = RuleImage(roi_front=(465,126,61,24), roi_back=(465,126,61,24), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_flag_2_on.png")
	# description 
	I_FLAG_2_OFF = RuleImage(roi_front=(469,127,58,21), roi_back=(469,127,58,21), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_flag_2_off.png")
	# description 
	I_FLAG_3_ON = RuleImage(roi_front=(588,126,48,22), roi_back=(588,126,48,22), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_flag_3_on.png")
	# description 
	I_FLAG_3_OFF = RuleImage(roi_front=(590,126,41,22), roi_back=(590,126,41,22), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_flag_3_off.png")
	# description 
	I_FLAG_4_ON = RuleImage(roi_front=(713,128,34,21), roi_back=(713,128,34,21), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_flag_4_on.png")
	# description 
	I_FLAG_4_OFF = RuleImage(roi_front=(703,128,53,21), roi_back=(703,128,53,21), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_flag_4_off.png")
	# 永生之海添加好友 
	I_ADD_SEA = RuleImage(roi_front=(836,231,100,100), roi_back=(836,231,100,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralInvite/gi/gi_add_sea.png")


	# Ocr Rule Assets
	# Ocr-description 
	O_TIME_1 = RuleOcr(roi=(541,12,96,33), area=(541,12,96,33), mode="Single", method="Default", keyword="", name="time_1")
	# 永生之海判断时间 
	O_TIME_2 = RuleOcr(roi=(538,70,100,34), area=(538,70,100,34), mode="Single", method="Default", keyword="", name="time_2")
	# 上方好友列表的左边第一个（一般是好友） 
	O_F_LIST_1 = RuleOcr(roi=(346,94,98,41), area=(346,94,98,41), mode="Single", method="Default", keyword="", name="f_list_1")
	# Ocr-description 
	O_F_LIST_2 = RuleOcr(roi=(463,94,97,43), area=(463,94,97,43), mode="Single", method="Default", keyword="", name="f_list_2")
	# Ocr-description 
	O_F_LIST_3 = RuleOcr(roi=(580,87,91,51), area=(580,87,91,51), mode="Single", method="Default", keyword="", name="f_list_3")
	# Ocr-description 
	O_F_LIST_4 = RuleOcr(roi=(688,91,74,45), area=(688,91,74,45), mode="Single", method="Default", keyword="", name="f_list_4")
	# 寻找左侧的好友 
	O_FRIEND_NAME_1 = RuleOcr(roi=(434,185,189,345), area=(434,185,189,345), mode="Full", method="Default", keyword="", name="friend_name_1")
	# 寻找右侧的好友 
	O_FRIEND_NAME_2 = RuleOcr(roi=(729,184,196,346), area=(729,184,196,346), mode="Full", method="Default", keyword="", name="friend_name_2")
	# Ocr-description 
	O_ONLINE = RuleOcr(roi=(790,102,124,42), area=(0,0,100,100), mode="Single", method="Default", keyword="", name="online")


