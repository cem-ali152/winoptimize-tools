import sys 
import toml
import term
import arg 
ascıı="""
 ▄████▄  ▓█████  ███▄ ▄███▓ ▒█████  
▒██▀ ▀█  ▓█   ▀ ▓██▒▀█▀ ██▒▒██▒  ██▒
▒▓█    ▄ ▒███   ▓██    ▓██░▒██░  ██▒
▒▓▓▄ ▄██▒▒▓█  ▄ ▒██    ▒██ ▒██   ██░
▒ ▓███▀ ░░▒████▒▒██▒   ░██▒░ ████▓▒░
░ ░▒ ▒  ░░░ ▒░ ░░ ▒░   ░  ░░ ▒░▒░▒░ 
  ░  ▒    ░ ░  ░░  ░      ░  ░ ▒ ▒░ 
░           ░   ░      ░   ░ ░ ░ ▒  
"""





        
if __name__=="__main__":

    t=term.Term()
    hello_screen=term.hello_screen(ascii_art=ascıı,explanation="Optimization program for Windows 10")
    
    if len(sys.argv)==1:
        print("--cf with the optimizer.toml file")

    elif (str(sys.argv[1])=="-config-files" or str(sys.argv[1])=="--cf") and len(sys.argv) > 2:
        hello_screen.cemo()
        config_files=str(sys.argv[2])
        try:
            config=toml.load(config_files)
        except FileNotFoundError:
            t.critic_error("File not found!")
        except toml.TomlDecodeError as e:
            t.critic_error({e})

        print(config_files + " applied from the config file") 
        arg_app=arg.arg_config_main(config=config)
        arg_app.main_task() 
        input(" The process is complete. Your computer is now more optimized!")
        sys.exit(10)

