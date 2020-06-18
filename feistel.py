# -*- coding: utf-8 -*-
# 每个分组8个字符，一个密钥4个字符

def strEncrypt(s1, s2, key):  # 每次传输8个字符,分成两组按位异或,密钥4个字符
    result = ''
    for i in range(0, 4):
        temp = ord(s1[i]) ^ ord(s2[i]) ^ ord(key[i])
        result += chr(temp)
    return result


def encode(plainText1,plainText2, keylist):
    cipherText1 = ''
    cipherText2 = ''
    for i in range(0, len(plainText1) // 8):
        temp1 = plainText1[i * 8:(i + 1) * 8]  # 每8个字符划分成一组加密
        L1 = temp1[:4]
        R1 = temp1[4:]
        temp2 = plainText2[i * 8:(i + 1) * 8]  # 每8个字符划分成一组加密
        L2 = temp2[:4]
        R2 = temp2[4:]
        j = 1
        for currentKey in keylist:
            temp11 = R1
            R1 = strEncrypt(L1, R1, currentKey)
            L1 = temp11
            tempText1 = ""
            tempText1 += R1 + L1
            print("********************第%d轮***************************"%j)
            print("明文1第%d轮加密后序列为：%s"%(j,tempText1))
            temp22 = R2
            R2 = strEncrypt(L2, R2, currentKey)
            L2 = temp22
            tempText2 = ""
            tempText2 += R2 + L2
            print("明文2第%d轮加密后序列为：%s" % (j, tempText2))
            num = count(tempText1,tempText2)
            print("改变比特的数量：%d"%num)
            print("雪崩效应：%f"%(num/len(tempText1)))
            j += 1
        cipherText1 += R1 + L1
        cipherText2 += R2 + L2
    return [cipherText1,cipherText2]

def count(m, n):
    count = 0
    index = 0
    for a in m:
        if a != n[index]:
            count+=1
        index+=1
    return count

def main():
    key = []
    a = input('请输入明文:')
    b = input('请输入改变一个比特明文:')
    keynum = input('请输入加密循环次数:')
    for i in range(0, int(keynum)):
        temp = input('请输入第' + str(i) + '组加密时使用的密钥（4个字符）')
        key.append(temp)
    [a,b] = encode(a,b, key)
    print('最终密文1：', a)
    print('最终密文2：', b)
    #####解密
    # key.reverse()
    # a = encode(a, key)
    # print('解密后的明文：', a)


if __name__ == '__main__':
    main()