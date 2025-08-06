from collections import defaultdict
import sys
import os

def process_files(input_files, output_file):
    # 使用字典存储 symbols 对应的中文名称集合
    emoji_dict = defaultdict(set)
    
    # 处理所有输入文件
    for filename in input_files:
        if not os.path.exists(filename):
            print(f"警告: 文件 {filename} 不存在，已跳过")
            continue
            
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if not line:  # 跳过空行
                        continue
                    
                    parts = line.split('\t')
                    if len(parts) < 2:  # 忽略无效行
                        print(f"警告: {filename} 第 {line_num} 行格式无效: '{line}'")
                        continue
                        
                    emoji = parts[0].strip()
                    # 添加非空名称到集合
                    for name in parts[1:]:
                        if name.strip():  # 忽略空名称
                            emoji_dict[emoji].add(name.strip())
        except Exception as e:
            print(f"处理文件 {filename} 时出错: {str(e)}")
            continue
    
    # 写入输出文件
    try:
        with open(output_file, 'w', encoding='utf-8') as out_f:
            for emoji, names_set in emoji_dict.items():
                # 将集合排序后转换为列表（可选，使输出更有序）
                sorted_names = sorted(names_set)
                # 写入格式：symbols + 制表符 + 去重后的名称（用制表符连接）
                out_f.write(emoji + '\t' + '\t'.join(sorted_names) + '\n')
        print(f"成功处理 {len(emoji_dict)} 个 symbols，结果已保存到 {output_file}")
    except Exception as e:
        print(f"写入输出文件时出错: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python script.py 文件1.txt 文件2.txt ...")
        print("示例: python script.py 01.txt 02.txt 03.txt")
        sys.exit(1)
    
    input_files = sys.argv[1:]
    output_file = "../all_symbols.txt"
    
    process_files(input_files, output_file)
