class MysqlAuthenticator(Authenticator):

	"""JupyterHub Authenticator Based on Mysql"""

	def __init__(self, **kwargs):
		super(MysqlAuthenticator, self).__init__(**kwargs)

	@gen.coroutine
	def authenticate(self, handler, data):

		db_url = "mysql+mysqlconnector://root:root@192.168.199.182:3306/jupyter"
		session = init(db_url)

		username = data['username']
		passwd = data['password']

		try:
			user = session.query(User).filter(User.username == username).filter(User.password == passwd).one()
			if user is not None:
				return user.username
			else:
				return None
		except:
			return None