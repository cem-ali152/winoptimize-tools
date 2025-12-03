import subprocess
import term
import os
from pathlib import Path
import shutil
class app(term.Term):

    def __init__(self):
        super().__init__()
        self.term = term.Term()
        input("Changes made before staring may damage your computer\nIf you are aware of this, press ENTER")
        

    def remove_edge(self):
        self.term.task_info("edge is being erased")
        subprocess.run(["taskkill", "/F", "/IM", "msedge.exe"])
        base_path = Path("C:/Program Files (x86)/Microsoft/Edge/Application")

        installer_dirs = [
            folder
            for folder in base_path.rglob("Installer")
            if folder.is_dir()
        ]
        print(len(installer_dirs),"edge found ")
        for folder in installer_dirs:
            self.term.task_info(f"{folder} deleted")
            setup_exe = folder / "setup.exe"  # Path objesi
            result = subprocess.run(
                [str(setup_exe), "--uninstall", "--system-level", "--verbose-logging","--force-uninstall"],
                capture_output=True,  # stdout ve stderr yakalar
                text=True             # çıktıyı string olarak al
            )





    def disable_service(self,service_list):
        self.term.task_info("Services are closing")
        print("Number of services to be closed: ",len(service_list))
        for service_name in service_list:
            self.term.task_info(f"{service_name} is closing")
            result=subprocess.run(
                    ["sc", "stop", str(service_name)],
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="ignore"
                )
            if result.returncode==1062:
                self.term.warning(f"{service_name} already closed")
            else:
                self.term.işlem_başarılı()


    def install_app(self,app_list,method):
        self.term.task_info("Programs are downloading")
        self.term.task_info(f"Number of programs to be installed: {len(app_list)}")
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
                    self.term.warning("the program is already installed")
                elif result.returncode==0:
                    self.term.işlem_başarılı()
                else:
                    self.term.error("unknown error")
        else:
            self.term.error(f"{method} is not supported")
                


    def dns_change(self,adapter_name,dns1):
        self.term.task_info("DNS is being changed")

        dns1_result=subprocess.run(f'netsh interface ip set dns name="{adapter_name}" static {dns1}', shell=True,capture_output=True)

        if dns1_result.returncode ==0:
            self.term.işlem_başarılı()


    def remove_app(self,app_list):
        self.term.task_info(" Unnecessary programs are being deleted.")
        self.term.task_info(f"number of programs to be deleted: {len(app_list)}")
        #Get-AppxPackage -AllUsers *Microsoft.MicrosoftEdge* | Remove-AppxPackage
        for app_name in app_list:
            self.term.task_info(f"{app_name} is being deleted")
            result=subprocess.run(
                ["powershell","-Command",f"Get-AppxPackage -AllUsers *{app_name}* | Remove-AppxPackage"],
                text=True,
                capture_output=True,
                encoding="utf-8",
                errors="ignore",
            )
            self.term.işlem_başarılı()



    def activate_win_10(self,edition,kms_server):
        dosya_yeri=r"C:\Windows\System32\slmgr.vbs"
        self.term.task_info("Windows is being activated")
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
            self.term.warning("Unable to connect to the KMS server")
        else:
            self.term.işlem_başarılı()



    def tempory_files_remove(self):
        self.term.task_info("The temporary file is being deleted.")
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
                            self.term.error(f"{file_path} could not be deleted:")
                    print(f"{path} The content has been cleared.")
                except PermissionError:
                    self.term.error(f"{path} could not be deleted, permission error.")
            else:
                self.term.error(f"{path} could not be found.")

    def screen_resolution(self, x, y):
            self.term.task_info("screen resolution is being changed")
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
                
                self.term.işlem_başarılı()

            except FileNotFoundError:
                self.term.error(f"The QRes.exe program could not be found at this path: {qres_path}")
            except subprocess.CalledProcessError as e:
                self.term.error(f"An error occurred while running QRes.exe (Return Code: {e.returncode})")
            except Exception as e:
                self.term.error(f"An unexpected error occurred: {e}")


    def dep_of(self):
        self.term.task_info("DEP is shutting down")
        result=subprocess.run(
            ["bcdedit.exe", "/set", "{current}", "nx", "AlwaysOff"],
            text=True,
            capture_output=True,
            encoding="utf-8",
            errors="ignore",
        )
        if  result.returncode==0:
            self.term.işlem_başarılı()
        else:
            self.term.error("An unknown error occurred")

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

            self.term.task_info(f"{added} Record added.")
            if added == 0:
                self.term.warning("All records are already available.")
            return True

        except Exception as e:
            self.term.error(f"{e}")
            return False
    def sistem_zamanlayıcısı(self,task_list):
        self.term.task_info("Unnecessary or telemetry system timers are being turned off.")
        for task_name in task_list:
            result=subprocess.run(
            ["powershell","-Command",f"Get-ScheduledTask -TaskPath '{task_name}' | Disable-ScheduledTask -ErrorAction SilentlyContinue"],
            text=True,
            capture_output=True,
            encoding="utf-8",
            errors="ignore",
            )
            if result.returncode==1:
                self.term.error("The transaction could not be completed.")
            else:
                self.term.işlem_başarılı()


    def dont_track_me_microsoft(self):
        self.term.task_info("Telemetry is being turned off")
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
        self.term.task_info("Telemetry partially closed")
        


    
