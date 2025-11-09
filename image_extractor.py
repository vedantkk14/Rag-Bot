from pypdf import PdfReader

reader = PdfReader("Attention.pdf")

for page_num, page in enumerate(reader.pages):
    for image in page.images:
        image_name = f"image_page{page_num+1}_{image.name}"
        with open(image_name, "wb") as f:
            f.write(image.data)
        print("Saved:", image_name)
