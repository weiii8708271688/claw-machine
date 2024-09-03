import random

def simulate_scratchcard(m, n, x, p):
    # 隨機選擇n個中獎號碼
    winning_numbers = random.sample(range(1, m+1), n)
    
    # 初始化變量
    scratched = set()
    cost = 0
    # 持續刮開直到所有中獎號碼都被找到
    
    while len(set(winning_numbers) - scratched) > 0:
        # 刮開一個新號碼
        new_scratch = random.randint(1, m)
        while new_scratch in scratched:
            new_scratch = random.randint(1, m)
            
        scratched.add(new_scratch)
        cost += p

    # 計算收益
    profit = cost - x
    return profit, len(scratched)

def run_simulations(m, n, x, p, num_simulations=10000):
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
m = 120  # 每版刮刮樂的號碼數量
n = 2   # 中獎號碼的數量
x = 4200 # 總獎項價值
p = 70  # 每次刮開的價格

print("模擬參數:")
print(f"總號碼數量 (m): {m}")
print(f"大獎數量 (n): {n}")
print(f"大獎價值 (x): ${x}")
print(f"每次刮開價格 (p): ${p}")
print("------------------------")

# 運行100次模擬並計算平均收益
average_profit = run_simulations(m, n, x, p)