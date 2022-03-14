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

from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('Data: %d/%m/%Y Hora: %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.year)
    print(data_atual.day)
    print(data_atual.month)
    print()
    #traduzir para o português:
    print("TRADUZIR PARA PORTUGUÊS")
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    print()

    #Converter data:
    print("CONVERTER DATA")
    data_criada = datetime(2018, 6, 20, 15, 30, 20) #Ano, mês, dia, hora, minutos, segundos
    print(data_criada)
    print(data_criada.strftime('%c'))
    #data_string = '01/01/2019'
    #data_convertida = datetime.strptime(data_string, '%d/%m/%Y')#só a data
    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y  %H:%M:%S')  #data e hora
    print(data_convertida)
    print()

    ##Subtração:
    print("SUBTRAINDO DATAS")
    nova_data = data_convertida - timedelta(days=365, hours=2) #tirou 365 dias e duas horas
    print(nova_data)


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
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()
