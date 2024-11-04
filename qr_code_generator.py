


# // Daniel T. K. W. - github.com/danieltkw - danielkopolo95@gmail.com
# ------------------------------------------------------------
import qrcode
import os

def generate_qr_code(link, filename='qrcode.png'):
    # Get the current directory of the .py file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, filename)

    # Create a QR code from the provided link
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    # Generate the image of the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)
    print(f"QR Code saved as {file_path}")
    return img

# ------------------------------------------------------------
if __name__ == "__main__":
    # Use the provided link to generate the QR code
    link = " ## "
    qr_image = generate_qr_code(link)
    qr_image.show()  # Opens the generated QR code image for viewing and printing

# Description: Generates a QR code from an input link and saves it as an image file (qrcode.png) in the same folder as the .py file.
# Filename: qr_code_generator.py
