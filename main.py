import subprocess
import time
import os
from pathlib import Path
import shutil
import sys 
import toml
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



class app:

    def __init__(self,t):
        
        input("Changes made before starting may damage your computer\nIf you are aware of this, press ENTER")


    def remove_edge(self):
        t.task_info("edge is being erased")
        subprocess.run(["taskkill", "/F", "/IM", "msedge.exe"])
        base_path = Path("C:/Program Files (x86)/Microsoft/Edge/Application")

        installer_dirs = [
            folder
            for folder in base_path.rglob("Installer")
            if folder.is_dir()
        ]
        print(len(installer_dirs),"edge found ")
        for folder in installer_dirs:
            t.task_info(f"{folder} deleted")
            setup_exe = folder / "setup.exe"  # Path objesi
            result = subprocess.run(
                [str(setup_exe), "--uninstall", "--system-level", "--verbose-logging","--force-uninstall"],
                capture_output=True,  # stdout ve stderr yakalar
                text=True             # çıktıyı string olarak al
            )





    def disable_service(self,service_list):
        t.task_info("Services are closing")
        print("Number of services to be closed: ",len(service_list))
        for service_name in service_list:
            t.task_info(f"{service_name} is closing")
            result=subprocess.run(
                    ["sc", "stop", str(service_name)],
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="ignore"
                )
            if result.returncode==1062:
                t.warning(f"{service_name} already closed")
            else:
                t.işlem_başarılı()


    def install_app(self,app_list,method):
        t.task_info("Programs are downloading")
        t.task_info(f"Number of programs to be installed: {len(app_list)}")
        if method=="winget":
            for app_ıd in app_list: 
                result=subprocess.run(
                    ["winget","install", "--id",str(app_ıd),"-e","--silent"],
                    text=True,
                    capture_output=True,
                    encoding="utf-8",
                    errors="ignore",
                    input="Y"
                )
                if result.returncode==2316632107:
                    t.warning("the program is already installed")
                elif result.returncode==0:
                    t.işlem_başarılı()
                else:
                    t.error("unknown error")
        else:
            t.error(f"{method} is not supported")
                


    def dns_change(self,adapter_name,dns1):
        t.task_info("DNS is being changed")

        dns1_result=subprocess.run(f'netsh interface ip set dns name="{adapter_name}" static {dns1}', shell=True,capture_output=True)

        if dns1_result.returncode ==0:
            t.işlem_başarılı()


    def remove_app(self,app_list):
        t.task_info(" Unnecessary programs are being deleted.")
        t.task_info(f"number of programs to be deleted: {len(app_list)}")
        #Get-AppxPackage -AllUsers *Microsoft.MicrosoftEdge* | Remove-AppxPackage
        for app_name in app_list:
            t.task_info(f"{app_name} is being deleted")
            result=subprocess.run(
                ["powershell","-Command",f"Get-AppxPackage -AllUsers *{app_name}* | Remove-AppxPackage"],
                text=True,
                capture_output=True,
                encoding="utf-8",
                errors="ignore",
            )
            t.işlem_başarılı()



    def activate_win_10(self,edition,kms_server):
        dosya_yeri=r"C:\Windows\System32\slmgr.vbs"
        t.task_info("Windows is being activated")
        if edition=="Professional":
            key="W269N-WFGWX-YVC9B-4J6C9-T83GX"
        elif edition=="Home":
            key="TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"
        
        subprocess.run(
            ["cscript", dosya_yeri, "/ipk",key],
            text=True,
            capture_output=True,
            encoding="utf-8",
            errors="ignore",

        )
        
        subprocess.run(
            ["cscript", dosya_yeri, "/skms", kms_server],
            text=True,
            capture_output=True,
            encoding="utf-8",
            errors="ignore",

        )
        result3=subprocess.run(
            ["cscript", dosya_yeri, "/ato"],
            text=True,
            capture_output=True,
            encoding="utf-8",
            errors="ignore",

        )
        if result3.returncode==3221549172:
            t.warning("Unable to connect to the KMS server")
        else:
            t.işlem_başarılı()



    def tempory_files_remove(self):
        t.task_info("The temporary file is being deleted.")
        startupp = os.path.join(
            os.path.expandvars(r"%APPDATA%")+  # veya os.environ.get("APPDATA")
            r"Microsoft\Windows\Start Menu\Programs\Startup"
        )
        temp_paths = [
            os.path.expandvars(r"%temp%"),
            r"C:\Windows\Temp",
            startupp
        ]

        for path in temp_paths:
            if os.path.exists(path):
                try:
                    # Klasördeki tüm dosya ve alt klasörleri sil
                    for filename in os.listdir(path):
                        file_path = os.path.join(path, filename)
                        try:
                            if os.path.isfile(file_path) or os.path.islink(file_path):
                                os.remove(file_path)
                            elif os.path.isdir(file_path):
                                shutil.rmtree(file_path)
                        except Exception as e:
                            t.error(f"{file_path} could not be deleted:")
                    print(f"{path} The content has been cleared.")
                except PermissionError:
                    t.error(f"{path} could not be deleted, permission error.")
            else:
                t.error(f"{path} could not be found.")

    def screen_resolution(self, x, y):
            t.task_info("screen resolution is being changed")
            base_dir = os.getcwd()
            qres_path = os.path.join(base_dir,"tools", "QRes.exe")
            

            try:
                result = subprocess.run(
                    [qres_path, f"/X:{x}", f"/Y:{y}"],
                    text=True,
                    capture_output=True,
                    encoding="utf-8",
                    errors="ignore",
                    check=True  # Program hata verirse (returncode != 0) exception atar
                )
                
                t.işlem_başarılı()

            except FileNotFoundError:
                t.error(f"The QRes.exe program could not be found at this path: {qres_path}")
            except subprocess.CalledProcessError as e:
                t.error(f"An error occurred while running QRes.exe (Return Code: {e.returncode})")
            except Exception as e:
                t.error(f"An unexpected error occurred: {e}")


    def dep_of(self):
        t.task_info("DEP is shutting down")
        result=subprocess.run(
            ["bcdedit.exe", "/set", "{current}", "nx", "AlwaysOff"],
            text=True,
            capture_output=True,
            encoding="utf-8",
            errors="ignore",
        )
        if  result.returncode==0:
            t.işlem_başarılı()
        else:
            t.error("An unknown error occurred")

    def add_domains_to_hosts(self,domains):
        hosts_path = r"C:\Windows\System32\drivers\etc\hosts"


        try:
            # Mevcut içerik okunur
            with open(hosts_path, "r", encoding="utf-8") as f:
                content = f.read()

            added = 0
            for domain in domains:
                line_to_add = f"0.0.0.0 {domain}"
                if line_to_add not in content:
                    with open(hosts_path, "a", encoding="utf-8") as f:
                        f.write("\n" + line_to_add)
                    added += 1

            t.task_info(f"{added} Record added.")
            if added == 0:
                t.warning("All records are already available.")
            return True

        except Exception as e:
            t.error(f"{e}")
            return False
    def sistem_zamanlayıcısı(self,task_list):
        t.task_info("Unnecessary or telemetry system timers are being turned off.")
        for task_name in task_list:
            result=subprocess.run(
            ["powershell","-Command",f"Get-ScheduledTask -TaskPath '{task_name}' | Disable-ScheduledTask -ErrorAction SilentlyContinue"],
            text=True,
            capture_output=True,
            encoding="utf-8",
            errors="ignore",
            )
            if result.returncode==1:
                t.error("The transaction could not be completed.")
            else:
                t.işlem_başarılı()


    def dont_track_me_microsoft(self):
        t.task_info("Telemetry is being turned off")
        task_paths = [
        r'\Microsoft\Windows\Application Experience\\',
        r'\Microsoft\Windows\Customer Experience Improvement Program\\',
        r'\Microsoft\Windows\DiskDiagnostic\\',
        r'\Microsoft\Windows\Feedback\\',
        r'\Microsoft\Windows\WDI\\'
        ]
        service=["DiagTrack","dmwappushsc"]
        hosts=["vortex-win.data.microsoft.com","settings-win.data.microsoft.com",
            "waltson.telemetry.microsoft.com","telemetry.microsoft.com","vortex.data.microsoft.com",
            "telecommand.telemetry.microsoft.com"]
        self.sistem_zamanlayıcısı(task_paths)
        self.disable_service(service_list=service)
        self.add_domains_to_hosts(hosts)
        t.task_info("Telemetry partially closed")
        


    

        

class Term:
    def __init__(self, ascii_art, explanation):
        # renkler
        self.default_color = "\033[37m"
        self.red = "\033[31m"
        self.yellow = "\033[33m"
        self.green="\033[32m"
        self.okay_emoji="✅"
        self.ascii = ascii_art
        self.explanation = explanation

    def error(self, error):
        print(self.red + "error : " + error + self.default_color)
    def critic_error(self, error):
        print(self.red + "critic error : " + error + self.default_color)
        sys.exit(0)
    def task_info(self,task_info):
        print(self.yellow,"task:",task_info,self.default_color)
    def warning(self, warning):
        print(self.yellow + "warning: " + warning + self.default_color)
    def işlem_başarılı(self):
        print(self.okay_emoji,self.green," The process was successful. ",self.default_color)

    def cemo(self):
        print(self.red + self.ascii + self.default_color)
        print(self.yellow + self.explanation + self.default_color)

class terminal_ui:
    def __init__(self):
        pass

class arg_config_main:
    def __init__(self,t,config):
        self.config=config
        self.t = t
        self.activate_win10=self.config["general"]["activate_win10"]
        self.screen_resolution=self.config["general"]["screen_resolution"]
        self.dep=self.config["general"]["DEP"]
        self.remove=self.config["general"]["remove"]
        self.dont_track_me=config["general"]["dont_track_me"]
        self.tempory_files_remove=config["general"]["tempory_files_remove"]
        self.disable_unnecessary_services=config["general"]["disable_unnecessary_services"]
        self.install_app=config["general"]["install_app"]
        self.dns=config["general"]["dns"]
        
    def main_task(self):
        app1=app(t=self.t)
        if self.activate_win10:
            try:
                self.win10_edition=self.config["advanced"]["activate_win10"]["win10_edition"]
                self.kms_server=self.config["advanced"]["activate_win10"]["kms_server"]
                app1.activate_win_10(self.win10_edition, self.kms_server)
            except KeyError:
                self.t.error("The config file is broken!")

        if self.screen_resolution:
            try:
                self.x = self.config["advanced"]["screen_resolution"]["change_resolution_x"]
                self.y = self.config["advanced"]["screen_resolution"]["change_resolution_y"]
                app1.screen_resolution(x=self.x,y=self.y)

            except KeyError:
                self.t.error("The config file is broken!")
        if self.dep:
            app1.dep_of()
        if self.remove:
            try:
                self.edge_remove=self.config["advanced"]["remove"]["edge_remove"]
                self.programs_to_be_deleted=self.config["advanced"]["remove"]["programs_to_be_deleted"]
                if self.edge_remove:
                    app1.remove_edge()
                app1.remove_app(app_list=self.programs_to_be_deleted)                
            except KeyError:
                self.t.error("The config file is broken!")
        
        if self.dont_track_me:
            app1.dont_track_me_microsoft()
        if self.tempory_files_remove:
            app1.tempory_files_remove()
        if self.disable_unnecessary_services:
            try:
                self.service_list=self.config["advanced"]["disable_unnecessary_services"]["service_list"]
                app1.disable_service(service_list=self.service_list)
            except KeyError:
                self.t.error("The config file is broken!")
        if self.install_app:
            try:
                self.install_method=self.config["advanced"]["install_app"]["install_method"]
                self.Programs_to_be_installed=self.config["advanced"]["install_app"]["Programs_to_be_installed"]
                app1.install_app(app_list=self.Programs_to_be_installed,method=self.install_method)
            except KeyError:
                self.t.error("The config file is broken!")
        if self.dns:
            try:
                self.adapter_name=config["advanced"]["dns"]["adapter_name"]
                self.dns_change=config["advanced"]["dns"]["dns_change"]
                app1.dns_change(dns1=self.dns_change,adapter_name=self.adapter_name)
            except KeyError:
                self.t.error("The config file is broken!")
            

if __name__=="__main__":

    t=Term(ascii_art=ascıı,explanation="Optimization program for Windows 10")

    if len(sys.argv)==1:
        print("--cf with the optimizer.toml file")

    elif (str(sys.argv[1])=="-config-files" or str(sys.argv[1])=="--cf") and len(sys.argv) > 2:
        t.cemo()
        config_files=str(sys.argv[2])
        try:
            config=toml.load(config_files)
        except FileNotFoundError:
            t.critic_error("File not found!")
        except toml.TomlDecodeError as e:
            t.critic_error({e})

        print(config_files + " applied from the config file") 
        arg_app=arg_config_main(t,config=config)
        arg_app.main_task() 
        input(" The process is complete. Your computer is now more optimized!")
        sys.exit(10)

