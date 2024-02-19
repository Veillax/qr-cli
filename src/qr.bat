@echo off
REM Place this in either your terminal's default directory or in a folder added to PATH
if "%1"=="" (
	echo -----------------------------------------------
	echo To encode a url into a qrcode, use
	echo "%0 [url]"
	echo To encode a uri into a qrcode, use
	echo "%0 uri-[uri]:[options]"
	echo -----------------------------------------------
	echo Examples
	echo "%0 veillax.com"
	echo "%0 http://127.0.0.1"
	echo "%0 uri-market:com.android.chrome"
	echo "%0 uri-mailto:example@example.com"
	echo -----------------------------------------------
	echo URIs supported:
	echo  - tel - Phone number - Usage: "tel:<phone_number>"
	echo  - sms - SMS Message - Usage: "sms:<phone_number>"
	echo  - mailto - Email Address - Usage: "mailto:<email_address>"
	echo  - market - App Store Listing - Usage: "market:<app_package>"
	echo  - wifi - Wifi connection - Usage: "wifi:<authentication_type>--<network_SSID>--<password>"
	echo  - facetime - FaceTime Video - Usage: "facetime:<icloud_email_address/phone_number>"
	echo  - facetime-audio - FaceTime Audio - Usage: "facetime-audio:<icloud_email_address/phone_number>"
	echo  - geo - Geolocation - Usage: "geo:<latitude>,<longitude>"
    exit /b
)

echo ------------------------------------
echo Generated QR code for %1
for /f "delims=" %%i in ('python batch\qr.py -u %1') do set qr_path=%%i
echo Saved QR code to %qr_path%
explorer /select, %qr_path%
