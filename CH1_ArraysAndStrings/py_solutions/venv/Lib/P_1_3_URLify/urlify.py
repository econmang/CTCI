import sys

_const_website = "https://www.fakedomain.com/"
def urlify(url_str: str)-> str:
    url_str = url_str.strip()
    url = _const_website + url_str.replace(" ","%20")
    return(url)

if __name__ == "__main__":
    try:    
        file_name = sys.argv[1]
        file = open(file_name)
    except:
        print("File not supplied")
    for line in file:
        line = line.replace("\n","")
        line_arr = line.split(",")
        print(urlify(line_arr[0]))
