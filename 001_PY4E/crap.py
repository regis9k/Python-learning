# def solve(s):
#     s=s.strip()
#     s=' '+s
#     x=0
#     for i in s:
#         if i==' ':
#             char=s[x+1:x+2].strip()
#             s=s.replace(char,char.capitalize())
        
#         x=x+1
#     return(s.strip())
# print(solve('oskar dabrowski'))


def solve(s):
    s=s.strip().capitalize()
    x=0
    for i in s:
        if i==' ':
            pos=s[x+1].strip()
            s=s.replace(pos,pos.capitalize())
        
        x=x+1
    return(s.strip())
print(solve('oskdar dabrowski sdbibiwbdi   asdbwid'))