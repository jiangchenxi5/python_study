# 编码和解码
# 把码位转换成字节序列的过程是编码（encode） 把字节序列转换为码位的过程是解码（decode）

s = 'c中国人民大学safss'
print(len(s))
b = s.encode(encoding='UTF-8')
print(b)
print(s.encode(encoding='GBK'))
print(len(b))
print(b.decode())
print('-' * 100)
# bytes和bytearray对象
cafe = bytes('cafe宁波大学', encoding='UTF-8')
print(cafe)
print(cafe[0])
print(cafe[:1])
cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe[0] == cafe[:1])

# 多种编码器
for codec in ['gb2312', 'utf_8', 'utf_16']:
    print(codec, 'EL ab 中国'.encode(codec), sep='\t')

# 处理UnicodeEncodeError errors常用的ignore(忽视跳过)\replace(替换成?)\xmlcharrefreplace(替换为XML实体)
# Python默认编码UTF-8
# 别依赖编码指定值