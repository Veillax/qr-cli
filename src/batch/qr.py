# Place the `batch` folder with this file in the same directory as the qr.bat
import os
import argparse
import qrcode
import re 

# Define the path to store generated QR codes
qrcodes_path = os.path.join(os.environ['USERPROFILE'], "batch\\qrcodes")

# Function to generate QR code for a given URL
def qr_gen(url):
    url.strip('"')  # Remove quotes from the URL
    # Regular expressions to match IP addresses with or without port numbers
    ip_with_port = re.compile(r'(\d+\.\d+\.\d+\.\d+):(\d+)')
    ip_without_port = re.compile(r'(\d+\.\d+\.\d+\.\d+)')
    
    # Extract URL content after the protocol, if present
    url = url.split("://")[1] if "https://" in url or "http://" in url else url 
    
    # Match IP addresses in the URL
    match_ip_address = ip_without_port.match(url) or ip_with_port.match(url)
                    
    if url.strip("http://").strip("https://").startswith("uri-"):
        print("------------------------------")
        data = ""
        url = url.strip("http://")
        url = url.strip("https://")
        uri = url.strip("uri-").split(":")[0].lower()
        d = url.strip("uri-").split(":")
        print(uri)
        i = 1
        for x in d:
            data += x
        data = data.split(uri)[1]
        print(data)
        # Handle different types of URIs
        if "tel" in uri:
            url = "tel:" + data
            filename = "qr-tel_" + data
        elif "sms" in uri:
            url = "sms:" + data
            filename = "qr-sms_" + data
        elif "mailto" in uri:
            url = "mailto:" + data
            filename = "qr-mailto_" + data
        elif "market" in uri:
            url = "market://details?id=" + data.strip('"')
            filename = "qr-market_" + data.replace(".", "_")
        elif "wifi" in uri: 
            protocol, ssid, passwd = data.split('--')
            protocol = protocol.strip('"')
            ssid = ssid.strip('"')
            passwd = passwd.strip('"')
            # Format the WiFi information into a URL
            filename = "qr-wifi_" + protocol + "_" + ssid
            url = f"WIFI:T:{protocol};S:{ssid};P:{passwd};;"
        elif "facetime-audio" in uri:
            url = "facetime-audio:" + data
            filename = "qr-facetime_audio_" + data
        elif "facetime" in uri:
            url = "facetime:" + data
            filename = "qr-facetime_" + data
        elif "geo" in uri:
            url = "geo:" + data
            filename = "qr-geo_" + data
    elif match_ip_address:
        url = "http://" + url
        filename = "qr-ip_" + url
    else:
        # Handle generic URLs
        if "://" not in url:
            url = "https://" + url
        filename = "qr-web_" + re.sub(r'/[^a-zA-Z ]/g', '_', url)
        
    # Modify filename to adhere to file naming conventions
    filename = filename.replace("://", "_")
    filename = re.sub(r'[.:/,;@+?!|\\*<>"\']', '_', filename.replace(' ', ''))
    filename = filename + ".png"

    file_path = os.path.join(qrcodes_path, filename)

    # Generate QR code only if it doesn't already exist
    if not os.path.exists(file_path):
        # Define image dimensions
        image_width = 512  # Choose desired width
        image_height = 512  # Choose desired height

        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image
        qr_img.save(file_path, "PNG")

    return file_path


if __name__ == "__main__":
    # Create the qrcodes directory if it doesn't exist
    if not os.path.exists(qrcodes_path):
        os.makedirs(qrcodes_path)

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Generate QR code for a given URL.')
    parser.add_argument('-u', '--url', type=str, help='The URL to generate the QR code for', required=True)
    args = parser.parse_args()

    # Generate QR code and print the path to the generated file
    result = qr_gen(args.url)
    print(result)
