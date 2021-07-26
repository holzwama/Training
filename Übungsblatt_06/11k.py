

def packer(chars):
    if chars.isalpha():        # Defines if unpacked
        groups= []
        last_char = None

        for c in chars:
            if c == last_char:
                groups[-1].append(c)
            else:
                groups.append([c])
            last_char = c

        return ''.join('%s%s' % (g[0], len(g)>1 and len(g) or '') for g in groups)

    else:                   # Seems to be packed

        stack = ""

        for i in range(len(chars)):
            if chars[i].isalpha():
                if i+1 < len(chars) and chars[i+1].isdigit():
                    digit = chars[i+1]
                    char = chars[i]
                    i += 2

                    while i < len(chars) and chars[i].isdigit():
                        digit +=chars[i]
                        i+=1
                    stack += char * int(digit)

                else:
                    stack+= chars[i]
            else:
                ""
        return "".join(stack) 
print (packer("aabbbcc"))
