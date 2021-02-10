import subprocess


def ip_address(interface):
    try:
        if network_interface_state(interface) == 'down':
            return None
        cmd = "ifconfig %s | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'" % interface
        return subprocess.check_output(cmd, shell=True).decode('ascii')[:-1]
    except:
        return None


def network_interface_state(interface):
    try:
        with open('/sys/class/net/%s/operstate' % interface, 'r') as f:
            return f.read()
    except:
        return 'down' # default to down

def wifi_name(interface):
    try:
        cmd = "iw dev wlan0 info | grep ssid | awk '{print $2}'"
        return subprocess.check_output(cmd, shell=True).decode('ascii')[:-1]
    except:
        return 'not available' # default to not available

def cpu_usage():
    """Gets the current CPU usage fraction
    
    Returns:
        float: The current CPU usage fraction.
    """
    return float(subprocess.check_output("top -bn1 | grep load | awk '{printf \"%.2f\", $(NF-2)}'", shell = True ).decode('utf-8'))

    
def memory_usage():
    """Gets the current RAM memory usage fraction
    
    Returns:
        float: The current RAM usage fraction.
    """
    return float(subprocess.check_output("free -m | awk 'NR==2{printf \"%.2f\", $3*100/$2 }'", shell = True ).decode('utf-8')) / 100.0