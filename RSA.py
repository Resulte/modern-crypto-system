from OpenSSL.crypto import PKey
from OpenSSL.crypto import TYPE_RSA, FILETYPE_PEM
from OpenSSL.crypto import dump_privatekey, dump_publickey
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
import os,rsa
from rsa import VerificationError


def generate_key():
    pk = PKey()
    pk.generate_key(TYPE_RSA, 2048)
    # 生成公钥文件
    public_key = dump_publickey(FILETYPE_PEM, pk)
    public_key_path = os.path.join(os.path.dirname(__file__), 'public_key.pem')
    file_public_key = open(public_key_path, 'wb')
    file_public_key.write(public_key)
    file_public_key.close()
    # 生成私钥文件
    private_key = dump_privatekey(FILETYPE_PEM, pk)
    private_key_path = os.path.join(os.path.dirname(__file__), 'private_key.pem')
    file_private_key = open(private_key_path, 'wb')
    file_private_key.write(private_key)
    file_private_key.close()

# 加密文件
def encrypt_file(key_file_name, file_path):
    key_file = open(key_file_name, 'rb')
    key_data = key_file.read()
    key_file.close()
    public_key = serialization.load_pem_public_key(key_data, backend=default_backend())
    file = open(file_path, 'rb')
    file_data = file.read()
    encrypt_file_data = public_key.encrypt(file_data, padding.PKCS1v15())
    encrypt_file_path = file_path + ".enc"
    encrypt_file = open(encrypt_file_path, 'wb')
    encrypt_file.write(encrypt_file_data)
    encrypt_file.close()

# 解密文件
def decrypt_file(key_file_name, file_path):
    key_file = open(key_file_name, 'rb')
    key_data = key_file.read()
    key_file.close()
    private_key = serialization.load_pem_private_key(key_data, password=None,backend=default_backend())
    file = open(file_path, 'rb')
    file_data = file.read()
    decrypt_file_data = private_key.decrypt(file_data,padding.PKCS1v15())
    decrypt_file_path = file_path + ".dec"
    decrypt_file = open(decrypt_file_path, 'wb')
    decrypt_file.write(decrypt_file_data)
    decrypt_file.close()

if __name__=='__main__':
    print("**********************************欢迎来到SSL文件加解密系统************************************")
    while True:
        print("1、生成RSA公钥和私钥    2、RSA公钥加密文件    3、RSA私钥解密文件    4、退出系统")
        chioce = input("请选择对应功能的序号：")
        if chioce == "1":
            print("生成RSA公钥和私钥开始!")
            generate_key()
            print("生成RSA公钥和私钥成功！")
            print("生成的RSA公钥文件在当前程序目录下，文件名为：public_key.pem")
            print("生成的RSA私钥文件在当前程序目录下，文件名为：private_key.pem")
            print("****************************************************************************")
        elif chioce == "2":
            print("RSA公钥加密开始!")
            file = input("请输入要加密的文件的路径+文件名：")
            key = input("请输入RSA公钥的文件的路径+文件名：")
            encrypt_file(key, file)
            print("加密成功！加密后的文件为:"+file+".enc")
            print("****************************************************************************")
        elif chioce == "3":
            print("RSA私钥解密开始!")
            file = input("请输入要解密的文件的路径+文件名：")
            key = input("请输入RSA私钥的文件的路径+文件名：")
            decrypt_file(key, file)
            print("解密成功！解密后的文件为:" + file + ".dec")
            print("****************************************************************************")
        elif chioce == "4":
            print("退出成功，拜拜~~")
            break
        else:
            print("错误！请输入1、2、3、4中的一个")
