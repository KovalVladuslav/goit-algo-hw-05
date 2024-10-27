import timeit

def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m > n:
        return -1
    
    # Створюємо таблицю зсувів
    shift_table = {}
    for i in range(m):
        shift_table[pattern[i]] = i
    
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            return i
        else:
            shift = shift_table.get(text[i + m - 1], -1)
            i += max(1, j - shift)
    
    return -1

def kmp_search(text, pattern):
    m, n = len(pattern), len(text)
    lps = [0] * m
    compute_lps_array(pattern, m, lps)
    
    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1

def compute_lps_array(pattern, m, lps):
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

def rabin_karp(text, pattern, q=101):
    m = len(pattern)
    n = len(text)
    d = 256
    h = 1
    p = 0
    t = 0
    
    # Обчислення h
    for i in range(m - 1):
        h = (h * d) % q

    # Початкове обчислення хешу для шаблону і тексту
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q

    return -1

# Зчитуємо статті
with open('article-1.txt', 'r', encoding='utf-8') as f:
    text1 = f.read()

with open('article-2.txt', 'r', encoding='utf-8') as f:
    text2 = f.read()

# Існуючий та вигаданий підрядки
existing_substring = "алгоритм"
non_existing_substring = "вигаданийпідрядок"

# Функція для заміру часу виконання
def measure_time(text, pattern, algorithm):
    return timeit.timeit(lambda: algorithm(text, pattern), number=10)

# Порівняння алгоритмів на двох статтях
algorithms = [("Boyer-Moore", boyer_moore), ("KMP", kmp_search), ("Rabin-Karp", rabin_karp)]

results = []

for name, algorithm in algorithms:
    for text, label in [(text1, "Стаття 1"), (text2, "Стаття 2")]:
        existing_time = measure_time(text, existing_substring, algorithm)
        non_existing_time = measure_time(text, non_existing_substring, algorithm)
        results.append((name, label, existing_time, non_existing_time))

# Виведення результатів
for name, label, existing_time, non_existing_time in results:
    print(f"{name} на {label}:")
    print(f"  Існуючий підрядок: {existing_time:.4f} секунд")
    print(f"  Вигаданий підрядок: {non_existing_time:.4f} секунд")
    print()
