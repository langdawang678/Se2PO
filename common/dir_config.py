import os

current_dir = os.path.abspath(__file__)

project_dir = os.path.split(os.path.split(current_dir)[0])[0]
print(project_dir)  # 当前项目根目录

testcases_dir = os.path.join(project_dir, "testcases")
testdata_dir = os.path.join(project_dir, "testdata")
reports_dir = os.path.join(project_dir, "output/reports")
logs_dir = os.path.join(project_dir, "output/logs")
screenshots_dir = os.path.join(project_dir, "output/screenshots")

