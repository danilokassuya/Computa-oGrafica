import math

op = 1
pontos = []
while(op != "7"):
    print(op)
    op = input("1-Adicionar novo ponto.\n"
            "2-Realizar Translação.\n"
            "3-Realizar Escala.\n"
            "4-Realizar Rotação.\n"
            "5-Realizar Cisalhamento\n"
            "6-Realizar Reflexão\n"
            "7-Sair\n")
    match op:
        case "1":
            print("Digite as coordendas do novo ponto")
            x = int(input("x = "))
            y  = int(input("y = "))
            pontos.append([x,y])
            print(pontos)
        case "2":
            print("Digite os valores de offset")
            x = int(input("Tx = "))
            y = int(input("Ty = "))
            ch = [[1,0,x],[0,1,y],[0,0,1]]
            for ponto in pontos:
                t = [ponto[0],ponto[1],1]
                x = t[0]*ch[0][0]+t[1]*ch[0][1]+t[2]*ch[0][2]
                x = t[1]*ch[1][0]+t[1]*ch[1][1]+t[2]*ch[1][2]
            print(pontos)
        case "3":
            print("Digite os valores de escala")
            x = float(input("Sx = "))
            y = float(input("Sy = "))
            for ponto in pontos:
                ponto[0] = ponto[0] * x
                ponto[1] = ponto[1] * y
            print(pontos)
        case "4":
            x = 0
            y = 0
            mx = pontos[0][0]
            my = pontos[0][1]
            for ponto in pontos:
                if ponto[0] <= mx:
                    mx = ponto[0]
                if ponto[1] <= my:
                    my = ponto[1]
                
            for ponto in pontos:
                ponto[0] = ponto[0] - mx
                ponto[1] = ponto[1] - my
                x = ponto[0] + x
                y = ponto[1] + y
            x = x/len(pontos)
            y = y/len(pontos)
            print("Digite o angulo da rotação")
            ang = float(input("angulo = "))
            for ponto in pontos:
                ponto[0] = (math.cos(ang) * ponto[0]) + (-math.sin(ang) * ponto[0])
                ponto[1] = (math.sin(ang) * ponto[0]) + (math.cos(ang) * ponto[1])
            for ponto in pontos:
                ponto[0] = ponto[0] + mx
                ponto[1] = ponto[1] + my
            print(pontos)
        case "5":
            print("Digite os valores de deformação")
            x = float(input("Sx = "))
            y = float(input("Sy = "))
            for ponto in pontos:
                ponto[0] = ponto[0] + (ponto[0]*x)
                ponto[1] = ponto[1] + (ponto[1]*y)
            print(pontos)
        case "6":
            op2 = input("Selecione o tipo de Reflexão\n"
                        "1-Em relação ao eixo X\n"
                        "2-Em relação ao eixo y\n"
                        "3-Em relação à linha y = x\n"
                        "4-Em relação à linha y = -x\n"
                        )
            match op2:
                case "1":
                    for ponto in pontos:
                        ponto[1] = ponto[1] * -1
                    print(pontos)
                case "2":
                    for ponto in pontos:
                        ponto[0] = ponto[0] * -1
                    print(pontos)
                case "3":
                    for ponto in pontos:
                        temp = ponto[0]
                        ponto[0] = ponto[1]
                        ponto[1] = temp
                    print(pontos)
                case "4":
                    for ponto in pontos:
                        temp = ponto[0]
                        ponto[0] = -ponto[1]
                        ponto[1] = -temp
                    print(pontos)

