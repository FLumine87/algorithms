import pyautogui
import time
import random
import win32gui
import win32ui
import win32con
import sys
from PIL import Image
import os 
import cv2
import numpy as np

# 
# donext = input('scan on(y/n):')
# while donext=='y':
#     st=random.random()
#     pyautogui.click(2040,170)
#     time.sleep(4+st*2)

win_main = None
running = True
pattern_p = None

class window:  #关于窗口的一些属性
	def __init__(self,rect=()):
		self.rect = rect
		self.cache_file = None

	def __str__(self): #监视参数 
		return "rect:\t"+str(self.rect)+"\n"	

class pattern_found:
	def __init__(self):
		current_dir = os.path.dirname(os.path.abspath(__file__))
		self.jump = os.path.join(current_dir, "pattern", "jump.jpg")
		self.jump_pos = None

def main():
	global running

	# 监听用户输入以退出程序
	def stop_program():
		global running
		running = False

	try:
		"""
    以下是核心算法逻辑
		:初始化：win_main.rect
		:监视窗口：win_main.pic_tmp
    """
		init()
		while running:
			capture_window()
			print(str(find_pattern_in_screenshot(win_main.cache_file,pattern_p.jump)))
			cap_win_remove()
			time.sleep(5)

	except KeyboardInterrupt:
			print("程序已被手动中止")

def init(): #初始化窗口信息
	"""
	对指定窗口初始化
	:param pos
		, win_main
	:调用函数: get_hwnd_pos
	:创建: win_main类
	"""
	global win_main
	global pattern_p

	while running:  # 初始化
		if input("初始化：(y/n)") != "y":
			sys.exit()
		pos = get_hwnd_pos()
		if pos is not None:
			win_main = window(pos)  # 创建窗口属性，可用来刷新位置
			print(f"窗口信息: {win_main}")#*
			pattern_p = pattern_found()
			break

def get_hwnd_pos():  #获取某个窗口的句柄并获取其位置
	hwnd = win32gui.FindWindow(None, "无标题 - Notepad")  # 替换为目标窗口的标题
	
	def get_window_position(hwnd):  #通过句柄获取窗口位置
		"""
		:param hwnd: 窗口句柄
		:return: (left, top, right, bottom) 窗口的绝对位置
		"""
		try:
			rect = win32gui.GetWindowRect(hwnd)
			return rect  # 返回窗口的 (left, top, right, bottom) 坐标
		except Exception as e:
			print(f"无法获取窗口位置: {e}")
			return None
	
	if hwnd:
		position = get_window_position(hwnd)
		# if position:
		#     print(f"窗口位置: {position}")
		return position
	else:
		print("未找到指定窗口")
		return None
    
def capture_window(rect= None):#捕获窗口
	"""
	对指定窗口进行截屏
	:param rect: 窗口的 (left, top, right, bottom) 坐标
	:return: 截取的图像对象 (Pillow Image)
	"""
	if rect is None: rect = win_main.rect
	while running:
		try:
			# hwnd = win32gui.FindWindow(None, "无标题 - Notepad")  # 替换为目标窗口标题
			# if hwnd:
			# 	win32gui.SetForegroundWindow(hwnd)  # 将窗口置于前台
			left, top, right, bottom = rect
			width = right - left
			height = bottom - top

			# 获取窗口的设备上下文 (DC)
			hwnd_dc = win32gui.GetWindowDC(0)
			mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
			save_dc = mfc_dc.CreateCompatibleDC()

			# 创建位图对象
			save_bitmap = win32ui.CreateBitmap()
			save_bitmap.CreateCompatibleBitmap(mfc_dc, width, height)
			save_dc.SelectObject(save_bitmap)

			# 截取窗口内容
			save_dc.BitBlt((0, 0), (width, height), mfc_dc, (left, top), win32con.SRCCOPY)

			# 转换为 Pillow 图像对象
			bmpinfo = save_bitmap.GetInfo()
			bmpstr = save_bitmap.GetBitmapBits(True)
			img = Image.frombuffer(
				"RGB",
				(bmpinfo["bmWidth"], bmpinfo["bmHeight"]),
				bmpstr,
				"raw",
				"BGRX",
				0,
				1,
			)

			# 释放资源
			win32gui.DeleteObject(save_bitmap.GetHandle())
			save_dc.DeleteDC()
			mfc_dc.DeleteDC()
			win32gui.ReleaseDC(0, hwnd_dc)

			win_main.cache_file = "cache_screenshot.png"
			img.save(win_main.cache_file)
			print(f"窗口截屏已保存为 '{win_main.cache_file}'")#*

			return win_main.cache_file
		except Exception as e:
			print(f"截屏失败: {e}")
			return None

def cap_win_remove():# 删除缓存文件
	if os.path.exists(win_main.cache_file):
		os.remove(win_main.cache_file)
		print(f"缓存文件 '{win_main.cache_file}' 已删除") #*
	else:
		print("错误111：缓存未被清空")

def find_pattern_with_orb_and_color(screenshot_path, pattern_path, color_threshold=0.8, orb_threshold=10):
	"""
	使用 ORB 特征匹配和颜色筛选在截屏中寻找目标图案
	:param screenshot_path: 截屏文件路径
	:param pattern_path: 目标图案文件路径
	:param color_threshold: 颜色相似度阈值（0~1）
	:param orb_threshold: ORB 匹配的最低匹配点数阈值
	:return: 匹配的区域坐标 (top_left_x, top_left_y, bottom_right_x, bottom_right_y)
	"""
	try:
		# 加载截屏和目标图案
		screenshot = cv2.imread(screenshot_path, cv2.IMREAD_COLOR)
		pattern = cv2.imread(pattern_path, cv2.IMREAD_COLOR)

		if screenshot is None or pattern is None:
			print("无法加载截屏或目标图案文件")
			return None

		# 初始化 ORB 检测器
		orb = cv2.ORB_create()

		# 检测特征点并计算描述符
		keypoints1, descriptors1 = orb.detectAndCompute(pattern, None)
		keypoints2, descriptors2 = orb.detectAndCompute(screenshot, None)

		# 使用 BFMatcher 进行特征匹配
		bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
		matches = bf.match(descriptors1, descriptors2)

		# 按匹配距离排序
		matches = sorted(matches, key=lambda x: x.distance)

		# 如果匹配点数不足，返回 None
		if len(matches) < orb_threshold:
			print("ORB 匹配点数不足，未找到目标图案")
			return None

		# 获取匹配点的坐标
		src_pts = np.float32([keypoints1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
		dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

		# 计算单应性矩阵
		matrix, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

		# 使用单应性矩阵计算目标图案在截屏中的位置
		h, w, _ = pattern.shape
		points = np.float32([[0, 0], [w, 0], [w, h], [0, h]]).reshape(-1, 1, 2)
		transformed_points = cv2.perspectiveTransform(points, matrix)

		# 获取目标区域的边界框
		top_left = tuple(np.int32(transformed_points[0][0]))
		bottom_right = tuple(np.int32(transformed_points[2][0]))

		# 提取匹配区域
		matched_region = screenshot[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

		# 如果匹配区域大小不符合，返回 None
		if matched_region.shape[0] <= 0 or matched_region.shape[1] <= 0:
			print("匹配区域无效")
			return None

		# 计算目标图案和匹配区域的颜色直方图
		pattern_hist = cv2.calcHist([pattern], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
		pattern_hist = cv2.normalize(pattern_hist, pattern_hist).flatten()

		matched_region_hist = cv2.calcHist([matched_region], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
		matched_region_hist = cv2.normalize(matched_region_hist, matched_region_hist).flatten()

		# 计算颜色相似性
		color_similarity = cv2.compareHist(pattern_hist, matched_region_hist, cv2.HISTCMP_CORREL)

		if color_similarity >= color_threshold:
			print(f"匹配成功，位置: 左上角 {top_left}, 右下角 {bottom_right}, 颜色相似度: {color_similarity}")
			return top_left[0], top_left[1], bottom_right[0], bottom_right[1]
		else:
			print(f"颜色相似度不足: {color_similarity}")
			return None

	except Exception as e:
		print(f"匹配失败: {e}")
		return None

def find_pattern_in_screenshot(screenshot_path, pattern_path, threshold=0.7, resize_scales=None):
	"""
	在截屏中寻找并匹配一个给定的图案，支持图案大小自适应和匹配阈值选项
	:param screenshot_path: 截屏文件路径
	:param pattern_path: 目标图案文件路径
	:param threshold: 匹配阈值，默认值为 0.8
	:param resize_scales: 图案缩放比例列表（如 [0.5, 1.0, 1.5]），默认为 None（不缩放）
	:return: 图案在截屏中的位置坐标 (top_left_x, top_left_y, bottom_right_x, bottom_right_y)
	"""
	try:
		# 加载截屏和目标图案
		screenshot = cv2.imread(screenshot_path, cv2.IMREAD_COLOR)
		pattern = cv2.imread(pattern_path, cv2.IMREAD_COLOR)

		if screenshot is None or pattern is None:
			print("无法加载截屏或目标图案文件")
			return None

		# 如果未指定缩放比例，则使用默认比例 [0.5, 1.0, 2.0]（即不缩放）
		if resize_scales is None:
			resize_scales = [0.5, 1.0, 2.0]

		best_match = None
		best_val = -1

		# 遍历所有缩放比例
		for scale in resize_scales:
			# 缩放目标图案
			resized_pattern = cv2.resize(pattern, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)

			# 模板匹配
			result = cv2.matchTemplate(screenshot, resized_pattern, cv2.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

			# 如果匹配值超过阈值并且是当前最佳匹配
			if max_val >= threshold and max_val > best_val:
				best_val = max_val
				best_match = {
					"top_left": max_loc,
					"bottom_right": (max_loc[0] + resized_pattern.shape[1], max_loc[1] + resized_pattern.shape[0]),
					"scale": scale,
					"confidence": max_val
				}

		# 如果找到最佳匹配
		if best_match:
			top_left = best_match["top_left"]
			bottom_right = best_match["bottom_right"]
			print(f"匹配成功，位置: 左上角 {top_left}, 右下角 {bottom_right}, 缩放比例: {best_match['scale']}, 置信度: {best_match['confidence']}")
			return top_left[0], top_left[1], bottom_right[0], bottom_right[1]
		else:
			print("未找到匹配的目标图案")
			return None

	except Exception as e:
		print(f"匹配失败: {e}")
		return None

# def capture_win_main():
#     while running:
#         if win_main:
#             print(f"正在截屏，窗口位置: {win_main.rect}")  # 调试信息
#             screenshot = capture_window(win_main.rect)
#             if screenshot:
#                 # 保存为缓存文件
#                 cache_file = "cache_screenshot.png"
#                 screenshot.save(cache_file)
#                 print(f"窗口截屏已保存为 '{cache_file}'")

#                 # 模拟对缓存文件的分析
#                 analyze_cache_file(cache_file)

#                 # 删除缓存文件
#                 if os.path.exists(cache_file):
#                     os.remove(cache_file)
#                     print(f"缓存文件 '{cache_file}' 已删除")
#             else:
#                 print("截屏失败，未获取到图像")

#             # 等待一段时间后再次截屏
#             time.sleep(2)  # 设置监视间隔时间（单位：秒）
#         else:
#             print("win_main 未初始化，无法进行截屏")
#             break

def analyze_cache_file(cache_file=None,pattern_path= None):
	"""
	模拟对缓存文件的分析
	:param cache_file: 缓存文件路径
	"""
	if cache_file is None: cache_file = win_main.cache_file
	if pattern_path is None: pattern_path = pattern_p.jump
	match_coordinates = find_pattern_in_screenshot(cache_file, pattern_path)

	if match_coordinates:
		print(f"目标图案位置: {match_coordinates}")
	else:
		print("未找到目标图案")
	# print(f"正在分析缓存文件 '{cache_file}'...")
	# # 在这里添加你的分析逻辑
	# time.sleep(1)  # 模拟分析时间

main()