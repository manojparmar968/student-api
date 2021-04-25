from common_app.models import Account

def is_mobile_number_exist(mobile_number):
    mobile_obj = Account.objects.filter(mobile_number=mobile_number)
    if mobile_obj is not None:
        email = [mobile_obj.email for mobile_obj in mobile_obj]
        return email
    else:
        return None

def is_email_exist(email):
    email_obj = Account.objects.filter(email=email)
    if email_obj:
        user_id = [email_obj.id for email_obj in email_obj]
        return user_id
    else:
        return None

# def send_OTP(mobile,country_code,otp_code,hash_Key=None):
#     try:
#         client = Client(ACCOUNT_SID, AUTH_TOKEN)
#         if not hash_Key:
#             message = client.messages.create(
#                 from_='+12072306900',
#                 body=str(
#                     otp_code) + " is the code specific to your account. NEVER SHARE THIS CODE WITH ANYONE. We will NEVER ask for this code over email or by phone!",
#                 to=str(country_code)+str(mobile)
#             )
#         else:
#             message = client.messages.create(
#                 from_=From_Number,
#                 body="<#>" +
#                 str(otp_code) + " is the code specific to your  account. NEVER SHARE THIS CODE WITH ANYONE. We will NEVER ask for this code over email, or by phone! "+" "+str(hash_Key),
#                 to=str(country_code)+str(mobile)
#             )
#         print(message.status)
#     except Exception as e:
#         print (e)