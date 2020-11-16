# A formula for the windchill index

def main():
    T = -20
    V = 5
    while T <= 60 and V <= 50:
        wi = 35.74 + 0.6215*T - 35.75 * (V**0.16) + 0.4275 * T * (V**0.16)
        print(T)
        print(V)        
        print(wi)
        T = T + 10
        V = V + 5

main()
