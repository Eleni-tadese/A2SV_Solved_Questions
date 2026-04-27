def solve():
   
    n = int(input())
    # x = የሰዎች መቆሚያ ቦታዎች
    x = list(map(int, input().split()))
    # v = የሰዎች ፍጥነት
    v = list(map(int, input().split()))

    # ይህ ተግባር የገመትነው ሰዓት (t) እንደሚያገናኛቸው ያረጋግጣል
    def check(t):
        max_left = -float('inf')  # በጣም ትንሽ ቁጥር
        min_right = float('inf')  # በጣም ትልቅ ቁጥር

        for i in range(n):
            # የአንድ ሰው የጉዞ ክልል (Lower and Upper bound)
            left_i = x[i] - (v[i] * t)
            right_i = x[i] + (v[i] * t)

            # የጋራ መደራረቢያውን መፈለግ
            max_left = max(max_left, left_i)
            min_right = min(min_right, right_i)

        return max_left <= min_right

    # Binary Search
    low = 0.0
    high = 1e9  # 1,000,000,000 ሜትር ከፍተኛው ርቀት ስለሆነ

    # ለ 100 ጊዜ ደጋግመን ስንሰራ በጣም ትክክለኛ መልስ እናገኛለን
    for _ in range(100):
        mid = (low + high) / 2
        if check(mid):
            high = mid  # ሰዓቱ ከበቃን፣ ከዚህ ያነሰ ይቻል እንደሆነ ለማየት high-ን ዝቅ እናደርጋለን
        else:
            low = mid  # ሰዓቱ ካልበቃን፣ ሰዓቱን እንጨምራለን

    print(f"{high:.12f}")

# ፕሮግራሙን ለማስጀመር
solve()
