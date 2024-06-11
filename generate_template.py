import base64

with open ("./helpers/assets/img.png", "rb") as f:
    img = base64.b64encode(f.read()).decode()

with open('./helpers/assets/template_base.svg', 'r') as file:
    template_data = file.read()
    src = f"data:image/jpeg;base64, {img}"
    template_data = template_data.replace('{img}', src)

with open('./helpers/assets/template.svg', 'w') as file:
    file.write(template_data)
