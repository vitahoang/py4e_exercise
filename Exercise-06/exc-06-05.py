text = "X-DSPAM-Confidence:    0.8475"
flo = text.find(".")
print(float(text[(flo-1):]))