from datetime import datetime

source_dir = '../data/raw/classical_data.txt'
target_dir = '../data/classical'

# 计数器
flag = 0
# 文件名
name = 1

# 存放数据
dataList = []

print("开始!")
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

with open(source_dir, mode='r',encoding='UTF-8') as f_source:
    for line in f_source:
        if(line != "" and line != "\n"):
            flag += 1
            dataList.append(line[:])
            if flag == 1800:
                with open(target_dir + "c_list_" + str(name) + ".txt", mode='w+',encoding='UTF-8') as f_target:
                    for data in dataList:
                        f_target.write(data)
                name += 1
                flag = 0
                print("\r已生成"+str(name),end="")
                dataList = []

# 处理最后一批
with open(target_dir + "c_list_" + str(name) + ".txt", mode='w+',encoding='UTF-8') as f_target:
    for data in dataList:
        f_target.write(data)
f_source.close()
print("完成!")
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))