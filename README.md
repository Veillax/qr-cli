# qr-cli
CLI for generating and saving QR codes

Download from the `src` folder and place it in a folder either set in PATH or your terminal's default directory.  

    How to use
	-----------------------------------------------
	To encode a url into a qrcode, use
	"qr [url]"
	To encode a uri into a qrcode, use
	"qr uri-[uri-prefix]:[options]"
	-----------------------------------------------
	Examples
	"qr veillax.com"
	"qr http://127.0.0.1"
	"qr uri-market:com.android.chrome"
	"qr uri-mailto:example@example.com"
	-----------------------------------------------
	URIs supported:
	 - tel - Phone number - Usage: "tel:<phone_number>"
	 - sms - SMS Message - Usage: "sms:<phone_number>"
	 - mailto - Email Address - Usage: "mailto:<email_address>"
	 - market - App Store Listing - Usage: "market:<app_package>"
	 - wifi - Wifi connection - Usage: "wifi:<authentication_type>--<network_SSID>--<password>"
	 - facetime - FaceTime Video - Usage: "facetime:<icloud_email_address/phone_number>"
	 - facetime-audio - FaceTime Audio - Usage: "facetime-audio:<icloud_email_address/phone_number>"
	 - geo - Geolocation - Usage: "geo:<latitude>,<longitude>" 
Supports most URIs, but some aren't common formatting to allow for propper parsing. An example of this is the Wifi, the common URI is `WIFI:T:{protocol};S:{ssid};P:{passwd};;`,  
but to properly parse it I had to set it to parse `WIFI:{protocol}--{ssid}--{passwd}`. Same thing happened with the market URI but you can still use `market://<app_package>`,  
but the naming convention for the qr code will say `qr-web_market_<app_package>` instead of `qr-market_<app_package>`  

QR codes will be saved to batch/qrcodes with these naming schemes:  
 - URLs:  
   - IP: `qr-ip_http_<ip>[:<port> if provided].png`  
   - HTTPS: `qr-web_https_<website>[_<route> if provided].png`  
   - HTTP: `qr-web_http_<website>[_<route> if provided].png`  


 - URIs:
   - tel: `qr-tel_[+<country_code> if provided]<phone_number>.png`
   - sms: `qr-sms_[+<country_code> if provided]<phone_number>.png`
   - mailto: `qr-maito_<email_address>`
   - market: `qr-market_<app_package>`
   - wifi: `qr-wifi_<protocol>_<ssid>`
   - facetime[-audio]: `qr-facetime[_audio]_[<icloud_email_address>/[+<country_code> if provided]<phone_number>].png`
   - geo: `qr-geo_<latitude>_<longitude>`
