# 输入文件路径
emoji_file = "all_emoji.txt"

# 输出文件路径
output_emoji_file = "emoji_opencc.txt"

def process_file(input_file, output_file):
    """处理单个文件，并将结果写入输出文件"""
    # 构建中文词到表情的映射
    word_to_emojis = {}
    
    # 读取输入文件
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    # 处理每一行
    for line in lines:
        # 去除换行符并按 tab 拆分
        parts = line.strip().split("\t")
        if not parts:
            continue
        
        # 表情是第一个部分
        emoji = parts[0]
        # 中文词是剩余部分
        words = parts[1:]
        
        # 将每个中文词映射到表情
        for word in words:
            if word not in word_to_emojis:
                word_to_emojis[word] = []
            word_to_emojis[word].append(emoji)
    
    # 生成结果并写入输出文件
    with open(output_file, "w", encoding="utf-8") as file:
        for word, emojis in word_to_emojis.items():
            # 合并表情，用空格分隔
            merged_emojis = " ".join(emojis)
            # 格式化为目标格式
            formatted_line = f"{word}\t{word} {merged_emojis}\n"
            file.write(formatted_line)

# 处理 emoji 文件
process_file(emoji_file, output_emoji_file)
print(f"Emoji 处理完成，结果已写入 {output_emoji_file}")

