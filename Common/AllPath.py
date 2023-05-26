import os
#获取项目所有模块路径，方便直接使用
current_path = os.path.abspath('..')  # 获取父目录路径
conmmon_path = os.path.join(current_path, "Common")  # Common的路径
config_path = os.path.join(current_path, "Config")  # Config的路径
Log_path = os.path.join(current_path, "Log")  # Log的路径
report_path = os.path.join(current_path, "Report")

print(report_path)
