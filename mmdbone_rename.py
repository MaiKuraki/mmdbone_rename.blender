import bpy

for x in bpy.context.object.data.bones:
	x.name = x.name.replace('全ての親','root')
	x.name = x.name.replace('つま先ＩＫ','ik_ball')
	x.name = x.name.replace('足ＩＫ','ik_foot')
	x.name = x.name.replace('足首先','ball')
	x.name = x.name.replace('足首','foot')
	x.name = x.name.replace('足','thigh')
	x.name = x.name.replace('センター','spine_01')
	x.name = x.name.replace('下半身','pelvis')
	x.name = x.name.replace('ひざ','calf')
	x.name = x.name.replace('上半身２','spine_03')
	x.name = x.name.replace('上半身','spine_02')
	x.name = x.name.replace('肩','clavicle')
	x.name = x.name.replace('腕捩','upperarm_twist_01')
	x.name = x.name.replace('腕','upperarm')
	x.name = x.name.replace('ひじ','lowerarm')
	x.name = x.name.replace('手捩','lowerarm_twist_01')
	x.name = x.name.replace('手首','hand')
	x.name = x.name.replace('親指０','thumb_01')
	x.name = x.name.replace('親指１','thumb_02')
	x.name = x.name.replace('親指２','thumb_03')
	x.name = x.name.replace('小指','pinky')
	x.name = x.name.replace('薬指','ring')
	x.name = x.name.replace('中指','middle')
	x.name = x.name.replace('人指','index')
	x.name = x.name.replace('首','neck_01')
	x.name = x.name.replace('頭','head')
	x.name = x.name.replace('スカート','skirt')
	x.name = x.name.replace('髪','hair')
	x.name = x.name.replace('両目','eyes')
	x.name = x.name.replace('目','eye')
	x.name = x.name.replace('横','side')
	x.name = x.name.replace('側','side')
	x.name = x.name.replace('後ろ','back')
	x.name = x.name.replace('後','back')
	x.name = x.name.replace('前','front')
	x.name = x.name.replace('１','_01')
	x.name = x.name.replace('２','_02')
	x.name = x.name.replace('３','_03')
	x.name = x.name.replace('４','_04')
	x.name = x.name.replace('５','_05')
	x.name = x.name.replace('６','_06')
	x.name = x.name.replace('７','_07')
	x.name = x.name.replace('８','_08')
	x.name = x.name.replace('９','_09')
	x.name = x.name.replace('.R','_r')
	x.name = x.name.replace('.L','_l')
