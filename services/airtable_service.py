import requests
import os

AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
TABLE_NAME = os.environ.get("AIRTABLE_TABLE_NAME")

def update_airtable_column(record_id, document_path):
    """
    Airtable 테이블의 특정 컬럼에 파일 URL을 업데이트
    """
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}/{record_id}"

    # Airtable 파일 업로드 (이 예제는 URL을 첨부한다고 가정)
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "fields": {
            "Generated Document": [
                {
                    "url": f"https://example.com/{document_path}"  # Vercel Storage 등을 통해 URL 제공
                }
            ]
        }
    }

    response = requests.patch(url, headers=headers, json=data)
    if response.status_code != 200:
        raise Exception(f"Failed to update Airtable: {response.text}")
