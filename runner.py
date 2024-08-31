import gi
import subprocess
from project_data import projects, actions

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3

LAUNCHER_SCRIPT = '/home/kamlesh/p-runner/indicator_launcher.py'

class Indicator:
    def __init__(self):
        self.app = 'project-indicator'
        iconpath = "/home/kamlesh/p-runner/launcher.png"
        self.indicator = AppIndicator3.Indicator.new(
            self.app, iconpath,
            AppIndicator3.IndicatorCategory.APPLICATION_STATUS)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.create_menu())

    def create_menu(self):
        menu = Gtk.Menu()
        
        for project in projects:
            project_item = Gtk.MenuItem(label=project['name'])
            project_submenu = Gtk.Menu()
            project_item.set_submenu(project_submenu)
            
            for child in project['children']:
                child_item = Gtk.MenuItem(label=child['name'])
                child_submenu = Gtk.Menu()
                child_item.set_submenu(child_submenu)
                
                for action in actions:
                    action_item = Gtk.MenuItem(label=action)
                    action_item.connect('activate', self.perform_action, action, child)
                    child_submenu.append(action_item)
                
                project_submenu.append(child_item)
            
            menu.append(project_item)
        
        menu.append(Gtk.SeparatorMenuItem())
        
        restart_item = Gtk.MenuItem(label='Restart')
        restart_item.connect('activate', self.restart)
        menu.append(restart_item)
        
        quit_item = Gtk.MenuItem(label='Quit')
        quit_item.connect('activate', self.quit)
        menu.append(quit_item)
        
        menu.show_all()
        return menu

    def perform_action(self, widget, action, child):
        if action == 'Open in VS Code':
            subprocess.Popen(['code', child['path']])
        elif action == 'Run':
            subprocess.Popen(child['command'], shell=True, cwd=child['path'])
        elif action == 'Open Folder':
            subprocess.Popen(['xdg-open', child['path']])
        print(f"Performing action: {action} on {child['name']}")

    def restart(self, source):
        print("Restarting...")
        subprocess.Popen(['python3', LAUNCHER_SCRIPT, 'restart'])
        self.quit(None)

    def quit(self, source):
        Gtk.main_quit()

Indicator()
Gtk.main()