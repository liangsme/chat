#讀取檔案 
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person: #如果person有值,才執行下一行
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
	with open(filename, 'w')as f:
		for line in lines:
			f.write(line + '\n')

def main():
    lines = read_file('input.txt') #因為有return,所以可以把他回傳的值存下來,我們將他存成lines
    lines = convert(lines)
    write_file('output.txt', lines)
main()






