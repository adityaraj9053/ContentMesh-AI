from google_services.drive_tools import docs_service

def create_marketing_doc(content_dict):
    doc_title = "Marketing Campaign Summary"
    body = {
        'title': doc_title
    }
    doc = docs_service.documents().create(body=body).execute()
    doc_id = doc.get('documentId')

    requests = []
    for section, text in content_dict.items():
        requests.append({"insertText": {"location": {"index": 1}, "text": f"\n== {section.upper()} ==\n{text}\n"}})

    docs_service.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()

    return f"https://docs.google.com/document/d/{doc_id}/edit"
