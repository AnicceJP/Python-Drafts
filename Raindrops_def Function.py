# A function to detect the raindrops rhythm

def convert(x):
    y = ''
    if x % 3 == 0:
        y += 'Pling'
    if x % 5 == 0:
        y += 'Plang'
    if x % 7 == 0:
        y += 'Plong'
    if y == '':
        return str(x)
    return y