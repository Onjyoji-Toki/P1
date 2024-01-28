import matplotlib.pyplot as plt
import numpy as np

with open(r'C:\Users\kyoto\WaveDump\down01201148\01201148down0.txt') as f:
    lines = f.readlines()
    num = len(lines)/1023
    print(num) #number of waves

test = np.array([int(line) for line in lines[:1023]])
plt.plot(test - test[0:500].mean()) #numpy arrayを使うと配列の各要素に加減乗除ができる
subtracted = test - test[0:500].mean()
subtracted[500:600].sum()
plt.xlim([500, 570])
plt.show()

N_points = 1023
data = np.array([int(line) for line in lines]) #lineを取り出してきて整数にしてnumpyのarrayに入れる
length = len(data)//N_points #1023で割って波形の個数を数える//は整数割り算の商の意味
data_res = data[:length * N_points].reshape(-1,N_points) #全データを取ってきて二次元配列にする

def intg(d):
    return (d[510:525] - d[:500].mean()).sum() #intg関数の定義 平均を差し引いて離散和をとる

plt.hist([-intg(d) for d in data_res], bins=3000) #intgを実行
plt.xlim([0, 3000])
plt.xlabel('ADC channel')
plt.ylabel('ADC counts')
plt.show()