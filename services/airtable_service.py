import requests
import os

AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
TABLE_NAME = os.environ.get("AIRTABLE_TABLE_NAME")

def upload_file_to_airtable(file_path):
    """
    파일을 Airtable에서 요구하는 URL 형식으로 업로드
    """
    file_name = os.path.basename(file_path)
    with open(file_path, 'rb') as file:
        response = requests.post(
            "https://api.airtable.com/v0/meta/attachments",
            headers={
                "Authorization": f"Bearer {AIRTABLE_API_KEY}",
            },
            files={"file": (file_name, file)}
        )
        if response.status_code == 200:
            return response.json().get("url")
        else:
            raise Exception(f"Failed to upload file: {response.text}")

def update_airtable_with_files(record_id, word_file_path, pdf_file_path):
    """
    Airtable의 특정 레코드에 Word 및 PDF 파일 제출
    """
    word_file_url = upload_file_to_airtable(word_file_path)
    pdf_file_url = upload_file_to_airtable(pdf_file_path)

    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}/{record_id}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "fields": {
            "Generated Files": [
                {"url": word_file_url},
                {"url": pdf_file_url}
            ]
        }
    }
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code != 200:
        raise Exception(f"Failed to update Airtable: {response.text}")
