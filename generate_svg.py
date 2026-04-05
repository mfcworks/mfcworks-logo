import numpy as np

COLOR_BASE = "#243447"
COLOR_RAY = "#6B7C86"

def vector(len, arg) -> np.ndarray:
    return np.array([len * np.cos(np.radians(arg)), len * np.sin(np.radians(arg))])

# パス生成
def create_path() -> list[np.ndarray]:
    r = 100 # 外接円の半径
    t = 20  # ラインの幅
    th = t / np.sin(np.radians(60)) # ラインの幅(傾き60度)に対して水平方向の長さ

    # 原点
    points = [np.array([0, 0])]

    # p1～p16の座標
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

    # p17～p32の座標（p1～p16を原点に対して反転したものを結合）
    reflected = list(map(lambda p: -p, points[1:]))
    points = points + reflected

    # 始点（p1）へ戻る
    points.append(points[1])

    return points

# 座標変換（左上を原点にする）
def convert(points):
    return list(map(lambda p: np.array([100 + p[0], 100 - p[1]]), points))

# 数値丸め
def round(points):
    return np.round(points, decimals=4)

# SVG作成
def create_svg_str(points):
    # open <svg>
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">'

    # <defs>
    svg += f"""
  <defs>
    <linearGradient id="linearGradient" gradientTransform="rotate(30 0.5 0.5)">
      <stop offset="42%" stop-color="{COLOR_BASE}"/>
      <stop offset="62%" stop-color="{COLOR_RAY}"/>
      <stop offset="72%" stop-color="{COLOR_BASE}"/>
    </linearGradient>
  </defs>
"""

    # open <path>
    svg += '  <path fill="url(#linearGradient)" d="\n'

    # path points
    svg += f'    M {points[1][0]} {points[1][1]}\n'
    for p in points[2:]:
        svg += f'    L {p[0]} {p[1]}\n'

    # close <path>
    svg += '    Z"/>\n'

    # close <svg>
    svg += '</svg>'

    return svg


def main():
    path_points = round(convert(create_path()))
    svg_str = create_svg_str(path_points)

    with open('logo.svg', 'w') as file:
        file.write(svg_str)


if __name__ == "__main__":
    main()
