def main():
        n1=1
        qp=0
        print("Descubra o quanto de proteina você come por dia:")
        while n1!=0:
                n1=int(input("Qual alimento vc consumiu hj? \1 - OVO COZIDO \2 - FRANGO \3 - BATATA DOCE \nDigite 0 para terminar o prato: "))
                if n1==1:
                        q=int(input("Quantos: "))
                        po= q*6
                        qp+= po
                if n1==2 or n1==3:
                        q=int(input("Quantidade em gramas: "))
                        if n1==2:
                                pf=q/100*20
                                qp+= pf
                        else:
                                pb=q/100*2.5
                                qp+= pb
        print("Você ingeriu",qp,"g de proteina nessa refeição")
