from PIL import Image

# List of PNG files
png_files = ["1.png", "2.png", "3.png", "4.png", "5.png",
             "6.png", "7.png", "8.png", "9.png", "10.png"]

# Convert and save as PDF
images = [Image.open(png).convert("RGB") for png in png_files]
images[0].save("output.pdf", save_all=True, append_images=images[1:])
