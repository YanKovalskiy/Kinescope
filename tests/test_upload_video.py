from playwright.sync_api import Page, expect
from config import TITLE, DESCRIPTION, URL_TO_VIDEO_FILE, URL


def test_upload_video(api_request, token, parent_id, page: Page, email, password):
    headers = {
        'Authorization': f'Bearer {token}',
        'X-Parent-ID': parent_id,
        'X-Video-Title': TITLE,
        'X-Video-Description': DESCRIPTION,
        'X-Video-URL': URL_TO_VIDEO_FILE
    }
    request = api_request.post(url='https://uploader.kinescope.io/v2/video',
                              headers=headers)
    assert request.status == 200
    assert request.status_text == 'OK'

    page.goto(URL)
    page.get_by_placeholder("Почта").fill(email)
    page.get_by_placeholder("Пароль").fill(password)
    page.locator("//button[@type='submit']").click()

    expect(page.locator(f"//div[@title='{TITLE}']")).to_be_visible()
