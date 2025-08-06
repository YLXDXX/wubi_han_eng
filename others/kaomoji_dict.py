import pypinyin

file_begin='''# Rime dictionary
# encoding: utf-8
#
#
---
name: icon_kaomoji
version: "2025-08-06"
sort: by_weight
...

'''


# 将中文转换为拼音的函数，每个字的拼音用空格隔开
def chinese_to_pinyin(chinese_text):
    pinyin_list = pypinyin.lazy_pinyin(chinese_text)  # 获取拼音列表
    return ' '.join(pinyin_list)  # 用空格连接拼音

# 处理单个文件的函数
def process_file(input_file, output_file):
    # 读取文件内容
    with open(input_file, "r", encoding="utf-8") as file:
        file_content = file.readlines()  # 读取所有行
    
    
    
    # 处理每一行
    result = []
    for line in file_content:
        line = line.strip()  # 去除行首尾的空白字符
        if not line:  # 跳过空行
            continue
        parts = line.split("\t")  # 按制表符分割
        symbol = parts[0]  # 表情符号或颜文字
        for chinese in parts[1:]:  # 遍历每个中文解释
            pinyin = chinese_to_pinyin(chinese)  # 转换为拼音（每个字用空格隔开）
            result.append(f"{symbol}\t{pinyin}")  # 表情/颜文字和拼音用制表符分隔

    # 将结果保存到文件
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(file_begin) # 写入文件头
        for line in result:
            f.write(line + "\t1\n")

# 处理 all_kaomoji.txt
process_file("all_kaomoji.txt", "../rime/rime_icons/icon_kaomoji.dict.yaml")
