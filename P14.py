def sort_list(input_list):
    ascending_sorted_list = sorted(input_list)
    descending_sorted_list = sorted(input_list, reverse=True)
    
    
    print("Original List:", input_list)
    print("Ascending Order:", ascending_sorted_list)
    print("Descending Order:", descending_sorted_list)

if __name__ == "__main__":
    input_list = [12, 45, 32, 67, 3, 56, 89]
    
    sort_list(input_list)
