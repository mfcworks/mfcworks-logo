import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def vector(len, arg):
    return np.array([len * np.cos(np.radians(arg)), len * np.sin(np.radians(arg))])

r = 100
t = 20

th = t / np.sin(np.radians(60))


# 原点
points = [np.array([0, 0])]

# 各座標（p1～p16）
points.append(points[0] + vector(r, 180))
points.append(points[1] + vector(r, 60))
points.append(points[2] + vector(th, 0))
points.append(points[3] + vector(r - 2 * th, 300))
points.append(points[4] + vector(r - 2 * th, 60))
points.append(points[5] + vector(th, 0))
points.append(points[6] + vector(r - 2 * th, 300))
points.append(points[7] + vector(5 / 2 * th, 240))
points.append(-(points[8] + vector(th, 120)))
points.append(points[9] + vector(3 / 2 * th, 240))
points.append(points[10] + vector(r - 3 * th, 300))
points.append(points[11] + vector(r - 2 * th, 60))
points.append(points[12] + vector(th, 0))
points.append(points[13] + vector(r - 2 * th, 300))
points.append(points[14] + vector(r - th, 60))
points.append(points[7])


# p1～p16を原点に対して反転したものを結合（p17～p32）
mapped = list(map(lambda p: -p, points[1:]))
points = points + mapped

# 始点へ戻る
points.append(points[1])


# 座標変換
conv = list(map(lambda p: np.array([100 + p[0], 100 - p[1]]), points))
#print(conv)

# 数値丸め
conv2 = np.round(conv, decimals=4)



svg_open = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">'
print(svg_open)

defs = """\
  <defs>
    <linearGradient id="linearGradient" gradientTransform="rotate(30 0.5 0.5)">
      <stop offset="42%" stop-color="#243447"/>
      <stop offset="62%" stop-color="#6B7C86"/>
      <stop offset="72%" stop-color="#243447"/>
    </linearGradient>
  </defs>\
"""

print(defs)

path_open = '  <path fill="url(#linearGradient)" d="'
print(path_open)

print(f'    M {conv2[1][0]} {conv2[1][1]}')
for p in conv2[2:]:
    print(f'    L {p[0]} {p[1]}')

path_close = '    Z"/>'
print(path_close)

svg_close = '</svg>'
print(svg_close)

with open('logo.svg', 'w') as file:
    file.write(svg_open + '\n')
    file.write(defs + '\n')
    file.write(path_open + '\n')
    file.write(f'    M {conv2[1][0]} {conv2[1][1]}\n')
    for i in conv2[2:]:
        file.write(f'    L {p[0]} {p[1]}\n')
    file.write(path_close + '\n')
    file.write(svg_close + '\n')