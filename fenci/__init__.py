import jieba
seg_list = jieba.cut("香农在信息论中提出的信息熵定义为自信息的期望",cut_all=True)
print(" ".join(seg_list))
seg_list = jieba.cut("香农在信息论中提出的信息熵定义为自信息的期望")
print(" ".join(seg_list))
seg_list = jieba.cut_for_search("香农在信息论中提出的信息熵定义为自信息的期望")
print(" ".join(seg_list))