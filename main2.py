import random

def simulate_scratchcard(m, n1, n2, x1, x2, p):
    # 隨機選擇n1個大獎號碼和n2個小獎號碼
    big_prize_numbers = set(random.sample(range(1, m+1), n1))
    small_prize_numbers = set(random.sample([i for i in range(1, m+1) if i not in big_prize_numbers], n2))
    
    # 初始化變量
    scratched = set()
    cost = 0
    prize = 0
    big_prizes_found = 0
    
    # 持續刮開直到所有大獎都被找到
    while big_prizes_found < n1:
        # 刮開一個新號碼
        new_scratch = random.randint(1, m)
        if new_scratch not in scratched:
            scratched.add(new_scratch)
            cost += p
            
            if new_scratch in big_prize_numbers:
                prize += x1
                big_prizes_found += 1
            elif new_scratch in small_prize_numbers:
                prize += x2
    
    # 計算收益
    profit = cost - prize
    return profit, len(scratched)

def run_simulations(m, n1, n2, x1, x2, p, num_simulations=10000):
    total_profit = 0
    total_scratches = 0
    for _ in range(num_simulations):
        profit, scratches = simulate_scratchcard(m, n1, n2, x1, x2, p)
        total_profit += profit
        total_scratches += scratches
    average_profit = total_profit / num_simulations
    average_scratches = total_scratches / num_simulations
    print(f"{num_simulations}次模擬的平均收益: {average_profit:.2f}")
    return average_profit, average_scratches

# 設置參數
m = 120  # 每版刮刮樂的號碼數量
n1 = 1   # 大獎號碼的數量
n2 = 1  # 小獎號碼的數量
x1 = 3200 # 大獎的價值
x2 = 900  # 小獎的價值
p = 120   # 每次刮開的價格

print("模擬參數:")
print(f"總號碼數量 (m): {m}")
print(f"大獎數量 (n1): {n1}")
print(f"小獎數量 (n2): {n2}")
print(f"大獎價值 (x1): ${x1}")
print(f"小獎價值 (x2): ${x2}")
print(f"每次刮開價格 (p): ${p}")
print("------------------------")

# 運行100次模擬並計算平均收益
average_profit = run_simulations(m, n1, n2, x1, x2, p)
