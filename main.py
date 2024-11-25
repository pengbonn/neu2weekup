import tkinter as tk
import os
from tkinter import filedialog
import os.path
import pandas as pd

g_filepath = None
g_filename = None
g_filedir = None


def open_file_dialog():
    global g_filename, g_filedir, g_filepath
    # 打开文件选择对话框，并获取选择的文件路径
    filepath = filedialog.askopenfilename()

    if filepath:
        # 获取文件名
        filename = os.path.basename(filepath)
        filedir = os.path.dirname(filepath)
        # 在文本标签中显示文件名
        file_label.config(text=f"{filepath}")

    g_filepath, g_filename, g_filedir = filepath, filename, filedir
    print(g_filepath, g_filename, g_filedir)


def neu2wakeup():
    wakeup_columns = ['课程名称', '星期', '开始节数', '结束节数', '老师', '地点', '周数']
    df_wakeup = pd.DataFrame(columns=wakeup_columns)
    # ['课程编号', '课程名称', '班级名称', '学分', '阶段', '任课教师', '开始周', '结束周', '时间', '上课地点', '选课人数']
    df_neu = pd.read_excel(g_filepath)

    # 将时间列拆分
    df_neu["星期"] = df_neu['时间'].str.extract(r'星期(.)')
    df_neu["开始节数"] = df_neu['时间'].str.extract(r'(\d+)\s*-')
    df_neu["结束节数"] = df_neu['时间'].str.extract(r'(\d+)\s*$')
    df_neu['周数'] = df_neu.apply(lambda row: "{}-{}".format(row['开始周'], row['结束周']), axis=1)

    for row in df_neu.itertuples():
        class_name = getattr(row, '课程名称')
        week = getattr(row, '星期')
        end_section = getattr(row, "结束节数")
        start_section = getattr(row, "开始节数")
        teacher = getattr(row, "任课教师")
        place = getattr(row, "上课地点")
        week_number = getattr(row, "周数")

        if pd.isna(start_section):
            start_section = end_section
        df_temp = pd.DataFrame([[class_name, week, start_section, end_section, teacher, place, week_number]],
                               columns=wakeup_columns)
        df_wakeup = pd.concat([df_wakeup, df_temp], ignore_index=True)

    # print(df_wakeup)
    only_name, _ = os.path.splitext(g_filename)
    output_path = os.path.join(g_filedir, "{}_wakeup.csv".format(only_name))
    df_wakeup.to_csv(output_path, index=False, encoding="utf-8-sig")
    process_label.config(text=output_path)


# 创建主窗口
root = tk.Tk()
root.title("NEU学生课表转 Wakeup 格式")

# 设置窗体大小（宽度x高度）
window_width = 400
window_height = 250
root.geometry(f"{window_width}x{window_height}")

# 创建一个按钮，点击时会打开文件选择对话框
browse_button = tk.Button(root, text="选择文件", command=open_file_dialog)
browse_button.pack(pady=20)

# 创建一个标签，用于显示选择的文件路径
file_label = tk.Label(root, text="没有选择文件")
file_label.pack(pady=10)

process_button = tk.Button(root, text="处理文件", command=neu2wakeup)
process_button.pack(pady=20)

# 创建一个标签，用于显示选择的文件路径
process_label = tk.Label(root, text="没有处理的文件")
process_label.pack(pady=10)
# 运行主事件循环
root.mainloop()
