from sys import version_info

major, minor, micro = version_info[0], version_info[1], version_info[2]
print(f'Python {major}.{minor}.{micro}')
