"""
LAB 4: LÝ THUYẾT TỔ HỢP & ĐẾM
Gộp toàn bộ 5 bài vào một file. Chạy: python lab4_all.py
"""

import math


# ==================================================================
# BÀI 1
# ==================================================================
def generate_binary_strings(n):
    results = []
    a = [0] * n  # Cấu hình đầu tiên: 000...0

    while True:
        # 1. Lưu cấu hình hiện tại
        results.append("".join(str(bit) for bit in a))

        # 2. Tìm bit 0 đầu tiên từ phải sang trái (các bit 1 đi qua được đặt về 0)
        i = n - 1
        while i >= 0 and a[i] == 1:
            a[i] = 0
            i -= 1

        # 3. Điều kiện dừng: không còn bit 0 nào (đã qua cấu hình 111...1)
        if i < 0:
            break

        # 4. Đổi bit 0 thành 1
        a[i] = 1

    return results


def demo_bai1():
    print("=" * 60)
    print("BÀI 1: Sinh chuỗi nhị phân độ dài n")
    print("=" * 60)
    n = 3
    binary_list = generate_binary_strings(n)
    print(f"Tổng số chuỗi nhị phân sinh được (2^{n} = {2 ** n}): {len(binary_list)}")
    print("Danh sách chuỗi:", binary_list)
    assert binary_list == ['000', '001', '010', '011', '100', '101', '110', '111']
    assert len(generate_binary_strings(5)) == 32


# ==================================================================
# BÀI 2
# ==================================================================
def generate_subsets_backtracking(features):
    all_subsets = []

    def backtrack(start_index, current_path):
        # Lưu tập con hiện tại (bản sao, vì current_path còn bị thay đổi)
        all_subsets.append(list(current_path))

        # Duyệt qua các đặc trưng tiếp theo
        for i in range(start_index, len(features)):
            current_path.append(features[i])   # 1. Chọn đặc trưng
            backtrack(i + 1, current_path)     # 2. Đệ quy
            current_path.pop()                 # 3. Quay lui (Undo)

    backtrack(0, [])
    return all_subsets


def demo_bai2():
    print("\n" + "=" * 60)
    print("BÀI 2: Sinh tập con đặc trưng bằng Quay lui")
    print("=" * 60)
    features = ['Age', 'Income', 'Score']
    subsets = generate_subsets_backtracking(features)
    print(f"Tổng số tập con sinh được (2^{len(features)} = {2 ** len(features)}): {len(subsets)}")
    for s in subsets:
        print(s)
    assert len(subsets) == 8


# ==================================================================
# BÀI 3
# ==================================================================
def generate_permutations(n):
    a = list(range(1, n + 1))   # Cấu hình đầu tiên: [1, 2, ..., n]
    results = []

    while True:
        results.append(list(a))

        # 1. Tìm i lớn nhất sao cho a[i] < a[i+1]
        i = n - 2
        while i >= 0 and a[i] > a[i + 1]:
            i -= 1

        # 2. Không tìm thấy -> cấu hình cuối cùng [n, ..., 2, 1]
        if i < 0:
            break

        # 3. Tìm k lớn nhất sao cho a[k] > a[i]
        k = n - 1
        while a[k] < a[i]:
            k -= 1

        # 4. Đổi chỗ a[i] và a[k]
        a[i], a[k] = a[k], a[i]

        # 5. Lật ngược đoạn a[i+1] .. a[n-1]
        l, r = i + 1, n - 1
        while l < r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1

    return results


def demo_bai3():
    print("\n" + "=" * 60)
    print("BÀI 3: Sinh hoán vị theo thứ tự từ điển")
    print("=" * 60)
    n = 3
    perms = generate_permutations(n)
    print(f"Số hoán vị của n = {n} (3! = 6): {len(perms)}")
    for p in perms:
        print(p)
    assert perms == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert len(generate_permutations(5)) == 120


# ==================================================================
# BÀI 4
# ==================================================================
def solve_n_queens(n, print_boards=True):
    """Trả về tổng số cách xếp hợp lệ; in các bàn cờ tìm được nếu print_boards=True."""
    cols = set()    # các cột đã bị chiếm
    diag1 = set()   # đường chéo chính:  r - c
    diag2 = set()   # đường chéo phụ:    r + c
    placement = [-1] * n   # placement[r] = cột đặt quân hậu ở hàng r
    solutions = []

    def backtrack(row):
        if row == n:
            board = ["." * c + "Q" + "." * (n - c - 1) for c in placement]
            solutions.append(board)
            return
        for c in range(n):
            # Cắt tỉa nhánh: kiểm tra an toàn O(1)
            if c in cols or (row - c) in diag1 or (row + c) in diag2:
                continue
            # Chọn
            cols.add(c); diag1.add(row - c); diag2.add(row + c)
            placement[row] = c
            backtrack(row + 1)
            # Quay lui
            cols.remove(c); diag1.remove(row - c); diag2.remove(row + c)
            placement[row] = -1

    backtrack(0)

    if print_boards:
        for idx, board in enumerate(solutions, 1):
            print(f"Cách {idx}: {board}")
            for line in board:
                print("  " + " ".join(line))
            print()
    return len(solutions)


def demo_bai4():
    print("\n" + "=" * 60)
    print("BÀI 4: N quân hậu bằng Quay lui")
    print("=" * 60)
    total4 = solve_n_queens(4)
    print(f"n = 4: tổng số cách xếp = {total4}")
    total8 = solve_n_queens(8, print_boards=False)
    print(f"n = 8: tổng số cách xếp = {total8}")
    # Lưu ý: bài toán 8 quân hậu kinh điển có 92 nghiệm (đề ghi 924 là nhầm)
    assert total4 == 2
    assert total8 == 92


# ==================================================================
# BÀI 5
# ==================================================================
param_grid = {
    'learning_rate': [0.001, 0.01, 0.1],
    'batch_size': [16, 32, 64],
    'optimizer': ['Adam', 'SGD'],
}


def custom_grid_search(param_grid):
    """Sinh mọi cấu hình bằng Quay lui: mỗi tham số là một 'tầng' của cây đệ quy,
    không dùng vòng for lồng nhau cứng."""
    keys = list(param_grid.keys())
    configs = []

    def backtrack(idx, current):
        if idx == len(keys):                 # đã chọn xong giá trị cho mọi tham số
            configs.append(dict(current))
            return
        key = keys[idx]
        for value in param_grid[key]:
            current[key] = value             # Chọn
            backtrack(idx + 1, current)      # Đệ quy sang tham số kế tiếp
            del current[key]                 # Quay lui

    backtrack(0, {})
    return configs


def count_configurations(param_grid):
    """Nguyên lý Nhân: |Configurations| = tích số lượng giá trị của từng tham số."""
    total = 1
    for values in param_grid.values():
        total *= len(values)
    return total


def dirichlet_min_bucket(num_items, num_buckets):
    """Dirichlet mở rộng: có ít nhất một cụm chứa >= ceil(N / k) cấu hình."""
    return math.ceil(num_items / num_buckets)


def demo_bai5():
    print("\n" + "=" * 60)
    print("BÀI 5: Grid Search, Nguyên lý Nhân & Dirichlet")
    print("=" * 60)

    configs = custom_grid_search(param_grid)
    total = count_configurations(param_grid)
    print(f"Số cấu hình theo Nguyên lý Nhân: "
          f"{' * '.join(str(len(v)) for v in param_grid.values())} = {total}")
    print(f"Số cấu hình sinh bằng Quay lui: {len(configs)}")
    for i, cfg in enumerate(configs, 1):
        print(f"  {i:2d}. {cfg}")
    assert len(configs) == total == 18

    # --- Dirichlet ---
    k = 10
    # Đề ghi "105 mô hình": nhiều khả năng là 10^5 (mất chỉ số mũ khi chuyển PDF)
    for n_models, label in ((10 ** 5, "10^5 = 100000"), (105, "105")):
        m = dirichlet_min_bucket(n_models, k)
        print(f"\nN = {label} mô hình, k = {k} cụm: "
              f"ít nhất 1 cụm chứa >= ceil({n_models}/{k}) = {m} cấu hình")

    # Ý nghĩa trong cân bằng tải hệ thống AI:
    # Dù hàm băm có phân phối đều đến đâu, theo Dirichlet mở rộng luôn tồn tại
    # ít nhất một cụm máy chủ phải gánh >= ceil(N/k) cấu hình, nên KHÔNG thể có
    # tải thấp hơn mức này ở cụm nặng nhất. Đây là cận dưới của "tải tối đa":
    # nếu N chia hết cho k thì phân phối hoàn hảo đạt đúng N/k mỗi cụm; còn nếu
    # không, đụng độ là không tránh khỏi. Vì vậy khi thiết kế hệ thống cần
    # (1) cấp dung lượng/bộ nhớ cho mỗi cụm >= ceil(N/k) cộng dự phòng,
    # (2) chọn hàm băm đủ đều (hoặc consistent hashing) để tải thực tế sát cận
    # này, (3) tăng số cụm k khi N tăng để giữ ceil(N/k) trong ngưỡng chịu tải.


if __name__ == "__main__":
    demo_bai1()
    demo_bai2()
    demo_bai3()
    demo_bai4()
    demo_bai5()
