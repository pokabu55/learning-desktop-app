a = "富士山"
b = 3776
txt = f"{a}の高さは{b}m"
print(txt)

a = 12
b = 1234567
print(f"桁区切り：a={a:,} b={b:,}")
print(f"５桁未満はゼロ埋め：a={a:020} b={b:020}")

c = 123.4
d = 123.456789
print(f"小数点以下３桁：c={c:.3f} d={d:.3f}")
print(f"小数点以下５桁：c={c:.5f} d={d:.5f}")

a = 123
b = 255
c = 65535
print(f"10進数：a={a:} b={b:} c={c:}")
print(f" 2進数：a={a:#b} b={b:#b} c={c:#b}")
print(f"16進数：a={a:#x} b={b:#x} c={c:#x}")
