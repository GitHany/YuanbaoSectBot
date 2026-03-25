"""
RSA加密算法实现
"""

import random
import math


def gcd(a, b):
    """
    计算最大公约数

    参数:
        a (int): 第一个整数
        b (int): 第二个整数

    返回:
        int: 最大公约数
    """
    while b != 0:
        a, b = b, a % b
    return a


def generate_prime(size):
    """
    生成素数

    参数:
        size (int): 素数的位数

    返回:
        int: 生成的素数
    """

    def is_prime(n):
        """判断是否为素数"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        # 测试从5到sqrt(n)
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6

        return True

    # 生成候选素数
    while True:
        candidate = random.getrandbits(size)
        # 确保是奇数
        candidate |= 1
        if is_prime(candidate):
            return candidate


class RSA:
    """
    RSA加密算法

    参数:
        prime_size (int): 素数位数
    """

    def __init__(self, prime_size=8):
        """
        初始化RSA加密算法

        参数:
            prime_size (int): 素数位数
        """
        self.prime_size = prime_size
        self.p = None
        self.q = None
        self.n = None
        self.e = None
        self.d = None

    def generate_keys(self):
        """
        生成RSA公钥和私钥

        返回:
            tuple: (公钥(n, e), 私钥(d))
        """
        # 生成两个素数
        self.p = generate_prime(self.prime_size)
        self.q = generate_prime(self.prime_size)

        # 计算n
        self.n = self.p * self.q

        # 计算φ(n)
        phi = (self.p - 1) * (self.q - 1)

        # 选择e（通常选择65537）
        self.e = 65537
        while gcd(self.e, phi) != 1:
            self.e += 2

        # 计算d（私钥）
        self.d = self._mod_inverse(self.e, phi)

        return (self.n, self.e), self.d

    def _mod_inverse(self, a, m):
        """
        计算模逆元

        参数:
            a (int): 要计算逆元的数
            m (int): 模

        返回:
            int: a mod m的逆元
        """
        m0, x0, x1 = m, 0, 1

        if m == 1:
            return 0

        while a > 1:
            # q是商
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0

        return x1 + m0 if x1 < 0 else x1

    def encrypt(self, message, public_key):
        """
        RSA加密

        参数:
            message (str): 要加密的消息
            public_key (tuple): 公钥(n, e)

        返回:
            list: 加密后的数字列表
        """
        n, e = public_key
        encrypted = []

        # 将消息转换为数字并加密
        for char in message:
            # 将字符转换为ASCII码
            m = ord(char)
            # 加密：c = m^e mod n
            c = pow(m, e, n)
            encrypted.append(c)

        return encrypted

    def decrypt(self, encrypted, private_key):
        """
        RSA解密

        参数:
            encrypted (list): 加密的数字列表
            private_key (int): 私钥d

        返回:
            str: 解密后的消息
        """
        d = private_key
        decrypted_chars = []

        # 解密每个数字
        for c in encrypted:
            # 解密：m = c^d mod n
            m = pow(c, d, self.n)
            decrypted_chars.append(chr(m))

        return "".join(decrypted_chars)

    def encrypt_message(self, message):
        """
        加密消息

        参数:
            message (str): 要加密的消息

        返回:
            tuple: (加密后的数字列表, 公钥, 私钥)
        """
        public_key, private_key = self.generate_keys()
        encrypted = self.encrypt(message, public_key)

        return encrypted, public_key, private_key

    def decrypt_message(self, encrypted, public_key, private_key):
        """
        解密消息

        参数:
            encrypted (list): 加密的数字列表
            public_key (tuple): 公钥(n, e)
            private_key (int): 私钥d

        返回:
            str: 解密后的消息
        """
        self.n, self.e = public_key
        self.d = private_key

        return self.decrypt(encrypted, private_key)

    def summary(self):
        """
        打印RSA密钥信息

        返回:
            str: 密钥信息摘要
        """
        if not self.p or not self.q:
            return "尚未生成密钥"

        info = f"RSA密钥信息:\n"
        info += f"素数p: {self.p}\n"
        info += f"素数q: {self.q}\n"
        info += f"公钥(n): {self.n}\n"
        info += f"公钥(e): {self.e}\n"
        info += f"私钥(d): {self.d}\n"
        info += f"φ(n): {(self.p - 1) * (self.q - 1)}\n"

        return info


def rsa_demo():
    """
    RSA算法演示示例
    """
    print("RSA加密算法演示:")

    # 创建RSA实例
    rsa = RSA(prime_size=8)

    # 生成密钥
    public_key, private_key = rsa.generate_keys()

    print("密钥信息:")
    print(rsa.summary())

    # 测试加密和解密
    message = "Hello World"
    print(f"\n原始消息: '{message}'")

    # 加密
    encrypted = rsa.encrypt(message, public_key)
    print(f"加密后的数字: {encrypted}")

    # 解密
    decrypted_message = rsa.decrypt(encrypted, private_key)
    print(f"解密后的消息: '{decrypted_message}'")

    # 验证解密结果
    if decrypted_message == message:
        print("✅ RSA加密和解密成功！")
    else:
        print("❌ RSA加密和解密失败！")

    return rsa


def rsa_long_message_demo():
    """
    RSA长消息演示示例
    """
    print("\nRSA长消息演示:")

    # 创建RSA实例
    rsa = RSA(prime_size=8)

    # 生成密钥
    public_key, private_key = rsa.generate_keys()

    # 加密长消息
    long_message = "RSA算法是一种非对称加密算法，广泛应用于安全通信"
    print(f"原始长消息: '{long_message}'")

    # 加密
    encrypted = rsa.encrypt(long_message, public_key)
    print(f"加密后的数字: {encrypted[:10]}... (总共{len(encrypted)}个数字)")

    # 解密
    decrypted_message = rsa.decrypt(encrypted, private_key)
    print(f"解密后的消息: '{decrypted_message}'")

    # 验证解密结果
    if decrypted_message == long_message:
        print("✅ RSA加密和解密成功！")
    else:
        print("❌ RSA加密和解密失败！")


def rsa_key_generation_demo():
    """
    RSA密钥生成演示
    """
    print("\nRSA密钥生成演示:")

    # 生成不同大小的密钥
    for size in [6, 8, 10]:
        rsa = RSA(prime_size=size)
        public_key, private_key = rsa.generate_keys()

        n, e = public_key
        print(f"素数位数: {size}")
        print(f"公钥n: {n}")
        print(f"公钥e: {e}")
        print(f"私钥d: {private_key}")
        print(f"可加密的最大字符值: {n}")
        print()


def rsa_math_demo():
    """
    RSA数学原理演示
    """
    print("\nRSA数学原理演示:")

    # 生成小素数用于演示
    p = 17  # 素数
    q = 19  # 素数

    n = p * q  # 323
    phi = (p - 1) * (q - 1)  # 288

    # 选择e
    e = 5

    # 计算d
    rsa = RSA(prime_size=8)
    rsa.p = p
    rsa.q = q
    rsa.n = n

    d = rsa._mod_inverse(e, phi)

    print(f"素数p: {p}")
    print(f"素数q: {q}")
    print(f"n = p × q = {n}")
    print(f"φ(n) = (p-1) × (q-1) = {phi}")
    print(f"选择的公钥e: {e}")
    print(f"计算的私钥d: {d}")

    # 验证: e × d ≡ 1 mod φ(n)
    if (e * d) % phi == 1:
        print(f"✅ 验证成功: {e} × {d} ≡ 1 mod {phi}")
    else:
        print(f"❌ 验证失败")

    # 加密解密演示
    message_num = post
    print(f"要加密的数字: {message_num}")

    # 加密: c = m^e mod n
    encrypted = pow(message_num, e, n)
    print(f"加密结果: {encrypted}")

    # 解密: m = c^d mod n
    decrypted = pow(encrypted, d, n)
    print(f"解密结果: {decrypted}")

    if decrypted == message_num:
        print("✅ RSA加密解密验证成功！")
    else:
        print("❌ RSA加密解密验证失败！")


if __name__ == "__main__":
    print("RSA加密算法演示")
    print("================\n")

    # 基本演示
    rsa_demo()

    # 长消息演示
    rsa_long_message_demo()

    # 密钥生成演示
    rsa_key_generation_demo()

    # 数学原理演示
    rsa_math_demo()
