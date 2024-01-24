def pirata():
    while True:
        Mdj1=float(input("entre Mdj1: "))
        MdjX=float(input("entre MdjX: "))
        Mdj2=float(input("entre Mdj2: "))
        
        Mdj1X=float(input("entre Mdj1X: "))
        MdjX2=float(input("entre MdjX2: "))
        Mdj12=float(input("entre Mdj12: "))
        
        Xbet1=float(input("entre Xbet1: "))
        XbetX=float(input("entre XbetX: "))
        Xbet2=float(input("entre Xbet2: "))
        
        Xbet1X=float(input("entre Xbet1X: "))
        XbetX2=float(input("entre XbetX2: "))
        Xbet12=float(input("entre Xbet12: "))
        
        proba_M1_BX2= (1/Mdj1)+(1/XbetX2)
        proba_MX_B12= (1/MdjX)+(1/Xbet12)
        proba_M2_B1X= (1/Mdj2)+(1/Xbet1X)
        proba_M1X_B2= (1/Mdj1X)+(1/Xbet2)
        proba_MX2_B1= (1/MdjX2)+(1/Xbet1)
        proba_M12_BX= (1/Mdj12)+(1/XbetX)
       
        print("proba_M1_BX2 = ", proba_M1_BX2, '\n'
        "proba_MX_B12 = ", proba_MX_B12, '\n'
        "proba_M2_B1X = ", proba_M2_B1X, '\n'
        "proba_M1X_B2 = ", proba_M1X_B2, '\n'
        "proba_MX2_B1 = ", proba_MX2_B1, '\n'
        "proba_M12_BX = ", proba_M12_BX, '\n' )
    
pirata()
