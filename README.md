

- 开发目的：自用
- 功能：将东北大学研究生教务系统导出的表格转换为 WakeUp APP 可识别的格式



请确保输入 Excel 表格格式如下：

| 课程编号     | 课程名称               | 班级名称   | 学分 | 阶段 | 任课教师 | 开始周 | 结束周 | 时间               | 上课地点 | 选课人数 |
| ------------ | ---------------------- | ---------- | ---- | ---- | -------- | ------ | ------ | ------------------ | -------- | -------- |
| yzxxxxxxxxxx | 人工智能前沿技术与应用 | xx班xx校区 | 2.0  | 1    | 张三     | 18     | 18     | 星期一 下午7-下午8 | F109     | 100      |



输出：

| 课程名称               | 星期 | 开始节数 | 结束节数 | 老师 | 地点 | 周数  |
| ---------------------- | ---- | -------- | -------- | ---- | ---- | ----- |
| 人工智能前沿技术与应用 | 一   | 7        | 8        | 张三 | F109 | 18-18 |





程序界面截图：

![image-20241125222245549](.\assets\image-20241125222245549.png)