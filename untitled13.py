import math

# ==============================================================================
# Array41. Yig'indisi eng katta bo'ladigan 2 ta qo'shni elementni topish.
# ==============================================================================
def array41(arr):
    if len(arr) < 2:
        return None
    
    max_sum = arr[0] + arr[1]
    elem1, elem2 = arr[0], arr[1]
    
    for i in range(1, len(arr) - 1):
        current_sum = arr[i] + arr[i+1]
        if current_sum > max_sum:
            max_sum = current_sum
            elem1, elem2 = arr[i], arr[i+1]
            
    return elem1, elem2


# ==============================================================================
# Array42. Yig'indisi berilgan R soniga eng yaqin bo'lgan 2 ta qo'shni element.
# ==============================================================================
def array42(arr, R):
    if len(arr) < 2:
        return None
    
    # Dastlabki yaqinlik (farqning absolyut qiymati)
    min_diff = abs((arr[0] + arr[1]) - R)
    elem1, elem2 = arr[0], arr[1]
    
    for i in range(1, len(arr) - 1):
        current_sum = arr[i] + arr[i+1]
        current_diff = abs(current_sum - R)
        if current_diff < min_diff:
            min_diff = current_diff
            elem1, elem2 = arr[i], arr[i+1]
            
    return elem1, elem2


# ==============================================================================
# Array43. Tartiblangan massivdagi har xil (unikal) elementlar sonini topish.
# ==============================================================================
def array43(arr):
    if not arr:
        return 0
    
    # Massiv allaqachon tartiblangan bo'lgani uchun, 
    # qo'shni elementlar bir xil bo'lmasa, demak yangi unikal element keldi.
    unique_count = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            unique_count += 1
            
    return unique_count


# ==============================================================================
# Array44. Massivda aniq 2 ta bir xil qiymatli element bor. Ularning indeksini topish.
# Dasturlashda indekslash odatda 0 dan boshlanadi.
# ==============================================================================
def array44(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return i, j  # 0 dan boshlanuvchi indekslar
    return None


# ==============================================================================
# Array45. Bir-biriga eng yaqin qo'shnilar indeksini topish (ayirmasining moduli eng kichik).
# ==============================================================================
def array45(arr):
    if len(arr) < 2:
        return None
    
    min_diff = abs(arr[0] - arr[1])
    idx1, idx2 = 0, 1
    
    for i in range(1, len(arr) - 1):
        current_diff = abs(arr[i] - arr[i+1])
        if current_diff < min_diff:
            min_diff = current_diff
            idx1, idx2 = i, i + 1
            
    return idx1, idx2


# ==============================================================================
# MASHQLARNI TEKSHIRIB KO'RISH (NAMUNA)
# ==============================================================================
if __name__ == "__main__":
    print("--- Masalalar Natijalari ---\n")
    
    # Array41 Test
    test_arr1 = [3, 8, 2, 5, 9, 4]
    print(f"Array41: Massiv {test_arr1} ichida yig'indisi eng katta qo'shnilar: {array41(test_arr1)}")
    
    # Array42 Test
    test_arr2 = [1, 5, 8, 3, 12, 4]
    R_soni = 10
    print(f"Array42: Massiv {test_arr2} ichida yig'indisi R={R_soni} ga eng yaqin qo'shnilar: {array42(test_arr2, R_soni)}")
    
    # Array43 Test (Massiv o'sish yoki kamayish tartibida bo'lishi kerak)
    test_arr3 = [1, 1, 2, 3, 3, 3, 4, 5, 5]
    print(f"Array43: Tartiblangan massiv {test_arr3} dagi har xil elementlar soni: {array43(test_arr3)}")
    
    # Array44 Test (Faqatgina 2 ta element bir xil)
    test_arr4 = [10, 25, 40, 25, 18, 9]
    print(f"Array44: Massiv {test_arr4} dagi bir xil elementlar indekslari: {array44(test_arr4)}")
    
    # Array45 Test
    test_arr5 = [12, 30, 33, 15, 22, 26]
    print(f"Array45: Massiv {test_arr5} dagi bir-biriga eng yaqin qo'shnilar indekslari: {array45(test_arr5)}")