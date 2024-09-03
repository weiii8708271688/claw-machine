import random

def simulate_scratchcard(m, n, x, p):
    # 隨機選擇n個大獎號碼
    prize_numbers = set(random.sample(range(1, m+1), n))
    threadhold = n/m*100
    #print('中獎機率為: ', threadhold, '%')
    # 初始化變量
    scratched = set()
    cost = 0
    prize = 0
    temp_m = m
    # 持續刮開直到找到任一大獎
    while True:
        # 刮開一個新號碼
        new_scratch = random.randint(1, m)
        if new_scratch not in scratched:
            scratched.add(new_scratch)
            cost += p
            temp_m-=1
            if new_scratch in prize_numbers:
                prize += x  # 找到大獎
                n-=1
                if temp_m == 0  or n==0:
                    break

                new_threadhold = n/temp_m*100
                
                #print('新中獎機率為: ', new_threadhold, '%')
                if new_threadhold < threadhold:
                    #print('跳出')
                    break
    
    # 計算收益
    profit = cost - prize
    return profit, len(scratched)

def run_simulations(m, n, x, p, num_simulations=100):
    total_profit = 0
    total_scratches = 0
    for _ in range(num_simulations):
        profit, scratches = simulate_scratchcard(m, n, x, p)
        total_profit += profit
        total_scratches += scratches

    average_profit = total_profit / num_simulations
    average_scratches = total_scratches / num_simulations
    print(f"{num_simulations}次模擬的平均收益: {average_profit:.2f}")
    return average_profit, average_scratches

# 設置參數
m = 200  # 每版刮刮樂的號碼數量
n = 2   # 大獎號碼的數量
x = 5000 # 大獎的價值
p = 100   # 每次刮開的價格

# 打印參數
print("模擬參數:")
print(f"總號碼數量 (m): {m}")
print(f"大獎數量 (n): {n}")
print(f"大獎價值 (x): ${x}")
print(f"每次刮開價格 (p): ${p}")
print("------------------------")

# 運行100次模擬並計算平均收益和獲獎率
average_profit, win_rate = run_simulations(m, n, x, p)
