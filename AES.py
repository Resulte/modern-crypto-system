import os, random, struct
from Crypto.Cipher import AES
try:
    from Crypto.Util.Padding import pad, unpad
except ImportError:
    from Crypto.Util.py3compat import bchr, bord
    def pad(data_to_pad, block_size):
        padding_len = block_size-len(data_to_pad)%block_size
        padding = bchr(padding_len)*padding_len
        return data_to_pad + padding
    def unpad(padded_data, block_size):
        pdata_len = len(padded_data)
        if pdata_len % block_size:
            raise ValueError("Input data is not padded")
        padding_len = bord(padded_data[-1])
        if padding_len<1 or padding_len>min(block_size, pdata_len):
            raise ValueError("Padding is incorrect.")
        if padded_data[-padding_len:]!=bchr(padding_len)*padding_len:
            raise ValueError("PKCS#7 padding is incorrect.")
        return padded_data[:-padding_len]
def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = in_filename + '.enc'
    iv = os.urandom(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)
            pos = 0
            while pos < filesize:
                chunk = infile.read(chunksize)
                pos += len(chunk)
                if pos == filesize:
                    chunk = pad(chunk, AES.block_size)
                outfile.write(encryptor.encrypt(chunk))
def decrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = in_filename + '.dec'
    with open(in_filename, 'rb') as infile:
        filesize = struct.unpack('<Q', infile.read(8))[0]
        iv = infile.read(16)
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        with open(out_filename, 'wb') as outfile:
            encrypted_filesize = os.path.getsize(in_filename)
            pos = 8 + 16 # the filesize and IV.
            while pos < encrypted_filesize:
                chunk = infile.read(chunksize)
                pos += len(chunk)
                chunk = encryptor.decrypt(chunk)
                if pos == encrypted_filesize:
                    chunk = unpad(chunk, AES.block_size)
                outfile.write(chunk)
#测试代码
if __name__=='__main__':
    # key = "keyskeyskeyskeys"
    print("******************欢迎来到离线内容保护系统**********************")
    while True:
        print("1、AES加密文件    2、AES解密文件    3、退出系统")
        chioce = input("请选择对应功能的序号：")
        if chioce == "1":
            print("AES加密开始!")
            file = input("请输入要加密的文件的路径+文件名：")
            key  = input("请输入加密密钥：")
            encrypt_file(key.encode('utf-8'),file)
            print("加密成功！加密后的文件为"+file+".enc")
            print("***************************************************")
        elif chioce == "2":
            print("AES解密开始!")
            file = input("请输入要解密的文件的路径+文件名：")
            key = input("请输入解密密钥：")
            decrypt_file(key.encode('utf-8'), file)
            print("解密成功！解密后的文件为" + file + ".dec")
            print("***************************************************")
        elif chioce == "3":
            print("退出成功，拜拜~~")
            break
        else:
            print("错误！请输入1、2、3中的一个")
