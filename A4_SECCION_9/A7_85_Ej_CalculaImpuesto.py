


def calculaImpuesto(monto, imp):
    impuesto = monto * (imp/100)
    total = monto + impuesto

    print(f'''
        valor neto:             {monto}
        tasa impositiva: {imp}%
        valor impuesto:         {impuesto}
        -------------------------------------------
        total a pagar:          {total}  
    ''')


monto = float(input('Proporcione el pago sin impuesto: '))
imp = float(input('Proportcione el porcentaje del impuesto: ')) 

calculaImpuesto(monto, imp)

