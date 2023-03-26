#!/usr/bin/env python

import sys
import json
import datetime as dt

file_path = '/home/lite/Documents/TaskManagement/'
arg_size = len(sys.argv)

if arg_size == 1:
    print('Falta de argumentos!')
    exit()

with open('{}data.json'.format(file_path)) as file:
    data = json.load(file)
    file.close()

dic_size = len(data)

def save_data ():
    global data

    with open('{}data.json'.format(file_path), 'w') as file:
        json.dump(data, file)
        file.close()
    
    with open('{}data.json.backup'.format(file_path), 'w') as file:
        json.dump(data, file)
        file.close()
    
    with open('{}data.json'.format(file_path)) as file:
        data = json.load(file)
        file.close()

    return data

def list_all ():
    print('ID\t {:{}} QUANTIDADE\n{}'.format('SIGLA', 10, '-' * 30))

    i = 0
    for key in data:
        print('{:02d}\t {:{}} [{}]'.format(i+1, key, 10, len(data[key])))
        i += 1

def list_task (key):
    print('Atividades em {}:\nID\t {:{}}{:{}} \tDATA\n{}'.format(key, '', 25, 'NOME', 25, '-' * 70))
    
    i = 0
    for k in data[key]:
        d = dt.datetime.strptime(data[key][k], '%Y-%m-%d').date()

        if d.year == 1:
            print('{:02d}\t {:{}} \tN/A'.format(i+1, k, 50))
        else:
            print('{:02d}\t {:{}} \t{:02d}/{:02d}'.format(i+1, k, 50, d.day, d.month))
        
        i +=  1

def task_index (mode):
    try:
        index = int(sys.argv[2])
        key = list(data.keys())[index-1]
    except:
        key = sys.argv[2].upper()

    if mode == 0:
        list_task(key)
    elif mode == 1:
        task_add(key)
    elif mode == -1:
        task_remove(key)

def task_select (add):
    list_all()

    key = input('\nSelecione uma tarefa: ')

    try:
        key = list(data.keys())[int(key)-1].upper()
    except:
        key = key.upper()

    if (add):
        task_add(key)
    else:
        task_remove(key)

def task_add (key):
    global data
    print('Inserir tarefa em %s' %(key))

    name = input('Nome da tarefa: ')
    
    if name == '':
        print('A tarefa deve ter um nome!')
        exit()

    date = input('Data [dia/mes]: ')

    if date == '':
        date = '0001-01-01'
    else:
        try:
            date = date.split('/')
            date = str(dt.date(dt.datetime.now().year, int(date[1]), int(date[0]))) 
        except:
            print('A data informada está errada!')
            exit()
        
    data[key][name] = date
    save_data()

def task_remove (key):
    list_task(key)
    id = int(input('\nSelecione o indice da tarefa para remover: '))

    k = list(data[key].keys())[id-1]
    del data[key][k]
    save_data()

    print('Tarefa "%s" removida com sucesso!' %(k))

def task_ordenate ():
    if arg_size == 2:
        date_sort(-1)
    else:
        try:
            count_task = int(sys.argv[2])
            date_sort(count_task)
        except:
            print('Informe a quantidade inteira máxima de tarefas para mostrar.')
            exit()

def date_sort (count):
    data_aux = {}
    for key in data:
        for k in data[key]:
            data_aux[k] =  data[key][k]

    data_aux = sorted(data_aux.items(), key=lambda x:x[1], reverse=True)

    for i in data_aux:
        print('{:{}}{}'.format(i[0], 40, i[1]))

def show_help ():
    print('Task Management - Organizador de Tarefas')
    print('-' * 50)
    print('Adicione o programa com um alias em um dos arquivos shell carregados ao iniciar o computador:')
    print('\talias tm="/caminho/do/arquivo/./main.py"')
    print('Mude a propriedade do arquivo para executável:')
    print('\tchmode +x /caminho/do/arquivo/main.py')
    print('Execute o programa em qualquer lugar do terminal:')
    print('\ttm [COMANDO] [ARGUMENTOS]')
    print('Opções de COMANDOS são:')
    print('\t{:{}}\tListar tarefas'.format('-l [ID/SIGLA]', 15))
    print('\t{:{}}\tAdicionar tarefa'.format('-a [ID/SIGLA]', 15))
    print('\t{:{}}\tRemover tarefa'.format('-r [ID/SIGLA]', 15))

if __name__ == '__main__':
    if sys.argv[1] == '-l':
        if arg_size == 2:
            list_all()
        elif arg_size == 3:
            task_index(0)
    elif sys.argv[1] == '-a':
        if arg_size == 2:
            task_select(True)
        elif arg_size == 3:
            task_index(1)
        elif arg_size == 5:
            print('passa amanhã')
    elif sys.argv[1] == '-r':
        if arg_size == 2:
            task_select(False)
        elif arg_size == 3:
            task_index(-1)
    elif sys.argv[1] == '-o':
        task_ordenate()
    elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
        show_help()
