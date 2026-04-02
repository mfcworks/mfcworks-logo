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

# 表示確認
x = [p[0] for p in points[1:]]
y = [p[1] for p in points[1:]]


#plt.figure(figsize=(5, 5))
#plt.axes().set_aspect('equal')

#plt.fill(x, y)
#plt.grid()
#plt.show()


# グラデーション確認
xmin, xmax = -100, 100
ymin, ymax = -100, 100
# グリッド作成
nx, ny = 256, 256
xx = np.linspace(xmin, xmax, nx)
yy = np.linspace(ymin, ymax, ny)
X, Y = np.meshgrid(xx, yy)


# 左上 → 右下の勾配を作る
# 左上：値小、右下：値大
gradient = (X - xmin) / (xmax - xmin) + (ymax - Y) / (ymax - ymin)
gradient = gradient / gradient.max()  # 正規化

# カラーマップ
# color_edge = '#1F3A5F'
# color_center = '#3FA9F5'
# color_edge = '#2C3E50'
# color_center = "#4CA1AF"
# color_edge = '#1A2A6C'
# color_center = "#00C6FF"

# color_edge = '#2C3E50'
# color_center = "#BDC3C7"
color_edge = '#243447'
color_center = "#6B7C86"
# color_edge = '#1F2A36'
# color_center = "#7A8F99"


cmap = LinearSegmentedColormap.from_list(
    "custom",
    [color_edge, color_edge, color_center, color_edge, color_edge]
)

# 画像として配置
fig, ax = plt.subplots(figsize=(7, 7))

# polygon = plt.Polygon(list(zip(x, y)), closed=True, edgecolor='#3FA9F5', facecolor='none')
polygon = plt.Polygon(list(zip(x, y)), closed=True, facecolor='none')
ax.add_patch(polygon)


im = ax.imshow(
    gradient,
    extent=(xmin, xmax, ymin, ymax),
    origin='lower',
    aspect='equal',
    cmap=cmap
)

im.set_clip_path(polygon)
#plt.gca().axis('off')
ax.set_xlim(-105, 105)
ax.set_ylim(-105, 105)
#ax.set_aspect('equal')
plt.show()