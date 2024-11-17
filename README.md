# script_system_optimizer



### **How to Use:**

1. **Run the Python Script**:
   - Save the Python script to a file (e.g., `generate_optimization_scripts.py`).
   - Run the script using Python:
     ```bash
     python generate_optimization_scripts.py
     ```

2. **Generated Scripts**:
   - **Windows**: A PowerShell script (`system_optimization.ps1`) will be generated with disk cleanup, performance monitoring, CPU usage optimization, and a port scan.
   - **Linux/Mac**: A Bash script (`system_optimization.sh`) will be generated with system optimization tasks, including CPU usage monitoring and optimization, along with a port scan.

3. **Running the Scripts**:
   - **For PowerShell (Windows)**:
     - Right-click and select "Run with PowerShell" or run it from the PowerShell terminal:
       ```powershell
       ./system_optimization.ps1
       ```

   - **For Bash (Linux/Mac)**:
     - Make the script executable and run it:
       ```bash
       chmod +x system_optimization.sh
       ./system_optimization.sh
       ```

---

### **Important Notes**:

1. **CPU Usage Monitoring**:
    - The CPU usage optimizer checks for high CPU usage processes and provides the option to terminate them.
    - **Be careful** when killing processes, as terminating essential system processes can cause instability. Always verify which processes are safe to kill.

2. **nmap**:
    - Ensure `nmap` is installed on Linux/macOS for the port scan feature to work. Use the following commands if it's not installed:
      ```bash
      sudo apt install nmap   # Debian/Ubuntu
      brew install nmap       # macOS
      ```

3. **Permissions**:
    - Running these scripts may require elevated privileges (`sudo` on Linux/macOS or **administrator privileges** on Windows) for tasks like system updates, stopping services, and killing processes.

4. **Customizing CPU Optimization**:
    - You can modify the script to optimize for specific use cases. For example, you can adjust the threshold for "high CPU usage" or use `nice` (on Linux) to adjust process priorities instead of killing them.

### **Conclusion**:
This updated Python script generates **PowerShell** and **Bash** scripts that now include CPU usage optimization. These scripts check for high CPU-consuming processes, optionally terminate them, and provide a performance summary. They also retain the original functionality for disk cleanup, system updates, port scanning, and more.
