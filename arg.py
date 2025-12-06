import app
import term



class arg_config_main(term.Term):
    def __init__(self,config):
        super().__init__()
        self.t = term.Term()
        self.config=config
        self.activate_win10=self.config["general"]["activate_win10"]
        self.screen_resolution=self.config["general"]["screen_resolution"]
        self.dep=self.config["general"]["DEP"]
        self.remove=self.config["general"]["remove"]
        self.dont_track_me=self.config["general"]["dont_track_me"]
        self.tempory_files_remove=self.config["general"]["tempory_files_remove"]
        self.disable_unnecessary_services=self.config["general"]["disable_unnecessary_services"]
        self.install_app=self.config["general"]["install_app"]
        self.dns=self.config["general"]["dns"]
        self.tweak=self.config["general"]["tweak"]
        
    def main_task(self):
        app1=app.app()
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
                self.adapter_name=self.config["advanced"]["dns"]["adapter_name"]
                self.dns_change=self.config["advanced"]["dns"]["dns_change"]
                app1.dns_change(dns1=self.dns_change,adapter_name=self.adapter_name)
            except KeyError:
                self.t.error("The config file is broken!")
        if self.tweak:
            try:
                self.tweak=self.config["advanced"]["tweak"]
                app1.tweak(self.tweak)
            except KeyError:
                self.t.error("The config file is broken!")
