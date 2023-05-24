import readline

from prompt_toolkit import prompt

from cli.commands import *

command = ""
cmd_history = []
out_history = []
session_vars = dict()

def _store(data=None):
    if data == None:
        return
    global out_history
    session_vars.append(data)

def process_command():
    global command
    cmd_history.append(command)
    cmd_list = command.split()
    cmd = cmd_list[0]
    
    match cmd:
        
        case 'exit':
            exit_cli()
        
        case 'quit':
            exit_cli()
        
        case 'color':
            if len(cmd_list) == 1:
                _store(color(prompt("What color would you like to preview? : ")))
                return
            _store(color(cmd_list[1:]))
        
        case 'search':
            _store(search())
        
        case 'list':
            _store(_list())

        case 'sample':
            if len(cmd_list) == 1:
                _store(sample(prompt("What table would you like a sample record from? : ")))
                return
            _store(sample(cmd_list[1]))

        case 'store':
            pass

        case 'vars':
            print_json(data=session_vars)

        case 'history':
            if len(cmd_list) == 1:
                print_history(prompt("What history would you like to see? ([i]n/[o]ut) : "))
            else:
                print_history(cmd_list[1])

            

        case _:
            not_recognized(cmd)

def print_history(option):
    if option.lower() in ['i', 'in']:
        print_json(data=cmd_history)
    elif option.lower() in ['o', 'out']:
        print_json(data=out_history)
    else:
        print(f"{option} is an unsupported option.")
    return

def main():
    authenticate('config.json')
    global command
    command = prompt(">> ")
    process_command()
    main()


if __name__ == "__main__":
    main()