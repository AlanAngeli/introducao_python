"1 - Manipular data e hora"
"2 - Realizar conversão de texto para data " \
"3 - Realizar soma e subtração em datas"

"Detalhes:" \
" - Como recuperar a data atual (DATE)" \
" - Como trabalhar com a data, alterando sua formatação" \
" - Como gerar m horário (TIME)" \
" - Retornar data e hora atual (DATETIME)" \
" - Alterar formatação do DATETIME" \
" - Realizar soma e subtração de datas com TIMEDELTA"

from datetime import date, time

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual) #anom mês e dia com hífen
    print(data_atual.strftime('%d/%m/%y')) #dia, mês e ano com barra
    print(data_atual.strftime('%d %m %y')) #dia, mês e ano com espaço
    print(data_atual.strftime('%A %B %Y'))
    print()
    print(type(data_atual))
    data_atual_string = data_atual.strftime(('%d/%m/%y')) #convertendo para str
    print(type(data_atual_string))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S'))
