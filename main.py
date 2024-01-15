import socket
import time

from rich.console import Console
from rich.progress import track
from rich.table import Table
from pyfiglet import figlet_format


class PortScanner:
    def __init__(self):
        self.console = Console()
        self.open_ports = []

    def start_page(self):
        art = '''

                        :                     :
                        :                     :
                     ;' ::                   ::      
                    .'  ';                   ;'  '.
                   ::    :;                 ;:    ::
                   ;      :;.             ,;:     ::
                   :;      :;:           ,;"      ::
                   ::.      ':;  ;   ;  ;:'     ,.;:
                    "'"...   '::,::::: ;:   .;.;"'    
                        '"""....;:::::;,;.;"""
                    .:::.....'"':::::::'",...;::::;.
                   ;:' '""'"";.,;:::::;.'""""""  ':;
                  ::'         ;::;:::;::..         :;
                 ::         ,;:::::::::::;:..       ::
                ::'     ,;;:;::::::::::::::;";..    '::
                ::     :;"  ::::::::::::::::  ":     ::
                 :.    ::   ::::::::::::::::   :     : 
                  ;    ::   ::::::::::::::::   :    :  
                   '   ::   ::::::....::::::  ::   '   
                    '  ::    ::::::::::::::   ::
                       ::     ':::::::::"'    ::
                       ':       """""""'      ::
                        ::                   ;:        
                        ':;                 ;:"        '''
        portscanner_text = figlet_format("* Port Scanner! *")
        self.console.print(f"[red]{art}[/red]")
        self.console.print(f"[white]{portscanner_text}[/white]")
        self.console.print("#" * 76, style="white")
        self.console.print(27 * "#", "by Mehmet Ali Tilgen", "#" * 27)
        self.console.print()
        self.target_page()

    def target_page(self):
        while True:
            try:
                target = self.console.input("[bold green]Enter Target IP: ")
                ip_addr = socket.gethostbyname(target)
                self.port_scan(ip_addr)
                break
            except socket.gaierror:
                print("[bold red]Invalid IP address. Please enter a valid IP.")
            except Exception as e:
                print(f"[bold red]An error occurred: {e}")

    def port_scan(self, ip_addr):
        print()
        self.console.print(f"Target ip: {ip_addr}\n")
        for port in track(range(1, 65536), description="Processing...:hourglass:"):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            status = sock.connect_ex((ip_addr, port))
            if status == 0:
                self.open_ports.append(port)
            sock.close()

        self.show_port_table(self.open_ports)

    def show_port_table(self, open_ports):
        print()
        self.console.print("Scan Completed Successfully:skull:\n")
        table = Table(show_header=True, header_style="bold green")
        table.add_column("No", style="white", justify="left")
        table.add_column("Port", style="white", justify="left")
        table.add_column("Status", justify="center", style="white")
        no = 1
        for port in open_ports:
            table.add_row(str(no), str(port), "Open")
            no += 1
        self.console.print(table)

    def run(self):
        self.start_page()


if __name__ == "__main__":
    app = PortScanner()
    app.run()
