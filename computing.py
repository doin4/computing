# doin4
# 2021.12.22
# 自用计算脚本，欢迎指正
import numpy as np
import math
import random

class node(object):
    def __init__(self, name=None, value=None):
        # 注意，这里给初始化要么两个都给，要么都不给，不能只给中间那个，不给后面的
        self.value = value
        self.name =  name
        self.left = None
        self.right = None

class HuffmanTree(object):
    def __init__(self, char_weight):
        # 注意，传过来的参数这里第一个是编码的变量名，第二个是出现的频数
        self.array_ = [node(part[0], part[1]) for part in char_weight]
        while(len(self.array_) != 1):
            # 把节点连成树，最后就只剩下最后一个根节点
            self.array_.sort(key=lambda node:node.value, reverse=True)
            # reverse=True意味着这是降序，最后的值是最小的点
            # 注意，这里使用lambda函数，直接对节点进行排序，必须是在循环内做
            # 因为每次计算之后会删去两个最小的点并且加上一个稍大的点，需要再次排序才能保证顺序正确
            c = node(value=(self.array_[-1].value + self.array_[-2].value))
            c.left = self.array_.pop(-1)
            c.right = self.array_.pop(-1)
            # .pop(-1)操作会把原来数组内的数据输出
            self.array_.append(c)
            # 至此，每次把最后两个节点拿出来合成一个大的节点，并且加在原始array_之后
            # 用这种方法迭代下去，就可以得到的Huffman树，后面还需要手动指出一个根节点
        self.root = self.array_[0]
    
    def coding(self, root, length, l):
        # 这又是一个迭代算法，输入树之后，需要分别对左树和右树做不同处理，这一才能得到最终的结果
        # 只能说对迭代算法设计还一窍不通，慢慢积累吧
        if not l:
            self.buffer = [0] * length
            # 初始化编码的长度，最长为树的深度
        node = root
        if not node:
            # 如果迭代完了，就退出编码
            return
        elif node.name:
            # 若是这个节点有名字，证明是我们需要编码的字母，所以要输出编码
            print(node.name +'的编码为：', end='')
            for i in range(l):
                print(self.buffer[i], end='')
            print('\t')
            return 
        self.buffer[l] = 0
        self.coding(node.left, length, l + 1)
        self.buffer[l] = 1
        self.coding(node.right, length, l + 1)

def my_random(array):
    return random.shuffle(array)

def C(m, n):
    # m中选出n个组合
    return math.factorial(m) / (math.factorial(n) * math.factorial(m - n))

def A(m, n):
    # m中选出n个排列
    return math.factorial(m) / math.factorial(m - n)

def huffman_coding(char_weight):
    tree = HuffmanTree(char_weight)
    length = len(char_weight)
    tree.coding(tree.root, length, 0)
    # 注意，这里一定是传入根节点，从节点开始遍历树，而不是说直接遍历树，计算机操作在这体现出了不同

def P_rlc(length, p1, p0):
    # 游程码的概率计算run length coding
    p_L0 = 1
    p_L1 = 1
    k_L0 = 0
    k_L1 = 0
    H_X0 = 0
    H_X1 = 0
    for i in range(length):
        if not i:
            p_L0 = p1
            p_L1 = p0
        else:
            p_L0 *= p0
            p_L1 *= p1
        k_L0 += (i + 1) * p_L0
        k_L1 += (i + 1) * p_L1
        H_X0 -= p_L0 * math.log(p_L0, 2)
        H_X1 -= p_L1 * math.log(p_L1, 2)
        print(f'游程长度为{i+1}  0的概率为:{p_L0}，1的概率为:{p_L1}')
    print(f'其中0的平均步长为:{k_L0}，1的平均步长为:{k_L1}')
    print(f'其中0的熵为:{H_X0}，1的熵为:{H_X1}')
    n0 = H_X0 / k_L0
    n1 = H_X1 / k_L1
    n = (H_X0 + H_X1) / (k_L0 + k_L1)
    print(f'其中0的编码效率为:{n0}，1的编码效率为:{n1}, 总的编码效率为:{n}')

# char_weights=[('0',384),('1',196),('2',96),('3',96),('4',84),('5',84),('6',32),('7',24)]
if __name__ == '__main__':
    print('-------------------test-------------------')
    P_rlc(16, 0.4, 0.6)
    print('-----------------end test------------------')
