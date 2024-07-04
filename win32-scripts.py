#Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
#Type "help", "copyright", "credits" or "license()" for more information.


import win32file
import win32clipboard as clipboard
import win32event
import win32con
import time
import ctypes
import win32api

# 定义系统信息结构
class SYSTEM_INFO(ctypes.Structure):
    _fields_ = [
        ("wProcessorArchitecture", ctypes.c_uint16),
        ("wReserved", ctypes.c_uint16),
        ("dwPageSize", ctypes.c_uint32),
        ("lpMinimumApplicationAddress", ctypes.c_void_p),
        ("lpMaximumApplicationAddress", ctypes.c_void_p),
        ("dwActiveProcessorMask", ctypes.c_uint64),
        ("dwNumberOfProcessors", ctypes.c_uint32),
        ("dwProcessorType", ctypes.c_uint32),
        ("dwAllocationGranularity", ctypes.c_uint32),
        ("wProcessorLevel", ctypes.c_uint16),
        ("wProcessorRevision", ctypes.c_uint16)
    ]

def get_system_info():
    system_info = SYSTEM_INFO()
    ctypes.windll.kernel32.GetSystemInfo(ctypes.byref(system_info))
    return system_info

def get_clipboard_text():
    clipboard.OpenClipboard()
    try:
        data = clipboard.GetClipboardData(win32con.CF_TEXT)
        return data.decode('utf-8')
    except Exception as e:
        return f"读取剪贴板内容失败: {e}"
    finally:
        clipboard.CloseClipboard()

def automate_tasks():
    try:
        # 模块1：使用 win32api 获取系统信息
        system_info = get_system_info()
        print(f"模块1 - 系统信息:\n"
              f"  处理器架构: {system_info.wProcessorArchitecture}\n"
              f"  页面大小: {system_info.dwPageSize}\n"
              f"  最小应用地址: {system_info.lpMinimumApplicationAddress}\n"
              f"  最大应用地址: {system_info.lpMaximumApplicationAddress}\n"
              f"  活动处理器掩码: {system_info.dwActiveProcessorMask}\n"
              f"  处理器数量: {system_info.dwNumberOfProcessors}\n"
              f"  处理器类型: {system_info.dwProcessorType}\n"
              f"  分配粒度: {system_info.dwAllocationGranularity}\n"
              f"  处理器级别: {system_info.wProcessorLevel}\n"
              f"  处理器修订: {system_info.wProcessorRevision}")
        
        # 模块2：使用 win32file 创建文件
        try:
            handle = win32file.CreateFile(
                "example.txt",
                win32file.GENERIC_WRITE,
                0,
                None,
                win32file.CREATE_ALWAYS,
                0,
                None
            )
            win32file.WriteFile(handle, b"Hello, World!")
            win32file.CloseHandle(handle)
            print("模块2 - 文件创建成功: example.txt")
        except Exception as e:
            print("模块2 - 文件创建失败:", e)
        
        # 模块3：记录过去十次鼠标点击的位置
        try:
            click_positions = []
            for i in range(10):
                pos = win32api.GetCursorPos()
                click_positions.append(pos)
                print(f"模块3 - 鼠标点击位置 {i+1}: {pos}")
                time.sleep(1)  # 模拟每秒点击一次
            
            # 将点击位置写入文件
            with open("click_positions.txt", "w") as file:
                for pos in click_positions:
                    file.write(f"{pos}\n")
            print("模块3 - 鼠标点击位置已写入文件: click_positions.txt")
        except Exception as e:
            print("模块3 - 记录鼠标点击位置失败:", e)
        
        # 模块4：使用 win32clipboard 处理剪贴板内容
        try:
            clipboard_text = get_clipboard_text()
            with open("clipboard.txt", "w") as file:
                file.write(clipboard_text)
            print("模块4 - 剪贴板内容已写入文件: clipboard.txt")
        except Exception as e:
            print("模块4 - 处理剪贴板内容失败:", e)
        
        # 模块5：使用 win32event 创建事件
        try:
            event_handle = win32event.CreateEvent(None, 0, 0, "ExampleEvent")
            win32event.SetEvent(event_handle)
            win32api.CloseHandle(event_handle)
            print("模块5 - 事件创建: 成功创建并设置 ExampleEvent 事件")
        except Exception as e:
            print("模块5 - 事件创建失败:", e)
    
        # 模块6：使用 win32api 处理鼠标事件
        try:
            screen_width = win32api.GetSystemMetrics(0)
            screen_height = win32api.GetSystemMetrics(1)
            center_x = screen_width // 2
            center_y = screen_height // 2
    
            # 移动鼠标到屏幕中央
            win32api.SetCursorPos((center_x, center_y))
            time.sleep(1)  # 暂停 1 秒
    
            # 执行鼠标点击
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, center_x, center_y, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, center_x, center_y, 0, 0)
            print("模块6 - 鼠标事件: 成功在屏幕中央点击")
        except Exception as e:
            print("模块6 - 鼠标事件失败:", e)
    
    except Exception as e:
        if "Access is denied" in str(e):
            print("请以管理员身份运行此脚本。")
        else:
            print("出现错误:", e)

if __name__ == "__main__":
    try:
        automate_tasks()
    except Exception as e:
        print("出现错误:", e)
