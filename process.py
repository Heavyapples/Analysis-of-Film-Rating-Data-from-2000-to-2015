import pandas as pd
import matplotlib.pyplot as plt
import os

# 修改显示设置为了显示完整前三行后两行
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# 函数1：读取 CSV 文件并显示前三行和后两行
def task1():
    file_path = input('请输入CSV文件的路径（例如：path\\filename.csv）: ')
    if not os.path.exists(file_path):
        print("文件不存在，请重新输入")
        return None
    df = pd.read_csv(file_path)
    print("前三行:")
    print(df.head(3))
    print("\n后两行:")
    print(df.tail(2))
    return df

# 函数2：数据预处理并导出到新的 CSV 文件
def task2(df):
    if df is None:
        print("无法进行数据预处理，因为数据框为空")
        return
    columns = ['id', 'release_date', 'title', 'vote_average', 'vote_count']
    export_path = input('请输入导出CSV文件的路径和文件名（例如：path\\filename.csv）: ')
    if os.path.isdir(export_path):
        print("输入的是一个目录，请包含文件名")
        return
    df = df.dropna()
    df = df[columns]
    try:
        df.to_csv(export_path, index=False)
        print("数据预处理完成，结果已导出到新的 CSV 文件")
    except PermissionError:
        print("权限错误：无法写入文件。请检查文件是否已打开，或者程序是否有写入权限。")

# 函数3：读取新的CSV文件，按 vote_average 降序排列，导出为txt文件
def task3():
    file_path = input('请输入读取CSV文件的路径和文件名（例如：path\\filename.csv）: ')
    if not os.path.isfile(file_path):
        print("文件不存在，请检查路径和文件名")
        return
    export_path = input('请输入导出txt文件的路径和文件名（例如：path\\filename.txt）: ')
    if os.path.isdir(export_path):
        print("输入的是一个目录，请包含文件名")
        return
    df = pd.read_csv(file_path)
    df.sort_values(by='vote_average', ascending=False, inplace=True)
    try:
        df.to_csv(export_path, index=False, sep=',')
        print("已按 vote_average 降序排列数据集，结果已导出到新的 txt 文件")
    except PermissionError:
        print("权限错误：无法写入文件。请检查文件是否已打开，或者程序是否有写入权限。")

# 函数4：读取新的txt文件，统计 vote_average 的最大值、最小值、平均值
def task4():
    file_path = input('请输入要读取的TXT文件的路径（例如：path\\filename.txt）: ')
    if not os.path.exists(file_path):
        print("文件不存在，请重新输入")
        return
    df = pd.read_csv(file_path)
    maxValue = df['vote_average'].max()
    minValue = df['vote_average'].min()
    meanValue = df['vote_average'].mean()
    print("最大值:", maxValue)
    print("最小值:", minValue)
    print("平均值:", meanValue)

# 函数5：读取txt文件，离散化 vote_average，添加新列，并画出饼状图
def task5():
    file_path = input('请输入读取txt文件的路径和文件名（例如：path\\filename.txt）: ')
    if not os.path.isfile(file_path):
        print("文件不存在，请检查路径和文件名")
        return
    csv_export_path = input('请输入导出CSV文件的路径和文件名（例如：path\\filename.csv）: ')
    if os.path.isdir(csv_export_path):
        print("输入的是一个目录，请包含文件名")
        return
    png_export_path = input('请输入导出PNG文件的路径和文件名（例如：path\\filename.png）: ')
    if os.path.isdir(png_export_path):
        print("输入的是一个目录，请包含文件名")
        return
    df = pd.read_csv(file_path)
    maxValue = df['vote_average'].max()
    minValue = df['vote_average'].min()

    # 根据最大值和最小值离散化 vote_average
    # 设置bins为4个等宽区间
    bins = pd.cut(df['vote_average'], bins=4, labels=['bad', 'ok', 'good', 'excellent'])
    df['Label'] = bins

    # 将新的数据集保存为csv文件
    df.to_csv(csv_export_path, index=False)

    # 根据离散化结果画出饼状图
    plot = df['Label'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.savefig(png_export_path, dpi=300)
    print("已完成离散化，结果已保存为csv文件，并已根据离散化结果画出饼状图")

def main():
    while True:
        print("请选择一个任务执行:")
        print("1. 读取 CSV 文件并显示前三行和后两行")
        print("2. 数据预处理并导出到新的 CSV 文件")
        print("3. 读取新的CSV文件，按 vote_average 降序排列，导出为txt文件")
        print("4. 读取新的txt文件，统计 vote_average 的最大值、最小值、平均值")
        print("5. 读取txt文件，离散化 vote_average，添加新列，并画出饼状图")
        print("0. 退出")
        task = input("请输入你的选择(0-5): ")
        if task == "1":
            df = task1()
        elif task == "2":
            task2(df)
        elif task == "3":
            task3()
        elif task == "4":
            task4()
        elif task == "5":
            task5()
        elif task == "0":
            break
        else:
            print("无效的输入，请输入 0-5 之间的数字")


if __name__ == "__main__":
    main()
