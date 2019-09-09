from faker import Faker



"""
# faker 使用文档
# 用来随机制造数据
# https://faker.readthedocs.io/en/master/locales/zh_CN.html
简体中文：zh_CN
繁体中文：zh_TW
美国英文：en_US
英国英文：en_GB
德文：de_DE
日文：ja_JP
韩文：ko_KR
法文：fr_FR
"""

faker = Faker('zh_CN')
print('name:', faker.name)
print('address:', faker.address)
print('text:', faker.text)

print('name:', faker.name())
print('address:', faker.address())
print('text:', faker.text())


for i in range(10):
    print('name:', faker.name())

    print('address:', faker.address())
    print('text:', faker.text())



