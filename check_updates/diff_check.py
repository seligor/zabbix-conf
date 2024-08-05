#!/usr/bin/python3
import requests
import re
import sys
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_data(url):
    headers = {
        'Accept-Language': 'ru-RU'
}
    try:
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        sys.exit(1)

def extract_version(content):
    pattern = re.compile(r'(\d\.\d\.\d{3,4})')
    matches = pattern.findall(content.decode('utf-8'))
    return matches[0] if matches else None

def json_parse(version):
    url = f'https://feedback.falcongaze.com/api/v1/check_version?forVersion={version}'
#    print(url)
    body_content = fetch_data(url)
    body_json = json.loads(body_content.decode('utf-8'))
    installed_version = body_json.get('installedVersion')
    available_version = body_json.get('availableVersion')
    if available_version:
        if installed_version < available_version:
            print("Обновление ", installed_version, ">", available_version)
        else:
            print("Обновлений нет")

    important_changes = body_json.get('importantChanges', [])
    common_changes = body_json.get('commonChanges', [])
    if important_changes:
        print("Важное:")
    for item in important_changes:
        print(f"{item}")
    if common_changes:
        print("Не важное:")
    for item in common_changes:
        print(f"{item}")

def main():
    if len(sys.argv) < 2:
        print("Usage: script.py <host>")
        sys.exit(1)

    host_conn = sys.argv[1]
    version_url = f'http://{host_conn}:39001/api/v1/services/update'

    # Fetch version data
    version_content = fetch_data(version_url)
    servver = extract_version(version_content)

    if servver:
#        print(servver)
        json_parse(servver)
    else:
        print("No version found.")

if __name__ == "__main__":
    main()
