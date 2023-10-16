original_list = [1, 2, 3, 4, 5, 6]
positions_to_remove = [0, 4, 5]
modified_list = [original_list[i] for i in range(len(original_list)) if i not in positions_to_remove]

print("Modified list after removing specified positions:", modified_list)
