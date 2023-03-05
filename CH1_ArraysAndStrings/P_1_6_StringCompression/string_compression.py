def compress_str(str_to_compress):
    edit_str = list(str_to_compress)
    build_str = ""

    while len(edit_str) > 0:
        check_char = edit_str[0]
        check_char_count = 1
        build_str += check_char
        edit_str.pop(0)

        while (len(edit_str) > 0 and edit_str[0] == check_char):
            edit_str.pop(0)
            check_char_count += 1

        build_str += str(check_char_count)

    if len(str_to_compress) == len(build_str):
        return str_to_compress
    else:
        return build_str

if __name__ == "__main__":
    test_strs = ["aabcccccaaa", "aabbccdd"]
    for word in test_strs:
        print(word)
        print(compress_str(word))
