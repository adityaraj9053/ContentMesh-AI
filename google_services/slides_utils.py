from google_services.drive_tools import slides_service

def create_summary_slide(content_dict):
    slide = slides_service.presentations().create(body={"title": "Marketing Summary"}).execute()
    presentation_id = slide["presentationId"]

    requests = []
    for section, text in content_dict.items():
        requests.append({
            "createSlide": {
                "slideLayoutReference": {"predefinedLayout": "TITLE_AND_BODY"}
            }
        })
        requests.append({
            "insertText": {
                "objectId": "title",
                "text": section
            }
        })
        requests.append({
            "insertText": {
                "objectId": "body",
                "text": text[:1000]  # Slides limit
            }
        })

    slides_service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={"requests": requests}
    ).execute()

    return f"https://docs.google.com/presentation/d/{presentation_id}/edit"
