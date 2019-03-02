import hashlib, binascii, os, datetime
import jwt

key = 'secret'

class PwdHelper:
	def hash_password(pwd):
		salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
		pwd_hash = hashlib.pbkdf2_hmac('sha512', pwd.encode('utf-8'), salt, 100000)
		pwd_hash = binascii.hexlify(pwd_hash)
		return (salt + pwd_hash).decode('ascii')

	def verify_password(stored_pwd, provided_pwd):
		salt = stored_pwd[:64]
		stored_pwd = stored_pwd[64:]
		pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_pwd.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
		pwdhash = binascii.hexlify(pwdhash).decode('ascii')
		return pwdhash == stored_pwd
	def create_token(email):
		# this token will expire after 3600 seconds
		tomorrow =  datetime.datetime.now() + datetime.timedelta(seconds=3600)
		tommorrow_utc = tomorrow.strftime("%s")
		return jwt.encode({'exp': tommorrow_utc,'email': email}, key, algorithm='HS256')

	def verify_token(token):
		try:
			return jwt.decode(token, key, algorithms=['HS256'])
		except:
			return False
