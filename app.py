import streamlit as st

#--------Kuttaka Solver-------
def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


def kuttakaSolve(a, c, b):
    A, B, C = abs(a), abs(b), abs(c)
    _gcd = gcd(A, gcd(B, C))
    A, B, C = A / _gcd, B / _gcd, C / _gcd
    quot = []
    rem = 0
    d, s = A, B
    while rem != 1:
        rem = d % s
        quot.append(d // s)
        d, s = s, d % s
    x, y = 0, C
    for i in range(0, len(quot)):
        x, y = y, quot[-(i + 1)] * y + x
    if len(quot) % 2 != 0:
        x, y = B - x, A - y
    # resolving c
    if c < 0:
        x, y = B - x, A - y
    # resolving a
    if a < 0:
        x, y = -x, y
    # resolving b
    if b < 0:
        x, y = x, -y
    q = min(x // B, y // A)
    x, y = x - q * b, y - q * a
    return (x, y)


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/

# Webpage Tab Config
st.set_page_config(page_title="Kuttaka Method", page_icon=":deciduous_tree:", layout="wide")


#---Header Section-----
st.subheader("Magical Aryabhatiyam")
st.title("Solutions for Linear Diophantine Equations using Kuttaka Method")
st.write("Credits : Aryabhata, IKS Tree, Lokaveer")
st.write("[More about Kuttaka from Wiki >](https://en.wikipedia.org/wiki/Ku%E1%B9%AD%E1%B9%ADaka)")

#----Variable Input-----
st.subheader("ax + c = by")
a = st.number_input('Enter a : ', value = 60)
st.write('a is ', a)
c = st.number_input('Enter c : ', value = 3)
st.write('c is ', c)
b = st.number_input('Enter b : ', value = 13)
st.write('b is ', b)
st.subheader("The Equation is : %dx + %d = %dy" % (a, c, b))
#----Solution Output---------

if ((a==0) and (b==0) and (c==0)) :
    st.subheader("Infinitely many solutions are possible for (x) & (y)")
elif ((abs(c) % gcd(abs(a), abs(b)) != 0)) :
    st.subheader("No possible solutions for (x) & (y), as gcd(%d) of a(%d) and b(%d) doesn't divide c(%d)" % (gcd(a, b), a, b, c))
elif ((a==b) and (a==c)) :
    st.subheader("(%d * 0) + %d = (%d * 1) = %d" % (a, c, b, b))
    st.subheader("Solution is (x = 0) & (y = 1)")
else:
    soln = kuttakaSolve(a, c, b)
    st.subheader("(%d * %d) + %d = (%d * %d) = %d" % (a, soln[0], c, b, soln[1], b * soln[1]))
    st.subheader("Solution is (x = %d) & (y = %d)" % (soln[0], soln[1]))
