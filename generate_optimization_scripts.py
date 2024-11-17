
import os

def generate_powershell_script():
    """Generate a PowerShell script for system optimization, including CPU usage optimization and port scan."""
    ps_script = """
# PowerShell Script for System Optimization

# Clean temporary files
Write-Host "Cleaning temporary files..."
Remove-Item -Path $env:TEMP\* -Recurse -Force
Remove-Item -Path "C:\\Windows\\Temp\\*" -Recurse -Force

# Clear Internet Explorer Cache
Write-Host "Clearing Internet Explorer Cache..."
RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 255

# Optimize the disk (Windows built-in command)
Write-Host "Optimizing the disk..."
defrag C: /O /H

# Disable unnecessary startup programs (example: disable OneDrive)
Write-Host "Disabling unnecessary startup programs..."
Stop-Process -Name OneDrive -Force
Remove-Item -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\OneDrive" -Force

# Check system performance (CPU & Memory usage)
Write-Host "Checking system performance..."
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 10

# Update system (Windows Update)
Write-Host "Running Windows Updates..."
Install-Module PSWindowsUpdate -Force -SkipPublisherCheck
Get-WindowsUpdate -AcceptAll -Install -AutoReboot

# Perform a simple port scan (Windows version of nmap or PowerShell alternative)
Write-Host "Performing port scan on localhost..."
$open_ports = Test-NetConnection -ComputerName localhost -Port 80,443,22,3389
$open_ports | Format-Table -Property ComputerName,RemoteAddress,RemotePort,TcpTestSucceeded

# CPU Usage Optimization:
Write-Host "Checking CPU usage and identifying high CPU processes..."
$high_cpu_processes = Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
$high_cpu_processes | Format-Table -Property Name, CPU, Id

# Optional: Kill high CPU consuming processes (be careful!)
# Stop-Process -Id $high_cpu_processes.Id[0]  # Uncomment to kill the top CPU process

Write-Host "CPU usage optimization complete. High CPU processes have been reviewed."
"""
    return ps_script


def generate_bash_script():
    """Generate a Bash script for system optimization, including CPU usage optimization and port scan."""
    bash_script = """
#!/bin/bash

# Bash Script for System Optimization

# Clean temporary files
echo "Cleaning temporary files..."
rm -rf /tmp/*

# Clean apt cache (for Debian/Ubuntu-based systems)
echo "Cleaning package manager cache..."
sudo apt-get clean

# Update the system and upgrade packages
echo "Updating system packages..."
sudo apt-get update -y && sudo apt-get upgrade -y

# Optimize the disk (e.g., using fstrim for SSD)
echo "Running disk optimization (fstrim)..."
sudo fstrim --all

# Check system performance (CPU & Memory usage)
echo "Checking system performance..."
top -n 1 | head -20

# Disable unnecessary services (e.g., Bluetooth on a server)
echo "Disabling unnecessary services..."
sudo systemctl stop bluetooth
sudo systemctl disable bluetooth

# Clean up old logs and unnecessary files
echo "Cleaning up old logs..."
sudo journalctl --vacuum-time=7d

# Check if there are any orphaned packages (Debian/Ubuntu)
echo "Removing orphaned packages..."
sudo apt-get autoremove -y

# Perform a simple port scan (nmap)
echo "Performing port scan on localhost..."
nmap -p 80,443,22,3389 localhost

# CPU Usage Optimization:
echo "Checking CPU usage and identifying high CPU processes..."
top -b -n 1 | head -20

# Optional: Kill high CPU consuming processes (be careful!)
# high_cpu_pid=$(top -b -n 1 | sort -rk 9 | head -n 2 | tail -n 1 | awk '{print $1}')
# kill -9 $high_cpu_pid  # Uncomment to kill the top CPU process

echo "CPU usage optimization complete. High CPU processes have been reviewed."
"""
    return bash_script


def save_script(filename, content):
    """Save the script content to a file."""
    with open(filename, "w") as f:
        f.write(content)
    print(f"Script saved as {filename}")


if __name__ == "__main__":
    # Generate and save PowerShell script
    ps_script = generate_powershell_script()
    save_script("system_optimization.ps1", ps_script)

    # Generate and save Bash script
    bash_script = generate_bash_script()
    save_script("system_optimization.sh", bash_script)

    print("\nOptimization scripts with CPU usage optimization and port scan have been generated successfully!")
