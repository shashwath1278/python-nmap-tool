# Simple Nmap Tool

This is a simple command-line tool that utilizes the Nmap library to perform various types of network scans. The tool allows users to scan a specified IP address for open ports and gather information about the services running on those ports.

## Features

- Perform different types of scans:
  - SYN ACK scan
  - UDP scan
  - Comprehensive scan
  - Casual/Regular scan
- Display open ports and their statuses.
- Easy to use with a command-line interface.

## Prerequisites

- Python 3.x
- Nmap installed on your machine
- Python-nmap library

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/simple-nmap-tool.git
   cd simple-nmap-tool
2. **Install the required Python library**:
   ```bash
   pip install python-nmap
3. **Install Nmap**:
   On Linux:
   ```bash
     sudo apt-get install nmap
   ```
   On MacOs:
   ```bash
     brew install nmap
   ```

## Usage

1. **Run the script**:
```bash
  python your_script.py
```
2. **Follow the prompts**:
   
   Enter the IP address you want to scan.
   Choose the type of scan you want to perform (1, 2, 3, or 4).


## Example

```bash
Enter the IP address you would like to scan: 192.168.1.1

Enter the type of scan you want:
1. SYN ACK scan
2. UDP scan
3. Comprehensive scan
4. Casual/Regular scan
Choose an option (1/2/3/4): 1
```

## Notes

  Some scans may require administrative privileges. Run the script using sudo on Linux or macOS if necessary.
  Ensure you have permission to scan the IP address you are targeting, especially for public IPs.


## Contribution

Contributions are welcome! Please feel free to submit a pull request or create an issue for any suggestions or improvements.
   
