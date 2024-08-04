from BL.classes.user import User
from SQLconnetction import get_connection
#from REACTconnection import get_connection
conn = get_connection()

u1 = User(user_name="miri", user_password="123456", is_admin=False)
#u1.save()



print(User.get_all_users())