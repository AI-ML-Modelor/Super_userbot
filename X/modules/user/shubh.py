from pyrogram import Client, idle
import onewordraid  # Ensure karo ki yeh sahi path pe ho

API_ID = 23538223  # Apna API ID daalo
API_HASH = "6d6a202ff2e1951bb954cdc302bd0bca"
SESSION_NAME = "BQFnKi8AIaYRHocC8Qw7-M7y0lEJuV_pArlHJo6blOIVVxPnQ2lo1jmLWjnfwujYG9SSfXLs-lhbBq-jP4MMD58uToKKt33zcKj2mA-MjweyOPbCZSNeB2mVUV8L6VbTxiBn_4KqC13REwLluObg2ZzN7Evb2-wU6K9ydnC7U-LAntOEThnoIdzvav3mguo_LHJ2HX5vsVl52ocqUJkRUuKF1lsjkOMfeKmaVDJuX7vQiy5IHTMMtqN9WMcmQLy-GtIw4nkGSe-SyDG54Sn109K3DgzQDNxgcJ5m9YWiGZ-8mhOlv5uOjgipkCpSTW-ZGR_mVKwNCLOJHeO2i31FmjBVG1kpHAAAAAHDZ31cAA"

M = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

M.add_handler(plugins.onewordraid.start_raid)
M.add_handler(plugins.onewordraid.stop_raid)

M.start()
print("Bot Started Successfully")
idle()
M.stop()
