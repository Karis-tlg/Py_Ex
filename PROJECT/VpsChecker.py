import socket
import logging
from concurrent.futures import ThreadPoolExecutor
import paramiko  # Thư viện để kiểm tra đăng nhập qua SSH

# Cấu hình logging
logging.basicConfig(filename='vps_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def check_port(ip, port, username, password):
    """
    Kiểm tra một cổng cụ thể trên IP và xác minh đăng nhập bằng SSH.
    """
    try:
        # Kiểm tra cổng có mở không
        with socket.create_connection((ip, port), timeout=2):
            try:
                # Kiểm tra khả năng đăng nhập bằng SSH
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ip, port=port, username=username, password=password, timeout=5)
                ssh.close()
                logging.info(f"Vps can connect: {ip}:{port}")
                print(f"Vps can connect: {ip}:{port}")
                return "success"
            except Exception as e:
                logging.info(f"Vps open on: {ip}:{port}")
                print(f"Vps open on: {ip}:{port}")
                return "open"
    except:
        return "closed"

def scan_ports(ip, start_port, end_port, username, password, max_threads=100):
    """
    Quét các cổng trên một IP bằng đa luồng và kiểm tra đăng nhập.
    """
    success_vps = []
    open_ports = []
    closed_ports = []

    def scan_and_record(port):
        status = check_port(ip, port, username, password)
        if status == "success":
            success_vps.append(f"{ip}:{port}")
        elif status == "open":
            open_ports.append(f"{ip}:{port}")
        else:
            closed_ports.append(f"{ip}:{port}")

    print(f"Scanning ports on {ip} from {start_port} to {end_port}...")
    with ThreadPoolExecutor(max_threads) as executor:
        executor.map(scan_and_record, range(start_port, end_port + 1))

    # Ghi kết quả vào các file
    with open('vps_success.txt', 'w') as success_file:
        for vps in success_vps:
            success_file.write(f"Vps can connect: {vps}\n")

    with open('vps_open.txt', 'w') as open_file:
        for vps in open_ports:
            open_file.write(f"Vps open on: {vps}\n")

    with open('port_no_vps.txt', 'w') as closed_file:
        for port in closed_ports:
            closed_file.write(f"{port}\n")

    print(f"Scanning completed. VPS can connect: {len(success_vps)}, VPS open but cannot connect: {len(open_ports)}, Closed ports: {len(closed_ports)}")
    logging.info(f"Scanning completed for {ip}. Success: {len(success_vps)}, Open: {len(open_ports)}, Closed: {len(closed_ports)}")

def read_vps_file(file_path, check_in_port=False, ip_check=None, username=None, password=None, port_range=None):
    """
    Đọc file hoặc quét cổng trên một IP dựa vào cấu hình.
    """
    try:
        if check_in_port:
            # Nếu check_in_port = True, quét các cổng trên IP được chỉ định
            if ip_check and username and password and port_range:
                start_port, end_port = port_range
                scan_ports(ip_check, start_port, end_port, username, password)
            else:
                print("Missing required parameters for port scanning.")
        else:
            # Đọc file để kiểm tra trạng thái của từng VPS
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if line.strip():
                        parts = line.split()
                        if len(parts) >= 3:
                            ip_port = parts[0]
                            username = parts[1]
                            password = parts[2]
                            
                            if ':' in ip_port:
                                ip, port = ip_port.split(':')
                                port = int(port)
                            else:
                                ip = ip_port
                                port = 3389  # Mặc định nếu không có port

                            # Kiểm tra cổng
                            check_port(ip, port, username, password)
    except FileNotFoundError:
        logging.error(f"File {file_path} not found")
        print(f"File {file_path} not found")
    except Exception as e:
        logging.error(f"Error reading file {file_path} - {e}")
        print(f"Error reading file {file_path} - {e}")

# Đường dẫn tới file vpsacc.txt
file_path = 'vpsacc.txt'

# Cấu hình quét cổng nếu cần
check_in_port = True  # Đặt True để quét cổng
ip_check = 'ducvps.servegame.com'  # IP để quét cổng
username = 'administrator'  # Tài khoản để kiểm tra đăng nhập
password = 'ducvps1@'  # Mật khẩu để kiểm tra đăng nhập
port_range = (4000, 65535)  # Khoảng cổng để quét

# Gọi hàm kiểm tra
read_vps_file(file_path, check_in_port, ip_check, username, password, port_range)
