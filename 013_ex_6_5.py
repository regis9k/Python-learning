text = "X-DSPAM-Confidence:    0.8475"
pos=text.find(' ')
txt1=text[pos: ]
txt2=txt1.strip()
print(float(txt2))