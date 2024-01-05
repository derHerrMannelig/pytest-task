import allure

def take_screenshot(page, name) -> None:
  allure.attach(
    body=page.screenshot(full_page=True),
    name=f'shot_{name}',
    attachment_type=allure.attachment_type.PNG
  )