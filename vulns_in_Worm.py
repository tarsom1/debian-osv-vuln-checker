import requests

def parse_packages(file_path):
    packages = []
    with open(file_path, 'r') as file:
        current_package = {}
        for line in file:
            line = line.strip()
            if line == 'ferdig':
                break
            elif line == '':
                if current_package:
                    packages.append(current_package)
                    current_package = {}
            else:
                if ':' in line:
                    key, value = line.split(':', 1)
                    current_package[key.strip()] = value.strip()
        if current_package:
            packages.append(current_package)
    return packages

def check_vulnerabilities_batch(packages):
    url = "https://api.osv.dev/v1/querybatch"
    queries = [{
        "package": {
            "name": pkg['Package'],
            "ecosystem": "Debian"
        },
        "version": pkg['Version']
    } for pkg in packages]

    response = requests.post(url, json={"queries": queries})
    response.raise_for_status()
    return response.json()

def print_vulnerability_results(results, packages, file):
    for index, result in enumerate(results.get('results', [])):
        if 'vulns' in result:
            file.write(f"\nPackage: {packages[index]['Package']}, Version: {packages[index]['Version']}\n")
            file.write("Vulnerabilities found:\n")
            for vuln in result['vulns']:
                file.write(f"  - CVE ID: {vuln['id']}, Modified: {vuln['modified']}\n")
        else:
            file.write(f"\nPackage: {packages[index]['Package']}, Version: {packages[index]['Version']} has no known vulnerabilities.\n")


file_path = 'Packages' 
packages = parse_packages(file_path)
batch_size = 100
start_index = 0

with open('Resultat.txt', 'w') as file:
    while start_index < len(packages):
        batch = packages[start_index:start_index + batch_size]
        if batch:
            results = check_vulnerabilities_batch(batch)
            print_vulnerability_results(results, batch, file)
        start_index += batch_size

