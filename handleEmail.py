import imaplib
import email
import re

# Gmail IMAP settings
IMAP_SERVER = "imap.gmail.com"
IMAP_PORT = 993

EMAIL_ACCOUNT = 'coktamyssovthingis@gmail.com'
APP_PASSWORD = "odpx mbkn qokc ldlp"  # from Google account (2FA required)

def get_verification_code():
    # Connect to Gmail
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(EMAIL_ACCOUNT, APP_PASSWORD)
    mail.select("inbox")

    # Search for unread emails with subject "Verify your email"
    status, messages = mail.search(
        None, '(UNSEEN SUBJECT "Verify your email")'
    )

    if status != "OK" or not messages[0]:
        print("No unread verification email found.")
        return None

    # Get the latest email ID (last one in the list)
    latest_email_id = messages[0].split()[-1]

    # Fetch the email
    status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)

    # Get email body
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            if content_type == "text/plain" and "attachment" not in content_disposition:
                body = part.get_payload(decode=True).decode(errors="ignore")
                break
    else:
        body = msg.get_payload(decode=True).decode(errors="ignore")

    # Find latest 4-digit code
    codes = re.findall(r"\b\d{4}\b", body)
    if codes:
        return codes[-1]  # get the last 4-digit sequence
    else:
        print("No 4-digit code found in email.")
        return None